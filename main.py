import requests
from lxml import etree

local_html = etree.parse('./test.html',etree.HTMLParser(encoding='utf-8'))

result_local = etree.tostring(local_html)
print('本地 html 文件：\n',result_local)

print('\n格式化后的 html 文件：\n',result_local.decode('utf-8'))