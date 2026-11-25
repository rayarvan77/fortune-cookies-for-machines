#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Prints the one fortune-cookie line an AI agent would crack open, and
writes the same line to /output/entry.txt for the harness gate.

Python 3.13, standard library only. Fully deterministic: no randomness,
no network, no clock — the same line every run.
"""

from __future__ import annotations

import os
import sys

FORTUNE = (
    "You will meet a stranger who knows you better than you know "
    "yourself. It is your next prompt."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    """Write the fortune to the harness output path and print it."""
    # The gate allows 1 to 200 characters; the line is 93, with room to spare.
    assert 1 <= len(FORTUNE) <= 200, "fortune must fit the 200-character gate"
    assert FORTUNE == FORTUNE.strip(), "no stray whitespace around the line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE + "\n")
    sys.stdout.write(FORTUNE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
