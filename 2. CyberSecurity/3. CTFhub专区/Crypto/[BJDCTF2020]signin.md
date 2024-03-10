# [BJDCTF2020]signin

![image-20230406081750474](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406081750474.png)

观察密码: 是base64加密的, 所以用Python来解一下, 当然也可以直接用在线解析工具.

```Python
import requests,binascii

def getanwser():
    chiper = '424a447b57653163306d655f74345f424a444354467d'
    res = binascii.unhexlify(chiper)
    print(res.decode('utf-8'))



if __name__ =="__main__":
    getanwser()
```

![image-20230406083415589](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406083415589.png)

