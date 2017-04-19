import requests
from bs4 import BeautifulSoup

# 技术路线：requests-bs4
# 定向爬取，固定url
# 可行性：网页静态文本形式，查看robots.txt

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    return ""

def fillUnivList(ulist, html):
    pass

def printUnivList(ulist, num):
    print("Suc" + str(num))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 50)    # 前50名
