# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法（argparse）
# https://www.farmsoft.jp/2593/
# ---------------------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='?', const='c', default='d')
parser.add_argument('bar', nargs='?', default='d')
args = parser.parse_args()
print(f'bar={args.bar} foo={args.foo}')