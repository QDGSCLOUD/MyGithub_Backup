# ***\*Xray下载与使用\****

## ***\*1\*******\*、下载Xray\****

下载地址：

https://stack.chaitin.com/tool/detail?id=1

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps1.jpg) 

下载后得到一个文件名无序的压缩包，解压会有一个exe文件

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps2.jpg) 

创建一个文件夹把Xray的exe文件放进去，

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps3.jpg) 

然后在目录处输入powershell，回车，打开powershell控制台

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps4.jpg) 

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps5.jpg) 

执行命令：

.\xray_windows_amd64.exe genca

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps6.jpg) 

`此时也可能会报错, 再执行一次命令就行`

保证会出现出新的文件

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps7.jpg) 

直接双击打开ca.crt文件

依次选择：安装证书->当前用户->下一页->将所有的证书都放入下列存储->浏览->受信任的根证书颁发机构->确认->下一页->完成->是

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps8.jpg) 

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps9.jpg) 

## ***\*2\*******\*、Xray使用\****

先双击运行xray的exe文件（此时会出错误，不用在意）

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps10.jpg) 

回到文件夹，会出现一个config.yaml文件

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps11.jpg) 

通过记事本方式打开，此处为禁止访问域名，可自行更改限制

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps12.jpg) 

在目录中打开cmd

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps13.jpg) 

输入命令：

.\xray_windows_amd64.exe webscan --listen 127.0.0.1:7777 --html-output xray-testphp.html

即可开启7777端口监听，通过代理访问即可

快速启动：

新建一个文件，命名为xray.bat

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps15.jpg) 

通过记事本打开，写入命令：

xray_windows_amd64 webscan --listen 0.0.0.0:7777 --html-output webscan%date%.html

然后直接运行xray.bat即可

## ***\*3\*******\*、联动演示\****

打开Burp，设置代理（User Options）

![image-20230610203612764](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230610203612764.png)



此时在将 浏览器的代理 改为 本地ip的 7777 就可以啦!(不该的话, 我们网上冲浪的时候的流量就没法带到 **xray **中)

![image-20230610203730088](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230610203730088.png)

然后打开浏览器进行访问，即可开始扫描

![img](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/wps17.jpg) 

PS，如果在未开启Xray监听的情况下勾选了Burp的7777端口代理，会导致流量无法通过而访问浏览器失败

