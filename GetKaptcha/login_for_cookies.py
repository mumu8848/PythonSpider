import requests
from PIL import Image

url = 'https://www.ptpress.com.cn/'
login_info = 'https://www.ptpress.com.cn/login/getUserName'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

cookie_str = 'acw_tc=2760824d17328886189493556e43e34352a084dda6d058822f7bf957d0e4ba; JSESSIONID=814B699BC127276A58EE1F962FFF9E7C'

cookies = {}
for line in cookie_str.split(';'):
    key,value = line.split('=')
    cookies[key] = value

r1 = requests.get(url,cookies=cookies,headers=header)
r2 = requests.get(login_info,cookies=cookies,headers=header)

print('获取用户登录信息：',r2.text)