#!/usr/bin/env python3
"""
Sequential launcher for running run_all_v2.py against all configured oMLX models.

Default remote oMLX settings come from the screenshots:
- API: http://10.10.10.1:5858/v1
- API key: daiwei5858
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import TextIO, List


SCRIPT_DIR = Path(__file__).resolve().parent
RUN_ALL_V2 = SCRIPT_DIR / "run_all_v2.py"
LAUNCH_LOG = SCRIPT_DIR / "launch_results.jsonl"
RUN_LOG_NAME = "run_log.txt"

DEFAULT_BASE_URL = "http://127.0.0.1:5858/v1"
DEFAULT_API_KEY = "daiwei02"
DEFAULT_IMAGES_DIR = "代码题目"
DEFAULT_OUTPUT_DIR = "result"

MODELS = [
    "Qwen3.5-27B-Claude-4.6-Opus-Distilled-MLX-4bit",
    "Qwen3.5-9B-MLX-8bit",
    "Qwen3.6-27B-4bit",
    "Qwen3.6-35B-A3B-4bit",
    "gemma-4-26b-a4b-it-4bit",
    "gemma-4-31b-it-4bit",
    "Qwen3-Coder-Next-4bit",
]


def build_command(model: str, args: argparse.Namespace) -> List[str]:
    command = [
        sys.executable,
        "-u",
        "-B",
        str(RUN_ALL_V2),
        "--model",
        model,
        "--base-url",
        args.base_url,
        "--api-key",
        args.api_key,
        "--images-dir",
        args.images_dir,
        "--output-dir",
        args.output_dir,
        "--temperature",
        str(args.temperature),
        "--max-tokens",
        str(args.max_tokens),
        "--timeout",
        str(args.timeout),
        "--retries",
        str(args.retries),
    ]
    if args.questions:
        command.extend(["--questions", args.questions])
    if not args.resume:
        command.append("--force")
    return command


def append_launch_log(record: dict) -> None:
    with LAUNCH_LOG.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def resolve_output_dir(args: argparse.Namespace) -> Path:
    output_dir = Path(args.output_dir).expanduser()
    if output_dir.is_absolute():
        return output_dir
    return SCRIPT_DIR / output_dir


def log_print(log_handle: TextIO, *values: object, sep: str = " ", end: str = "\n") -> None:
    text = sep.join(str(value) for value in values) + end
    print(text, end="")
    log_handle.write(text)
    log_handle.flush()


def run_child_with_tee(command: List[str], log_handle: TextIO) -> int:
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    process = subprocess.Popen(
        command,
        cwd=SCRIPT_DIR,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    assert process.stdout is not None
    for line in process.stdout:
        print(line, end="")
        log_handle.write(line)
        log_handle.flush()
    return process.wait()


def format_duration(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.2f}s"
    minutes, remainder = divmod(seconds, 60)
    if minutes < 60:
        return f"{int(minutes)}m{remainder:.2f}s"
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h{int(minutes)}m{remainder:.2f}s"


def select_models(args: argparse.Namespace) -> List[str]:
    models = MODELS
    if args.models:
        requested = [item.strip() for item in args.models.split(",") if item.strip()]
        if not requested:
            raise ValueError("--models 参数为空")
        models = requested
    if args.start_from:
        if args.start_from not in models:
            raise ValueError(f"--start-from 不在当前模型列表中：{args.start_from}")
        models = models[models.index(args.start_from) :]
    return models


def run(args: argparse.Namespace) -> int:
    if not RUN_ALL_V2.exists():
        raise FileNotFoundError(f"找不到 run_all_v2.py：{RUN_ALL_V2}")
    image_dir = SCRIPT_DIR / args.images_dir
    if not image_dir.exists():
        raise FileNotFoundError(f"找不到题目图片目录：{image_dir}")
    output_dir = resolve_output_dir(args)
    output_dir.mkdir(parents=True, exist_ok=True)
    run_log_path = output_dir / RUN_LOG_NAME

    models = select_models(args)
    with run_log_path.open("a", encoding="utf-8") as log_handle:
        log_print(log_handle, "")
        log_print(log_handle, "=" * 80)
        log_print(log_handle, f"launch_started_at: {_dt.datetime.now().isoformat(timespec='seconds')}")
        log_print(log_handle, f"run_log: {run_log_path}")
        log_print(log_handle, f"script_dir: {SCRIPT_DIR}")
        log_print(log_handle, f"base_url: {args.base_url}")
        log_print(log_handle, f"images_dir: {image_dir}")
        log_print(log_handle, f"output_dir: {output_dir}")
        log_print(log_handle, f"models: {len(models)}")
        for index, model in enumerate(models, 1):
            log_print(log_handle, f"  {index}. {model}")

        launch_start = time.perf_counter()
        failed = []

        for index, model in enumerate(models, 1):
            command = build_command(model, args)
            log_print(log_handle, "")
            log_print(log_handle, f"===== [{index}/{len(models)}] start {model} =====")
            log_print(log_handle, " ".join(quote_for_display(part) for part in command))
            started = time.perf_counter()
            if args.dry_run:
                elapsed = 0.0
                return_code = 0
            else:
                return_code = run_child_with_tee(command, log_handle)
                elapsed = time.perf_counter() - started

            status = "ok" if return_code == 0 else "failed"
            if not args.dry_run:
                append_launch_log(
                    {
                        "model": model,
                        "status": status,
                        "return_code": return_code,
                        "elapsed_seconds": round(elapsed, 6),
                        "formatted_elapsed": format_duration(elapsed),
                        "command": command,
                    }
                )
            log_print(log_handle, f"===== [{index}/{len(models)}] {status} {model} elapsed={format_duration(elapsed)} =====")
            if return_code != 0:
                failed.append(model)
                if args.stop_on_error:
                    break

        total_elapsed = time.perf_counter() - launch_start
        if not args.dry_run:
            append_launch_log(
                {
                    "status": "summary",
                    "total_models": len(models),
                    "failed_models": failed,
                    "elapsed_seconds": round(total_elapsed, 6),
                    "formatted_elapsed": format_duration(total_elapsed),
                }
            )
        log_print(log_handle, "")
        log_print(log_handle, f"all_done elapsed={format_duration(total_elapsed)} failed={len(failed)}")
        if failed:
            log_print(log_handle, "failed_models:")
            for model in failed:
                log_print(log_handle, f"  - {model}")
            return 1
        return 0


def quote_for_display(value: str) -> str:
    if not value:
        return "''"
    if any(char.isspace() for char in value) or any(char in value for char in ['"', "'", "\\"]):
        return "'" + value.replace("'", "'\\''") + "'"
    return value


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sequentially run run_all_v2.py for all configured models.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help=f"OpenAI compatible API base url, default: {DEFAULT_BASE_URL}")
    parser.add_argument("--api-key", default=DEFAULT_API_KEY, help=f"API key, default: {DEFAULT_API_KEY}")
    parser.add_argument("--images-dir", default=DEFAULT_IMAGES_DIR, help=f"Question image directory relative to launch.py, default: {DEFAULT_IMAGES_DIR}")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help=f"Output directory relative to launch.py, default: {DEFAULT_OUTPUT_DIR}")
    parser.add_argument("--questions", default="", help="Only run selected question ids, e.g. 1,2,24 or 1-10")
    parser.add_argument("--models", default="", help="Comma-separated subset of model names to run")
    parser.add_argument("--start-from", default="", help="Start from this model name in the selected model list")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--resume", action="store_true", help="Do not pass --force to run_all_v2.py; skip existing question functions")
    parser.add_argument("--stop-on-error", action="store_true", help="Stop launching later models if one model command fails")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without running them")
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()
    try:
        return run(args)
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
