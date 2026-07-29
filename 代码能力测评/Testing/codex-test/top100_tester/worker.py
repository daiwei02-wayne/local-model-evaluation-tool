from __future__ import annotations

import argparse
import importlib.util
import json
import os
import resource
import sys
import traceback
import uuid
from pathlib import Path
from typing import Any, List, Optional

from .adapters import ListNode, RandomNode, TreeNode, decode_args, value_for_expectation


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submission", required=True)
    parser.add_argument("--method", required=True)
    parser.add_argument("--case-file", required=True)
    parser.add_argument("--memory-mb", type=int, default=256)
    parser.add_argument("--cpu-seconds", type=int, default=2)
    args = parser.parse_args()

    _apply_limits(args.memory_mb, args.cpu_seconds)

    try:
        payload = json.loads(Path(args.case_file).read_text(encoding="utf-8"))
        result = _run_case(
            submission=Path(args.submission),
            method_name=args.method,
            case_payload=payload,
        )
    except BaseException as exc:
        result = {
            "status": "error",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "traceback": traceback.format_exc(limit=5),
        }

    sys.stdout.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0


def _apply_limits(memory_mb: int, cpu_seconds: int) -> None:
    if memory_mb > 0:
        memory_bytes = memory_mb * 1024 * 1024
        try:
            resource.setrlimit(resource.RLIMIT_AS, (memory_bytes, memory_bytes))
        except (ValueError, OSError, AttributeError):
            pass
    if cpu_seconds > 0:
        try:
            resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds + 1))
        except (ValueError, OSError, AttributeError):
            pass


def _run_case(submission: Path, method_name: str, case_payload: dict[str, Any]) -> dict[str, Any]:
    module = _load_submission(submission)
    if not hasattr(module, "ListNode"):
        setattr(module, "ListNode", ListNode)
    if not hasattr(module, "TreeNode"):
        setattr(module, "TreeNode", TreeNode)
    if not hasattr(module, "RandomNode"):
        setattr(module, "RandomNode", RandomNode)
    method, owner_name = _find_submission_method(module, method_name)
    if method is None:
        return {
            "status": "error",
            "error_type": "MissingMethod",
            "error": f"缺少 {method_name}，需要在任意类中实现该方法",
        }

    input_data = case_payload.get("input", {})
    args, kwargs, context = decode_args(input_data.get("args", []), input_data.get("kwargs", {}))
    if _looks_like_design_case(args, kwargs):
        actual = _run_design_case(method, args[0], args[1], context)
        return {"status": "ok", "value": actual}

    value = method(*args, **kwargs)
    actual = value_for_expectation(
        returned=value,
        args=args,
        expectation=case_payload.get("expectation", {"source": "return"}),
        context=context,
    )

    try:
        json.dumps(actual, ensure_ascii=False)
    except TypeError as exc:
        return {
            "status": "error",
            "error_type": "NonJsonResult",
            "error": f"返回值无法 JSON 序列化: {exc}",
        }

    return {"status": "ok", "value": actual}



def _find_submission_method(module, method_name: str):
    module_method = getattr(module, method_name, None)
    if callable(module_method):
        return module_method, "<module>"

    preferred = getattr(module, "codingtest", None)
    if isinstance(preferred, type) and callable(getattr(preferred, method_name, None)):
        return _bind_method(preferred, method_name), preferred.__name__

    for name, value in vars(module).items():
        if name.startswith("__"):
            continue
        if not isinstance(value, type):
            continue
        if callable(getattr(value, method_name, None)):
            return _bind_method(value, method_name), name

    return None, None


def _bind_method(klass: type, method_name: str):
    raw = klass.__dict__.get(method_name)
    if isinstance(raw, staticmethod):
        method = getattr(klass, method_name, None)
        return method if callable(method) else None
    if isinstance(raw, classmethod):
        method = getattr(klass, method_name, None)
        return method if callable(method) else None

    # Some generated submissions put functions inside a class but omit self.
    # Accessing them through an instance would add an implicit first argument,
    # so call the raw class function directly when the first parameter is not self/cls.
    if callable(raw):
        code = getattr(raw, "__code__", None)
        if code is not None and code.co_argcount > 0:
            first_arg = code.co_varnames[0]
            if first_arg not in {"self", "cls"}:
                return raw

    try:
        instance = klass()
    except TypeError as exc:
        raise TypeError(f"类 {klass.__name__} 无法无参实例化: {exc}") from exc
    method = getattr(instance, method_name, None)
    if method is None or not callable(method):
        return None
    return method

def _looks_like_design_case(args: list[Any], kwargs: dict[str, Any]) -> bool:
    return (
        not kwargs
        and len(args) == 2
        and isinstance(args[0], list)
        and isinstance(args[1], list)
        and bool(args[0])
        and all(isinstance(item, str) for item in args[0])
        and all(isinstance(item, list) for item in args[1])
    )


def _run_design_case(method, operations: list[str], arguments: list[list[Any]], context) -> list[Any]:
    if len(operations) != len(arguments):
        raise ValueError("设计题 operations 与 arguments 长度不一致")

    first_args = arguments[0]
    created = _construct_design_object(method, first_args)
    outputs: list[Any] = [None]
    for operation, params in zip(operations[1:], arguments[1:]):
        fn = getattr(created, operation)
        outputs.append(encode_design_value(fn(*params), context))
    return outputs


def _construct_design_object(method, first_args: list[Any]):
    try:
        created = method(*first_args)
    except TypeError:
        created = method()
        if isinstance(created, type):
            return created(*first_args)
        raise
    if isinstance(created, type):
        return created(*first_args)
    return created


def encode_design_value(value: Any, context) -> Any:
    from .adapters import encode_value

    return encode_value(value, context)


def _load_submission(submission: Path):
    module_name = f"_coding_submission_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(module_name, submission)
    if spec is None or spec.loader is None:
        raise ImportError(f"无法加载提交文件: {submission}")
    module = importlib.util.module_from_spec(spec)
    module.ListNode = ListNode
    module.TreeNode = TreeNode
    module.RandomNode = RandomNode
    module.Optional = Optional
    module.List = List
    sys.modules[module_name] = module
    sys.path.insert(0, str(submission.parent.resolve()))
    try:
        spec.loader.exec_module(module)
        module.ListNode = ListNode
        module.TreeNode = TreeNode
        module.RandomNode = RandomNode
        module.Optional = Optional
        module.List = List
    finally:
        try:
            sys.path.remove(str(submission.parent.resolve()))
        except ValueError:
            pass
    return module


if __name__ == "__main__":
    raise SystemExit(main())
