#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun bounty entry.

Writes a single-line review of Monday to /output/entry.txt.
"""

import os

ENTRY = (
    "Monday reviewed: showed up uninvited, stayed all day, "
    "ruined the weekend's leftovers, and left a meeting on my calendar. "
    "One star."
)


def main() -> None:
    # Bounty rule: the line must be under 200 characters.
    assert len(ENTRY) < 200, f"entry too long: {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
