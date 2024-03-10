# This file introduce the moudle of python named request
from urllib.parse import urlencode

import requests

def get_ai_weight(prepared_domain):

    # 我们想要拿到参数爱站词云, 可以这样
    Init_CheckICPWebSite_Url = "https://www.aizhan.com/cha/{}".format(prepared_domain)
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    print(Init_CheckICPWebSite_Url)
    resp = requests.get(Init_CheckICPWebSite_Url,headers=headers)   # 不加 headers , 就不会被显示出来.
    print(resp.text)

# 配置代理
def set_ip():
    url = "http://httpbin.org/ip"
    proxies = {"http":"http://47.106.105.236:80"}  # 这个代理ip不能用了, 只是为了示范
    resp = requests.get(url,proxies=proxies)
    print(resp.text)



if __name__ == "__main__":
    prepared_domain = "www.baidu.com"
    # get_ai_weight(prepared_domain)
    set_ip()












