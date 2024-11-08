import requests
from lxml import etree

url = 'http://www.baidu.com'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
rqg.encoding = 'utf-8'
html = etree.HTML(rqg.text,parser=etree.HTMLParser(encoding='utf-8'))

result = etree.tostring(html,encoding='utf-8',pretty_print=True,method='html')

result0 = html.xpath('/html/body/div[1]')
print('第一个div节点：',result0)

result1 = html.xpath('/html/body/div[last()]')
print('最后一个div节点：',result1)

result2 = html.xpath('/html/body/div[last()-1]')
print('倒数第二个div节点：',result2)

result3 = html.xpath('/html/body/div[position()<3]')
print('body子节点的前两个div节点：',result3)

result4 = html.xpath('/html/body/div[@id]')
print('body子节点的带有id属性的div节点：',result4)




