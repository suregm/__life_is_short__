# 信息标记


# 目前国际公认的信息标记语言有三种：
# XML eXtensible Markup Language
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
#     newName : newValue
#     oldName : oldValue

# name :    # 并列关系使用“-”表达
# -newValue
# -oldValue

# text: |
# 使用“|”表达整块数据

# #comment
# 使用“#”表示注释