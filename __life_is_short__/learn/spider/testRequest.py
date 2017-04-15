import requests

# r = requests.get(url) 构造一个向服务器请求资源的Request对象，返回一个包含服务器资源的Response对象
# requests.get(url=, params=None, **kwargs)
r = requests.get("http://www.baidu.com")
print(r.status_code)    # 状态码返回200，表示连接成功，404表示失败

print(type(r))

print(r.headers)

print(r.encoding)   # 从HTTP header中猜测的响应内容编码方式
print(r.apparent_encoding)   # 从内容中分析出的响应内容编码方式（备选编码方式）
r.encoding = 'utf-8'
print(r.encoding)

print(r.text)   # HTTP响应内容的字符串形式，即页面内容
print(r.content)    # HTTP响应内容的十六进制形式
