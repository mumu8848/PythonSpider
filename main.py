from selenium.webdriver.common.by import By
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.implicitly_wait(10) # 隐式等待10s

browser.get('https://weread.qq.com/web/category/newbook') # 中国出版集团

# browser.maximize_window()

elem = browser.find_element(By.XPATH,'//div[@class="ranking_page_content_list_container"]//a[1]')
elem.click()


# browser.quit()
