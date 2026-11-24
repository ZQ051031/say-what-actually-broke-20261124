"""Write the "Say What Actually Broke" entry to /output/entry.txt.

One line of software error copy: it names the real failure (the disk
filled up in the middle of a save), says what happened to the user's
file, tells them what to do next, and admits the embarrassing part —
the logs that would have explained why are gone, because they were
deleted to make room.
"""

import os

ENTRY = (
    "The disk filled up mid-save, so your file is half-written. "
    "Free up space and retry; the logs that would have explained why "
    "were deleted to make room."
)


def main() -> None:
    # The gate requires 1-200 characters, a single line, not only
    # whitespace, and no trailing newline. Fail loudly here rather
    # than shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
