import requests
from lxml import etree

url = 'http://www.baidu.com'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
rqg.encoding = 'utf-8'
html = etree.HTML(rqg.text,parser=etree.HTMLParser(encoding='utf-8'))

result = etree.tostring(html,encoding='utf-8',pretty_print=True,method='html')

print('修正后的HTML对象：',result)
