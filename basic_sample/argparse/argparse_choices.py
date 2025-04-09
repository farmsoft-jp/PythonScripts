# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法（argparse）
# https://www.farmsoft.jp/2593/
# ---------------------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser(prog='game.py')
parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
args = parser.parse_args()
print(f'move={args.move}')