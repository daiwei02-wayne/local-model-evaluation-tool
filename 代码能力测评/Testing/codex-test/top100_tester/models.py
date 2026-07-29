from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


DIFFICULTIES = {"简单", "中等", "困难"}


@dataclass(frozen=True)
class TestCase:
    name: str
    args: list[Any] = field(default_factory=list)
    kwargs: dict[str, Any] = field(default_factory=dict)
    expected: Any = None
    expectation: dict[str, Any] = field(default_factory=dict)
    comparison: str = "exact"


@dataclass(frozen=True)
class Problem:
    id: int
    title: str
    difficulty: str
    cases: list[TestCase]
    method: str | None = None
    source: str | None = None

    @property
    def method_name(self) -> str:
        return self.method or f"question_{self.id}"


@dataclass
class CaseResult:
    problem_id: int
    case_name: str
    passed: bool
    elapsed_ms: int
    reason: str = ""
    actual: Any = None
    expected: Any = None


@dataclass
class ProblemResult:
    problem: Problem
    total: int
    passed: int
    failed: int
    elapsed_ms: int
    case_results: list[CaseResult]
    submitted: bool


@dataclass
class RunSummary:
    submitted: int
    expected_problems: int
    total_cases: int
    passed_cases: int
    failed_cases: int
    elapsed_ms: int
    problem_results: list[ProblemResult]
