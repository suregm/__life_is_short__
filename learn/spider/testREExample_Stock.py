import re
import requests
from bs4 import BeautifulSoup
import traceback


# 速度提高：
# 1.编码识别的优化
# r.apparent_encoding需要很长时间，如果知道网页的编码方式，可以手工赋值
# 2.增加进度动态显示
# 进度条


# def getHTMLText(url):   # 增加code='utf-8'
def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        r.encoding = code
        return r.text
    except:
        return ""

def getStockList(lst, stockUrl):
    # html = getHTMLText(stockUrl)
    html = getHTMLText(stockUrl, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue
    return ""

def getStockInfo(lst, stockUrl, fpath):
    count = 0
    for stock in lst:
        url = stockUrl + stock + ".html"
        html = getHTMLText(url) # 不加code参数时，默认为'utf-8'编码
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')

            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:   # 保存为文件
                f.write(str(infoDict) + "\n")
                count = count + 1
                # 不换行\r
                print('\r当前进度：{:.2f}'.format(count*100/len(lst)), end='')
        except:
            count = count + 1
            print('\r当前进度：{:.2f}'.format(count * 100 / len(lst)), end='')
            traceback.print_exc()   # 回溯异常
            continue

def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = "D:/StockInfo.txt"
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()