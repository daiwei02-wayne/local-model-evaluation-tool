from __future__ import annotations

from .models import Problem


def validate_problem_set(
    problems: list[Problem],
    expected_problems: int = 100,
    min_cases: int = 30,
) -> list[str]:
    messages: list[str] = []

    if len(problems) != expected_problems:
        messages.append(f"题目数量为 {len(problems)}，预期 {expected_problems}")

    for problem in problems:
        if len(problem.cases) < min_cases:
            messages.append(
                f"题目{problem.id} 用例数量为 {len(problem.cases)}，少于 {min_cases}"
            )
        if not problem.cases:
            messages.append(f"题目{problem.id} 没有测试用例")

    return messages
