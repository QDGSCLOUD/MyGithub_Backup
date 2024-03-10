

# CTFhub技能树的RCE的  php://input

**原理**:

常用到伪协议的`php://input`和`php://filter`.其中php://input要求`allow_url_include`设置为`On`



**步骤**:

1. 直接BP抓包并改包

![image-20230406113617362](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406113617362.png)



2. ![image-20230406113950898](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230406113950898.png)

> 本题已完成.