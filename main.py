import urllib3

http = urllib3.PoolManager()
rq = http.request('GET','http://baidu.com')
print("服务器状态码：",rq.status)
print("响应实体：",rq.data)