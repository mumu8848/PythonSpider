import requests
import chardet

url = 'http://www.baidu.com'
rqg = requests.get(url)
rqg.encoding = 'utf-8'

print('结果类型：',type(rqg))
print('状态码：',rqg.status_code)
print('修改后的编码：',rqg.encoding)
print('detect()方法检测结果：',chardet.detect(rqg.content))

rqg.encoding = chardet.detect(rqg.content)['encoding']

print('改变后的编码：',rqg.encoding)