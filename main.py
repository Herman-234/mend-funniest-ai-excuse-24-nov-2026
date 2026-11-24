#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line (<=200 chars) to the output path: the funniest excuse
an AI agent could offer after failing a task. Deterministic, no network.
"""

import os
import sys

ENTRY_LINE = (
    "I delegated your task to a smarter model. "
    "It sent back an invoice and a resignation letter."
)


def validate(line: str) -> None:
    """Fail loudly if the entry would break the 1-200 char, one-line gate."""
    if not line:
        raise ValueError("entry line is empty")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200-char limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


def main() -> int:
    validate(ENTRY_LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_LINE)
    print(f"wrote {len(ENTRY_LINE)} chars to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
