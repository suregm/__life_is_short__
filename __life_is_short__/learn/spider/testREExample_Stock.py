import re
import requests
import bs4 from BeautifulSoup
import traceback

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst, stockUrl):
    html = getHTMLText(stockUrl)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.findall('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue
    return ""

def getStockInfo(lst, stockUrl, fpath):
    for stock in lst:
        url = stockUrl + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class', 'stock-bets'})

            name = stockInfo.find_all(sttrs={'class', 'gets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')

            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + "\n")
        except:
            traceback.print_exc()
            continue

def main():
    stock_list_url = "http://quote.eastmoney.com/stock"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = "D://StockInfo.txt"
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)