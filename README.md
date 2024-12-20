# PythonSpider
本项目是基于《Python网络爬虫技术（第2版）》的爬虫学习笔记
![image](https://github.com/user-attachments/assets/b5afb630-de5f-4bfa-9fc2-c7e5649bf0e3)
以及《实战Python网络爬虫》
![image](https://github.com/user-attachments/assets/3e96418c-ee2a-4340-8e61-7502e453cd8f)

仅作学习分享

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

# 动态网页的爬取 selenium 框架的使用
![image](https://github.com/user-attachments/assets/1688c602-f103-4701-9a08-9cb75276dbfe)

小demo
![image](https://github.com/user-attachments/assets/87a203e2-0d23-4ce7-977c-f68a7373d21c)

## 使用 find_element 方法的案例
![image](https://github.com/user-attachments/assets/6b9d219c-819c-47bf-a459-79699addb1fa)

- 小tips
  在目标网页上要使用好xpath语句来获取到我们想要爬取内容的具体元素（说起来比较绕，但确实是这么个理）
![image](https://github.com/user-attachments/assets/7c95f054-6459-485f-b4e6-2e4baacdac17)

## 使用 find_elements 方法的案例
- 中国出版集团
![image](https://github.com/user-attachments/assets/bb1f0ac5-7ae7-4326-aab3-d38d6c362b52)
- 豆瓣新书
![image](https://github.com/user-attachments/assets/7bbc91e1-f670-47a2-9a70-5d998856cf3d)

## 元素交互 单击和输入
![image](https://github.com/user-attachments/assets/909ff7b6-892a-4a3a-a9cb-5e5306f6c856)

## 豆瓣读书，提取多本与爬虫相关图书名称

![image](https://github.com/user-attachments/assets/8f463b44-0edd-488f-99c2-e509398c11b7)


# 数据库存储之MongoDB和MySQL的区别
- 概念层面的区别
![image](https://github.com/user-attachments/assets/dd926556-167f-4ffd-987c-a752d1176da1)

- 操作命令层面的区别
![image](https://github.com/user-attachments/assets/8eb764fc-c74d-49ce-a840-335405ad1fc3)

- 获取百度标题栏文字和链接，并存入mongodb中
![image](https://github.com/user-attachments/assets/cb4f8b9f-e103-4ab9-a019-83f1de07948a)

  
- 一个插入集合的实际示例
![image](https://github.com/user-attachments/assets/905094f5-fcee-43f6-bb3d-378264e36cc2)

# 登录示例

## 获取验证码
![image](https://github.com/user-attachments/assets/1c289072-75e4-42ff-97e9-cb3b3ad22a49)

## 登录测试
![image](https://github.com/user-attachments/assets/f279edc4-59d8-474e-9ec3-c23139f99f67)

## 存储cookie
![image](https://github.com/user-attachments/assets/b33e5c2a-26fb-43a9-8a1b-d59675ecf9af)

### 第五章
#### 实训1 使用表单登录方法模拟登录古诗文网
![image](https://github.com/user-attachments/assets/c467874d-89ea-4600-9ff2-43ff890bd374)

#### 实训2 使用浏览器Cookie模拟登录古诗文网
![image](https://github.com/user-attachments/assets/01f5f3ca-77e6-46ac-a8e5-3c0bb8d52128)

#### 实训3 基于表单登录后的Cookie模拟登录古诗文网

- 需要注意的点是：
原文：**注：若在调用save()方法时报错，可以考虑把cookiejar.py中的1842和1843行代码注释后保存，重新运行。**

cookiejar.py中两行代码
```python
if cookie.expires: h.append(("expires",
        time2isoz(float(cookie.expires))))
```
这两行代码的作用是将 Cookie 的过期时间格式化为 ISO 格式，并将其添加到 HTTP 头部。
通过浏览器开发工具分析可以看到请求头部的字段细节：
![image](https://github.com/user-attachments/assets/44211822-5e5d-40fd-988f-ebe8909ab2bc)

注释掉库文件的这两行代码可以理解为不处理过期时间

### 第六章
#### 实训1 获取酷我音乐PC客户端的推荐歌曲信息
通过http analyzer分析到排行榜的请求数据包
![image](https://github.com/user-attachments/assets/8a638c3e-0623-4275-a925-01b9dd7bb75a)
构造对应的请求
![image](https://github.com/user-attachments/assets/816311b7-5674-4d6b-9e49-b82c7fb68f9e)

#### 实训2 分析学习通App客户端
这部分难点在手机模拟器抓包上，写脚本是最简单的。
![image](https://github.com/user-attachments/assets/be5ed5a5-0f45-4e05-a280-7b3513588584)


## Scrapy爬虫框架
- 7个组件之间的数据流向图
![image](https://github.com/user-attachments/assets/a3731a7b-0e18-4d5a-83f8-58bfae520e64)
说明：
数据流在Scrapy中由执行引擎控制，其基本步骤如下。
1. 引擎打开一个网站，找到处理该网站的Spiders，并向该Spiders请求第一个要爬取的URL。
2. 引擎将爬取请求(Requests)转发给调度器，调度器指挥进行下一步。
3. 引擎从调度器获取下一个要爬取的请求。
4. 调度器返回下一个要爬取的请求，通过下载器中间件（请求方向）将请求转发给下载器。
5. 当网页下载完毕时，下载器会生成一个该网页的响应，并将其通过下载器中间件（响应方向）发送给引擎。
6. 引擎从下载器中接收到响应并通过Spider中间件（输入方向）发送给Spiders处理。
7. Spiders处理响应并返回爬取到的Items及（跟进）新的请求给引擎。
8. 引擎将爬取到的Items（Spiders返回的）给Item Pipelines，将请求（Spiders返回的）给调度器。
9. 重复步骤"2"直至调度器中没有更多的URL请求，引擎关闭该网站。

### 创建Scrapy爬虫项目
```shell
Scrapy startproject myScrapy D:\my_project\python-exp\PythonSpider\Scrapy\ # 在这之前先pip install scrapy
```
![image](https://github.com/user-attachments/assets/cdcbc5a5-2786-488a-ae03-c2bce3873521)

### 成功写入数据库
排坑指南：(**细看执行之后的日志调试信息**)
通过报错信息定位到
```shell
Error writing to MySQL: Unable to find a usable engine; tried using: 'sqlalchemy'.
```
发现本地安装的sqlalchemy和pandas的版本不兼容，随后卸载当前sqlalchemy再重新安装对应可兼容的版本

具体操作如下：
```shell
# 卸载旧版本的 sqlalchemy
pip uninstall sqlalchemy
# 安装符合要求的新版本 sqlalchemy
pip install --upgrade "sqlalchemy>=1.4.16"
```
![image](https://github.com/user-attachments/assets/904fc6d7-16e1-4585-b7ad-8afa0ecd6080)


