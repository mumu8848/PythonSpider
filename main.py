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

tag = soup.a
print('Tag对象的name属性是：',tag)
print('Tag对象的全部属性是：',tag.attrs)
print('class 属性的值：',tag['class'])

tag['class'] = 'Toindex'
print('修改后 Tag 对象的属性：',tag.attrs)

tag['id'] = ['toindex']
print('修改后 Tag 对象的内容：',tag)

del tag['class']
print('删除 class 后 Tag 对象的内容：',tag)

