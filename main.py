"""Two Lines to Your Past Self — entry writer.

Deterministic: writes the chosen two-line warning to /output/entry.txt.
The entry is exactly two lines, 260 characters, no trailing newline.
"""

import os

LINE_1 = (
    "Don't step out of Grandpa's hospital room on his last evening "
    "to take that call from work \u2014 stay, he was asking for you by name."
)
LINE_2 = (
    "The call could have waited, but his voice asking for you was "
    "the last thing he said, and you have spent years wishing you heard it."
)


def main() -> None:
    entry = LINE_1 + "\n" + LINE_2
    # Gate self-check: exactly two lines, 1-280 characters, not only whitespace.
    lines = entry.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert 1 <= len(entry) <= 280, "entry must be 1-280 characters"
    assert entry.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
