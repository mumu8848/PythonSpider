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

tag = soup.title
print('Tag 对象中包含的字符串：',tag.string)
print('tag.string 的类型：',type(tag.string))
tag.string.replace_with('谷歌搜索')
print('替换后的内容：',tag.string)

