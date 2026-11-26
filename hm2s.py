#!/usr/bin/python3

import sys
import re


def parse_hm(text):
    match = re.fullmatch(r"(\d+)h(\d+)m", text.strip())
    if not match:
        raise ValueError(f"Invalid format: '{text.strip()}' (expected: <hours>h<minutes>m)")

    hours = int(match.group(1))
    minutes = int(match.group(2))
    return hours * 3600 + minutes * 60


def main():
    has_input = False
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped:
            continue
        has_input = True
        try:
            seconds = parse_hm(stripped)
            print(seconds)
        except ValueError as e:
            sys.stderr.write(f"Error: {e}\n")
            sys.exit(1)

    if not has_input:
        sys.stderr.write("Error: no input provided\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
