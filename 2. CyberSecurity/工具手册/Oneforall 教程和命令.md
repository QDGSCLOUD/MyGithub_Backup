```
NAME
    oneforall.py - OneForAll帮助信息

SYNOPSIS
    oneforall.py COMMAND | --target=TARGET <flags>

DESCRIPTION
    OneForAll是一款功能强大的子域收集工具

    Example:
        python3 oneforall.py version
        python3 oneforall.py --target example.com run
        python3 oneforall.py --targets ./domains.txt run
        python3 oneforall.py --target example.com --valid None run
        python3 oneforall.py --target example.com --brute True run
        python3 oneforall.py --target example.com --port small run
        python3 oneforall.py --target example.com --fmt csv run
        python3 oneforall.py --target example.com --dns False run
        python3 oneforall.py --target example.com --req False run
        python3 oneforall.py --target example.com --takeover False run
        python3 oneforall.py --target example.com --show True run

    Note:
        参数alive可选值True，False分别表示导出存活，全部子域结果
        参数port可选值有'default', 'small', 'large', 详见config.py配置
        参数fmt可选格式有 'csv','json'
        参数path默认None使用OneForAll结果目录生成路径

ARGUMENTS
    TARGET
        单个域名(二选一必需参数)
    TARGETS
        每行一个域名的文件路径(二选一必需参数)

FLAGS
    --brute=BRUTE
        s
    --dns=DNS
        DNS解析子域(默认True)
    --req=REQ
        HTTP请求子域(默认True)
    --port=PORT
        请求验证子域的端口范围(默认只探测80端口)
    --valid=VALID
        只导出存活的子域结果(默认False)
    --fmt=FMT
        结果保存格式(默认csv)
    --path=PATH
        结果保存路径(默认None)
    --takeover=TAKEOVER
        检查子域接管(默认False)
```
水
