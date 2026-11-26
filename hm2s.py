#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Genga Ueda
# SPDX-License-Identifier: BSD-3-Clause

import sys
import re


def parse_input(text):
    text = text.strip()

    match_hm = re.fullmatch(r"(\d+)h(\d+)m", text)
    if match_hm:
        hours = int(match_hm.group(1))
        minutes = int(match_hm.group(2))
        return [hours * 3600 + minutes * 60]

    match_h = re.fullmatch(r"(\d+)h", text)
    if match_h:
        hours = int(match_h.group(1))
        return [hours * 60, hours * 3600]

    raise ValueError("無効な入力です")


def main():
    has_input = False
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped:
            continue
        has_input = True
        try:
            results = parse_input(stripped)
            for val in results:
                print(val)
        except ValueError as e:
            sys.stderr.write(f"エラー: {e}\n")
            sys.exit(1)

    if not has_input:
        sys.stderr.write("エラー: 入力がありません\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
