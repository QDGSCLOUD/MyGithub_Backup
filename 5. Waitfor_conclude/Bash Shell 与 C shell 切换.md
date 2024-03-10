# Bash Shell 与 C shell 相互切换

## 安装cshell 

```
sudo apt-get install csh
```



## 将`bash shell` 转换为 `C sehll`

在普通用户终端下输入：

输入：

```
which csh
```

会显示 `csh` 出现的路径， 这个出现的路径要记住以下。

接着输入：

```
chsh
```

```
# 出现下面的内容：
提示
正在更改 root 的 SHELL
请输入新值，或直接敲回车键以使用默认值
	    登录 Shell [/bin/bash]:
输入
/bin/csh
\# echo $SHELL



返回s“/bin/csh”,说明SHELL修改成功。
```



此时输入：刚才记住的路径。 比如`/usr/bin/csh` 

**现在重启 Ubuntu， 重启后在`root`账号下， 输入：`echo $SHELL`** 

如果出现 `/bin/csh` 就代表成 功了。



## 将普通用户的`Shell` 也转化为 `Cshell`

直接在 **root** 账号下， 输入： `chsh -s /bin/csh 用户名`  

输入完成后， 重启Ubuntu就可以了。 一打开Shell ， 就是Cshell的 `%`





## Cshell 转换为 Bash Shell

```
chsh -s /usr/bin/csh 用户名
```

重启客户机， 就行了。









