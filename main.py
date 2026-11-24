#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry program.

Writes one funny one-line review of Monday to /output/entry.txt.
"""

import os

ENTRY = (
    "Monday gets one star: my alarm filed for overtime, "
    "my coffee filed a complaint, and my 9 a.m. meeting "
    "could have been an email \u2014 and it was only 9:05."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the one-line review.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
