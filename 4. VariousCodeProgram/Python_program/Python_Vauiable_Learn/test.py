
import requests
url = "https://icp.aizhan.com/www.baidu.com/"
resp = requests.get(url)
print(resp)
print(resp.text)
