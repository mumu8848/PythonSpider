from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.get('https://book.douban.com/latest') # 中国出版集团

browser.maximize_window()

search_input = browser.find_element(By.XPATH,'//div[@class="nav-search"]//input')
search_input.send_keys('爬虫')
search_input.send_keys(Keys.ENTER)

# 切换到最新的窗口
handles = browser.window_handles
browser.switch_to.window(handles[-1])

# 定位最新窗口中的所有图书名所在的标签
books = browser.find_elements(By.XPATH,'//div[@id="wrapper"]//div[@class="title"]//a')

for book in books:
    print(book.text)

browser.quit()
