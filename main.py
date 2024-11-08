import requests
from lxml import etree

url = 'http://www.xinhuanet.com/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
rqg.encoding = 'utf-8'
html = etree.HTML(rqg.text,parser=etree.HTMLParser(encoding='utf-8'))

result = etree.tostring(html,encoding='utf-8',pretty_print=True,method='html')

result0 = html.xpath('//div[starts-with(@id,"h")]')
print('id值以 a 开头的div节点：',result0)

result1 = html.xpath('//div[contains(@id,"a")]')
print('id值包含 a 的div节点：',result1)

result2 = html.xpath('//div[contains(@id,"a") and contains(@id,"c")]')
print('id值包含 a 和 c 的div节点：',result2)

result3 = html.xpath('//div[contains(text(),"如")]')
print('文本包含 "如" 的div节点：',result3)


