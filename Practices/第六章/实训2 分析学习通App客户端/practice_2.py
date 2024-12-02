import requests
import json

bang_url = 'https://home-yd.chaoxing.com/apis/data/getIdxSourceVoByPoolId?poolId=qikan&incode=000000&page=6&pageSize=20&nowTime=1733123311353'

# 定义请求头
headers = {
    'Host': 'home-yd.chaoxing.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; MI 9 Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36 com.chaoxing.mobile/ChaoXingStudy_3_4.3.4_android_phone_494_27 (@Kalimdor)_38758f56e57346a2ad9511f9b2c26455',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cookie': 'lv=0; chaoxinguser=1; uname=""; _uid=372831698; UID=372831698; vc=BBF50D6B180F236074050C2F267E146B; vc2=931EAC7C300097FB4D8ABB75155F107E; xxtenc=db05ad97a7e7ddbb159e0849a7c822b6; fidsCount=1; _industry=null; uf=f9866f9a46b70622f014648e30910447113103d49fa43da17a4fb73fc63758497d3dbdc6e34ea772b01550292511c42f9b0594e13f4b452fbdd6b93a43158491f81fb60e07cc873396015a46b0f001c711cb6b5528a1c222; _d=1733123229961; vc3=Ix0hronDe87by55sMNZoXd6KTBqp%2By%2Bf4e98iO%2BPT23PnEceSJ7zDvKg1P%2Bf7YGSzYOuDLuRfh77m2BbzZWBZGyfzhfE3mlsquigAMmSzU1wa1ukWgojH8WFogtvum1xZEPAZI7f5W0jgKtHS8DEVtxCwyNSvtdGO2zwZmNZ%2BsY%3Dec8fbb64a00442a7f1c7b51c10f5e5bf; cx_p_token=affa9bcde77f354488df02cea70e4193; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIzNzI4MzE2OTgiLCJsb2dpblRpbWUiOjE3MzMxMjMyMjk5NjMsImV4cCI6MTczMzcyODAyOX0.p-eMEhgseS4lht1furpim9Fn7GCrbQPVH92wujAL9uI; DSSTASH_LOG=C_0-UN_0-US_372831698-T_1733123229963; KI4SO_SERVER_EC=RERFSWdRQWdsckJiQXZ5ZmdkWW10a3YrRmRLUktQaXJOZHIvZUtXMThWYW5kNXlYUFVSYXhqOCtW%0AMy9vZVNGekRtU2djWlRjU2NTVQp1NG13bWtscWxaWDhUMFRsbHloK3ZsdnF5Tzd3RjdrN3dlclJt%0ARDFtdWE0OVd4bXBHSTZoYXFNdm1QcnBMbHJtTy9vcmVxUmxXdzZlCnYyWWxNcHIyZWFFM2ZUNW5B%0AaDEybkZGYmNSQ0hwUlRUMkdjeFY0QU1HMjM2VW5lWUo0YkVyRGdybjU1SllYYWo3SndVT3NOTG04%0ASnMKWWREb1NyWlpZWEFUK1dXTkNYMHVBME13d0FhQkNHWjBIRzJGYjF5Um5tQ3cxN053ZU5tck0w%0AaUVETm5BWHpOQ0RuTnM5WU54TWRhNwpRVHdDRmExVWo2MEV2TTd6QWs2VzZLa1VvZTEvbjZSeTdW%0AK3Z1YUlONm5seVV3RTJSWWlVMFJ4NTZUWUNUcGJvcVJTaDdmb3Y0OFl1CjhhSVZsMFBEcXBVMjh2%0AOD0%2FYXBwSWQ9MSZrZXlJZD0x; _tid=326316781; sso_puid=372831698; latotvp=0; route=04de4c8a3014ce93f1da96d2f942bf87; JSESSIONID=60E8D6181B64640AC2A32B66859AB2F2.HomeManageService; fanyamoocs=C3C8849CC5703D273606855810916A7B',
    'Accept-Encoding': 'gzip, deflate'
}

'''
GET https://home-yd.chaoxing.com/apis/data/getIdxSourceVoByPoolId?poolId=qikan&incode=000000&page=6&pageSize=20&nowTime=1733123311353 HTTP/1.1
Host: home-yd.chaoxing.com
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 9; MI 9 Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36 com.chaoxing.mobile/ChaoXingStudy_3_4.3.4_android_phone_494_27 (@Kalimdor)_38758f56e57346a2ad9511f9b2c26455
Referer: https://home-yd.chaoxing.com/home/getcxHomePage?incode=recommend
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.9
Cookie: lv=0; chaoxinguser=1; uname=""; _uid=372831698; UID=372831698; vc=BBF50D6B180F236074050C2F267E146B; vc2=931EAC7C300097FB4D8ABB75155F107E; xxtenc=db05ad97a7e7ddbb159e0849a7c822b6; fidsCount=1; _industry=null; uf=f9866f9a46b70622f014648e30910447113103d49fa43da17a4fb73fc63758497d3dbdc6e34ea772b01550292511c42f9b0594e13f4b452fbdd6b93a43158491f81fb60e07cc873396015a46b0f001c711cb6b5528a1c222; _d=1733123229961; vc3=Ix0hronDe87by55sMNZoXd6KTBqp%2By%2Bf4e98iO%2BPT23PnEceSJ7zDvKg1P%2Bf7YGSzYOuDLuRfh77m2BbzZWBZGyfzhfE3mlsquigAMmSzU1wa1ukWgojH8WFogtvum1xZEPAZI7f5W0jgKtHS8DEVtxCwyNSvtdGO2zwZmNZ%2BsY%3Dec8fbb64a00442a7f1c7b51c10f5e5bf; cx_p_token=affa9bcde77f354488df02cea70e4193; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIzNzI4MzE2OTgiLCJsb2dpblRpbWUiOjE3MzMxMjMyMjk5NjMsImV4cCI6MTczMzcyODAyOX0.p-eMEhgseS4lht1furpim9Fn7GCrbQPVH92wujAL9uI; DSSTASH_LOG=C_0-UN_0-US_372831698-T_1733123229963; KI4SO_SERVER_EC=RERFSWdRQWdsckJiQXZ5ZmdkWW10a3YrRmRLUktQaXJOZHIvZUtXMThWYW5kNXlYUFVSYXhqOCtW%0AMy9vZVNGekRtU2djWlRjU2NTVQp1NG13bWtscWxaWDhUMFRsbHloK3ZsdnF5Tzd3RjdrN3dlclJt%0ARDFtdWE0OVd4bXBHSTZoYXFNdm1QcnBMbHJtTy9vcmVxUmxXdzZlCnYyWWxNcHIyZWFFM2ZUNW5B%0AaDEybkZGYmNSQ0hwUlRUMkdjeFY0QU1HMjM2VW5lWUo0YkVyRGdybjU1SllYYWo3SndVT3NOTG04%0ASnMKWWREb1NyWlpZWEFUK1dXTkNYMHVBME13d0FhQkNHWjBIRzJGYjF5Um5tQ3cxN053ZU5tck0w%0AaUVETm5BWHpOQ0RuTnM5WU54TWRhNwpRVHdDRmExVWo2MEV2TTd6QWs2VzZLa1VvZTEvbjZSeTdW%0AK3Z1YUlONm5seVV3RTJSWWlVMFJ4NTZUWUNUcGJvcVJTaDdmb3Y0OFl1CjhhSVZsMFBEcXBVMjh2%0AOD0%2FYXBwSWQ9MSZrZXlJZD0x; _tid=326316781; sso_puid=372831698; latotvp=0; route=04de4c8a3014ce93f1da96d2f942bf87; JSESSIONID=60E8D6181B64640AC2A32B66859AB2F2.HomeManageService; fanyamoocs=C3C8849CC5703D273606855810916A7B


'''
# 发送GET请求
response = requests.get(bang_url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 打印响应内容
    print(response.text)
    # 将响应内容转换为Python字典
    data = response.json()

    # 定义要保存的文件名
    filename = 'response_data.json'

    # 打开文件并以写入模式（'w'）和UTF-8编码保存数据
    with open(filename, 'w', encoding='utf-8') as file:
        # 使用json.dump将数据写入文件
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"数据已成功保存到 {filename}")
else:
    print(f"请求失败，状态码: {response.status_code}")
