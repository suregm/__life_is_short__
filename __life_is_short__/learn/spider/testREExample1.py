import re
import requests

def getHTMLText(url):
    print("")

def parsePage(ilt, html):
    print("")

def printGoodsList(ilt):
    print("")

def if __name__ == '__main__':

def main():
    goods = '书'
    depth = 2
    start_url = 'http://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
        except:
            return ""

