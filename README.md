# PythonSpider

## urllib3库 使用效果截图

![1730963885637](https://github.com/user-attachments/assets/ac1297ed-0bb5-48af-88ab-edc515ed0e7a)


## requests库 使用效果截图

![image](https://github.com/user-attachments/assets/3e5c565b-cca5-4c3a-b1a1-738069c33d54)

### 使用默认的编码

![image](https://github.com/user-attachments/assets/27e2d2d0-c510-416b-836c-b07b8ec653e6)

### 修改成 utf-8 编码

![image](https://github.com/user-attachments/assets/e96d218f-1a2b-4594-8857-16b18d2cc552)

### 使用 chardet 库
chardet检测出当前页面编码类型之后，再使用该类型编码
![image](https://github.com/user-attachments/assets/9cef737a-3396-447a-bbec-b80c523b6e8f)

### 设置 timeout 时间过短会报错
![image](https://github.com/user-attachments/assets/ca6b936c-eddb-4115-ba3d-c8881de26654)

## xpath 使用效果
- Xpath常用的谓语表达式
![image](https://github.com/user-attachments/assets/8678adfe-ffc2-40ba-99cb-84c9146d22d1)
实际代码执行效果
![image](https://github.com/user-attachments/assets/03b9eb35-c5b3-4040-b6dc-424e6cf63fd1)

- Xpath常用的功能函数
![image](https://github.com/user-attachments/assets/4ab711ed-f4f1-439a-b6b6-7410d2dab829)
实际的代码执行效果
![image](https://github.com/user-attachments/assets/18dba6f9-717b-40a2-908e-231e60482ae3)

- 提取52破解网站首页ul节点下的所有文本内容和对应链接
![image](https://github.com/user-attachments/assets/b9075737-1e2b-4648-b391-41de3fd875da)


## BeautifulSoup 库的使用
使用 BeautifulSoup 库对目标网站进行格式化输出
![image](https://github.com/user-attachments/assets/4d9118ba-ce0b-4b8b-9b38-e05709b2b075)
### 测试 BeautifulSoup 库的对象类型 Tag
![image](https://github.com/user-attachments/assets/cebd1a26-2d7c-45d0-8fe4-0c24022d7caa)
- Tag的name属性
![image](https://github.com/user-attachments/assets/40da7a77-560e-48b6-8d33-0a8e219b4808)
- Tag的attributes属性
- ![image](https://github.com/user-attachments/assets/e759d616-0f56-4884-b131-2f05925652b8)

### find_all() 方法
函数声明
```
BeautifulSoup.find_all(name=None, attrs={}, recursive=True, string=None,
limit=None, **kwargs)
```
![image](https://github.com/user-attachments/assets/53207d94-fc98-4d66-8683-38d9963db997)

代码执行效果
![image](https://github.com/user-attachments/assets/37a9f346-8b9c-4099-86c2-c429032b2211)

### select() 方法
函数声明
```
BeautifulSoup.select(selector, namespaces=None, limit=None, **kwargs)
```
![image](https://github.com/user-attachments/assets/e56cff81-9a2e-4929-a98f-b56875973ebb)
代码执行效果
![image](https://github.com/user-attachments/assets/d9518885-ca36-4f39-9b15-6cd1ea0fbc52)

## 正则表达式
正则表达式是通用型语法，不局限于`python`，其它语言也经常会使用到。这部分主要是介绍在`python`中的正则表达式模块。

- 常见符号及其描述 
![image](https://github.com/user-attachments/assets/975b02ab-90c6-4a31-8dab-29d6a4045c65)

代码运行效果
![image](https://github.com/user-attachments/assets/cb23ea09-e5dd-4fcd-ab34-6b586de1b93f)

## 数据存储
### JSON-将数据存储为JSON文件
`json`库中的关键函数
- dump函数 和 dumps函数
![image](https://github.com/user-attachments/assets/4ec4dbd3-0127-49dc-b369-7159cfc0cb6c)

代码运行效果：
![image](https://github.com/user-attachments/assets/6140437c-e416-4bc6-b452-d633fd1dc510)




### MYSQL-将数据存储到MySQL数据库
`pymysql`库中的关键函数 
`connect`函数
- 函数声明

```
pymysql.connect(user=None, password="", host=None, database=None, port=0,
charset="", connect_timeout=10,…) 
```

`connect`函数的常用参数以及相关说明
![image](https://github.com/user-attachments/assets/23d3516b-19c6-432a-8dd3-3e9a3ff3fc88)

代码运行效果：
![image](https://github.com/user-attachments/assets/831cfa8e-1efe-4e96-8692-55da2487b832)



# 虎扑历史板块测试案例
题目：
通过使用Xpath或 BeautifulSoup 库，获取虎扑—历史栏目中各帖子的标题、标题的超链接地址。同时，在本地数据库中新建一个html_text表，要求该表有两列，列名为“标题”​“链接”​，分别用于存储标题和标题相对应的链接。将爬取下来的多个帖子的数据按行插入html_text表中，并查看数据是否存储成功。

代码运行效果
![1731909341073](https://github.com/user-attachments/assets/9b61f0e7-dc48-45ec-9cbd-f6155f4b9bea)

# src厂商列表测试案例
获取cnvd的src列表，使用 BeautifulSoup 库解析 td 标签
代码运行效果
![image](https://github.com/user-attachments/assets/7b95e8d4-9c9e-4765-b381-6f96bcae1af2)


