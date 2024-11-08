import requests
from lxml import etree

url = 'http://www.52pojie.cn/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
rqg.encoding = 'gbk'
html = etree.HTML(rqg.text,parser=etree.HTMLParser(encoding='gbk'))

result = etree.tostring(html,encoding='utf-8',pretty_print=True,method='html')

content = html.xpath('//ul[starts-with(@id,"mn")]/li//a/text()')
for i in content:
    print(i)


