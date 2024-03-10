# Jupyter使用教程

# 命令和快捷键

## 启动

打开 Anaconda 环境, 直接在终端中输入 `jupyter notebook`, 此时jupyter 会用默认的的浏览器打开, 如果不想用默认的浏览器, 可以更改每次打开的浏览器(网上教程很多)

## Tab键补全

我们在使用 Notebook的时候, 可以通过输入几个字母,而不是全部的**模块名**, 或者**函数名** , 亦或者 **路径** 来写入代码;当然, 对于一些私有方法, 我们需要 **键入下划线**才能显示提示, 进而补全. 

## 运行

`%run 文件`

通过上方的命令, 我们就可以直接运行写好的文件

```python
# 直接在jupyter notebook的方块中输入:
%run test.py
```

> 如果运行的脚本需要传递参数, 直接在 `%run`后面传递就行.



## 自省

1. 在变量前面加 **问号**, 例如`b?` , 便可以十分方便的显示出变量的相关信息

2. 如果用在**函数**后面, 加一个问号, **显示文档字符串**; 加两个问号, **显示源码**

   ```python
   例如: 有个函数名叫  myFunction
   myFunction?       # 显示一些文档信息
   myFunction??      # 显示源码
   ```

3. 问号还可以用来查找 IPython的命名空间

   ```python 
   # 例如:
   import numpy as numpy
   np.*load*?
   
   # 显示结果如下:
   np.__loader__
   np.load
   np.loads
   np.loadtxt
   ```



## 导入脚本

使用`%load` 将脚本导入到代码格中

```python
%load test.py        # 要注意导入的文件在哪里, 也就是说导入的路径是啥
def myfunction :
		pass
  return
```



## 中断运行

使用 `Ctrl+C  `可以直接中断程序.

**注意;有些时候程序由于引入了其他的扩展块儿不会直接中断, 需要等一会.**



## 从剪切板执行命令

使用`%paste 或者 %cpaste`



## 快捷键专区

> **由于受到浏览器自身的快捷键的影响,  下面的命令可能没法用**

```Python
Ctrl + P           # 使用当前输入的文本搜索之前的命令

Ctrl + N           # 使用当前输入的文本搜索之后的命令

Ctrl + R           # 翻转历史搜索

Ctrl + C           # 中断代码

Ctrl + V           # 粘贴

Ctrl + A           # 将光标移到一行的开头

Ctrl + E           # 将光标移到一行的结尾

Ctrl + K           # 删除光标到行尾

Ctrl + U           # 删除前行所有的文本

Ctrl + F           # 光标向前移动一个字符

Ctrl + B           # 光标向后移动一个字符

Ctrl + L           # 清空屏幕

```



# 魔术函数

**魔术函数只要IPython 才有, 原生的Python是不具备的**

在notebook的代码块中输入, `%quickref`或者 `%magic` 可以常看相关文档.

> 下面列出的是一些常用的魔术韩束

```Python
%quick			# 显示IPython 的快速参考命令

%magic      # 显示所有魔术命令的详细文档

%debug      # 在出现异常的语句进行调试

%hist       # 打印所有输入的历史命令

%pdb        # 出现异常时, 自动调试

%paste      # 执行粘贴板中的代码

%cpaste     # 开启特别提醒, 手动张贴待执行代码

%pasteOBJECT    # 美化打印对象, 分页显示

% prun  statement       # 用 CProfile 运行代码, 并交给报告分析器输出

%time statement         # 报告单条语句执行时间

%timeit statement       # 多次执行一条语句并计算平均时间

%who , who_Is , %whos    # 显示命名空间的变量

%xdel variable           # 删除一个变量, 并清空任何对它的应用
```



