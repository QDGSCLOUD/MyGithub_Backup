# VMware 虚拟机问题

## 虚拟机无ip

```
vim /etc/network/interfaces   # 在kali中输入该命令
```

> 添加相关内容(输入红框中的内容)
>
> ![image-20230619195952996](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230619195952996.png)

> 接着执行下面两条命令,  之后重启虚拟机便可
>
> ```
> ifconfig eth0 down
> ifconfig eth0 up
> ```



## Xshell 还是链接不上虚拟机

1. 检查自己输入的账号, 密码, ip 是不是都是正确的, 可能由于不小心输入错误链接不上
2. **`虚拟机和 物理机 互相 ping 一下`**, 如果不能ping通, 那就说明这不是Xshell问题, 而是 **虚拟机与物理机压根就没配置好**