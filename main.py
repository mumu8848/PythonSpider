import pymysql
from  lxml import etree
import requests
import chardet
from bs4 import BeautifulSoup

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='test',charset='utf8',connect_timeout=1000)

cursor = conn.cursor()

sql = '''create table if not exists class (id int(10) primary key auto_increment, name varchar(20) not null,text varchar(20) not null);'''

cursor.execute(sql)
cursor.execute('show tables;')
data = cursor.fetchall()
print('查看当前数据库中已有表：',data)

url = 'http://www.tipdm.com/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
print('网站编码：',rqg.encoding)
rqg.encoding = chardet.detect(rqg.content)['encoding']

html = rqg.text
soup = BeautifulSoup(html,'lxml')
target = soup.title.string
print('标题的内容：',target)

#将数据插入到mysql的test表中
title = 'tipdm'
sql = "INSERT INTO class (name,text) VALUES(%s, %s)"
cursor.execute(sql, (title, target))
conn.commit()

data = cursor.execute('select * from class')
data = cursor.fetchmany()
print('查询获取的结果：',data)

conn.close()


