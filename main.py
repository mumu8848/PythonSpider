from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.get('https://book.douban.com/latest') # 中国出版集团
elems = browser.find_elements(By.XPATH,'//div[@id="content"]//li//a[@class="fleft"]')

for elem in elems:
    print(elem.text)
