from bs4 import BeautifulSoup
import requests
import chardet

url = 'http://www.baidu.cn/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
print('网站编码：',rqg.encoding)
rqg.encoding = chardet.detect(rqg.content)['encoding']


html = rqg.text
soup = BeautifulSoup(html,'lxml')

print('BeautifulSoup对象的name属性是：',soup.name)

tag = soup.a
print('Tag对象的name属性是：',tag)

tag.name = 'b'
print('修改name属性后的Tag对象的内容是：',tag)