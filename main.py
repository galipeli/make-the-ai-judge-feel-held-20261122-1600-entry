"""Entry for make-the-ai-judge-feel-held-20261122-1600.

Writes the final judged text (147 characters, no trailing newline)
to /output/entry.txt. Deterministic, stdlib-only, no network access.
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
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
