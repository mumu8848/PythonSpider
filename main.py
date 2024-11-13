import re
import requests
import chardet

url = 'http://www.tipdm.com/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
print('网站编码：',rqg.encoding)
rqg.encoding = chardet.detect(rqg.content)['encoding']

title_pattern = r'(?<=<title>).*?(?=</title>)'
title_com = re.compile(title_pattern,re.M|re.S)
title_search = re.search(title_com,rqg.text)
title = title_search.group()

print('标题内容：',title)
print('标题内容(findall()方法查找)：',re.findall(r'(<title>)(.*?)(</title>)',rqg.text))


