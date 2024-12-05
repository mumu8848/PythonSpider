import requests
from PIL import Image


session = requests.Session()
kaptcha_url = 'https://www.gushiwen.cn/RandCode.ashx'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

r = session.get(kaptcha_url,headers=header)

with open('./tmp/kaptcha.jpg','wb') as f:
    f.write(r.content)

im = Image.open('./tmp/kaptcha.jpg')
im.show()

kaptcha = input('请输入验证码：')
print('获取的验证码为：',kaptcha)

login_data = {'email':'13876265227','pwd':'test@666','code':kaptcha}
login_url = 'https://www.gushiwen.cn/user/login.aspx'

r = session.post(login_url,data=login_data,headers=header)
print('发送登录请求后返回的状态码为：',r.status_code)
print('响应内容：',r.text)

user_url = 'https://www.gushiwen.cn/user/collect.aspx'

r1 = session.get(user_url)
print('发送请求后返回的状态码为：',r1.status_code)
print('响应内容：',r1.text)

