import requests

# response = requests.get("http://gomx.win")
# print(response.text)

requests.ConnectionError
requests.HTTPError
requests.URLRequired
requests.TooManyRedirects
requests.ConnectTimeout
requests.Timeout

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()    # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding    #
        return r.text
    except:
        return "throw exception"

if __name__ == "__main__":
    url = "http://gomx.win"
    print(getHTMLText(url))