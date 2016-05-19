from statsmodels.tsa.vector_ar.tests.example_svar import end

__author__ = 'sure GM' '2016/5/16 0:25'
# coding: UTF-8

# now the time is 02:53 2016/5/16
# 03:05 Sure, good night!

# 有5名某界大佬xiaoyun、xiaohong、xiaoteng、xiaoyi和xiaoyang，其QQ号分别是88888、5555555、11111、1234321和1212121，用字典将这些数据组织起来。编程实现以下两个功能：
# （1）用户输入某一个大佬的姓名后可以输出其QQ号，如果输入的姓名不在字典中则返回提示信息并允许再次输入；
# （2）寻找所有有QQ靓号（5位数或小于5位数）的大佬，输出所有姓名。
# 其中Python 2中提示输入和输出结果的两句提示语请使用如下形式：
# name = raw_input("Please input the name:")
# print  "Who has the nice QQ number?"
# 其中Python 3中提示输入和输出结果的两句提示语请使用如下形式：
# name = input("Please input the name:")
# print("Who has the nice QQ number?")

qqInfo = dict(xiaoyun=88888, xiaohong=5555555, xiaoteng=11111, xiaoyi=1234321, xiaoyang=1212121)
print(qqInfo)


def findQQ(qqInfo):
    nameIsExist = True
    while nameIsExist:
        name = input("Please input the name:")
        if name == "-1":
            nameIsExist = False
            break
        elif qqInfo.keys().__contains__(name):
        # elif name in qqInfo:
            print("%s's QQ number is %s" % (name, str(qqInfo[name])))
        else:
            print("%s is not exist, pls input a name again." % name)
            findQQ(qqInfo)
            break


def findAllNiceQQNumber(qqInfo):
    print("Who has the nice QQ number?")
    for name in qqInfo.keys():
        if len(str(qqInfo[name])) <= 5:
            print(name, end=' ')
    print()


def main():
    findAllNiceQQNumber(qqInfo)
    print("pls input someone's name to find his QQ number, input \'-1\' to quit.")
    findQQ(qqInfo)


if __name__ == '__main__':
    main()