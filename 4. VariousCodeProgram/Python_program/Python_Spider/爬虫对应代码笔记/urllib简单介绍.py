# 这个文件 对 urllib库进行简单的介绍
# urllib 分为四个模块
'''
1. 请求模块
2. 异常处理模块
3. url解析模块
4. robots.txt解析模块

'''
import urllib.request
from urllib import request

url = "https://httpbin.org/get"

headers = {
    # 此处填写headers
}

# 发起请求,  url可以是字符串, 也可以是一个 request对象
resp = request.urlopen(url)

# read()返回响应的数据
data = resp.read()


# info()   获取响应头的信息
print(resp.info())

# geturl() 获取访问链接
print(resp.geturl())

#getcode()返回状态码
print(resp.getcode())



# 请求对象的构造
req = urllib.request.Request(url,headers= headers)
response = urllib.request.urlopen(req).read().decode()


# 添加代理
proxies = {"http":"60168.206.199:1133"}

# 代理处理器
handnler = urllib.request.ProxyHandler(proxies=proxies)

# 获取open对象
openner = urllib.request.build_opener(handnler)

# 调用open方法
response = openner.open(req)

res = response.read()



