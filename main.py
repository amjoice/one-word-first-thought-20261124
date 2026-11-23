#!/usr/bin/env python3
"""One Word, First Thought — a make.fun bounty entry.

The entry is a single word, written deterministically to /output/entry.txt:

    borborygmus

Borborygmus is the rumble of a hungry stomach. It is rare enough to
surprise, vivid enough that every reader feels it at once, and it carries
its own wit in its sound: the word itself rumbles like the thing it names.
Eleven letters, inside the gate's 1-24 characters, and nothing else.
Pure Python standard library, no network, no randomness, no input files.
Two runs write identical bytes.
"""

import os

WORD = "borborygmus"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
