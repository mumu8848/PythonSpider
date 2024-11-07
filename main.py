import urllib3

http = urllib3.PoolManager()
ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
rq = http.request('GET','http://baidu.com',headers = ua)
print("服务器状态码：",rq.status)
print("响应实体：",rq.data)