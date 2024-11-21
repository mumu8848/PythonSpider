from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.get('https://www.52pojie.cn/')
elem = browser.find_element(By.XPATH,'//div[@id="nv"]/descendant::li/a[1]')
print('定位到的元素返回值：',elem)
print('元素的文本信息',elem.text)
print('元素的属性值：',elem.get_attribute('href'))
