import requests
from PIL import Image
from http import cookiejar

session = requests.Session()
session.cookies = cookiejar.LWPCookieJar('cookie')

login_url = 'https://www.ptpress.com.cn/login'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

def get_kaptcha():
    kaptcha_url = 'https://www.ptpress.com.cn/kaptcha.jpg'
    response = session.get(kaptcha_url, headers=header)

    with open('./tmp/kaptcha.jpg', 'wb') as f:
        f.write(response.content)

    img = Image.open('./tmp/kaptcha.jpg')
    img.show()
    verifyCode = input('请输入验证码：')
    return verifyCode

login_data = {'username':'18927565259','password':'@tipdm666','verifyCode':get_kaptcha()}
r = session.post(login_url, data=login_data, headers=header)

print('发送请求后返回的网址为：',r.url)

session.cookies.save(ignore_discard=True,ignore_expires=True)

try:
    session.cookies.load(ignore_discard=True)
except:
    print('Cookie 未能加载！')

login_info = 'https://www.ptpress.com.cn/login/getUserName'
r = session.get(login_info, headers=header)
print('获取用户登录信息：',r.text)