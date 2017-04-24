import re


#
# .      任意单个字符
# []      字符集，约定取值范围 [abc]表示a/b/c中的任意一个，[a-z]
# [^]      非字符集，给出排除范围 [^abc]表示除a/b/c之外的单个字符
# *      前一个字符0次或多次扩展
# +      前一个字符1次或多次扩展
# ?      前一个字符出现0次或1次
# |      或，并列的任意一个
# {m}      扩展前一个字符m次
# {m,n}      扩展前一个字符m至n次（含n）
# ^      匹配字符串开头
# $      匹配字符串结尾
# ()      分组标记，内部只能使用“|”操作符 (abc)表示abc，(abc|def)表示abc或def
# \d      数字，等价于[0-9]
# \w      单词字符，等价于[A-Za-z0-9_]


# 经典正则表达式实例
re.compile("^[A-Za-z]+$")   # 由26个英文字母组成的字符串
re.compile("^-?\d+$")   # 整数形式的字符串
re.compile("[\u4e00=\u9fa5]")   # 匹配中文字符
re.compile("(([1-9]?\d | 1\d{2} | 2[0-4]\d | 25[0-5]).){3}([1-9]?\d | 1\d{2} | 2[0-4]\d | 25[0-5])")  # 匹配IP


# 正则表达式的表示类型
# raw string类型（原生字符串类型，是不包含转义符的字符串），表示为r'text'
# string类型，需要加转义字符“\”


# re库主要功能函数
# re.search(pattern, string, flags=0) # 返回match对象，match.group(0)
# re.match()  # 从头位置开始匹配，返回匹配到的match对象
# re.findall()    # 返回子串的列表类型
# re.split(pattern, string, maxsplit=0, flags=0)  # 返回分割对象的列表类型 maxsplit最大分割数，剩余部分作为最后一个元素输出
# re.finditer()   #返回一个匹配结果的迭代类型，每个迭代元素是match对象
# re.sub(pattern, repl, string, count=0, flags=0)    # 替换匹配的子字符串，返回替换后的字符串 repl是替换匹配字符串的字符串 count匹配的最大替换次数

# flags: 控制标记
# re.I re.IGNORECASE 忽略正则表达式的大小写
# re.M re.MULTILINE 正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
# re.S re.DOTALL 正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符

match = re.search(r'[1-9]\d{5}', "Wuhan 430070")
if match:
    print(match.group(0))

# match = re.match(r'[1-9]\d{5}', "Wuhan 430070")
# print(match.group(0))   # 此时match对象为空，从头位置未匹配到，报错'NoneType' object has no attribute 'group'

match = re.match(r'[1-9]\d{5}', "430070 Wuhan")
# if match: # 加上if判断是否为空
print(match.group(0))   # 430070

ls = re.findall(r'[1-9]\d{5}', "Wuhan430070 Langkou442100")
print(ls)

ls = re.split(r'[1-9]\d{5}', "Wuhan430070 Langkou442100")
print(ls)   # ['Wuhan', ' Langkou', '']
ls = re.split(r'[1-9]\d{5}', "Wuhan430070 Langkou442100", maxsplit=1)
print(ls)

# 迭代类型使用循环迭代
for m in re.finditer(r'[1-9]\d{5}', "Wuhan430070 Langkou442100"):
    if m:
        print(m.group(0))

# 正则替换
str = re.sub(r'[1-9]\d{5}', ':sureGM', "Wuhan430070 Langkou442100")
print(str)


# Re库的等价用法
# 函数式用法：一次性操作
rst = re.search(r'[1-9]\d{5}', "Wuhan430070 Langkou442100")
# 面向对象用法：编译后的多次操作
pat = re.compile(r'[1-9]\d{5}', flags=0)    #将正则表达式的字符串形式编译成正则表达式对象
rst = pat.search("Wuhan430070 Langkou442100")
print(rst)  # <_sre.SRE_Match object; span=(5, 11), match='430070'>


# r'[1-9]\d{5}'只是正则表达式的字符串表示，compile后的regex才是正则表达式对象，此时regex可以使用对象方法
regex = re.compile(r'[1-9]\d{5}', flags=0)
regex.search()
regex.match()
regex.findall()
regex.split()
regex.finditer()
regex.sub()