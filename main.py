import requests
import chardet
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlalchemy import create_engine,insert,MetaData,Table,Column,Integer,String

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

# 定义新表
src_list = Table(
    'src_list',  # 表名
    metadata,  # 元数据对象
    Column('id', Integer, primary_key=True, autoincrement=True),  # 主键，自增
    Column('厂商', String(64)),  # 标题，最大长度255
    Column('链接', String(64))  # 链接，最大长度255
)

# 创建表
metadata.create_all(engine)
# 获取表名列表
tables = metadata.tables.keys()
# 打印表名列表
print('查看当前数据库中已有表：', list(tables))


url = 'https://blog.csdn.net/Aaron_Miller/article/details/107103519'
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

td_elements = soup.select('table td')

# 提取每个 <td> 标签的内容和 href 属性
for td in td_elements:
    # 查找 <a> 标签
    a_tag = td.find('a')

    # 如果 <a> 标签存在且有 href 属性
    if a_tag and 'href' in a_tag.attrs:
        # 提取文本内容
        text_content = a_tag.get_text(strip=True)

        # 提取 href 属性
        href_content = a_tag['href']

        print(f"Text: {text_content}, Href: {href_content}")
        data.append({
            "厂商":text_content,
            "链接":href_content
        })

# 使用 insert() 构造插入语句
stmt = insert(src_list).values(data)

# 执行插入语句
with engine.connect() as connection:
    result = connection.execute(stmt)
    print(f"{result.rowcount} 行被插入。")
