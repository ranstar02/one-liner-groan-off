"""One-liner Groan-Off entry.

Writes a single original one-line dad joke to /output/entry.txt.
Python 3.13, standard library only. Deterministic: no randomness,
no network, no secrets, no files read outside this repository.
"""

import os

LINE = "I told my alarm clock a joke \u2014 it didn't laugh, it just hit snooze on the punchline."

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not LINE.strip():
        raise ValueError("LINE must not be empty or only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("LINE must be a single line")
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"LINE must be 1-{MAX_CHARS} characters, got {len(LINE)}")

    output_path = os.environ.get("ENTRY_OUTPUT_PATH", OUTPUT_PATH)
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(output_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("verification failed: file content differs from LINE")

    print(f"{len(LINE)} characters")
    print(LINE)


if __name__ == "__main__":
    main()
