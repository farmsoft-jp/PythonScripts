# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法（argparse）
# https://www.farmsoft.jp/2593/
# ---------------------------------------------------------------------------
import argparse

# 1. ArgumentParser オブジェクト
parser = argparse.ArgumentParser()

# 2. add_argument() メソッド
parser.add_argument('arg')              # 位置（必須）引数
parser.add_argument('-o', '--option')   # オプション引数

# 3. parse_args() メソッド
args = parser.parse_args()

print(f'arg    = {args.arg}')
print(f'option = {args.option}')