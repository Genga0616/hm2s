Markdown
# hm2s

![test](https://github.com/Genga0616/hm2s/actions/workflows/test.yml/badge.svg)

標準入力から `<hours>h<minutes>m` または `<hours>h` 形式の時間文字列を読み込み、秒数（`<hours>h` の場合は分と秒）に変換して標準出力に出力するコマンドです。

## インストール方法

```bash
git clone [https://github.com/Genga0616/hm2s.git](https://github.com/Genga0616/hm2s.git)
cd hm2s
使い方
<hours>h<minutes>m を入力した場合（秒数を出力）
Bash
$ echo "1h30m" | ./hm2s.py
5400
<hours>h を入力した場合（分と秒を改行して出力）
Bash
$ echo "2h" | ./hm2s.py
120
7200
複数行をまとめて変換する場合
Bash
$ printf "1h0m\n0h15m\n" | ./hm2s.py
3600
900
必要なソフトウェア
Python

テスト済みバージョン: 3.10〜3.14

テスト環境
Ubuntu 24.04 LTS

ライセンス
このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

© 2026 Genga Ueda
