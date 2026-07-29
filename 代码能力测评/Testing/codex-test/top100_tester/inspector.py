from __future__ import annotations

import ast
from pathlib import Path


class SubmissionInspectError(ValueError):
    pass


def find_submitted_methods(submission: str | Path, class_name: str | None = None) -> set[str]:
    path = Path(submission)
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        raise SubmissionInspectError(f"提交文件语法错误: {exc}") from exc
    except OSError as exc:
        raise SubmissionInspectError(f"无法读取提交文件: {path}") from exc

    methods: set[str] = set()
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        if class_name is not None and node.name != class_name:
            continue
        methods.update(
            item.name
            for item in node.body
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
            and item.name.startswith("question_")
        )
    return methods
