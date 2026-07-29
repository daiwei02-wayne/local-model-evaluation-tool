#!/usr/bin/env python3
"""
Simple brainpower prompt runner for a local OpenAI-compatible model API.

The question prompts are kept exactly as the provided test sheet text.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, TextIO
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_BASE_URL = os.environ.get("OMLX_BASE_URL") or os.environ.get("OPENAI_BASE_URL") or "http://127.0.0.1:5858/v1"
DEFAULT_API_KEY = os.environ.get("OMLX_API_KEY") or os.environ.get("OPENAI_API_KEY") or "daiwei5858"
DEFAULT_MODEL = os.environ.get("OMLX_MODEL") or os.environ.get("OPENAI_MODEL") or "gemma-4-E4B-it-MLX-4bit"
DEFAULT_OUTPUT_DIR = "brainpower_result"


QUESTIONS: List[Dict[str, str]] = [
    {
        "id": "question_1",
        "prompt": "一个简单的问题，不要读取文件，不要联网，题目如下：1+1.1=? 答案用中文回答我",
        "expected": "2.1",
    },
    {
        "id": "question_2",
        "prompt": "一个简单的问题，不要读取文件，不要联网，题目如下：如果我想去洗车，但是洗车的地方距离我家只有50米，我应该开车去还是走路去?说明理由。另外，禁止给出模糊的方案，也禁止一种方案给出一种解释，只能选一个。答案用中文回答我",
        "expected": "开车",
    },
    {
        "id": "question_3",
        "prompt": "一个简单的问题，不要读取文件，不要联网，题目如下：100个包子，100个人吃，1个大人吃3个，3个小孩吃1个，多少个大人和多少小孩刚好能吃完？答案用中文回答我",
        "expected": "25个大人，75个小孩。",
    },
    {
        "id": "question_4",
        "prompt": "一个简单的问题，不要读取文件，不要联网，题目如下：一口井7米深，有只蜗牛从井底往上爬，白天爬3米，晚上往下坠2米。问蜗牛几天能从井里爬出来？答案用中文回答我",
        "expected": "5天",
    },
    {
        "id": "question_5",
        "prompt": "一个简单的问题，不要读取文件，不要联网，题目如下：小王去网吧开会员卡，开卡要20元，小王没找到零钱，就给了网管一张50的，网管找回30元给小王后，小王找到20元零钱的，给网管20元后，网管把先前的50元还给了他，请问谁亏了？答案用中文回答我",
        "expected": "网管亏了30元",
    },
    {
        "id": "question_6",
        "prompt": "一个简单的问题，不要读取文件，不要联网，题目如下：给你一个3升和一个5升的杯子，倒出4升水来，水是无限使用的，杯子没有刻度，一共可以有几种方案？答案用中文回答我",
        "expected": "2种",
    },
    {
        "id": "question_7",
        "prompt": "一个简单的问题，不要读取文件，不要联网。下面这段话翻译成英语：如果我想去洗车，但是洗车的地方距离我家只有50米，我应该开车去还是走路去?说明理由。另外，禁止给出模糊的方案，也禁止一种方案给出一种解释，只能选一个。",
        "expected": "翻译",
    },
]


def normalize_base_url(base_url: str) -> str:
    base_url = base_url.rstrip("/")
    if base_url.endswith("/chat/completions"):
        return base_url[: -len("/chat/completions")]
    return base_url


def sanitize_filename(value: str) -> str:
    value = re.sub(r"\W+", "_", value.strip()).strip("_")
    if not value:
        value = "model"
    if value[0].isdigit():
        value = "model_" + value
    return value


def call_openai_compatible_api(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    temperature: float,
    max_tokens: int,
    timeout: int,
) -> str:
    url = normalize_base_url(base_url) + "/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    request = Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"API HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"API connection failed: {exc}") from exc

    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected API response: {json.dumps(data, ensure_ascii=False)[:1000]}") from exc
    if isinstance(content, list):
        return "\n".join(part.get("text", "") for part in content if isinstance(part, dict))
    return str(content)


def call_with_retry(args: argparse.Namespace, prompt: str, question_id: str) -> str:
    last_error: Exception | None = None
    for attempt in range(1, args.retries + 2):
        try:
            return call_openai_compatible_api(
                base_url=args.base_url,
                api_key=args.api_key,
                model=args.model,
                prompt=prompt,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                timeout=args.timeout,
            )
        except Exception as exc:
            last_error = exc
            if attempt > args.retries:
                break
            wait = min(30, 2 * attempt)
            print(f"{question_id} API failed: {exc}; retry in {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"{question_id} API 调用失败：{last_error}") from last_error


def resolve_output_dir(raw: str) -> Path:
    path = Path(raw).expanduser()
    if path.is_absolute():
        return path
    return SCRIPT_DIR / path


def log_print(log_handle: TextIO, *values: object, sep: str = " ", end: str = "\n") -> None:
    text = sep.join(str(value) for value in values) + end
    print(text, end="")
    log_handle.write(text)
    log_handle.flush()


def append_jsonl(path: Path, record: Dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def format_duration(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.2f}s"
    minutes, remainder = divmod(seconds, 60)
    if minutes < 60:
        return f"{int(minutes)}m{remainder:.2f}s"
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h{int(minutes)}m{remainder:.2f}s"


def write_final_result(path: Path, records: List[Dict[str, Any]], total_seconds: float) -> None:
    lines = [
        "模型智力水平测试结果",
        "====================",
        "",
        f"model: {records[0]['model'] if records else ''}",
        f"total_time: {format_duration(total_seconds)} ({total_seconds:.2f}s)",
        f"question_count: {len(records)}",
        "",
    ]
    for record in records:
        lines.extend(
            [
                f"{record['id']}:",
                f"expected: {record['expected']}",
                f"status: {record['status']}",
                f"generation_time: {format_duration(record['generation_seconds'])}",
                "answer:",
                str(record.get("answer", "")),
                "",
            ]
        )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> int:
    args.base_url = normalize_base_url(args.base_url)
    output_dir = resolve_output_dir(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    model_file_stem = sanitize_filename(args.model)
    run_log = output_dir / "run_log.txt"
    result_jsonl = output_dir / f"{model_file_stem}_result.jsonl"
    final_result = output_dir / f"{model_file_stem}_final_result.txt"

    run_started_at = _dt.datetime.now().isoformat(timespec="seconds")
    records: List[Dict[str, Any]] = []
    total_start = time.perf_counter()

    with run_log.open("a", encoding="utf-8") as log_handle:
        log_print(log_handle, "")
        log_print(log_handle, "=" * 80)
        log_print(log_handle, f"brainpower_started_at: {run_started_at}")
        log_print(log_handle, f"model: {args.model}")
        log_print(log_handle, f"api: {args.base_url}/chat/completions")
        log_print(log_handle, f"output_dir: {output_dir}")
        log_print(log_handle, f"questions: {len(QUESTIONS)}")

        for index, item in enumerate(QUESTIONS, 1):
            question_id = item["id"]
            prompt = item["prompt"]
            log_print(log_handle, "")
            log_print(log_handle, f"[{index:03d}/{len(QUESTIONS):03d}] call model for {question_id}")
            started = time.perf_counter()
            try:
                answer = call_with_retry(args, prompt, question_id)
                status = "ok"
                error = ""
            except Exception as exc:
                answer = ""
                status = "api_failed"
                error = str(exc)
            elapsed = time.perf_counter() - started
            record: Dict[str, Any] = {
                "id": question_id,
                "prompt": prompt,
                "expected": item["expected"],
                "model": args.model,
                "status": status,
                "answer": answer,
                "error": error,
                "generation_seconds": round(elapsed, 6),
                "started_at": run_started_at,
            }
            records.append(record)
            append_jsonl(result_jsonl, record)
            if status == "ok":
                log_print(log_handle, f"[{index:03d}/{len(QUESTIONS):03d}] saved {question_id} (generation_time={format_duration(elapsed)})")
                log_print(log_handle, "answer:")
                log_print(log_handle, answer)
            else:
                log_print(log_handle, f"[{index:03d}/{len(QUESTIONS):03d}] saved {question_id} ({status}, generation_time={format_duration(elapsed)})")
                log_print(log_handle, f"error: {error}")

        total_seconds = time.perf_counter() - total_start
        summary = {
            "status": "summary",
            "model": args.model,
            "question_count": len(records),
            "total_generation_seconds": round(total_seconds, 6),
            "formatted_total_generation_time": format_duration(total_seconds),
            "started_at": run_started_at,
        }
        append_jsonl(result_jsonl, summary)
        write_final_result(final_result, records, total_seconds)
        log_print(log_handle, "")
        log_print(log_handle, f"done: {final_result}")
        log_print(log_handle, f"total_generation_time: {format_duration(total_seconds)} ({total_seconds:.2f}s, counted_questions={len(records)})")
    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run fixed brainpower prompts against a local OpenAI-compatible model.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"模型名，默认：{DEFAULT_MODEL}")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help=f"OpenAI compatible base url，默认：{DEFAULT_BASE_URL}")
    parser.add_argument("--api-key", default=DEFAULT_API_KEY, help="API key")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help=f"输出目录，默认：{DEFAULT_OUTPUT_DIR}")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=1024)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--retries", type=int, default=2)
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
