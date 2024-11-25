from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo


import time

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.implicitly_wait(10) # 隐式等待10s

browser.get('https://weread.qq.com/web/category/newbook') # 中国出版集团

# browser.maximize_window()

elems = browser.find_elements(By.XPATH,'//div[@class="ranking_page_content_list_container"]//p[@class="wr_bookList_item_title"]')

# 建立本地链接，使用默认端口和用户名密码
conn = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = conn['mydb'] # 创建数据库‘mydb’
test = mydb['Nav'] # 通过属性的方式创建集合

for elem in elems:
    test.insert_one({'name':elem.text})

for x in test.find():
    print(x)

