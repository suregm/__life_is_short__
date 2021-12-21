import re

import requests
from bs4 import BeautifulSoup

url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")   # 解析器

# 信息标记


# 目前国际公认的信息标记语言有三种：
# XML eXtensible Markup Language，HTML属于XML的一种
# JSON
# YAML


# XML
# <img src="sure.jpg" size="10"> ... </img>
# 若标签中无内容，则可以使用空元素缩写形式：<img src="sure.jpg" size="10" />
# 注释形式 <!--  -->


# JSON JavaScript Object Notation 面向对象
# 有类型的键值对，若为数值不加引号
# "key" : "value"
# "key" : ["value1", "value2"]    # 值可以是列表
# "key" : {"subkey1" : "subvalue1", "subkey2" : "subvalue2"}   # 值可嵌套


# YAML 全称是递归的定义形式(程序员对命名的一种思考，赞) YAML Ain't Markup Language
# 无类型的键值对
# key : value     # 无双引号

# name :    # 从属关系使用和Python一样的缩进来表达
#     subkey : subvalue

# name :    # 并列关系使用“-”表达
# -newValue
# -oldValue

# text: |
# 使用“|”表达整块数据

# #comment
# 使用“#”表示注释


# 三种信息标记语言的比较：
# XML 最早的通用信息标记语言，可扩展性好，但是繁琐。适用于Internet上信息交互和传递。
# JSON 信息有类型，适合程序处理。适用于移动应用云端和节点的信息通信（接口处理），无注释。
# YAML 信息无类型，文本信息比例最高，可读性好。适用于各类系统的配置文件，有注释易读。


# 信息提取的一般方法：
# 1.信息解析
# 2.直接搜索
# 3.两者结合，先搜索再解析

for link in soup.find_all('a'):
    print(link.get('href'))

# <>.find_all(name, attrs, recursive, string, **kwargs) 返回一个列表类型，存储查找的结果
# name
print(soup.find_all('a'))
print(soup.find_all(['a', 'b']))    # a, b标签组成列表作为第一个参数
for tag in soup.find_all(True):     # 搜索所有标签
    print(tag.name)
for tag in soup.find_all(re.compile('b')):      # 正则表达式搜索
    print(tag.name)     # body, b
# attrs 标签属性值的检索字符串，可标注属性检索
print(soup.find_all('p', 'course'))     # 限定标签和属性值
print(soup.find_all(id='link1'))    # 限定属性和属性值
print(soup.find_all(id='link'))    # 为空[]，无id=link
print(soup.find_all(id=re.compile('link')))
# recursive 是否对子孙全部检索，默认为True
print(soup.find_all('a'))
print(soup.find_all('a', recursive=False))  # 为空[]
# string 对标签中的字符串进行检索
print(soup.find_all(string="Basic Python"))
print(soup.find_all(string=re.compile("python")))   #正则表达式大小写敏感
# 简写形式
# <tag>(..) 等价于 <tag>.find_all(..)
