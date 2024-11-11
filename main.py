from bs4 import BeautifulSoup
import requests
import chardet

url = 'http://www.baidu.com/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
print('网站编码：',rqg.encoding)
rqg.encoding = chardet.detect(rqg.content)['encoding']


html = rqg.text
soup = BeautifulSoup(html,'lxml')

print('soup 的类型：',type(soup))
print('BeautifulSoup 对象的特殊 name 属性：',soup.name)
print('soup.name 的类型：',type(soup.name))
print('BeautifulSoup 对象的 attributes 属性：',type(soup.attrs))

