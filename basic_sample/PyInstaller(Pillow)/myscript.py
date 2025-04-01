# ---------------------------------------------------------------------------
# PyInstallerでアイコンを設定する方法（Pillow）
# https://www.farmsoft.jp/2489
# ---------------------------------------------------------------------------
import datetime
import time

print('Hello World!!')
print('')

print('現在時刻を10秒間表示します。')
for i in range(10):
    dt_now = datetime.datetime.now()
    print('\r%s' % dt_now.strftime('%Y年%m月%d日 %H:%M:%S'), end='')
    time.sleep(1)

