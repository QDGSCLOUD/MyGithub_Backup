# Wireshark介绍

1、wirshark介绍：

Wireshark是一个网络封包分析软件。使用WinPCAP作为接口，直接与网卡进行数据报文交换。我们网络安全工程师或者软件工程师可以利用wireshark来进行分析网络。

wireshark只能查看封包，而不能修改封包的内容，或者发送封包。bp、Fiddler就可以改包

仅仅只是监听共享网络上传送的数据包。

2、什么人会用到wireshark

1. 网络管理员会使用wireshark来检查网络问题
2. 软件测试工程师使用wireshark抓包，来分析自己测试的软件
3. 从事socket编程的工程师会用wireshark来调试
4. 安全工程师用到wireshark来分析TCP,UDP流量。
   总之跟网络相关的东西，都可能会用到wireshark.

# Wireshark使用


## 网卡选择模式


**2、开启混杂模式**

局域网的所有流量都会发送给我们的电脑，默认情况下，我们的电脑只会对自己mac的流量进行解包，而丢弃其他mac的数据包。

开启混杂模式后，我们就可以解析其他mac的数据包，因此，我们使用Wireshark时，通常都会开启混杂模式。

点击菜单栏的「捕获」按钮，点击「选项」

## 过滤器

* Wireshark提供了两种过滤器：
  * 1、捕获过滤器
  * 2、显示过滤器

**1、捕获过滤器**
在抓包之前就设定好过滤条件，然后只抓取符合条件的数据包

捕获（Capture）--捕获过滤器（Option）

捕获（Capture）--捕获过滤器（Capture Filters)


过滤基本的语法格式：BPF语法格式。

1）BPF语法

BPF（全称 Berkeley Packet Filter），中文叫伯克利封包过滤器，它有四个核心元素：类型、方向、协议 和 逻辑运算符。

1. 类型Type：主机（host）、网段（net）、端口（port）
2. 方向Dir：源地址（src）、目标地址（dst）
3. 协议Proto：各种网络协议，比如：tcp、udp、http
4. 逻辑运算符：与（ && ）、或（ || ）、非（ ！）

四个元素可以自由组合，比如：

1. src host 192.168.31.1：抓取源IP为 192.168.31.1 的数据包
2. tcp || udp：抓取 TCP 或者 UDP 协议的数据包



**2、显示过滤器**
在已捕获的数据包集合中设置过滤条件，隐藏不想显示的数据包，只显示符合条件的数据包。
用于在抓取数据包后设置过滤条件进行过滤数据包。通常是在抓取数据包时设置条件相对宽泛，抓取的数据包内容较多时使用显示过滤器设置条件顾虑以方便分析。同样上述场景，在捕获时未设置捕获规则直接通过网卡进行抓取所有数据包。

显示过滤器的语法包含5个核心元素：IP、端口、协议、比较运算符和逻辑运算符。

1. IP地址：ip.addr、ip.src、ip.dst
2. 端口：tcp.port、tcp.srcport、tcp.dstport
3. 协议：tcp、udp、http
4. 比较运算符：> < == >= <= !=
5. 逻辑运算符：and、or、not、xor（有且仅有一个条件被满足）

5个核心元素可以自由组合，比如：

* ip.addr == 192.168.32.121：显示IP地址为 192.168.32.121 的数据包
* tcp.port == 80 ：显示端口为 80 的数据包

使用方法：在过滤栏输入过滤语句，修改后立即生效。


**3、过滤器具体写法**
  * 显示过滤器写法
    * 1、过滤值比较符号及表达式之间的组合
    * 2、针对ip的过滤
    * 3、针对协议的过滤
    * 4、针对端口的过滤（视传输协议而定）
    * 5、针对长度和内容的过滤
    * 5、针对http请求的一些过滤实例。
  * 捕捉过滤器写法
    * 1、比较符号
    * 2、常用表达式实例


注意：这两种过滤器所使用的语法是完全不同的，捕捉网卡数据的其实并不是Wireshark,而是WinPcap,当然要按WinPcap的规则来，显示过滤器就是Wireshark对已捕捉的数据进行筛选。

使用捕获过滤器的主要原因就是性能。如果你知道并不需要分析某个类型的流量，那么可以简单地使用捕获过滤器过滤掉它，从而节省那些会被用来捕获这些数据包的处理器资源。当处理大量数据的时候，使用捕获过滤器是相当好用的。

Wireshark拦截通过网卡访问的所有数据，前提是没有设置任何代理。Wireshark不能拦截本地回环访问的请求，即127.0.0.1或者localhost。



![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/18449/1670206151094/a6756652be3e48eab112e1b7dab98e05.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/18449/1670206151094/7e0314ef86e14159943ef349fc8daf84.png)

**2、针对ip的过滤**
* 对源地址进行过滤

```
ip.src == 192.168.0.1
```

* 对目的地址进行过滤

```
ip.dst == 192.168.0.1
```

* 对源地址或者目的地址进行过滤

```
ip.addr == 192.168.0.1
```

* 如果想排除以上的数据包，只需要将其用括号囊括，然后使用 “!” 即可

```
!(ip.addr == 192.168.0.1)
```

**3、针对协议的过滤**
* 获某种协议的数据包，表达式很简单仅仅需要把协议的名字输入即可

```
http
```

注意：是区分大小写，只能为小写

* 捕获多种协议的数据包

```
http or telnet
```

* 排除某种协议的数据包

```
not arp 或者 !tcp
```

**4、针对端口的过滤（视传输协议而定）**
* 捕获某一端口的数据包（以tcp协议为例）

```
tcp.port == 80
```

* 捕获多端口的数据包，可以使用and来连接，下面是捕获高于某端口的表达式（以udp协议为例）

```
udp.port >= 2048
```

**5、针对长度和内容的过滤**
* 针对长度的过虑（这里的长度指定的是数据段的长度）

```
udp.length < 20   http.content_length <=30
```

* 针对uri 内容的过滤

```
http.request.uri matches 'user' (请求的uri中包含“user”关键字的)
```

注意：matches 后的关键字是不区分大小写的！

```
http.request.uri contains 'User' (请求的uri中包含“user”关键字的)
```

注意：contains 后的关键字是区分大小写的！

**5、针对http请求的一些过滤实例。** 
* 过滤出请求地址中包含“user”的请求，不包括域名；

```
http.request.uri contains 'User'
```

* 精确过滤域名

```
http.host==baidu.com
```

* 模糊过滤域名

```
http.host contains 'baidu'
```

* 过滤请求的content_type类型

```
http.content_type =='text/html'
```

* 过滤http请求方法

```
http.request.method=='POST'
```

* 过滤tcp端口

```
tcp.port==80
```

```
http && tcp.port==80 or tcp.port==5566
```

* 过滤http响应状态码

```
http.response.code==302
```

* 过滤含有指定cookie的http数据包

`http.cookie contains 'userid'`

比较符号

```

与：&&或者and或：||或者or非：！或者not
```

实例：
```
src or dst portrange 6000-8000 && tcp or ip6
```

**2、常用表达式实例**
* 源地址过滤

```
src www.baidu.com
```

* 目的地址过滤 
```
dst www.baidu.com

```
* 目的地址端口过滤

```
dst post 80
```