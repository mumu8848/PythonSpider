from bs4 import BeautifulSoup
import requests
import chardet

url = 'http://www.tipdm.com/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
print('网站编码：',rqg.encoding)
rqg.encoding = chardet.detect(rqg.content)['encoding']


html = rqg.text
soup = BeautifulSoup(html,'lxml')

print('名为 title 的全部子节点：',soup.find_all('title'))
print('title 子节点的文本内容：',soup.title.string)
print('使用 get_text() 获取的文本内容：',soup.title.get_text())

target = soup.find_all('a',class_='next')
print('CSS 类名匹配获取的节点：',target)

target = soup.find_all(id='search')
print('关键字 id 匹配获取的节点：',target)

target = soup.ul.find_all('a')
print('第一个 ul 节点名称为 a 的节点：',target)

urls = []
text = []
for tag in target:
    urls.append(tag.get('href'))
    text.append(tag.get_text())
print('a 节点的 href 属性值构成的列表：',urls)
print('a 节点的文本内容构成的列表：',text)

