import requests
from PIL import Image

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
kaptcha_url = 'https://www.ptpress.com.cn/kaptcha.jpg' # 验证码图片地址

session = requests.Session() # 会话对象能够跨请求保持某些参数，在这里是验证码

r = session.get(kaptcha_url,headers=header)

with open('./tmp/kaptcha.jpg','wb') as f:
    f.write(r.content)

im = Image.open('./tmp/kaptcha.jpg')

im.show()

kaptcha = input('请输入验证码：')

print('获取的验证码为：',kaptcha)

login_data = {'username':'18927565259','password':'@tipdm666','verifyCode':kaptcha}
login_url = 'https://www.ptpress.com.cn/login'


r = session.post(login_url,data=login_data)

r = session.get(login_url)
print('发送请求后返回的状态码为：',r.status_code)
print('响应内容：',r.text)