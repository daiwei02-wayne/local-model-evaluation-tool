from __future__ import annotations

from .models import ProblemResult, RunSummary


SEP = "=" * 70
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"


DIFFICULTY_COLOR = {
    "简单": GREEN,
    "中等": YELLOW,
    "困难": RED,
}


def format_problem_result(result: ProblemResult) -> str:
    difficulty = _colored_difficulty(result.problem.difficulty)
    title = result.problem.title
    prefix = f"{BOLD}【题目{result.problem.id}】{RESET} <{difficulty}>{title}"
    if not result.submitted:
        return f"{prefix}；{_red('未提交')}，运行耗时： {result.elapsed_ms}ms"

    rate = _rate(result.passed, result.total)
    return (
        f"{prefix}；结果： 正确({result.passed}/{result.total})，"
        f"错误({result.failed}/{result.total})；通过率： {_colored_rate(rate)}，"
        f"运行耗时： {result.elapsed_ms}ms"
    )


def format_summary(summary: RunSummary) -> str:
    lines = ["", SEP, "    测试汇总", SEP]
    lines.append(_format_summary_line("总计", summary.submitted, summary.expected_problems, summary))
    for difficulty in ("简单", "中等", "困难"):
        results = [item for item in summary.problem_results if item.problem.difficulty == difficulty]
        lines.append(_format_difficulty_summary(difficulty, results))
    lines.append(SEP)
    return "\n".join(lines)


def format_header(submission: str, cases: str, timeout_ms: int) -> str:
    return "\n".join(
        [
            SEP,
            "    Top100 代码测试框架",
            SEP,
            f"解题文件  ： {submission}",
            f"测试目录  ： {cases}",
            f"超时限制  ： {_format_timeout(timeout_ms)} / 用例",
            SEP,
            "",
        ]
    )


def format_engine_start(problem_count: int) -> str:
    return (
        f"找到 {problem_count} 道有测试用例的题目，正在启动执行引擎...\n"
        "执行引擎就绪，开始测试...\n"
    )


def _format_summary_line(label: str, submitted: int, expected: int, summary: RunSummary) -> str:
    submit_rate = _rate(submitted, expected)
    pass_rate = _rate(summary.passed_cases, summary.total_cases)
    return (
        f"{label if label == '总计' else _colored_difficulty(label)} > "
        f"提交题目： {submitted}/{expected}，"
        f"总正确： {summary.passed_cases}/{summary.total_cases}，"
        f"总错误： {summary.failed_cases}/{summary.total_cases}；"
        f"提交率： {_colored_rate(submit_rate)}，"
        f"通过率： {_colored_rate(pass_rate)}，"
        f"总运行耗时： {summary.elapsed_ms}ms"
    )


def _format_difficulty_summary(difficulty: str, results: list[ProblemResult]) -> str:
    expected = len(results)
    submitted = sum(1 for item in results if item.submitted)
    passed = sum(item.passed for item in results)
    total = sum(item.total for item in results)
    failed = total - passed
    elapsed = sum(item.elapsed_ms for item in results)
    submit_rate = _rate(submitted, expected)
    pass_rate = _rate(passed, total)
    return (
        f"<{_colored_difficulty(difficulty)}> "
        f"提交题目： {submitted}/{expected}，"
        f"总正确： {passed}/{total}，"
        f"总错误： {failed}/{total}；"
        f"提交率： {_colored_rate(submit_rate)}，"
        f"通过率： {_colored_rate(pass_rate)}，"
        f"运行耗时： {elapsed}ms"
    )


def _colored_difficulty(difficulty: str) -> str:
    color = DIFFICULTY_COLOR.get(difficulty, RESET)
    return f"{color}{difficulty}{RESET}"


def _colored_rate(rate: float) -> str:
    text = f"{rate:.1f}%"
    if rate >= 99.95:
        return f"{GREEN}{text}{RESET}"
    if rate <= 0:
        return f"{RED}{text}{RESET}"
    if rate < 70:
        return f"{RED}{text}{RESET}"
    if rate < 100:
        return f"{YELLOW}{text}{RESET}"
    return f"{GREEN}{text}{RESET}"


def _red(text: str) -> str:
    return f"{RED}{text}{RESET}"


def _rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 0.0
    return numerator * 100.0 / denominator


def _format_timeout(timeout_ms: int) -> str:
    if timeout_ms % 1000 == 0:
        return f"{timeout_ms // 1000}s"
    return f"{timeout_ms}ms"
