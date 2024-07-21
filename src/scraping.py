from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import config

# ドライバ設定とURL取得
driver = webdriver.Chrome()
driver.get("https://parents.codmon.com/menu")
time.sleep(1)

# environment variables
codmon_email = config.CODMON_EMAIL
codmon_password = config.CODMON_PASSWORD

# ブラウザの操作
# 「すでにアカウントをお持ちの方」画面
time.sleep(3)
elm = driver.find_element(by=By.CSS_SELECTOR, value="body > div > div:nth-child(1) > ons-page > ons-page > div.page__content > ons-navigator > ons-page > div.page__content > section > div.menu__loginLink")
elm.click()
time.sleep(3)
# driver.get_screenshot_as_file("screenshot2.png")

# ログイン画面
elm = driver.find_element(by=By.CSS_SELECTOR, value="body > div > div:nth-child(1) > ons-page > ons-page > div.page__content > ons-navigator > ons-page > div.page__content > div.loginPage--parent > section > input")
elm.send_keys(codmon_email)
elm = driver.find_element(by=By.CSS_SELECTOR, value="body > div > div:nth-child(1) > ons-page > ons-page > div.page__content > ons-navigator > ons-page > div.page__content > div.loginPage--parent > section > div:nth-child(4) > input")
elm.send_keys(codmon_password)
elm = driver.find_element(by=By.CSS_SELECTOR, value="body > div > div:nth-child(1) > ons-page > ons-page > div.page__content > ons-navigator > ons-page > div.page__content > div.loginPage--parent > section > ons-button")
elm.click()
time.sleep(3)
# driver.get_screenshot_as_file("screenshot3.png")

# ログイン後、「連絡帳」でフィルター
## フィルター表示
elm = driver.find_element(by=By.CSS_SELECTOR, value="#timeline_page > div.page__content > ons-navigator > ons-page > div.page__content > ons-splitter > ons-splitter-content > ons-page > div.content.page__content > div.timelineHeader__wrapper > div > div.timelineHeader__filter")
elm.click()
time.sleep(3)

## 「連絡帳」チェック
elm = driver.find_element(by=By.CSS_SELECTOR, value="#timeline_page > div.page__content > ons-navigator > ons-page > div.page__content > div > div > div.timelineFilter__container > div:nth-child(4) > label:nth-child(2)")
elm.click()

## 決定ボタンクリック
elm = driver.find_element(by=By.CSS_SELECTOR, value="#timeline_page > div.page__content > ons-navigator > ons-page > div.page__content > div > div > div.timelineFilter__footer > div.timelineFilter__searchBtn")
elm.click()

time.sleep(3)
# driver.get_screenshot_as_file("screenshot4.png")

# タイムラインの取得
# ループ
# skip_count = 0
# while skip_count < 27:
#     skip_count += 1
#     next = driver.find_element(by=By.CSS_SELECTOR, value="#timeline_page > div.page__content > ons-navigator > ons-page > div.page__content > ons-splitter > ons-splitter-content > ons-page > div.content.page__content > div.timeline_content > section > div:nth-child(2) > ons-button")
#     next.click()
#     time.sleep(1)

hasNext = True
while hasNext:
    posts = driver.find_elements(by=By.CSS_SELECTOR, value="#timeline_page > div.page__content > ons-navigator > ons-page > div.page__content > ons-splitter > ons-splitter-content > ons-page > div.content.page__content > div.timeline_content > div")
    for i in range(1, min(20, len(posts)) + 1):
        post = posts[i]

        # 詳細ページに入る
        post.click()
        time.sleep(2)
        # 
        content = driver.find_element(by=By.CSS_SELECTOR, value="#timeline_page > div.page__content > ons-navigator > ons-page.selectable-container.page > div.page__content > div.block__white--padding.block__white--noborder")
        # print(content.text)
        # print(content.text.split("の連絡帳")[0])
        # print(content.text.split("")[0])
        date = content.text.split("\n")[-1].split("日")[0] + "日"
        driver.get_screenshot_as_file(date + ".png")
        # TODO: PDF/csv etc にコンテントを保存？(ref. https://stackoverflow.com/questions/2252726/how-to-create-pdf-files-in-python)
        # 戻るボタンクリック
        back = driver.find_element(by=By.CSS_SELECTOR, value="#timeline_page > div.page__content > ons-navigator > ons-page.selectable-container.page > ons-toolbar > div.left.toolbar__left > ons-back-button > span.back-button__label")
        back.click()
        time.sleep(1)
        
    # 次のページがあるかどうか
    next = driver.find_element(by=By.CSS_SELECTOR, value="#timeline_page > div.page__content > ons-navigator > ons-page > div.page__content > ons-splitter > ons-splitter-content > ons-page > div.content.page__content > div.timeline_content > section > div:nth-child(2) > ons-button")
    hasNext = next.get_attribute("disabled") == None
    if hasNext:
        next.click()
        time.sleep(2)
        

# WebDriverの終了
driver.close()
driver.quit()
