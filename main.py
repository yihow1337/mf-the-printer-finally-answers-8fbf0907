#!/usr/bin/env python3
"""Write the competition artifact: one line, the office printer's comeback.

Reads the line from entry.txt (next to this file) and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when that is unset.
Deterministic: the same bytes every run.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")


def load_line():
    """Return the single line, checked against the gate before it is written."""
    with open(SOURCE, encoding="utf-8") as fh:
        line = fh.read().strip()
    # entry.txt keeps a trailing newline for tidy diffs; the artifact is the
    # bare line, so nothing but the comeback reaches the judge.
    if not 1 <= len(line) <= 240:
        raise SystemExit("entry.txt must hold 1 to 240 characters of text")
    if "\n" in line:
        raise SystemExit("the entry is a single line")
    return line


def main():
    line = load_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    # newline="" keeps the bytes byte-for-byte identical on every platform.
    with open(target, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)
    print("wrote %s (%d characters)" % (target, len(line)), file=sys.stderr)


if __name__ == "__main__":
    main()
