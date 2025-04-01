# ---------------------------------------------------------------------------
# instagram自動いいね
# https://www.farmsoft.jp/
# ---------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pickle,os
import time
import random
import requests
# ---------------------------------------------------------------------------
# 設定
# ---------------------------------------------------------------------------
USER = [["320farm", "mitsuo0320"], ["moka_bike99", "mitsuo0320"]]
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 1080
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1352130376734216222/lgYebDIeQexl_OyxAgiubVauOscnxV9IwSLteHPH09kDSlom56NOhVDGraOvvQHTM5J9"
# ---------------------------------------------------------------------------
driver : webdriver
INSTAGRAM_URL = "https://www.instagram.com/accounts/login/?source=auth_switcher"
position_y = SCREEN_HEIGHT / 2
nice_count = 0
# ---------------------------------------------------------------------------
def insta_init():
    global driver
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(SCREEN_WIDTH, SCREEN_HEIGHT)
    driver.set_window_position(0, 0)
# ---------------------------------------------------------------------------
def insta_end():
    driver.close(), driver.quit()
# ---------------------------------------------------------------------------
# ログイン
def login(username, password):
    cookies_file = username + '.pkl'  # クッキーを保存するファイルの名前
    if not os.path.exists(cookies_file):
        # メアドとパスワードを入力
        driver.get(INSTAGRAM_URL)
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys(username)
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(2)
        # ログインボタンを押す
        driver.find_element(By.XPATH, '//div[text()="ログイン"]').click()
        time.sleep(5)
        # クッキー保存
        pickle.dump(driver.get_cookies(), open(cookies_file, 'wb'))
    else:
        # クッキー読込み
        cookies = pickle.load(open(cookies_file, 'rb'))
        driver.get(INSTAGRAM_URL)
        # クッキー設定
        for c in cookies:
            driver.add_cookie(c)
        driver.get(INSTAGRAM_URL)
        time.sleep(5)
    for i in range(2):
        #後で
        try:
            driver.find_element(By.XPATH, '//div[text()="後で"]').click()
            time.sleep(5)
        except:
            pass
# ---------------------------------------------------------------------------
# いいね！ができる記事を検索（広告は除外）
def search_article():
    article_list = driver.find_elements(By.XPATH, '//article')
    for article in article_list:
        svg_list = article.find_elements(By.XPATH, './/*[@aria-label="いいね！"]')
        adv_list = article.find_elements(By.XPATH, './/span[text()="広告"]')
        if len(svg_list) > 0 and len(adv_list) == 0:
            return svg_list
# ---------------------------------------------------------------------------
# 次のいいね！エレメントを検索
def search_nice():
    svg_list = search_article()
    for svg in svg_list:
        if svg.get_attribute('aria-label') == 'いいね！':
            return svg
# ---------------------------------------------------------------------------
# 次の位置までマウススクロールするように移動
def scroll_element(element):
    global position_y
    y = element.location["y"] - position_y
    for i in range(int(y//50)):
        driver.execute_script('window.scrollBy(0, 50);')
        time.sleep(random.uniform(0.03, 0.08))
        if random.random() < 0.1: time.sleep(random.uniform(0.1, 0.5))
    driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center"});', search_nice())
# ---------------------------------------------------------------------------
# いいね！
def push_nice(user_name, nice_num):
    global position_y, nice_count
    nice_count = 0
    actions = ActionChains(driver)
    print(f"アカウント「{user_name}」で、{nice_num}回のいいね！を実行します。")
    for i in range(nice_num):
        try:
            # 画面中央までスクロール
            nice = search_nice()
            scroll_element(nice)
            time.sleep(random.uniform(1.0, 4.0))
            # いいね！クリック
            nice = search_nice()
            position_y = nice.location["y"]
            actions.move_to_element_with_offset(nice, 0, 0).click().perform()
            print(f"{i+1}/{nice_num}回目のいいね！が完了。")
            time.sleep(random.uniform(1.0, 3.0))
        except:
            pass
        else:
            nice_count = nice_count + 1
    print(f"アカウント「{user_name}」で、{nice_count}回のいいね！が完了しました。")
# ---------------------------------------------------------------------------
def send_discord(user_name):
    if DISCORD_WEBHOOK_URL != "":
        data = {"content": f"アカウント「{user_name}」で、{nice_count}回のいいね！が完了しました。"}
        requests.post(DISCORD_WEBHOOK_URL, data=data)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    for user in USER:
        insta_init()
        # ログイン
        login(user[0], user[1])
        # いいね！
        push_nice(user[0], random.randint(40, 80))
        send_discord(user[0])
        # driver終了
        insta_end()
# ---------------------------------------------------------------------------