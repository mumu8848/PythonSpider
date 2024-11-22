from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.get('https://book.douban.com/latest') # 中国出版集团

# 元素交互操作之--单击
elem = browser.find_element(By.XPATH,'//div[@class="xbar"]//a')
elem.click()

# 元素交互操作之--输入文字
search_input = browser.find_element(By.XPATH,'//div[@class="nav-search"]//input')
search_input.send_keys('爬虫')
search_input.send_keys(Keys.ENTER)

# browser.quit()
