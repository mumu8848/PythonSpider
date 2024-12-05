import requests
from PIL import Image

url = 'https://www.ptpress.com.cn/'
login_info = 'https://www.ptpress.com.cn/login/getUserName'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

cookie_str = 'acw_tc=1a0c652217329704292421497e00beae03aafc23391a459f9bbdc5220e862e; JSESSIONID=F0AA24EEB1AC43B54189F409DC257C95'

cookies = {}
for line in cookie_str.split(';'):
    key,value = line.split('=')
    cookies[key] = value

r1 = requests.get(url,cookies=cookies,headers=header)
r2 = requests.get(login_info,cookies=cookies,headers=header)

print('获取用户登录信息：',r2.text)