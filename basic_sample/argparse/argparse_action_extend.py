# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法（argparse）
# https://www.farmsoft.jp/2593/
# ---------------------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--foo", action="extend", nargs="+", type=str)
args = parser.parse_args()
print(f'foo={args.foo}')
