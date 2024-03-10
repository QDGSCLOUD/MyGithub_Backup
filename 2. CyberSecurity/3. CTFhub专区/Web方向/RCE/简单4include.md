# include的理解

原理:

下面是ctfhub上给出的解释:

假如在index.php中include了一个文件, 那么**不管这个文件后缀是什么 这个文件中的内容将会直接出现在index.php.**

所以这道题的payload构造思路就是把shell.txt里的内容想办法放到index.php中去



**具体步骤:**

直接用蚁剑连接:

`题目给的url` 拼接上 `?file=shell.txt`

![image-20230406121145733](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406121145733.png)

**连接密码** 是从源代码中 下载 **shell.txt** 看到的, 我们要包含的也就是这个 **shell.txt**

![image-20230406121324891](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406121324891.png)

