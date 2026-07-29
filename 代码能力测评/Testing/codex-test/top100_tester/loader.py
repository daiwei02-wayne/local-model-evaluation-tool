from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .models import DIFFICULTIES, Problem, TestCase


JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL)


class ProblemLoadError(ValueError):
    pass


def load_problems(path: str | Path) -> list[Problem]:
    root = Path(path)
    if not root.exists():
        raise ProblemLoadError(f"题库路径不存在: {root}")

    files: list[Path]
    if root.is_file():
        files = [root]
    else:
        files = sorted(
            [*root.rglob("*.json"), *root.rglob("*.md")],
            key=lambda p: (p.stem, p.suffix),
        )

    problems: list[Problem] = []
    seen_ids: set[int] = set()
    for file in files:
        if file.name.startswith(".") or file.name in {"schema.json", "official_hot100_ids.json"}:
            continue
        problem = _load_problem_file(file)
        if problem.id in seen_ids:
            raise ProblemLoadError(f"重复题号 {problem.id}: {file}")
        seen_ids.add(problem.id)
        problems.append(problem)

    return sorted(problems, key=lambda p: p.id)


def _load_problem_file(file: Path) -> Problem:
    try:
        raw = file.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ProblemLoadError(f"{file} 不是 UTF-8 文本文件") from exc

    if file.suffix == ".json":
        data = json.loads(raw)
    elif file.suffix == ".md":
        match = JSON_FENCE_RE.search(raw)
        if not match:
            raise ProblemLoadError(f"{file} 中没有找到 JSON 代码块")
        data = json.loads(match.group(1))
    else:
        raise ProblemLoadError(f"不支持的题库文件格式: {file}")

    return _problem_from_dict(data, str(file))


def _problem_from_dict(data: dict[str, Any], source: str) -> Problem:
    required = {"id", "title", "difficulty", "cases"}
    missing = required - data.keys()
    if missing:
        raise ProblemLoadError(f"{source} 缺少字段: {', '.join(sorted(missing))}")

    problem_id = data["id"]
    if not isinstance(problem_id, int):
        raise ProblemLoadError(f"{source} 的 id 必须是整数")

    difficulty = data["difficulty"]
    if difficulty not in DIFFICULTIES:
        raise ProblemLoadError(f"{source} 的 difficulty 必须是 简单/中等/困难")

    cases_data = data["cases"]
    if not isinstance(cases_data, list):
        raise ProblemLoadError(f"{source} 的 cases 必须是数组")

    cases: list[TestCase] = []
    for idx, case_data in enumerate(cases_data, start=1):
        if not isinstance(case_data, dict):
            raise ProblemLoadError(f"{source} 第 {idx} 个用例必须是对象")
        input_data = case_data.get("input", {})
        if not isinstance(input_data, dict):
            raise ProblemLoadError(f"{source} 第 {idx} 个用例 input 必须是对象")
        args = input_data.get("args", [])
        kwargs = input_data.get("kwargs", {})
        if not isinstance(args, list):
            raise ProblemLoadError(f"{source} 第 {idx} 个用例 input.args 必须是数组")
        if not isinstance(kwargs, dict):
            raise ProblemLoadError(f"{source} 第 {idx} 个用例 input.kwargs 必须是对象")
        if "expected" not in case_data:
            raise ProblemLoadError(f"{source} 第 {idx} 个用例缺少 expected")
        cases.append(
            TestCase(
                name=str(case_data.get("name", f"case_{idx}")),
                args=args,
                kwargs=kwargs,
                expected=case_data["expected"],
                expectation=case_data.get("expectation", {"source": "return"}),
                comparison=str(case_data.get("comparison", "exact")),
            )
        )

    return Problem(
        id=problem_id,
        title=str(data["title"]),
        difficulty=difficulty,
        method=data.get("method"),
        cases=cases,
        source=source,
    )
