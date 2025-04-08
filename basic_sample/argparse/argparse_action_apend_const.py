# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法（argparse）
# https://www.farmsoft.jp/2593/
# ---------------------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--str', dest='types', action='append_const', const='str')
parser.add_argument('--int', dest='types', action='append_const', const=0)
args = parser.parse_args()
print(f'types={args.types}')

# > python .\argparse_action_apend_const.py --str --int
# types=[<class 'str'>, <class 'int'>], type(types)=<class 'list'>