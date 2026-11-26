#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.

Writes one line, at most 160 characters: an out-of-office auto-reply
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only, no network, no clock, no randomness: running it twice
writes identical bytes. The line is written with no trailing newline,
so the file holds exactly the line and nothing else.
"""

import os
import sys

# An out-of-office reply that admits the inbox triage is fiction.
LINE = (
    "Out of office: I'm recharging my will to live. Emails will be "
    "answered in the order I pretend to have read them."
)


def main() -> int:
    if not 1 <= len(LINE) <= 160:
        print(f"error: line is {len(LINE)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if LINE.strip() == "" or "\n" in LINE:
        print("error: line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(dest, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("error: output does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(written)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
