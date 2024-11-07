import requests
import chardet

url = 'http://www.baidu.com'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua,timeout = 2) # timeout若设置为0.001，会因为时间过短而报错
rqg.encoding = 'utf-8'

print('结果类型：',type(rqg))
print('状态码：',rqg.status_code)
print('修改后的编码：',rqg.encoding)
print('detect()方法检测结果：',chardet.detect(rqg.content))

rqg.encoding = chardet.detect(rqg.content)['encoding']

print('改变后的编码：',rqg.encoding)
print('响应头：',rqg.headers)
print('网页内容：',rqg.text)
