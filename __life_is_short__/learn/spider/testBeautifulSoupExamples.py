import requests
from bs4 import BeautifulSoup
import bs4

# 技术路线：requests-bs4
# 定向爬取，固定url
# 可行性：网页静态文本形式，查看robots.txt


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):     # bs4.element.Tag的tr实例，表明是表格的一行
            tds = tr('td')
            # print(tds[0].string)  # 2017时tds[0].string为None，2016时为序号
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
    print(ulist)
    # pass

def printUnivList(ulist, num):
    # 引导符号:前面加上序号，助于引用定位对应参数
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"   # {1:{3}^10} 槽宽为10，需要填充时填充第(3+1)个位置的参数（中文空格chr(12288)）
    print(tplt.format("排名", "学校", "得分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        # print(tplt.format(u[0], u[1], u[2], chr(12288)))  # 2017为None时会报错 non-empty format string passed to object.__format__
        print(tplt.format(i + 1, u[1].strip(), u[2].strip(), chr(12288)))   # .strip() 去除两侧空格
    print("Success", str(num))

def main():
    uinfo = []
    # url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 50)    # 前50名


main()


# 格式化输出，槽{}与format参数中的顺序一一对应
# print("{}: 计算机{}的CPU占用率为{}%。".format("2017-04-19", "PYTHON", 12))
# 中文对齐问题
# ：         <填充>    <对齐>    <宽度>            ,           <精度>  <类型>
# 引导符号      中英文             槽的设定输出宽度    千分位分隔符
# 系统默认：当中文字符宽度不够时，采用西文字符填充，而中西文字符占用宽度不同。
# 中文对齐解决方法
# 采用中文字符的空格填充 chr(12288)