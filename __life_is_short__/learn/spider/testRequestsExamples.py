import requests
import os

# 爬取内容
url = 'http://gomx.win/2017/03/12/booklist-2017/'

try:
    r = requests.get(url)
    print(r.raise_for_status())
    print(r.request.headers)
    kv = {'user-agent': 'Mozilla/5.0'}  # 模拟UA
    r = requests.get(url, headers = kv)
    print(r.request.headers)
    print(r.raise_for_status())
    r.encoding = r.apparent_encoding
    print(r.text[:10000])
except:
    print("爬取失败！")


# 提交内容
keyword = 'Python'
kv = {'wd': keyword}
r = requests.get('http://www.baidu.com/s', params=kv)
print(r.status_code)
print(r.request.url)    # http://www.baidu.com/s?wd=Python  http://www.so.com/s?q=Python
print(len(r.text))


# 网络图片的爬取
url = 'http://gomx.win/2016/06/19/live-YOUNG/'
root = "D://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("file saved successfully.")
    else:
        print("file exists.")
except:
    print("爬取失败！")


