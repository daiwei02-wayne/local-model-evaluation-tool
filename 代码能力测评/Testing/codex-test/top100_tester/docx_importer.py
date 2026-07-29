from __future__ import annotations

import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree


QUESTION_RE = re.compile(r"(?:题目|第)\s*(\d+)\s*(?:题)?")
HEADING_RE = re.compile(r"^(\d+)\.\s+(.+)$")
DIFFICULTY_RE = re.compile(r"(简单|中等|困难)")


def extract_docx_outline(docx_path: str | Path) -> list[dict[str, str | int]]:
    """Extract a best-effort question outline from a docx file.

    The importer intentionally does not guess function signatures or test answers.
    It only helps turn a Word document into editable problem skeletons.
    """

    path = Path(docx_path)
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml")

    root = ElementTree.fromstring(xml)
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    paragraphs: list[str] = []
    for paragraph in root.findall(".//w:p", namespace):
        texts = [node.text or "" for node in paragraph.findall(".//w:t", namespace)]
        text = "".join(texts).strip()
        if text:
            paragraphs.append(text)

    hot100_outline = _extract_hot100_blocks(paragraphs)
    if hot100_outline:
        return hot100_outline

    outline: list[dict[str, str | int]] = []
    current: dict[str, str | int] | None = None
    for text in paragraphs:
        question_match = QUESTION_RE.search(text)
        if question_match:
            if current:
                outline.append(current)
            difficulty_match = DIFFICULTY_RE.search(text)
            current = {
                "id": int(question_match.group(1)),
                "title": text,
                "difficulty": difficulty_match.group(1) if difficulty_match else "中等",
                "description": "",
            }
        elif current:
            current["description"] = f"{current['description']}\n{text}".strip()

    if current:
        outline.append(current)
    return outline


def _extract_hot100_blocks(paragraphs: list[str]) -> list[dict[str, str | int]]:
    starts: list[tuple[int, int, str]] = []
    for index, text in enumerate(paragraphs):
        match = HEADING_RE.match(text)
        if not match:
            continue
        if "题号" in paragraphs[index + 1 : index + 8]:
            starts.append((index, int(match.group(1)), match.group(2).strip()))

    if len(starts) < 2:
        return []

    outline: list[dict[str, str | int]] = []
    for position, (start, problem_id, title) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else len(paragraphs)
        block = paragraphs[start:end]
        difficulty = _find_first_difficulty(block) or "中等"
        description = _slice_section(block, "题目描述", "Java 接口 Demo")
        outline.append(
            {
                "id": problem_id,
                "title": title,
                "difficulty": difficulty,
                "description": description,
            }
        )
    return outline


def _find_first_difficulty(block: list[str]) -> str | None:
    for text in block[:20]:
        match = DIFFICULTY_RE.search(text)
        if match:
            return match.group(1)
    return None


def _slice_section(block: list[str], start_marker: str, end_marker: str) -> str:
    try:
        start = block.index(start_marker) + 1
    except ValueError:
        start = 1
    try:
        end = block.index(end_marker)
    except ValueError:
        end = len(block)
    return "\n".join(block[start:end]).strip()
