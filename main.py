#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single original line of text to /output/entry.txt:
a quiet, earned moment of pride for a night guard who taught
himself to read by torchlight and finishes the last page at dawn.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "The night guard who taught himself to read by torchlight "
    "finished the last page as the sun came up."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 240 characters, not only whitespace.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, gate wants 1-240"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
