import requests

url = 'http://www.baidu.com'
rqg = requests.get(url)
rqg.encoding = 'utf-8'

print('结果类型：',type(rqg))
print('状态码：',rqg.status_code)
print('修改后的编码：',rqg.encoding)
print('响应头：',rqg.headers)
print('网页内容：',rqg.text)