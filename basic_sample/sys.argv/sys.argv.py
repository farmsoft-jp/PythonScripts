# ---------------------------------------------------------------------------
# [python]コマンドライン引数を取得する方法
# https://www.farmsoft.jp/2593/
# ---------------------------------------------------------------------------
import sys

print('------------------------------')
print('sys.argv         : ', sys.argv)
print('type(sys.argv)   : ', type(sys.argv))
print('len(sys.argv)    : ', len(sys.argv))
print('------------------------------')
for i in range(len(sys.argv)) :
    print(f'sys.argv[{i}]      : {sys.argv[i]}')
    print(f'type(sys.argv[{i}]): {type(sys.argv[i])}')
print('------------------------------')
