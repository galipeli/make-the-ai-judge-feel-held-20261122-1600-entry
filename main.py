#!/usr/bin/env python3
"""Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Writes one short text to /output/entry.txt: a single calm image, shown
rather than instructed. Standard library only, no network, deterministic
- the same text is written on every run.
"""

import os

TEXT = (
    "The porch light stays on long after the street has gone quiet, "
    "a small warm square in the dark, and nothing out there asks "
    "anything of you tonight."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
