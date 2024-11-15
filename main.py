import json
from  lxml import etree
import requests
import chardet

url = 'http://www.tipdm.com/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
print('网站编码：',rqg.encoding)
rqg.encoding = chardet.detect(rqg.content)['encoding']
html = rqg.text

t = etree.HTML(html)
content = t.xpath('//ul[@id="menu"]/li/a/text()')
print('标题菜单的文本：',content)

with open('./output.json','w',encoding='utf-8') as fp:
    json.dump(content,fp,ensure_ascii=False)
