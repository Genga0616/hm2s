#!/bin/bash -xv
# SPDX-FileCopyrightText: 2026 Genga Ueda
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo "${1}行目が違います"
	res=1
}

res=0

# 普通の入力
out=$(echo "1h30m" | ./hm2s.py)
[ "$?" = 0 ] || ng "$LINENO"
[ "$out" = 5400 ] || ng "$LINENO"

out=$(echo "0h5m" | ./hm2s.py)
[ "$?" = 0 ] || ng "$LINENO"
[ "$out" = 300 ] || ng "$LINENO"

# hだけのとき
out=$(echo "2h" | ./hm2s.py)
[ "$?" = 0 ] || ng "$LINENO"
[ "$out" = $'120\n7200' ] || ng "$LINENO"

# 複数行
out=$(printf "1h0m\n0h1m\n" | ./hm2s.py)
[ "$?" = 0 ] || ng "$LINENO"
[ "$out" = $'3600\n60' ] || ng "$LINENO"

# エラーになる入力
out=$(echo "あいう" | ./hm2s.py 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "$out" = "" ] || ng "$LINENO"

out=$(echo "90m" | ./hm2s.py 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "$out" = "" ] || ng "$LINENO"

out=$(echo "" | ./hm2s.py 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "$out" = "" ] || ng "$LINENO"

[ "$res" = 0 ] && echo "OK"
exit $res
