from bs4 import BeautifulSoup
import requests

# Beautiful Soup库是解析、遍历、维护“标签树”的功能库

url = 'http://python123.io/ws/demo.html'
# <html>
#  <head>
#   <title>
#    This is a python demo page
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The demo python introduces several python courses.
#    </b>
#   </p>
#   <p class="course">
#    Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
#    <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
#     Basic Python
#    </a>
#    and
#    <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
#     Advanced Python
#    </a>
#    .
#   </p>
#  </body>
# </html>


r = requests.get(url)
print(r.text)

print("\n======================\n")

demo = r.text
# from bs4 import BeautifulSoup     # 第二种引用 import bs4
# soup = BeautifulSoup('<p>data</p>', 'html.parser')
# 共四种解析器
# 'html.parser' 条件：安装bs4库
# 'lxml' 条件：pip install lxml
# 'xml' 条件：pip install lxml
# 'html5lib' 条件：pip install html5lib
soup = BeautifulSoup(demo, "html.parser")   # 解析器
# soup2 = BeautifulSoup(open("D://demo.html"), "html.parser")  # 打开HTML文件的方式
print(soup.prettify())

# Beautiful Soup类的基本元素
# tag
# Name 格式：<tag>.name
# Attributes 格式：<tag>.attrs
# NavigableString 标签内非属性字符串 格式：<tag>.string
# Comment 标签内字符串的注释部分，一种特殊的Comment类型

print("\n======================\n")

print(soup.title)
tag = soup.a
print(tag)
print(tag.name)
print(tag.parent.name)
print(tag.parent.parent.name)
print(tag.attrs)
print(tag.attrs['class'])
print(tag.attrs['href'])
print(type(tag.attrs))
print(type(tag))

print(tag.string)
print(soup.p)   # <class 'bs4.element.Tag'>
print(type(soup.p))
print(soup.p.string)    # 非属性字符串，可跨越多个标签层次直接获取文本字符串
print(type(soup.p.string))  # <class 'bs4.element.NavigableString'>

newSoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
print(newSoup.b.string)
print(type(newSoup.b.string))   # <class 'bs4.element.Comment'> # 判断是否是注释，type为bs4.element.Comment
print(newSoup.p.string)
print(type(newSoup.p.string))   # <class 'bs4.element.NavigableString'>




# 基于bs4的HTML遍历方法
# 上行遍历、下行遍历、平行遍历


# 下行遍历
# .contents 子节点的列表
# .children 子节点的迭代类型，循环遍历儿子节点
# .descendants 子孙节点的迭代类型，循环遍历包括所有子孙节点
print(soup.head)
print(soup.head.contents)
print(soup.body.contents)
print(len(soup.body.contents))
print(soup.body.contents[1])

print("\n======================\n")
# 遍历儿子节点
for child in soup.body.children:
    print(child)

print("\n======================\n")
# 遍历子孙节点
for child in soup.body.descendants:
    print(child)
print("\n======================\n")


# 上行遍历
# .parent
# .parents 节点先辈标签的迭代类型
print(soup.title.parent)
print(soup.html.parent) # html最高层标签，其父亲标签是其自身
print(soup.parent)  # 为空None
# 由此通用代码：
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
# 输出：
# None
# p
# body
# html
# [document]
print("\n======================\n")


# 平行遍历
# 平行遍历发生在同一个父节点下的各节点间
# .next_sibling 返回按照HTML文本顺序的下一个平行节点标签
# .previous_sibling 返回按照HTML文本顺序的上一个平行节点标签
# .next_siblings 迭代返回按照HTML文本顺序的后续所有平行节点标签
# .previous_siblings 返回按照HTML文本顺序的前置所有平行节点标签
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)
print(soup.a.previous_sibling.previous_sibling) # 返回None，已无再前一个平行节点标签
print(soup.a.parent)

# 循环遍历后续节点
for sibling in soup.a.next_siblings:
    print(sibling)
print("\n======================\n")
# 循环遍历前续节点
for sibling in soup.a.previous_sibling:
    print(sibling)
print("\n======================\n")



# 基于bs4库的HTML格式输出
# bs4转换为UTF-8
soup.prettify() # 增加换行符，美观
newSoup = BeautifulSoup("<p>《中文》</p>", "html.parser")
print(newSoup.p.string)
print(newSoup.p.prettify())