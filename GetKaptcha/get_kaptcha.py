import requests
from PIL import Image

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
kaptcha_url = 'https://www.ptpress.com.cn/kaptcha.jpg' # 验证码图片地址

r= requests.get(kaptcha_url,headers=header)

with open('./tmp/kaptcha.jpg','wb') as f:
    f.write(r.content)

im = Image.open('./tmp/kaptcha.jpg')

im.show()

kaptcha = input('请输入验证码：')

print('获取的验证码为：',kaptcha)