# shell 编程简单示例

> # `脚本就是堆积的命令和语法`

一般常用的脚本解释器是 `bash` , 我们不能简单的通过 **后缀**来区分是不是 `shell脚本`, 因为有些shell 脚本**没后缀**



Linux里面的`空格` 的含义, 一般是: 语句的执行结束 , 或者 变量 间隔的空格. 在写Shell的时候一定要特别小心. 

本次演示环境:  **Kali(2023年的)**

**由于Kali中的tab键是 8个空格, 所以我们需要手动修改默认的空格数, 编辑`/etc/vim/virc`**, 在任意一个地方添加语句`set ts=4`, 这样 `tab`的默认空格数就是 4 个了. 

![image-20230611213751919](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611213751919.png)

## Shell的创建和编辑

1. 查看 操作系统已有的解释器, 并创建文件

   ```shell
   echo $SHELL
   
   # 查看bash (编辑shell脚本的时候需要指定)
   where bash
   
   # 创建shell脚本
   vim test1.sh
   ```

   ![image-20230611175014030](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611175014030.png)

```shell
#!/bin/bash                    # 这句的作用就是指定shell编辑器
											# 换句话说就是一个超链接, 相当于Windows中的快捷方式
											# 就相当于打开了一个软件, 叫  bash
											
echo "Hello World!"
```

这样第一个Shell脚本就写好啦



## Shell 运行

运行有两种方式, 但是最最常用的一种方式就是使用`bash`命令来运行, 可能是习惯性问题.

```
bash test1.sh
```

![image-20230611175856990](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611175856990.png)

但是, 此时是没有执行权限的, 所以需要手动加上权限

```
# 查看拥有的权限 
ll test1.sh
# 加上 可执行权限
chmod +x tes1.sh

# 运行脚本
./test1.sh
```

​	![image-20230611180525178](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611180525178.png)



## 趣味例子

> 下面还有一个简单的例子
>
> 作用就是, 在 `home`文件夹下创建了 `example.txt`文件, 然后将 `Come on` 输入到了其中

```shell
#!/bin/bash
cd /home
touch example.txt
echo "Come on" >> example.txt
```

​		![image-20230611181436788](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611181436788.png)



# Shell 中的变量

### 环境变量(作用域整个系统的)

如果在 `/etc/profile` 里面定义环境环境变量, 那就是永久生效的, 但是如果通过 命令来定, 那就是`临时的`, 只要我们退出系统, 变量就会**失效**



### 普通变量(作用在Shell文件中的)

1. 实际的例子:

   下面就是在shell文件中定义变量

![image-20230611183021997](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611183021997.png)

```shell
#!/bin/bash
A=10
B="I am character"

echo $A
echo $B
```

![image-20230611183357202](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611183357202.png)





# 变量的作用域

1. 当我们在开启Linux操作系统的时候, 系统会自动的开启一个bash, 比如`ls, cd , echo`等等这些命令都是这个打开操作系统的时候开启的`bash`执行的, 此处我们假如叫它`bash1号`
2. 当我们自己写脚本的时候就会重新开启一个bash, 此处叫它`bash2号`, 这两个bash是 **不同的bash**

基于以上两点, 会有如下情况:

## 情况一

当我们命名一个`用户变量`的时候, 假如叫这个变量为`C `; 当我们在写脚本的时候, **脚本文件里面**再写一个 **C**变量.那么当我们运行脚本文件的时候, `用户变量C ` 是不会被执行的. 因为我们用的是系统开启后的 `bash2号`来运行的脚本文件. 

一般, **`bash1号叫做 父bash,  bash2号叫做 子bash`**

```shell
# 下方的命令可以查看已经启动的bash
ps aux | grep bash

# 直接输入bash , 就会开启一个新的bash
bash
```

![image-20230611190333975](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611190333975.png)



## 情况二

**上面说的是 `用户变量`**, 由于用户定义的变量是在不同的bash里面的所以不能共享. 但是`系统变量`却是可以的, 系统环境变量是定义在`整个操作系统里面的` , 所以是可以被共享执行的. 



## 情况三

> `临时的环境环境变量可以作用当前的bash以及其子bash`

即使说, 如果我们在某个bash中创建了一个临时环境变量, 那么但我们运行某个文件的时候会产生一个 子bash, 那么这个子bash是可以使用这个父bash定义的 环境变量的.



# 特殊变量

### $n​

0代表脚本的名字, `$1`  到 `$9` 直接写, 但是如果是两位及以上的数字就要用花括号了 , 例如: `${10}`

下面写一个脚本并进行**传参**

```
#!/bin/bash
echo "$0 $1 $2"
```

![image-20230611192128225](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611192128225.png)

传参方式如上: `文件名 + 要传的值` ,  可以看到传了3个参数, 但是由于只定义了两个个可以传的值, 所以传的第三个参数被忽略了.



### $

作用是统计给脚本传参的个数

具体的脚本内容一下

```
#!/bin/bash
echo "$0 $1 $2"
echo $#
```

![image-20230611193011883](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611193011883.png)

传了5个参数, 但是没有被忽略的就只有两个.



### `$* 和 $@`

这个个作用都是代表所有的变量, 但是 `$*`是将所有的变量作为一个整体, 而 `$@`代表的就是一个个独立的变量(按照原先的空格分隔)

从效果上看, 打印效果是一样的

![image-20230611193809060](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611193809060.png)



$?

作用是判断**最近一次执行的命令的执行状态**, 如果输出的是 `0` ,那就代表正常执行, 如果是非零, 那就代表没正确执行

![image-20230611194305136](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611194305136.png)



# 运算符

## 在黑窗口中

运算之间要有空格 , **否则就是变量**

![image-20230611194642469](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611194642469.png)

还可以将计算的结果复制给变量(需要在 `shell` 对应的文件文件夹里面, )

```
D  = `expr 3 + 8 `
echo $D
```

​	![image-20230611195112849](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611195112849.png)



## 在脚本中

新建一个名叫`workout.sh`的脚本, 内容如下:

```shell
#!/bin/bash
A=100
B=200

# 第一种写法 , 直接用两个圆括号包裹
C=$((A+B))
echo "First1" $C

#第二种写法, 用$[]
D=$[A+B]
echo "Second" $D 

# 第三种,  反引号  expr 注意要有空格
E=`expr $A + $B`
echo "Third" $E
```

运行结果如下(需要给文件赋权):

![image-20230611200821076](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611200821076.png)

一些较为复杂的运算`大多采用 $[] , 但是也可以使用expr`, 一般`expr比较麻烦, 而且容易犯错`

```shel
H=$[(2+3)*4]
echo $H
```



# 条件判断

创建一个名叫`condition.sh`的脚本文件, 编写内容如下:

```shell
#!/bin/bash
[ $# -gt 2  ] && echo " number not only 2"

# 作用: 如果输入的参数的个数超过2 个, 就打印 number not only 2
```

![image-20230611205103987](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611205103987.png)



### 示例

#### 逻辑判断

下面这个例子通过装填来判断是否添加用户, 脚本内容如下:

```shell
#!/bin/bash
id wang5 &> /dev/null &&  echo"Haven user"
id wang5 &> /dev/null useradd wang5
```

![image-20230611210654532](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611210654532.png)

第一次执行: 由于用户不存在, 所以为 `Fals`, 所以不会进行打印, 

但是第二条语句 用过  `或` 的关系, 执行了添加用户的功能

第二次执行: 由于用户已经被添加了, 所以说会直接打印语句. 并且由于用户是存在的, 所以不会执行添加用户的命令.



#### if判断

```shell
#!/bin/bash
if [  $1 -lt 18  ] ;then 
    echo "child"
elif [ $1 -gt 18 -a $1 lt 30   ] ;then 
		echo "youth"
else 
		echo "elder"
fi
```

![image-20230611212939148](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611212939148.png)

`一定要注意空格,  空格 ,  空格!!!! 尤其是条件判断里面的空格`

#### case 判断

```shell
#!/bin/bash
case $1 in 
"start")
		echo "inputed value: start"
;;
"stop")
		echo "inputed value: stop"
;;

"restart")
	echo "inputed value: restart"

*) 
	echo "this is else content"
esac
```

![image-20230611215139184](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230611215139184.png)



# 循环

## for循环

```shell
#!/bin/bash
# workout 1 to 100 
for ((i=0; i<=100; i++));do
		s=$[$s+$i]
done 
echo "从1到100的和是$s"

# 此处虽然没有指定初始的 $s , 但是$s本就是 默认为 0的, 所以不会报错.
```



## while循环

```shell
#!/bin/bash

for i in {1..100};do 
		s=$[$s + $i]
done

echo "从1 到 100 结果为 $s"
```



## sel循环(其他的linux命令)

```shell
#!/bin/bash

for i `seq 1 100`; do 
		s = $[$s +$i]
done
echo "从 1 到 100 结果为: $s"
```

> 同理我们还可以打印出目录的名字(因为linux中的目录也是按照空格和回车换行符隔开的)

```shell
#!/bin/bash
for i in 'ls /home' ; do 
	echo $i 
done
```

## `$*  和 $@`区别

```shell
#!/bin/bash
for i in "$*"; do
	echo "传入$i"
done 
echo "-----------"
for i in "$@"; do
	echo "传入$i"
done 
```

**打印的结果就是 `加入了 引号后, $* 会是一个整体, 而$@ 仍然是不同的变量`**





## while 循环

```shell
#!/bin/bash
i=1
sum=0
while [ $i-le 100   ] ;do
	let sum=sum+i
	let i++
done
echo "从1到100的和为: $sum"
```



# read输入

```shell
#!/bin/bash

read -p "请输入大于1的数字: " n
i=1
sum=0
while [  $i -le $n ] ;do 
		let sum=sum+i
		let i++
done 
echo "从1到n的和为: $sum"
```



# 文件路径的剪切

```shell
#!/bin/bash

dir="/opt/test/"
for f in `ls /opt/test/*.txt` ;do
                file_name=`basename $f .txt`
                dist_name=$filename".sh"
                mv $f $dir$dist_filename
done
```



# 函数



### 简单的和计算

```shell
#!/bin/bash

function sum(){
                let s=$l+$2
                return $s
}

sum 10 200 
echo $?

# 注意: return的返回直接用  $?  而且return的返回值只能从 0 ~255
#      如果 return的返回值超过255 , 那么从0开始

# 如果想要计算 超过255的和, 那就不要用return , 直接echo返回不就完了

```



### 阶乘的计算

```shell
#!/bin/bash

if [  $# -ne 1 ] ;then 
                echo "more than one param, error!"
                exit 3
fi 

function jiecheng(){
        n=$1
        if [ $n  -le 1 ]; then
                echo 1 
                return 0
        elif [ $n -gt 1 ] ;then
                        let pre_n=n-1 
                        temp=`jiecheng $pre_n`
            let result=n*temp
                        echo $result
                        return 0
        fi 



}

jiecheng $1
           
```



# Shell工具

## cut

这是一个比 `basename`更加常用的剪切工具

例如: 原理的1.txt文件中有两列, 用空格隔开的, 现在就按照原文件中的空格, 取出1.txt 文件中的第1列 和 第2列. 

```
cut -d " " -f1,2 1.txt
```



## sed

```

```



## awk

1. 将1.txt文件中的第一列和第二类取出, 并按照空格隔开展示

```shell
awk -F: '{print $1" "$2}' 1.txt
```



## sort

主要作用为**排序**

