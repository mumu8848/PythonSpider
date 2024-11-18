import requests
import chardet
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlalchemy import create_engine,insert,MetaData,Table

# 连接到 MySQL 数据库
engine = create_engine(
    'mysql+pymysql://root:123456@127.0.0.1:3306/test',
    pool_size=10,  # 连接池大小
    max_overflow=20,  # 连接池最大溢出大小
    pool_timeout=30,  # 连接池连接超时时间
    pool_recycle=1800,  # 连接池连接回收时间
    echo=False  # 打印 SQL 语句，方便调试
)

# 初始化元数据对象
metadata = MetaData()
# 反射现有的表
html_text = Table('html_text', metadata, autoload_with=engine)
# 获取表名列表
tables = metadata.tables.keys()
# 打印表名列表
print('查看当前数据库中已有表：', list(tables))


url = 'https://bbs.hupu.com/history/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

rqg = requests.get(url,headers = ua)
print('网站编码：',rqg.encoding)
rqg.encoding = chardet.detect(rqg.content)['encoding']

html = rqg.text
soup = BeautifulSoup(html,'lxml')
target = soup.title.string
print('标题的内容：',target)

# 查找base_url
base_tag = soup.find('base')
if base_tag and 'href' in base_tag.attrs:
    base_url = base_tag['href']
else:
    # 如果没有找到base_url，你可以根据实际情况进行处理，这里假设使用原始请求的URL作为基础URL（可能不正确）
    base_url = url

# 确保 base_url 是一个绝对 URL
base_url = urljoin(url, base_url)
print('base_url:',base_url)
data = []

post_titles = soup.select('div.post-title')
post_links = soup.select('div.post-title a')
for i, (title, link) in enumerate(zip(post_titles, post_links)):
    absolute_link = urljoin(base_url, link['href'])
    print(i, '文章标题:', title.text)
    print(i, '文章链接:', absolute_link)
    data.append({
        '标题': title.text.strip(),
        '链接': absolute_link
    })

# 使用 insert() 构造插入语句
stmt = insert(html_text).values(data)

# 执行插入语句
with engine.connect() as connection:
    result = connection.execute(stmt)
    print(f"{result.rowcount} 行被插入。")
