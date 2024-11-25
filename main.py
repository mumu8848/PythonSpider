from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.implicitly_wait(10) # 隐式等待10s

browser.get('https://weread.qq.com/web/category/newbook') # 中国出版集团

# browser.maximize_window()

elem = browser.find_element(By.XPATH,'//div[@class="ranking_page_content_list_container"]//a[@class="wr_bookList_item_link"][2]')

try:
    wait = WebDriverWait(browser,20,0.5)
    wait.until(EC.element_to_be_clickable(elem))
    elem.click()
    time.sleep(5)
finally:
    browser.quit()


