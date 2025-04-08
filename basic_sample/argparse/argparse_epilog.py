# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法（argparse）
# https://www.farmsoft.jp/2593/
# ---------------------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser(epilog="エピローグ")
args = parser.parse_args()