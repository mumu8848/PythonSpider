from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.get('https://book.douban.com/latest') # 中国出版集团
pics = browser.find_elements(By.XPATH,'//div[@class="media__img"]//img')

for index,pic in enumerate(pics):
    pic_url = pic.get_attribute('src')
    pic_name = './tmp1/'+ pic_url.split('/')[-1].split('/')[0] +'.png'
    print('正在存储图片：',pic_name)

    # 使用 request 获取原图
    resp = requests.get(pic_url)

    with open(pic_name,'wb') as f:
        f.write(resp.content)

browser.quit()
