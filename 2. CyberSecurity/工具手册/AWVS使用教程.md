# AWVS使用教程

# 界面介绍

> 左边栏:

- **Dashboard**：仪表盘，显示扫描过的网站的漏洞信息
- **Targets**：目标网站，需要被扫描的网站
- **Vulnerabilities**：漏洞，显示所有被扫描出来的网站漏洞
- **Scans**：扫描目标站点，从Target里面选择目标站点进行扫描
- **Reports**：漏洞扫描完成后生成的报告

设置菜单功能介绍：设置菜单共有8个模块，分别为Users、Scan Types、Network Scanner、Issue Trackers、Email Settings、Engines、Excluded Hours、Proxy Settings

- **Users**：用户，添加网站的使用者、新增用户身份验证、用户登录会话和锁定设置
- **Scan Types**：扫描类型，可根据需要勾选完全扫描、高风险漏洞、跨站点脚本漏洞、SQL 注入漏洞、弱密码、仅爬网、恶意软件扫描
- **Network Scanner**：网络扫描仪，配置网络信息包括地址、用户名、密码、端口、协议
- **Issue Trackers**：问题跟踪器，可配置问题跟踪平台如github、gitlab、JIRA等
- **Email Settings**：邮件设置，配置邮件发送信息
- **Engines**：引擎，引擎安装删除禁用设置
- **Excluded Hours**：扫描时间设置，可设置空闲时间扫描
- **Proxy Settings**：代理设置，设置代理服务器信息



##  简单使用

### 模式一: 可以自动登录的(没有验证码的)

> 1. 

![image-20230322214735114](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230322214735114.png)

> 2.

![image-20230322214923228](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230322214923228.png)

> 3. **扫描速度**

![image-20230322220048068](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230322220048068.png)

> 自动登录 模式

![image-20230322220802297](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230322220802297.png)



> 设置 **防止不小心退出**

![image-20230322221220307](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230322221220307.png)



> 开始扫描 , 之后 自动询问是否保存, **直接选择保存**就行

![image-20230322221729254](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230322221729254.png)





![image-20230322221901236](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230322221901236.png)



> 一般 **Report** 选项一般设置为 **Comprehensive(new)**
>
> 一般 **Schedule**  这一项设置为 **Future**, 这个时候下方会有时间显示.



> 最后, 直接**Create Scan**

> 这个时候它会自己出来, **直接点击看到的 , 自己设置的url 就可以看到正在扫描的情况**



> **扫描完成后, 在列表的右上方, 会有Generate 选项, 我们可以点击, 选择生成不同类型的报告**







# 模式二 : 使用登录序列脚本进行扫描

![image-20230323220328982](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230323220328982.png)



**之后就是 输入   账号   和   密码 **, 之后,  **Next** , 此时就可以了

> 如果没有  awvs没有记录上输入的账号密码, **多试几次, 既可以啦!**



# 模式三: 登录绕过(有验证码的)

**一直往下滑, 找到 =====>   Advance **

![image-20230323221507711](https://cdn.jsdelivr.net/gh/wangyuhubugui/BJYH_picture@main/img/image-20230323221507711.png)