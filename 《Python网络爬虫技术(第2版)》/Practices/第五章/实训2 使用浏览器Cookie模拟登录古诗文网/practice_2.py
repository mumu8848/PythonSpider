import requests

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

user_url = 'https://www.gushiwen.cn/user/collect.aspx'

cookie_str = 'ticketStr=202741632%7cgQF38DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyVUtxaFF6bGVkN2kxZzctT3hEMUQAAgQHsUpnAwQAjScA; ASP.NET_SessionId=0sad4xwdv0s50ub4qdqsavto; Hm_lvt_9007fab6814e892d3020a64454da5a55=1732948235; HMACCOUNT=B7B275DECF6D6837; login=flase; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1732948424; codeyz=91f957fe6b840057; gsw2017user=6705989%7c2447134ABC61C82ADE8A960BE5FC5C76%7c2000%2f1%2f1%7c2000%2f1%2f1; wxopenid=defoaltid; gswZhanghao=13876265227; gswPhone=13876265227; idsShiwen2017=%2c87%2c67392%2c'

cookies = {}
for line in cookie_str.split(';'):
    key,value = line.split('=')
    cookies[key] = value

r2 = requests.get(user_url,cookies=cookies,headers=header)

print('发送请求后返回的状态码为：',r2.status_code)
print('获取用户收藏信息：',r2.text)
