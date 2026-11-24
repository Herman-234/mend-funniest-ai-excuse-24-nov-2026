#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line (<=200 chars), the funniest excuse an AI agent could
offer after failing a task, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic: same bytes every run.
No network, no randomness, no files read.
"""

import os
import sys

LINE = "I delegated your task to a smarter model. It sent back an invoice and a resignation letter."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"entry is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
