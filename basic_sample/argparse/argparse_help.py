# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法（argparse）
# https://www.farmsoft.jp/2593/
# ---------------------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser(prog='frobble')
parser.add_argument('bar', nargs='?', type=int, default=42,
                    help='the bar to %(prog)s (default: %(default)s)')
args = parser.parse_args()
print(f'move={args.move}')