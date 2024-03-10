---
IDEA 介绍和使用

---

# 安装

1. 直接解压压缩包. (我的windows电脑已经安装了jdk17 和 18)
2. 先点击加压出来的 `绿化.bat`
3. 直接点击解压出的 ` ideaIU_2021.2.3_64bit_Portable\bin`   下的 `idea64.exe` . 这样就可以直接启动并使用了.

# IDEA介绍和使用

> 由于 `IDEA工具非常强大` , 所以在下面介绍一些常用的设置和使用.
>
> 遇到不知道咋设置直接 用浏览器搜索就行.

## 创建项目

1. 我们起初创建的`Project` 不是真正的项目那只是一个工作空间,

   整整的项目是在`Project` 下的 `Model`

   ![image-20230716122252696](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230716122252696.png)



## 改变主题

![image-20230716130935259](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716130935259.png)



接着, 选择主题就行.

![image-20230716130836185](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716130836185.png)



## 用 鼠标管轮改变字体大小

进入`File==>Settings`

![image-20230716131106921](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716131106921.png)

接着 **打钩**就行

![image-20230716131229144](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716131229144.png)

点击  `Ok`  之后,就可以通过  `Ctrl + 鼠标滚轮` 控制字体大小了



## 设置默认的字体大小

![image-20230716131843048](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716131843048.png)



## 自动导包和优化包(自动删除)

![image-20230716132325526](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716132325526.png)

> **手动导包**快捷键:  鼠标放在单词上, 按 alt + enter 就可以了



## 不区分大小写



![image-20230716133613536](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716133613536.png)

## 将工具栏放在一起

![image-20230716122629991](C:\Users\2892706668\AppData\Roaming\Typora\typora-user-images\image-20230716122629991.png)



## 扩大显示的文件标签

![image-20230716133849434](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716133849434.png)















```
/**
* @Auther: QDGS
* @Date: ${DATE} - ${MONTH} - ${DAY} - ${TIME}
* @Description: ${PACKAGE_NAME}
*/
```



## 创建文件打开的模板

![image-20230716134840499](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716134840499.png)

**注意: 这个模板只对`新建`的类有效**



## 配置编码格式为utf-8

配置如下: 

![image-20230716135151150](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716135151150.png)

> `Tips`: 一打开导入的文件, 我们可以在IDEA的`右下角`调整编码格式





## 实现自动编译

![image-20230716135511620](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716135511620.png)



## 省电模式(关闭代码提示)

![image-20230716135722215](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716135722215.png)

打开省点模式, 代码提示就没有了.



## 导入jar包

1. `Settings` ==> `Project Structure` ==> 点击左边栏的 `Libraries ` ==> 点击 `+` 号, 选择 `java`

2. 找到 准备好的java包

3. 选在要添加到那个模块项目

4. 点击`Apply` , 在点击 `Ok`

   ![image-20230716140509869](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716140509869.png)



## 自动添加序列化版本号

![image-20230716140709332](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716140709332.png)

假如此处想给`Person`添加版本号 , 那么让光标放在`Person `上, 然后按住 `Alt + Enter` .

![image-20230716141257916](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716141257916.png)





# 常用快捷键

在`Setting` ==> `KeyMap`里面都是默认得到快捷键. 下面介绍几个常用的.

1. 创建main 方法: 直接输入 `psvm`
2. 输出语句 `sout`
3. 复制一行: Ctrl + d
4. 删除一行: Ctrl + y  (第一次用, 选择删除整行, 不选 Redo)
5. 代码向上或者向下移动:  Ctrl + Shift + Up /Down
6. 搜索 `类` : Ctl + n
7. 生成代码: atl + insert 
8. 导入包, 生成变量等: alt + Enter 
9. `fori`  回车可以构造for循环
10. 底层代码查看:  按住 Ctrl , 然后鼠标点进去即可.
11. 注释:   Ctrl + /
12. 代码块包围:  Ctl + Alt + t
13. 代码自动补全: tab键
14. 选中的代码块整体后退: tab
15. 选中的代码块整体前进: tab + shift
16. 显示代码结构: alt + 7



# 代码模板

通过一些缩短的词来快速生成已经写好的代码

具体命令请查看 `Settings`里面的设置.

![image-20230716160907184](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716160907184.png)

> **注意: **
>
> 1.  只有 `Live Templates` 可以更由使用者手动更改, 剩下的那个不能更改
>
> 2. 使用者还可以通过`Live Template`还可以创建创建自己的分组 , 在分组中在取创建自己喜欢的简短命令 , `+ ` 代表创建, `-`代表移除.
>
>    ![image-20230716162621226](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716162621226.png)

> 常用代码模板入戏下:

```
psvm   //显示main方法

.sout   // 输出语句

soutp   // 打印方法的形参

soutm    // 打印方法的名字

soutv    //打印变量

fori 或者  .fori   // 正向循环.
.forr      // 逆向循环

.for 或者 iter  // 用于数组, 集合 的遍历

ifn 或者 .null   // 判断是否为null

inn 或者 .nn  判断不等于null 


属性修饰符: 
prsf   // private static final

psf    // public static final
```



# 断点调试

### IDEA断点设置

对于windows来说, 配置如下可以节省一些内存.

![image-20230716163429428](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716163429428.png)



### 了解断点和相应技巧.

![image-20230716164046086](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716164046086.png)



**在标注红色断点处, 可以 `右键` 输入条件, 表示从哪里开始(那个条件开始)**



我们可以通过如下方法查看表达式的值: 

![image-20230716164502491](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716164502491.png)





# 创建java web

![image-20230716165252137](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716165252137.png)





# 忘记配置Tomcat

忘记部署Tomcat的时候可以这样: 

![image-20230716171225071](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716171225071.png)

之后, 部署就行, 这样可以自动的生成配置文件

![image-20230716172141721](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/image2/image-20230716172141721.png)



此时tomcat就已经配置好了, 可以运行了.

