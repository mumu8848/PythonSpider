from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.implicitly_wait(10) # 隐式等待10s

browser.get('https://www.5iai.com/#/index') # 百度首页

# browser.maximize_window()

elems = browser.find_elements(By.XPATH,'//div[@class="container"]//ul[@class="clearfix position"]//span[@class="left"]//span')

# 建立本地链接，使用默认端口和用户名密码
conn = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = conn['mydb'] # 创建数据库‘mydb’
test = mydb['Jobs'] # 通过属性的方式创建集合

for elem in elems:
    Jobname = elem.text  # 获取文本内容
    test.insert_one({'岗位名称': Jobname})


for x in test.find():
    print(x)

browser.quit()
