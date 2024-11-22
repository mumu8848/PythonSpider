from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.get('http://cn.cnpubg.com/') # 中国出版集团
elems = browser.find_elements(By.XPATH,'//div[@id="navCon"]/ul/descendant::a')

for elem in elems:
    print(elem.text)
