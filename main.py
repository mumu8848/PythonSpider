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

markup = '<c><!--This is a markup --></b>'
soup_comment = BeautifulSoup(markup,'lxml')
comment = soup_comment.c.string
print('注释的内容：',comment)
print('注释的类型：',type(comment))

