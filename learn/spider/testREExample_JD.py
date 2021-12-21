import re
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "网络连接异常，请检查！"

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)   # 最小匹配
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  # eval()去掉双引号
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '书包'
    depth = 2
    # 'http://search.jd.com/Search?keyword=' + goods + '&enc=utf-8&wq=" + goods
    # http://search.jd.com/Search?keyword=书包&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=3&wq=书包&page=3&s=54&click=0  1-1， 3-54， 5-111， 7-171， 9-231， 11-291
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()