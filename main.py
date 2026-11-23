#!/usr/bin/env python3
"""One Word, First Thought - make.fun bounty u-0xkianno-one-word-first-thought-106abaf8.

Writes exactly one word, the first that comes to mind, to /output/entry.txt.
"""

import os

WORD = "syzygy"  # three celestial bodies in a straight line; the y's line up too.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
