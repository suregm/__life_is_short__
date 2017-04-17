import requests

url = 'http://gomx.win/2017/03/12/booklist-2017/'

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:10000])
except:
    print("爬取失败！")