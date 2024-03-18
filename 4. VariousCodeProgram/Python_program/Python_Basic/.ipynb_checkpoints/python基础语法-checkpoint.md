# Python 的安装

## Windows下

直接 Anaconda , 不用发愁大多数的安装包以及python版本问题



## Linux 下

![image-20240314154850384](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img3/image-20240314154850384.png)



**编译**：一次性翻译，之后不再需要源代码（类似英文翻译）

**解释**：每次程序运行时随翻译随执行（类似实时的同声传译）

**静态语言**：使用编译执行的编程语言，编译器一次性生成目标代码，优化更充分，程序运行速度更快。例如**Fortran、C**

**脚本语言**：使用解释执行的编程语言，执行程序时需要源代码，维护更灵活，源代码在维护灵活、跨多个操作系统平台



# 数据类型, 用法 和零碎知识点

> **单行**    注释符号 `  #  `   (井号)
>
> **多行注释**    用  一对单引号 , 或者  一对双引号



> **Python中的转义符和其他的符号符**
>
> ```python
> \          续行符
> \\         反斜杠
> \'         单引号'
> \"         双引号"
> \a         响铃
> \b         退格
> \000       空 (打印出来, 啥也没有)
> \n         换行
> \v         纵向制表符
> \t         横向制表符
> \r         将\r表示的单词作为字符串的开头 , 
>            使用 r 可以让反斜杠不发生转义
> +          直接用于字符串的拼接
> *          直接用于字符串的重复
> 
> ```
>
> ​			
>
> 字符串的格式化: 
>
> <img src="https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img3/image-20240314163118893.png" alt="image-20240314163118893" style="zoom:80%;" />
>
> <img src="https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img3/image-20240314163301365.png" alt="image-20240314163301365" style="zoom:80%;" />
>
> 
>
> 



> Python可以在同一行中使用多条语句，语句之间使用 , 分号` ;`分割。如非必须，应避免使用这种方式
>
> ```python
> a = 1 ; b = 2 
> ```



> **变量命名规则: **
>
> 1. 大小写字母、数字、下划线 _ 、汉字等字符及组合可作为标识符
> 2. 标识符对大小写敏感
> 3. 第一个字符不可以是数字
> 4. 不能与保留字相同



> **保留字查看**
>
> ```python
> import keyword 
> print(keyword.kwlist)
> # 结果如下: 
> ```
>
> 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'



> **Python的内置函数: **
>
> **`官网连接:`** https://docs.python.org/zh-cn/3/library/functions.html



> **Python中的六种数据类型:**
>
> - Number(数值) 
> - String(字符串)
> - List(列表)
> - Tuple(元组)
> - Set(集合)
> - Dictionary(字典)
>
> >  在Python3中支持的类型还有: 
> >
> > `int `整型  , ==> 没有限制
> >
> > `float`浮点型  ,==>有一点的位数限制, 但是一般用不到
> >
> > `bool`布尔型
> >
> > `complex` 复数



> Python的运算符
>
> - 算术运算符
>
>   ​	`+ , - ,  * ,  / `为常用` 加 , 减 , 乘, 除 `
>
>   ​	`**` 表示 `幂运算`
>
>   ​	`%` 表示   `取模, 也就是 取余数`
>
>   ​	`//` 表示`取整数`
>
>   
>
> - 比较运算符
>
>   `==` 表示`等于`
>
>   `!=` 表示`不等于`
>
>   `> , <   , >=  , <=` 分别表示 `大于 ,小于 , 大于等于 , 小于等于`
>
>   
>
> - 赋值运算符 
>
>   `=` 表示赋值
>
>   `c/=a` 表示 `c = c/a`  , 类似的, 都可以用`=`与`算数运算符`结合使用. 
>
>   
>
> - 逻辑运算符
>
>   `and , or , not` 
>
>   
>
> - 成员运算符 
>
>   `in` 和 `not in`
>
>   
>
> - 身份运算符
>
>   `is `和`is not `
>
> **运算符的优先级**
>
> <img src="https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img3/image-20240314162150497.png" alt="image-20240314162150497" style="zoom: 67%;" />
>
> 也就是在运算的时候  **指数最高, 逻辑最低**



> **Python的强制转换**
>
> ```python
> int(x)		# 将x转换为一个整数
> float(x)  # 将x转换到一个浮点数
> str(x)    # 将x转换为字符串
> repr(x)   # 将x 转换为表达式字符串
> eval(str) # 用来计算python中的表达式, 返回一个对象
> tuple(s)  # x 转换为 元组
> complex(real)  # x被转换为复数
> list(s)    #    s 被转换为 列表
> set(s)     # s变为集合
> dict(d)    # 创建了字典, 注意: 需要 key 和 value
> fronzenset(s)  # 得到一个不可变的集合
> chr(x)    # 将 整数 x 转换为字符串
> ord(x)    # 将字符串数字转换为它所对应的整数
> hex(x)    # 将整数转换为十六进制
> oct(x)    # 将一个整数转换为八进制
> ```



> **列表注意事项: **
>
> •列表的数据项不需要具有相同的类型。
>
> 列表索引从 0 开始 , 最后一个元素的索引为 -1
>
> 不用的列表可以通过 `+ `来拼接,  通过`*` 来重复
>
> **一些常用的方法: **
>
> ​	`len(list)`   得到列表的元素个数
>
> ​	`max(list)`    得到列表元素的最大值
>
> ​	`min(list)`    得到列表元素的最小值
>
> `list(seq)`       将元组转换为列表
>
> `list.append()  ` 添加元素
>
> `list.count(obj)`  统计某个元素在列表中出现的次数
>
> `list.extend(seq)`    在列表的末尾添加另一个序列的多个值
>
> `list.index(obj)`    从列表中找出某个值第一个匹配项的索引位置
>
> `list.insert(index, obj)` 将某个对象插入列表中
>
> `list.pop([index=-1])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值`
>
> `list.remove(obj)`  移除列表中某个值的第一个匹配项
>
> `list.reverse()`   反向列表中元素
>
> `list.sort(key=None, reverse=False) `对于原表进行排序
>
> `del list[a:b]` 删除列表中, 索引从 a 到b 的元素
>
> `list.clear ` 清空列表
>
> `list.copy` 赋值列表



> **字典的用法:**
>
> `dict.clear()` 清空字典
>
> `dict.copy()`  返回字典的浅复制
>
> `dict.fromkeys` 创建一个新字典
>
> `dict.get(key)`   返回指定键的值
>
> `dict.values()`  
>
> `dict.keys()`
>
> `dict.updat(dict2)` 将`dict2`合并到`dict`中
>
> `dict.setdefault(key)`
>
> `pop(key)` 删除`key` 对应的`value`
>
> `popitem()`随机放回并删除字典中的最后一对键和值



> **集合的用法:**
>
> | [add()](https://www.runoob.com/python3/ref-set-add.html)     | 为集合添加元素                                               |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> | [clear()](https://www.runoob.com/python3/ref-set-clear.html) | 移除集合中的所有元素                                         |
> | [copy()](https://www.runoob.com/python3/ref-set-copy.html)   | 拷贝一个集合                                                 |
> | [difference()](https://www.runoob.com/python3/ref-set-difference.html) | 返回多个集合的差集                                           |
> | [difference_update()](https://www.runoob.com/python3/ref-set-difference_update.html) | 移除集合中的元素，该元素在指定的集合也存在。                 |
> | [discard()](https://www.runoob.com/python3/ref-set-discard.html) | 删除集合中指定的元素                                         |
> | [intersection()](https://www.runoob.com/python3/ref-set-intersection.html) | 返回集合的交集                                               |
> | [intersection_update()](https://www.runoob.com/python3/ref-set-intersection_update.html) | 返回集合的交集。                                             |
> | [isdisjoint()](https://www.runoob.com/python3/ref-set-isdisjoint.html) | 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。 |
> | [issubset()](https://www.runoob.com/python3/ref-set-issubset.html) | 判断指定集合是否为该方法参数集合的子集。                     |
> | [issuperset()](https://www.runoob.com/python3/ref-set-issuperset.html) | 判断该方法的参数集合是否为指定集合的子集                     |
>
> | [pop()](https://www.runoob.com/python3/ref-set-pop.html)     | 随机移除元素                                                 |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> | [remove()](https://www.runoob.com/python3/ref-set-remove.html) | 移除指定元素                                                 |
> | [symmetric_difference](https://www.runoob.com/python3/ref-set-symmetric_difference.html)[()](https://www.runoob.com/python3/ref-set-symmetric_difference.html) | 返回两个集合中不重复的元素集合。                             |
> | [symmetric_difference_update()](https://www.runoob.com/python3/ref-set-symmetric_difference_update.html) | 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。 |
> | [union()](https://www.runoob.com/python3/ref-set-union.html) | 返回两个集合的并集                                           |
> | [update()](https://www.runoob.com/python3/ref-set-update.html) | 给集合添加元素                                               |



> **元组数据不可改变**, 元组中的数据为 **静态数据** , 元祖的用法基本与列表相同



# 重要的语句

## if 条件

```python
if (逻辑判断) : 
  pass
elif (逻辑判断) : 
  pass
elif(逻辑判断):
  pass
else: 
  pass
```



## 循环语句

```python
# while 循环
# 具体用法: 
while 成立的条件:       # 在条件成立的情况下运行, 否则直接运行else部分的内容
  pass 
else: 
  pass      
```



```python
# for 循环语句
for i in range(数字): 
  pass
else: 
  pass 

# 再比如: 
for key , value in enumerate(list_a): 
  print(key, value)
```

**循环中重要的保留字: **

```
continue    # 跳过本次循环,  执行下一次循环
break       # 终端循环

```





# 函数

**注意事项: **

> **任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数**
>
> **函数内容以冒号**` : `起始，并且缩进. 
>
> **return [变量 或者 表达式 ]**结束函数，选择性地返回一个值给调用方，不带表达式的** **return** **相当于返回** **None。**



> **导库的几种方法: **
>
>  `import 库名.函数名.函数里面的参数`
>
> `import 库名 as 新库名`
>
> `from moudulename import name1 , name2`







# Python 数据读写

## Pandas , Series 常用

**常见气象数据的类型**： 

1.文本型（表格）：`.txt`, `.csv` `.xlsx`

2.二进制（格点）：`.nc` `.hdf` ` .grib` 



数据处理最常用的两个包: `Pandas , Numpy`

**Pandas**的两种核心数据对象： **Series** , **DataFrame** 

​	**Series**:每个元素都有对应标签的一维数组

```python
import  pandas as pd

s1 = pd.Series([5,6,7,8])
print(s1)

'''
# 输出结果: 
0    5
1    6
2    7
3    8
dtype: int64

'''
```

​	**DataFrame**:由多个**相同行标签**且具有**列标签的series**对象组成的二维表格

```python
import  pandas as pd
import  numpy as np

# 文本文件, 常用 Pandas  , 对应的数据结构就是Series
# # 下面是Series部分
# s1 = pd.Series([5,6,7,8])
# s1.index = ["A", "B", "C" , "D"]
# s1.index.name = "Letter"
# print(s1.index[0])
# print(s1[0] , s1[s1.index[0]])
# print(s1)
#
#
# # 下面是Dataframe部分
# data = {'years': [2023, 2024, 2025],
#         'pre': [1, 2, 3]}
# df1 = pd.DataFrame(data)
# df1.index = ["第一行", "第二行", "第三行"]
# df1.columns = ["new years", "new pre"]
# df1.index.name = "index"
# df1.columns.name = "columns"
# print(df1.columns)
# print(df1.index)
#
#

## 多层嵌套
# mindex = [np.arange(2001,2007,1), [6,7,8]*2]  # 对应数据:  [array([2001, 2002, 2003, 2004, 2005, 2006]), [6, 7, 8, 6, 7, 8]]
# df2 = pd.DataFrame(np.arange(12).reshape(6,2),
#                    index= mindex , columns=['pre', 'temp'])
# print(df2)


#  iloc , loc
# print(df2.loc[2001])   # loc[index, column) 基于标签
# print(df2.iloc[0,1])   # iloc[index,column) 基于索引

```

**文件读取**

```python

# 文件读取

'''
# excel  和  csv 读取基本差不多,  只是 csv里面多了一个sep 参数, 例如: sep = '\s+' , 表示以一个或多个空格分隔. 
                                   csv中还有 chunksize , 来指定分块读取, 也就是指定每次读取多少行. 
    header  指定那一行为列名
    names   指定表头
    skiprows   掉指定的行数 或  去掉指定的某一行或者几行
    skipfooter  从末尾开始算,  跳过多少行;  
    nrows       指定读取的行数,  改参数不可与   skipfooter联用
    na_values   指定某一个空, 将其变为 Na
    index_col   指定某一列,  将其变为索引 index 
    usecols     拿出指定的列, (写代码的时候可能会有警告,  但没有报错)
'''
SheetBook = pd.ExcelFile(r"C:\Users\2892706668\Desktop\高数竞赛班级时间表.xlsx")
names = ["1", "2"]
with   SheetBook  as sheetb:
    df1 = pd.read_excel(sheetb,sheet_name=sheetb.sheet_names[0],
                        # names=names,
                        header=1,
                        # skiprows=[16]   ,               # 建议先打印出来最原始的式子, 之后再去掉行数
                        # skiprows=2                  # 从开始那一行, 去掉 两行
                        na_values= {"序号": [1.0, 2.0 , "Na"]} ,   # 有一个列的列名叫做 "序号" , 将其下的 1.0 , 2.0 这两个值, 变为Na
                        index_col = "序号",
                        # skipfooter= 1,
                        # nrows=2,
                        # usecols= ["序号"]
                        )

    print(df1)


```



**文件写入**

```python
# 文件的写入
df2 = df1.to_excel(r"填写路径")  # 以此类推, 也可以根据需要直接 to_nc  , to_grib 等方法
```



## Xrray, Numpy (常用)

```python

'''
Xrray里面的 DataArray 和 Dataset: 
DataArray 常用属性
    dims:   数据对象每个维度的名字 (例如: lat   ,  lon )
    coords:  每个维度的坐标  :    lat:  90 ~ -90  lon 0~ 360
    values:  实际数据
    attrs:   保存数据的字典( 分辨率, 单位  缺测值 等)
    
    
Dataset:由多个维度相关联的DataArray组成的字典, 常用属性: 
    dims: 数据对象每个维度的名字和长度
    coords: 每个维度的坐标
    attrs: 保存数据的字典
    data_vars: 数据中包含的DataArray 
'''
import  numpy as np
import pandas as pd
import  xarray  as xr
# 下面介绍二进制文件的读写
# 二进制文件最常用的就是   Xrray , 对应的就是 Numpy

exp_data = np.random.randint(0, 40, (3,180, 360))
lat = np.linspace(90, -90 , 180)
lon = np.linspace(0, 360, 360)
time = pd.date_range(start = '2022-01',
                     periods=3,
                     freq='MS')
temp = xr.DataArray(exp_data,
                  dims = ['month', 'latitude', 'longitude'],
                  coords=[time, lat , lon ])


exp_data2_dataset = np.random.randint(50,80, (3,180, 360))
pre =  xr.DataArray(exp_data2_dataset,
                  dims = ['month', 'latitude', 'lontitude'],   # 一定要注意:  dims 和 coords的key 一定要一致.
                  coords= {"month":time, 'latitude':lat, 'lontitude':lon},
                  # coords=[time, lat , lon ])
                    )
ds = xr.Dataset({'teimperature':temp, 'precipitation':pre})    # 相当于将两个 DataArray合并了


# 下面使用DataArray拿出数据
# 通过 sel 拿到指定内容的数据
# print(pre.coords)
# print(pre.values)          # 拿出所有的数据
# print(pre.sel(month="2022-01-01").values)           #
# print(pre.sel(month="2022-01-01",latitude=lat[8],lontitude=lon[0] ).values)  # 注意这里如果填写不正确, 那就报错, all in ....

# 通过loc属性, 结合具体要找的内容, 得到数据
# print(pre.loc[time[1], lat[1],lon[2]].values)

# 按照行索引 寻找数据
# print(pre[1,2,3].values)

# 下面拿出Dataset拿出数据
# print(ds.to_array().values)                      #拿出所有数据, 实际上, 只是能看到所欲的数据而已, 要想拿出纯数据, 使用.to_array()
# print(ds["teimperature"].values)      #拿出temperature 对应的数据
# print(ds.sel(lontitude=slice(10,20)).to_array().values)
# print(ds.loc[dict(month=time[0],  latitude=lat[0], lontitude=lon[0])])    # 一定要用 dict()


# 下面是二进制的读取  # 需要暗账 netCDF4 , eccodes, cfgrib库
# xr.open_dataset(r'绝对路径即可')  # 对于 .nc  .grib   .HDF 等 二进制文件均可

# 下面是二进制文件的写入
# filename.to_netcdf(r"保存路径")

```

















# Python 绘图---> (`Cartopy, matplotlib `)

> **对于画图这部分, 强烈建议使用`Jupyter Notebook ` 来写代码, 用`原生的Pycharm`在画图的时候会出现很多奇怪的错误**

**下面的代码内容介绍如下:**

```python
# 两张图的叠加 
# 图例的设置,  除了 label 不要忘记 legend
# 字体的相关设置
# 设置每个数据的标记符号,  线条的样式, , 粗细 
#  添加网格
#  画各种图:    常用的图 ax.plot
#              茎叶图  ax.stem 
#              阶梯型的图  ax.step 
#              条形图      ax.bar 
#              区域填充    ax.fill_between 
#              scatter  
# 改变主题风格:   查找有哪些主题:  plt.style.available
#                 使用主题:       plt.style.use('查找到的主题')
# 自定义主题样例:  
 '''              import matplotlib as mpl 
                  stylel_dict = {
                        'axes.spines.left': True,
                        'axes.spines.bottom': True,
                        'axes.spines.right': Flase,
                        'axes.spines.top': False,
                        'legend.frameon': False
                        
                  }
                  mpl.rcParams.update(style_dict)
''' 


import matplotlib
import matplotlib.pyplot as plt
import numpy   as np

plt.rcParams['font.size'] = 10                                               # 这个代码会将整张图的字体都做大小的调整
fig  = plt.figure(figsize=(10,4))
ax = fig.add_subplot()
t = np.arange(100)
# ax.plot(t , np.sin(t), 
#         c='red' , 
#         label = r"Red",                                                     # 使用c 也就是 color , 得到不用的颜色
#         marker='x', ls='dotted', lw= 1                                         # 设置每个数据的标记符号,  线条的样式, , 粗细  
#         )           




ax.fill_between(t , np.sin(t),  np.sin(t) + 1 ,
                alpha=0.2                                                    # 设置区域颜色的透明度
                )  
ax.set_xlabel("Day")   
ax.set_ylabel("IamY", c="red")
ax.legend(loc="upper left", bbox_to_anchor=(0.82,0.95),frameon=False)
# ax.legend(loc="upper left",frameon=False)                                  # 也可以直接用  loc="upper left",
ax.grid(':')                                                                 # 设置网格
ax_pr.set_ylim(0,60)                                                         # 将y轴的值设置在0~60之间的部分, 不在此范围的图偶不会被画出
ax.set_yticks([10,20,30])                                                    # 设置y的刻度, 显示, 只是调整一下刻度的现实而已, 不影响主体的图.



ax_pr = ax.twinx()



ax_pr.plot(t,np.linspace(1,100,100),
           c="b",                                                            # 指定颜色
           label=r"Blue",
           marker ='o', ls='-', linewidth=0.01)     

ax_pr.legend(loc="upper right",  bbox_to_anchor=(0.95,1), frameon=False)      # frameon = False 就是去除框的意思
ax_pr.set_ylabel("Precip", c ="b")
ax_pr.grid(ls=':')
ax_pr.set_ylim(0,60)                                                          # 显示 y轴的值在  0~60之间的部分
ax_pr.set_yticks([0, 10, 20, 30])                                            

```























































