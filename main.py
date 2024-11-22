from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.get('https://book.douban.com/latest') # 中国出版集团

browser.maximize_window()

for i in range(5):
    browser.execute_script('window.scrollBy(0,100)')
    time.sleep(1)

browser.save_screenshot('./tmp2/scrollBy.png')


browser.quit()
