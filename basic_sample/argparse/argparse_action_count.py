# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法（argparse）
# https://www.farmsoft.jp/2593/
# ---------------------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count', default=0)
args = parser.parse_args()
print(f'verbose={args.verbose}')
