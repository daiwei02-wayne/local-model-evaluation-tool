from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

from .docx_importer import extract_docx_outline
from .executor import Executor
from .formatters import format_engine_start, format_header, format_problem_result, format_summary
from .inspector import SubmissionInspectError, find_submitted_methods
from .loader import ProblemLoadError, load_problems
from .models import RunSummary
from .validator import validate_problem_set


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="top100-tester")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="运行提交代码")
    run_parser.add_argument("submission", help="待测试 Python 文件")
    run_parser.add_argument("--cases", default="cases", help="题库目录或单个题目文件")
    run_parser.add_argument("--timeout-ms", type=int, default=1000, help="单个用例超时时间")
    run_parser.add_argument("--memory-mb", type=int, default=256, help="单个用例内存限制")
    run_parser.add_argument("--expected-problems", type=int, default=100, help="预期题目总数")
    run_parser.add_argument("--json", action="store_true", help="输出机器可读 JSON")
    run_parser.add_argument("--result-dir", default=None, help="测试结果输出目录，默认写入 CodingTest/result")

    validate_parser = subparsers.add_parser("validate", help="校验题库完整性")
    validate_parser.add_argument("--cases", default="cases", help="题库目录或单个题目文件")
    validate_parser.add_argument("--expected-problems", type=int, default=100)
    validate_parser.add_argument("--min-cases", type=int, default=30)

    import_parser = subparsers.add_parser("import-docx", help="从 Word 文档提取题目骨架")
    import_parser.add_argument("docx", help="题目 Word 文档")
    import_parser.add_argument("--out", default="cases", help="输出题目骨架目录")
    import_parser.add_argument("--overwrite", action="store_true", help="允许覆盖已有题目文件")

    args = parser.parse_args(argv)

    if args.command == "run":
        return _run(args)
    if args.command == "validate":
        return _validate(args)
    if args.command == "import-docx":
        return _import_docx(args)
    return 2


def _run(args: argparse.Namespace) -> int:
    try:
        problems = load_problems(args.cases)
        submitted_methods = find_submitted_methods(args.submission)
    except (ProblemLoadError, SubmissionInspectError, OSError, json.JSONDecodeError) as exc:
        print(f"错误：{exc}")
        return 2

    executor = Executor(
        submission=args.submission,
        timeout_ms=args.timeout_ms,
        memory_mb=args.memory_mb,
    )
    if args.json:
        summary = executor.run(
            problems=problems,
            submitted_methods=submitted_methods,
            expected_problems=args.expected_problems,
        )
        output = _summary_to_json(summary)
        print(output)
        _write_result_file(args, output)
        return 0

    _, output = _run_text_stream(args, executor, problems, submitted_methods)
    _write_result_file(args, output)
    return 0


def _run_text_stream(
    args: argparse.Namespace,
    executor: Executor,
    problems,
    submitted_methods: set[str],
) -> tuple[RunSummary, str]:
    started = time.perf_counter()
    output_lines: list[str] = []

    def emit(text: str = "") -> None:
        print(text, flush=True)
        output_lines.append(_strip_ansi(text))

    problem_results = []
    submitted_count = sum(1 for problem in problems if problem.method_name in submitted_methods)
    emit(
        format_header(
            submission=str(Path(args.submission)),
            cases=str(Path(args.cases).resolve()),
            timeout_ms=args.timeout_ms,
        )
    )
    emit(format_engine_start(len(problems)))

    for problem in problems:
        submitted = problem.method_name in submitted_methods
        result = executor.run_problem(problem, submitted)
        problem_results.append(result)
        emit(format_problem_result(result))

    elapsed_ms = int(round((time.perf_counter() - started) * 1000))
    passed_cases = sum(result.passed for result in problem_results)
    total_cases = sum(result.total for result in problem_results)
    summary = RunSummary(
        submitted=submitted_count,
        expected_problems=args.expected_problems,
        total_cases=total_cases,
        passed_cases=passed_cases,
        failed_cases=total_cases - passed_cases,
        elapsed_ms=elapsed_ms,
        problem_results=problem_results,
    )
    emit(format_summary(summary))
    return summary, "\n".join(output_lines) + "\n"


def _write_result_file(args: argparse.Namespace, output: str) -> Path | None:
    result_dir = _resolve_result_dir(args)
    result_file = result_dir / f"{_safe_model_name(args.submission)}.txt"
    try:
        result_dir.mkdir(parents=True, exist_ok=True)
        result_file.write_text(_strip_ansi(output), encoding="utf-8")
    except OSError as exc:
        print(f"结果文件写入失败：{result_file}，原因：{exc}", flush=True)
        return None
    print(f"结果文件  ： {result_file}", flush=True)
    return result_file


def _resolve_result_dir(args: argparse.Namespace) -> Path:
    if args.result_dir:
        return Path(args.result_dir).expanduser().resolve()
    cases_path = Path(args.cases).expanduser().resolve()
    if cases_path.is_dir() and cases_path.name == "cases":
        return cases_path.parent.parent / "result"
    if cases_path.is_file() and cases_path.parent.name == "cases":
        return cases_path.parent.parent.parent / "result"
    return Path.cwd().resolve() / "result"


def _safe_model_name(submission: str) -> str:
    name = Path(submission).stem.strip() or "submission"
    return re.sub(r"[\\/:*?\"<>|]+", "_", name)


def _strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def _validate(args: argparse.Namespace) -> int:
    try:
        problems = load_problems(args.cases)
    except (ProblemLoadError, OSError, json.JSONDecodeError) as exc:
        print(f"错误：{exc}")
        return 2

    messages = validate_problem_set(
        problems,
        expected_problems=args.expected_problems,
        min_cases=args.min_cases,
    )
    if not messages:
        print("题库校验通过")
        return 0
    for message in messages:
        print(f"校验失败：{message}")
    return 1


def _import_docx(args: argparse.Namespace) -> int:
    outline = extract_docx_outline(args.docx)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0
    for item in outline:
        problem_id = item["id"]
        target = out_dir / f"problem_{problem_id}.md"
        if target.exists() and not args.overwrite:
            skipped += 1
            continue
        target.write_text(_problem_md(item), encoding="utf-8")
        created += 1
    print(f"已生成 {created} 个题目骨架到 {out_dir}，跳过 {skipped} 个已有文件")
    return 0


def _problem_md(item: dict[str, str | int]) -> str:
    problem_id = item["id"]
    data = {
        "id": problem_id,
        "title": item["title"],
        "difficulty": item["difficulty"],
        "method": f"question_{problem_id}",
        "cases": [],
    }
    return (
        f"# 题目{problem_id}\n\n"
        f"{item.get('description', '')}\n\n"
        "```json\n"
        f"{json.dumps(data, ensure_ascii=False, indent=2)}\n"
        "```\n"
    )


def _summary_to_json(summary) -> str:
    data = {
        "submitted": summary.submitted,
        "expected_problems": summary.expected_problems,
        "total_cases": summary.total_cases,
        "passed_cases": summary.passed_cases,
        "failed_cases": summary.failed_cases,
        "elapsed_ms": summary.elapsed_ms,
        "problems": [
            {
                "id": result.problem.id,
                "difficulty": result.problem.difficulty,
                "submitted": result.submitted,
                "total": result.total,
                "passed": result.passed,
                "failed": result.failed,
                "elapsed_ms": result.elapsed_ms,
                "cases": [
                    {
                        "name": case.case_name,
                        "passed": case.passed,
                        "elapsed_ms": case.elapsed_ms,
                        "reason": case.reason,
                    }
                    for case in result.case_results
                ],
            }
            for result in summary.problem_results
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
