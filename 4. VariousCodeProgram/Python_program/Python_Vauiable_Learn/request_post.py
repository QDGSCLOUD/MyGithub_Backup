import json

import  requests
import time

def get_post_Url (url):
    headers = {
        # 如果还是不显示, 那就再添加 Request header字段.
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
 ,       "Referer":"https: // fanyi.youdao.com /",
        "Cookie": "OUTFOX_SEARCH_USER_ID=847645929@10.105.253.23; OUTFOX_SEARCH_USER_ID_NCOO=1436624305.9027302"
    }

    data = {
        "i": " 你好",
        "from": " auto",
        "to": "",
        "dictResult": " true",
        "keyid": " webfanyi",
        "sign": " cc52206542e7fb14fe99149c5ff93788",
        "client": " fanyideskweb",
        "product": " webfanyi",
        "appVersion": " 1.0.0",
        "vendor": " web",
        "pointParam": " client,mysticTime,product",
        "mysticTime": " 1692259728059",
        "keyfrom": " fanyi.web",
        "mid": " 1",
        "screen": " 1",
        "model": " 1",
        "network": " wifi",
        "abtest": " 0",
        "yduuid": " abcdefg",
    }

    resp = requests.post(url,headers=headers,data=data)

    # 注意此时从网页中拿到的是json根式的数据, 从Python角度来看, 是字典, 但实际上不是字典
    # 我们需要将json格式的数据 转化为  Python格式的数据.
    Python_data = json.loads(resp.text)
    # 之后就可以按照python的 列表的索引,字典的下标 等获取到想要的值.
    print(resp.text)

if __name__ == '__main__':
    url ="https://dict.youdao.com/webtranslate"
    get_post_Url(url)


