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

data = []

def add_data(text, href):
    """将数据添加到 data 列表中"""
    data.append({
        "厂商": text,
        "链接": href
    })

# 初始化元数据对象
metadata = MetaData()

# 定义新表
src_list2 = Table(
    'src_list2',  # 表名
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


url = 'https://blog.csdn.net/xiao8485/article/details/119237279'
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


# 选择表格中的所有 <tr> 标签
tr_elements = soup.select('table tr')

# 遍历每一行
for tr in tr_elements:
    # 获取该行的所有 <td> 标签
    td_elements = tr.find_all('td')

    # 初始化变量
    current_text = None
    last_href = None

    # 遍历每个 <td> 标签
    for td in td_elements:
        # 查找 <a> 标签
        a_tag = td.find('a')

        if a_tag and 'href' in a_tag.attrs:
            # 如果当前单元格有 <a> 标签，提取文本和 href 属性
            text_content = a_tag.get_text(strip=True)
            href_content = a_tag['href']

            # 如果之前有未匹配的文本，将其与当前的 href 合并
            if current_text:
                add_data(current_text,href_content)
                current_text = None
            else:
                add_data(current_text, href_content)

            last_href = href_content
        else:
            # 如果当前单元格没有 <a> 标签，保存其文本内容
            current_text = td.get_text(strip=True)

    # 循环结束后检查 current_text
    if current_text and last_href:
        add_data(current_text, href_content)


# 使用 insert() 构造插入语句
stmt = insert(src_list2).values(data)

# 执行插入语句
with engine.connect() as connection:
    result = connection.execute(stmt)
    print(f"{result.rowcount} 行被插入。")
