from selenium.webdriver.common.by import By
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.implicitly_wait(10) # 隐式等待10s

browser.get('https://www.baidu.com/') # 百度首页

elems = browser.find_elements(By.XPATH,'//div[@id="s-top-left"]//a')

for elem in elems:
    if elem.text == '新闻':
        elem.click()

handle = browser.window_handles # 获取当前浏览器窗口句柄
browser.switch_to.window(handle[-1]) # 将浏览器当前窗口切换成最新的窗口

browser.save_screenshot('./tmp4/xinwen.png')

browser.quit()
