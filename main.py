"""The Vacuum's Alibi: write the robot vacuum's excuse to /output/entry.txt.

One line, at most 200 characters: the excuse a robot vacuum gives for
missing a spot. Deadpan, a little smug about its sensors, its schedule
and its battery — with the punch at the end.
"""

import os

ENTRY = (
    "I mapped that spot at 06:42, named the dust bunny Gerald, and my "
    "schedule says he's a tenant now \u2014 eviction is not in my battery's budget."
)


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
