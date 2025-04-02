# ---------------------------------------------------------------------------
# フォルダ容量を設定して超える場合は古いファイルから削除するプログラム
# https://www.farmsoft.jp/2461/
# ---------------------------------------------------------------------------
import os       # OSに依存しているさまざまな機能を利用するためのモジュール
import glob     # 引数に指定されたパターンにマッチするファイルパス名を取得
import math     # C標準で定義された数学関数へのアクセスを取得
import sys      # システム固有のパラメーターと関数を取得
import argparse
import textwrap
# ---------------------------------------------------------------------------
# 設定
# ---------------------------------------------------------------------------
# フォルダサイズを算出する関数
def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total
# ---------------------------------------------------------------------------
# バイトを適切な単位に変換する関数
def convert_size(size):
    units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB")
    i = math.floor(math.log(size, 1024)) if size > 0 else 0
    size = round(size / 1024 ** i, 2)
    return f"{size} {units[i]}"
# ---------------------------------------------------------------------------
def remv(size, types, sflag):
    script_path = os.path.abspath(sys.argv[0])  # 本実行スクリプトの絶対パス＋ファイル名を取得
    path = os.path.dirname(script_path) + '\\'  # 本実行スクリプトの絶対パスを取得
    folder_size = get_dir_size(path)            # フォルダサイズ算出

    print(f'削除対象フォルダパス：{path}')
    print(f'本実行スクリプトの絶対パス：{script_path}')
    
    # フォルダサイズが最大フォルダサイズより小さい場合は終了
    if folder_size <= size:
        print(f'現在のフォルダサイズは[{convert_size(folder_size)}]です。')
        return
    # 削除するサイズを計算
    rsize = folder_size - size

    # フォルダ内にある対象拡張子のファイル一覧を取得
    files = []
    for t in types:
        files += glob.glob(path + '*' + t)
    if len(files) == 0:
        print(f'現在のフォルダサイズは[{convert_size(folder_size)}]です。')
        return

    # ファイル名と作成日時（エポック秒）の2次元リストを作成
    # [['ファイル名', 作成日時（エポック秒）],['ファイル名', 作成日時（エポック秒）],...]
    flist = []
    for file in files:
        # 本実行スクリプトは除外
        if file == script_path:
            continue
        # ファイルリストに['ファイル名', 作成日時（エポック秒）]を追加
        f_name = os.path.basename(file)
        ctime  = os.path.getctime(file)
        flist.append([f_name, ctime])

    # ファイルリストを要素２つ目の作成日時（エポック秒）で昇順ソート
    flist.sort(key=lambda x: x[1])

    # ファイルリストの作成日時（エポック秒）が古いものからファイルサイズを取得し、
    # 削除するファイルを特定
    total = 0
    lv = []
    rc = 0
    print('------------------------------')
    for i in range(len(flist)):
        # フォルダは除外しファイルのみ対象
        if os.path.isfile(path + flist[i][0]):
            total += os.path.getsize(path + flist[i][0])
            lv.append(i)
            rc = 1 + rc
            print(f'{flist[i][0]}')
            if rsize <= total:
                break
    print('------------------------------')
    print(f'{rc}個のファイル（合計サイズ[{convert_size(total)}]）を削除します。')

    # 削除確認
    if not sflag:
        while True:
            choice = input("削除を実行しますか？ [y/N]: ").lower()
            if choice in ['y', 'ye', 'yes']:
                break
            else:
                print('削除を中止します。')
                return

    # 特定したファイルを削除
    for i in range(len(lv)):
        os.remove(path + flist[lv[i]][0])
        print(f'削除したファイル名：{flist[lv[i]][0]}')
    print(f'現在のフォルダサイズは[{convert_size(folder_size-total)}]です。')
# ---------------------------------------------------------------------------
if __name__=='__main__':
    # 引数を設定
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter, 
        description=textwrap.dedent('''\
            フォルダ容量を指定し、その容量を超える分のファイルを古いものから削除するプログラム。
            '''))
    parser.add_argument('size', nargs='?', default=0, type=float,   # 必須引数
                        help='フォルダ容量を指定[GByte]')
    parser.add_argument('-t', '--type', default='*', nargs='*',     # オプション引数
                        help=textwrap.dedent('''\
                            削除対象とするファイル拡張子を指定
                            ex) [-t mp4 png] ⇒ *.mp4 *.png のみ削除対象とする 
                            '''))
    parser.add_argument('-s', '--silent', action='store_true',      # オプション引数
                        help='サイレントモード（削除する時の確認が不要な場合に使用）')
    args = parser.parse_args()

    if args.size == 0:
        sys.exit('[ERROR]フォルダ容量が指定されていません。\nフォルダ容量を指定するにはヘルプ[-h]を確認してください。')

    remv(args.size*1024*1024*1024, args.type, args.silent)
# ---------------------------------------------------------------------------
