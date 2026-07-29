from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from .adapters import normalize_expected
from .models import CaseResult, Problem, ProblemResult, RunSummary, TestCase


class Executor:
    def __init__(
        self,
        submission: str | Path,
        timeout_ms: int = 1000,
        memory_mb: int = 256,
        class_name: str = "codingtest",
    ) -> None:
        self.submission = Path(submission).resolve()
        self.timeout_ms = timeout_ms
        self.memory_mb = memory_mb
        self.class_name = class_name

    def run(
        self,
        problems: list[Problem],
        submitted_methods: set[str],
        expected_problems: int,
    ) -> RunSummary:
        started = time.perf_counter()
        results: list[ProblemResult] = []

        for problem in problems:
            results.append(self.run_problem(problem, problem.method_name in submitted_methods))

        elapsed_ms = _elapsed_ms(started)
        passed = sum(item.passed for item in results)
        total = sum(item.total for item in results)
        submitted = sum(1 for problem in problems if problem.method_name in submitted_methods)
        return RunSummary(
            submitted=submitted,
            expected_problems=expected_problems,
            total_cases=total,
            passed_cases=passed,
            failed_cases=total - passed,
            elapsed_ms=elapsed_ms,
            problem_results=results,
        )

    def run_problem(self, problem: Problem, submitted: bool) -> ProblemResult:
        started = time.perf_counter()
        case_results: list[CaseResult] = []
        result_cache: dict[str, CaseResult] = {}

        if not submitted:
            case_results = [
                CaseResult(
                    problem_id=problem.id,
                    case_name=case.name,
                    passed=False,
                    elapsed_ms=0,
                    reason=f"缺少方法 {problem.method_name}",
                    expected=case.expected,
                )
                for case in problem.cases
            ]
            return _problem_result(problem, started, case_results, submitted=False)

        for case in problem.cases:
            cache_key = _case_cache_key(case)
            if cache_key in result_cache:
                case_results.append(_clone_cached_result(result_cache[cache_key], case.name))
                continue
            result = self._run_case(problem, case)
            result_cache[cache_key] = result
            case_results.append(result)

        return _problem_result(problem, started, case_results, submitted=True)

    def _run_case(self, problem: Problem, case: TestCase) -> CaseResult:
        started = time.perf_counter()
        payload = {
            "input": {"args": case.args, "kwargs": case.kwargs},
            "expectation": case.expectation,
        }

        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8", delete=False) as handle:
            json.dump(payload, handle, ensure_ascii=False)
            case_file = handle.name

        try:
            command = [
                sys.executable,
                "-m",
                "top100_tester.worker",
                "--submission",
                str(self.submission),
                "--method",
                problem.method_name,
                "--case-file",
                case_file,
                "--memory-mb",
                str(self.memory_mb),
                "--cpu-seconds",
                str(max(1, (self.timeout_ms + 999) // 1000)),
            ]
            completed = subprocess.run(
                command,
                cwd=str(Path(__file__).resolve().parents[1]),
                capture_output=True,
                text=True,
                timeout=self.timeout_ms / 1000,
                env=_child_env(),
            )
        except subprocess.TimeoutExpired:
            return CaseResult(
                problem_id=problem.id,
                case_name=case.name,
                passed=False,
                elapsed_ms=_elapsed_ms(started),
                reason=f"超时>{self.timeout_ms}ms",
                expected=case.expected,
            )
        finally:
            try:
                os.unlink(case_file)
            except OSError:
                pass

        elapsed_ms = _elapsed_ms(started)
        if completed.returncode != 0:
            return CaseResult(
                problem_id=problem.id,
                case_name=case.name,
                passed=False,
                elapsed_ms=elapsed_ms,
                reason=f"进程异常退出({completed.returncode})",
                expected=case.expected,
            )

        try:
            data = json.loads(completed.stdout)
        except json.JSONDecodeError:
            return CaseResult(
                problem_id=problem.id,
                case_name=case.name,
                passed=False,
                elapsed_ms=elapsed_ms,
                reason="执行结果不是合法 JSON",
                expected=case.expected,
            )

        if data.get("status") != "ok":
            return CaseResult(
                problem_id=problem.id,
                case_name=case.name,
                passed=False,
                elapsed_ms=elapsed_ms,
                reason=f"{data.get('error_type', 'Error')}: {data.get('error', '')}",
                expected=case.expected,
            )

        actual = _normalize_actual_for_expected(data.get("value"), case.expected)
        expected = normalize_expected(case.expected)
        passed = _compare(actual, expected, case.comparison)
        return CaseResult(
            problem_id=problem.id,
            case_name=case.name,
            passed=passed,
            elapsed_ms=elapsed_ms,
            reason="" if passed else "输出不匹配",
            actual=actual,
            expected=expected,
        )


def _problem_result(
    problem: Problem,
    started: float,
    case_results: list[CaseResult],
    submitted: bool,
) -> ProblemResult:
    passed = sum(1 for item in case_results if item.passed)
    total = len(case_results)
    return ProblemResult(
        problem=problem,
        total=total,
        passed=passed,
        failed=total - passed,
        elapsed_ms=_elapsed_ms(started),
        case_results=case_results,
        submitted=submitted,
    )


def _elapsed_ms(started: float) -> int:
    return int(round((time.perf_counter() - started) * 1000))


def _child_env() -> dict[str, str]:
    env = os.environ.copy()
    project_root = str(Path(__file__).resolve().parents[1])
    current = env.get("PYTHONPATH")
    env["PYTHONPATH"] = project_root if not current else f"{project_root}{os.pathsep}{current}"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def _compare(actual, expected, comparison: str) -> bool:
    if comparison == "exact":
        return actual == expected
    if comparison == "any_order":
        return _json_sorted(actual) == _json_sorted(expected)
    if comparison == "set_of_lists":
        return _list_set(actual) == _list_set(expected)
    if comparison == "group_anagrams":
        return _group_set(actual) == _group_set(expected)
    return actual == expected


def _normalize_actual_for_expected(actual, raw_expected):
    if (
        actual is None
        and isinstance(raw_expected, dict)
        and raw_expected.get("__type__") in {"ListNode", "TreeNode", "ListNodeArray", "RandomNode"}
        and raw_expected.get("value") == []
    ):
        return []
    return actual


def _case_cache_key(case: TestCase) -> str:
    return json.dumps(
        {
            "args": case.args,
            "kwargs": case.kwargs,
            "expected": case.expected,
            "expectation": case.expectation,
            "comparison": case.comparison,
        },
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _clone_cached_result(result: CaseResult, case_name: str) -> CaseResult:
    return CaseResult(
        problem_id=result.problem_id,
        case_name=case_name,
        passed=result.passed,
        elapsed_ms=0,
        reason=result.reason,
        actual=result.actual,
        expected=result.expected,
    )


def _json_sorted(value):
    if not isinstance(value, list):
        return value
    return sorted(value, key=lambda item: json.dumps(item, ensure_ascii=False, sort_keys=True))


def _list_set(value):
    if not isinstance(value, list):
        return value
    return sorted(
        [tuple(item if isinstance(item, list) else [item]) for item in value],
        key=lambda item: json.dumps(item, ensure_ascii=False),
    )


def _group_set(value):
    if not isinstance(value, list):
        return value
    return sorted(
        [tuple(sorted(group)) for group in value],
        key=lambda item: json.dumps(item, ensure_ascii=False),
    )
