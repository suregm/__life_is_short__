import requests

# HTTP协议
# URL格式 http://host[:port][path]
# port缺省值为80

# URL是通过HTTP协议存取Internet资源的Internet路径，一个URL对应一个数据资源。

# HTTP协议对资源的操作
# 六大方法 与Requests库方法一一对应
# GET   requests.get()
# HEAD  requests.head() 请求获取URL位置资源的响应消息报告，即获得该资源的头部信息
# POST  requests.post() 请求向URL位置的资源附加新的数据
# PUT  requests.put() 请求向URL位置存储一个资源，覆盖原资源
# PATCH  requests.patch() 请求局部更新URL位置的资源，即改变该处资源的部分内容
# DELETE  requests.delete()

r = requests.head('http://gomx.win')    # requests.head()节省带宽获取概要信息
print(r.headers)
print(r.text)   # 此时r只是头部信息，text为空

# post方法
payload = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.post('http://gomx.win', data = payload)
print(r2.text)
# 向URL post一个字典，自动编码为form表单
{
    "form": {
        "key2": "value2",
        "key1": "value1"
    },
}
r3 = requests.post('http://gomx.win', data = 'DeepBLUE')
print(r3.text)
# 像URL post一个字符串，自动编码为data
{
    "data": "DeepBLUE",
    "form": {}
}

# put方法
# 同post方法，但是会将原有数据覆盖。


# requests.request(method=, url=, **kwargs)
# method: 请求方式，共7种，对应get/head/post/put/patch/delete/options.
# **kwargs: 控制访问的参数，共13个，均为可选项

#   params: 字典或字节序列，作为参数增加到url中
kv = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('GET', 'http://gomx.win/ws', params=kv)
print(r.url)    # http://gomx.win/ws?key2=value2&key1=value1

#   data: 字典、字节序列或文件对象，作为Requests的内容
r = requests.request('POST', 'http://gomx.win/ws', data=kv)
body = '主体内容'
r = requests.request('POST', 'http://gomx.win/ws', data=body)

#   json: JSON格式的数据，作为Requests的内容
r = requests.request('POST', 'http://gomx.win/ws', json=kv)

#   headers: 字典，HTTP定制头
hd = {'user-agent': 'chrome/10'}    # 浏览器模拟
r = requests.request('POST', 'http://gomx.win', headers=hd)

#   cookies: 字典或CookieJar，Requests中的cookie

#   auth: 元组，支持HTTP认证功能

#   file: 字典类型，传输文件
fs = {'file': open('sure.txt', 'rb')}
r = requests.request('POST', 'http://gomx.win', file=fs)

#   timeout: 设定超时时间，秒为单位
r = requests.request('GET', 'http://gomx.win', timeout=10)

#   proxies: 字典类型，设定访问代理服务器，可以增加登录认证
pxs = {'http': 'http://user:pass@10.10.10.1:1234',
       'https': 'https://10.10.10.1:4321'}
r = requests.request('GET', 'http://gomx.win', proxies=pxs)

#   allow_redirects: True/False，默认为True，重定向开关

#   stream: True/False，默认为True，获取内容立即下载开关

#   verify: True/False，默认为True，认证SSL证书开关

#   cert: 本地SSL证书路径



# requests.get(url，params=None, **kwargs)
# params: url中的额外参数，字典或字节流格式，可选
# **kwargs是除了headers之外的12个可选参数

# requests.head(url, **kwargs)
# **kwargs是13个可选控制访问参数

# requests.post(url=, data=None, json=None, **kwargs)
# data: 字典、字节序列或文件，Requests的内容
# json: JSON格式的数据，Requests的内容
# **kwargs: 除data、json之外的11个控制访问的参数

# requests.patch(url=, data=None, **kwargs)
# data: 字典、字节序列或文件，Requests的内容
# **kwargs: 除data之外的12个控制访问的参数

# requests.delete(url=, **kwargs)
# **kwargs: 13个控制访问的参数