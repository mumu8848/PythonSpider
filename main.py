import urllib3


http = urllib3.PoolManager()
url = 'http://baidu.com'
ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
rq = http.request('GET',url,headers=ua,timeout = urllib3.Timeout(connect=1.0,read=3.0))#第三种timeout的使用方式

print("服务器状态码：",rq.status)
print("响应实体：",rq.data)