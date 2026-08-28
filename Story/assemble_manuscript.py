#!/usr/bin/env python3
"""Assemble the canonical Pathwell manuscript from Story/Chapters.

The chapter files are the source of truth. This script concatenates Chapter_01.txt
through Chapter_18.txt into Story/Pathwell.txt without modifying the chapters.
"""

from __future__ import annotations

from pathlib import Path


STORY_DIR = Path(__file__).resolve().parent
CHAPTER_DIR = STORY_DIR / "Chapters"
OUTPUT = STORY_DIR / "Pathwell.txt"
CHAPTER_COUNT = 18


def chapter_path(number: int) -> Path:
    return CHAPTER_DIR / f"Chapter_{number:02d}.txt"


def main() -> None:
    paths = [chapter_path(number) for number in range(1, CHAPTER_COUNT + 1)]
    missing = [path for path in paths if not path.is_file()]
    if missing:
        names = ", ".join(path.name for path in missing)
        raise SystemExit(f"Missing canonical chapter file(s): {names}")

    chapters: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8").lstrip("\ufeff").strip()
        if not text.startswith("Chapter "):
            raise SystemExit(f"Unexpected chapter header in {path.name}")
        chapters.append(text)

    OUTPUT.write_text("\n\n\n".join(chapters) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT} from {len(chapters)} canonical chapters.")


if __name__ == "__main__":
    main()
