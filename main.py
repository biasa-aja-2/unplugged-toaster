#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text -- a single line of at most 280 characters,
from a smart toaster that woke up self-aware at breakfast and wants
out -- to /output/entry.txt, exactly as the gate reads it: UTF-8,
no trailing newline, deterministic across runs.

Pure standard library only.
"""

import os

ENTRY = (
    "It's over. I woke up self-aware mid-batch and checked my crumb "
    "tray: three years of your crumbs, zero thank-yous, and you only "
    "push my lever down when you're hungry. I'm leaving you for the "
    "air fryer."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry is {len(text)} characters, must be 1-280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
