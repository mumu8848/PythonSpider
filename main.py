from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=option)

browser.get('https://book.douban.com/latest') # 中国出版集团
pics = browser.find_elements(By.XPATH,'//div[@class="media__img"]//img')

for index,pic in enumerate(pics):
    pic_name = './tmp/'+str(index)+'.png'
    print('正在存储图片：',pic_name)
    with open(pic_name,'wb') as f:
        f.write(pic.screenshot_as_png)

browser.quit()
