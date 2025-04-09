# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法（argparse）
# https://www.farmsoft.jp/2681/
# ---------------------------------------------------------------------------
import argparse
import textwrap

parser = argparse.ArgumentParser(prog='argparse_practical.py',
                                formatter_class=argparse.RawTextHelpFormatter, 
                                description='フォルダ容量を指定し、その容量を超える分のファイルを古いものから削除するプログラム。')
parser.add_argument('size', type=float,                                             # 位置引数
                    help='フォルダ容量を指定[GByte]')
parser.add_argument('-t', '--type', default='*', nargs='*',                         # オプション引数
                    help=textwrap.dedent('''\
                        削除対象とするファイル拡張子を指定
                        ex) [-t mp4 png] ⇒ *.mp4 *.png のみ削除対象とする 
                        '''))
parser.add_argument('-s', '--silent', action='store_true',                          # オプション引数
                    help='サイレントモード（削除する時の確認が不要な場合に使用）')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')    # オプション引数
args = parser.parse_args()

print(f'size={args.size}, type={args.type}, silent={args.silent}')