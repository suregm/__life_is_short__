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
    "data": "DeepBLUE"
    "form": {},
}