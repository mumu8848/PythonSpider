from bs4 import BeautifulSoup
import requests
import chardet

url = 'http://www.tipdm.com/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
print('网站编码：',rqg.encoding)
rqg.encoding = chardet.detect(rqg.content)['encoding']


html = rqg.text
soup = BeautifulSoup(html,'lxml')

print('查找名为 title 的标签：',soup.select('title')) #标签名查找
print('获取标签中的文字：',soup.select('title')[0].text) #text属性获取列表中标签元素的文字
print('查找类名为 slogan 的标签：',soup.select('.slogan')) #类名查找

# print('查找 id 名为 menu 的标签：',soup.select('#menu')) #id名查找

print('查找 <div>标签的类名为 introTxt 的标签：',soup.select('div.introTxt')) #组合查找

print('查找父标签为 head 的 <title> 标签：',soup.select('head > title')) #子标签查找

print('查找属性 class="logo" 的 <a> 标签：',soup.select('a[class="logo"]')) #使用属性查找

print('获取标签中的属性值：',soup.select('a[class="logo"] > img')[0]['src']) #使用 [] 获取标签的属性值


