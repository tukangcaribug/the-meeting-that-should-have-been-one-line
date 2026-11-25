#!/usr/bin/env python3
"""The meeting that should have been one line.

Running this script drops the entry line into entry.txt under
$MAKEFUN_OUTPUT_DIR (falling back to /output). The output is byte-for-byte
identical on every run: no trailing newline, no timestamps, no randomness.
"""

import os
import sys

ENTRY = "9 people, 47 minutes, 0 decisions — ship it Tuesday, send the doc, and cancel the next meeting."

MIN_CHARS = 1
MAX_CHARS = 200


def _check(entry: str) -> None:
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(entry)} chars, outside {MIN_CHARS}-{MAX_CHARS}"
        )
    if not entry.strip():
        raise SystemExit("entry must not be blank")


def _emit(entry: str) -> str:
    # newline="" keeps the em dash and the final period byte-exact;
    # the file ends with the last character of the line, nothing after it.
    target = os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
    )
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry)
    return target


if __name__ == "__main__":
    _check(ENTRY)
    _emit(ENTRY)
    sys.exit(0)
