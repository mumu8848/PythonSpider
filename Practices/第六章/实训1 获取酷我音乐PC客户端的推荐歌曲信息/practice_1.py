import requests
import  json

bang_url = 'http://kbangserver.kuwo.cn/ksong.s?from=pc&fmt=json&pn=0&rn=20&type=bang&data=content&id=93&show_copyright_off=0&pcmp4=1&isbang=1&userid=0'

cookie_str = 'ad_dist=%B1%B1%BE%A9; userid=0; websid=0; BusinessId={"std_plat":410,"std_dev":"806977c0-a38e-459e-874b-470835200639","std_imei":"806977c0-a38e-459e-874b-470835200639","version":"MUSIC_9.3.8.0_W1"}'

# 定义请求头
headers = {
    'Host': 'kbangserver.kuwo.cn',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cookie': 'ad_dist=%B1%B1%BE%A9; userid=0; websid=0; BusinessId={"std_plat":410,"std_dev":"806977c0-a38e-459e-874b-470835200639","std_imei":"806977c0-a38e-459e-874b-470835200639","version":"MUSIC_9.3.8.0_W1"}',
    'Accept-Encoding': 'gzip, deflate'
}

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