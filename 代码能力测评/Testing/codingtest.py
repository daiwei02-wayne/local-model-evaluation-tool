#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if args and args[0] in {"-h", "--help"}:
        print("用法:")
        print("  python3 -B codingtest.py ./待测试代码.py")
        print("  python3 -B codingtest.py")
        print("说明:")
        print("  有 1 个参数时，只测试指定 Python 提交脚本。")
        print("  无参数时，按字母顺序测试 ongoing 目录下的所有 .py 脚本。")
        return 0
    if len(args) > 1:
        print("错误: 参数过多。")
        print("用法: python3 -B codingtest.py [./待测试代码.py]")
        return 2

    base_dir = Path(__file__).resolve().parent
    original_cwd = Path.cwd()
    project_root = base_dir / "codex-test"
    cases_dir = project_root / "cases"
    result_dir = base_dir / "result"
    ongoing_dir = base_dir / "ongoing"
    if not cases_dir.exists():
        print(f"错误: 找不到测试用例目录: {cases_dir}")
        return 2

    sys.path.insert(0, str(project_root))
    from top100_tester.cli import main as cli_main

    batch_mode = len(args) == 0
    expected_problems = len(list(cases_dir.glob("problem_*.md")))
    submissions = _resolve_submissions(args, ongoing_dir, original_cwd)
    if not submissions:
        print(f"错误: ongoing 目录下没有可测试的 .py 文件: {ongoing_dir}")
        return 2

    if batch_mode:
        os.chdir(base_dir)

    exit_code = 0
    for index, submission in enumerate(submissions, 1):
        if len(submissions) > 1:
            print("\n" + "#" * 70)
            print(f"批量测试 {index}/{len(submissions)}: {submission}")
            print("#" * 70 + "\n")
        code = cli_main(
            [
                "run",
                str(submission),
                "--cases",
                str(cases_dir),
                "--expected-problems",
                str(expected_problems),
                "--result-dir",
                str(result_dir),
            ]
        )
        if code != 0:
            exit_code = code
    return exit_code


def _resolve_submissions(args: list[str], ongoing_dir: Path, original_cwd: Path) -> list[Path]:
    if args:
        path = Path(args[0]).expanduser()
        return [path if path.is_absolute() else original_cwd / path]
    if not ongoing_dir.exists():
        return []
    return sorted(
        (
            Path("ongoing") / path.name
            for path in ongoing_dir.iterdir()
            if path.is_file() and path.suffix == ".py"
        ),
        key=lambda path: path.name.lower(),
    )


if __name__ == "__main__":
    raise SystemExit(main())
