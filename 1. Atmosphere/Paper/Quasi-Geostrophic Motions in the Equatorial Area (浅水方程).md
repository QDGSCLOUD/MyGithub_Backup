# Quasi-Geostrophic Motions in the Equatorial Area* 

## 文章之源

地球与海洋是准水平的两种运动, 一个是是用于大尺度运动的惯性重力波, 另一个是在中高纬度的准地转波. 而在Matsuno之前的诸多前辈已经设计了许多方法滤去准地转波的影响, 而Matsuno对时间进行有限积分, 从而达到滤波的目的.并且他的方法在高纬度十分有效.

基于Yoshida (1959) , 可以知道, 低频的重力波被束缚在沿着赤道的一个非常窄的地区. 而 Ichiye (1960)  在作出大量假设的前提下, 得出了Rossby 波 和 惯性重力波同时存在,  Matsuno 则是做了更加精确的讨论.

## 两个重要的前置知识

> 1. 惯性重力波
> 2. Rossby波

在文章摘要部分, Matsuno 已经告诉我们 在一个 **均匀不可压**的流体表面, 并且科式力看做是与纬向成正比的前提下, 通常得到的就是 两种波, 这两种波就是 惯性重力波和 Rossby 波, 这两种波在频率上有区别的, 在压力和风场上是由联系的. Matsuno 发现了两个非常重要的特点 :

**以下两个特点都是在低模态也就是赤道附近进行的.**

> 1. 有一个向西传的波, 一个非常重要的一点便是这个波是一个混合的波, 包含着 重力波 和 Rossby波的特点,  而这种特点, Matsuno主要是通过压力和 风场来进行比较得到的. 他发现很难将重力波给过滤出来某种波, 因为总能看到某种波的特点.  但是我们可以通过变换频率和波长来使得某种波更加明显. 
>    1. 在波长很长的时候, **重力波**更加明显; 
>    2. 增大波数, 减少频率, 这个时候 **Rossby**波更加明显
> 2. 上面的一个特点说的直白一点就是波的混合, 那么下面一个有趣的特点就是波被束缚在赤道附近.
>    1. 由于赤道附近的扰动, 上方所述的Rossby 波 和惯性重力波只有在赤道附近才有, 也就是说此二者被束缚于赤道附近.
>    2. 在向东传播的方向上, 有质量的源和汇, 有高低气压的形成. 

## 假设条件

> 1. 自由表面
> 2. **均匀不可压**流体
> 3. 科式力与纬向成正比
> 4. 采用 β 平面近似

# 推导

## Model and basic equations

> 此部分非常的神奇, 验证了**运动方程与连续方程**结合  和  **运动方程与热量方程**结合后  发现二者可以在一定条件下等价. 这就使得我们可以进行方程的替换, 方便相关物理量和物理过程的研究.

在发散的正压大气条件下:

1. 建立一个直角坐标轴, x 轴正向向东, y 正向向北, z正向代表向上的高度.

2.  H 表示波的高度的平均值, h 表示小的偏差也就是扰动. 

3. f 为地转参数, 非常需要注意的是此处 f 为变量,不是常量.
   $$
   f = \beta y \\
   其中\beta 为Rossby波参数, 此处取 \beta  为常量.
   $$

首先基于 **动量和质量守恒**, 有方程组:

![image-20230515131333529](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230515131333529.png)



将 **几何高度**转换为 **位势高度**

![image-20230515131509853](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230515131509853.png)
$$
注意:
c^2 = gH  \\
c 代表纯的惯性重力波的速度的平方, 上方给出的是 c 最终化简的形式.
$$
接着对方程进行**无量纲化**

![image-20230515132546582](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230515132546582.png)

纯的重力波的 **时间尺度****与 **特征尺度**如下:

![image-20230518193218619](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230518193218619.png)



> 此时上方已经推导出了运动方程与连续方程的组合形式, 
>
> 西面推导运动方程与热量方程的组合形式

根据热量方程和运动方程有:![image-20230519075507590](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230519075507590.png)

![image-20230519075613094](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230519075613094.png)

接着, 

用 下标为 1的 顶层 减去 下标为3的底层, 得到:![image-20230519075720268](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230519075720268.png)



> 1. 此处很明显, 如果想得到中间层, 我们就用与其相邻的顶层和顶层作差得到中间层. 也就是气层的内部的方程组.
>
> 2. 此时对一些变量进行替换.![image-20230519080033447](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230519080033447.png)
>
>    **替换完了以后, 发现就是 运动方程与连续方程的结合.** , 所以, 这两个方程组是等价的. 这意味着此二者可以互换着使用. 



## The frequency equation

因为:

![image-20230519081005027](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230519081005027.png)



进行替换
$$
原物理量 =  原物理量 * e^{iwt+ikx }
$$

> 为啥这里要用 e的指数替换呢? 怎么想到的?  为啥合理呢???
>
> 还有一个问题, 此处的 $ \omega $的物理意义是啥? 这个参数在下方的推导中非常的重要, 需要搞清楚. 
>
> 从下方的解释来看, $\omega$ 代表的是  对应的 *波的频率*

![image-20230519080740333](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230519080740333.png)

利用上方的三个方程, 解除 **v**的相关表达式:

![image-20230519081426984](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230519081426984.png)



观察该方程: 有如下可能: (**我也不知道为啥?** )

![image-20230519091400786](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230519091400786.png)



求解上面的方程:![image-20230519091546345](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230519091546345.png)



当观$式子(8)$的时候, 变形一下得到:

$\omega^3 - k^2 \omega + k = (2n + 1) \omega $ 

对于一个最高项为 `3`的三次多项式, 那么最多有 3 个根, 考虑到实际的情况, 这三个根实际上影响着波速(包括大小和反向), 这是由于我们在上方解$v$的时候, 将这个关于$\omega$的部分看做常数来考虑的, 而实际上这部分的影响还是比较大的 . **考虑 k 非常大**的时候, 可以的得到关于 $\omega$的三个近似值. 

![image-20230523213412020](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230523213412020.png)

考虑用重力波的相对速度考虑上方的关系, 可以得到:

![image-20230523214628243](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230523214628243.png)

上方考虑的是一种比较特殊的情况, 也就是说在`k`非常大的时候, 来观察 $\omega$的变换, 当k取不同的值的时候, 对应的$\omega$也是会变化的,结合一部分 $n$的取值. 可以得到如下图所示的关系:

![image-20230523215521325](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230523215521325.png)![image-20230523220409965](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230523220409965.png)

那么这里结合上面的$c_{1,2}$ 的值, 通过调节$k,\omega$就可以简单想到$波速c$是变化的, 正负代表方向. 也就是我们可以看出波传播的方向和大小. 

但是, **`很奇怪的是, 图中画的是参数$\omega$ 与 波数$k$ 之间的关系, 而不是$波速v$与波数的关系.`** , 而在分析的时候, 原文用的波速, 以波速的大小和正负来判断是实际中的波, 也就是猜想的, 两个重力内波 和  Rossby波.   

但是稍有留心就会发现, 其实$w 与 波速c$的大小和数值的正负变化是一致的(具体请仔细看一下上面的两个式子).   而原文也说了, 我们可以直接通过 将$\omega$ 换为原始的$ 波的相对速度$ 来看出.

> 具体的带换此处省略, 后期万却想明白了来此补充具体的求解过程, 并作进一步的详细说明



> `说明白了上方其实画出的是波速和k之间的关系`, 可以非常明显的看到, 对于诸多的`n` 固定的时候, `k趋向无穷`, 曲线是 快速的向两边扩展, 对于某些曲线, 则是被束缚在x轴的, 也就是说越来越趋向于x轴. 

`此时, 我们大致就可以猜想到 至少有三个波`, 一个$c>0$`往东传; 一个$c<0 $往西传. 还有一个被束缚于赤道. 

> 这个时候, 原文还没有解释, 为啥会有个数的变化. 如果不往下看, 此时如果细心点, 就会发现, $n=0$的时候, 只有2条曲线.   而当$n=3$的时候, 却只有一条.   此时还不明白, 可下方会有解释. 好吧, 接着往下看. 



> 下面针对于n= 0的时候进行讨论

将 $n=0$ 带入上方的公式得到:

![image-20230525211521689](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230525211521689.png)

如果此时将 $k$看做是常数, 频率$\omega$ 看做是未知量, 此时对于上方的这个式子就有 三个解, 而这三个解对应的就是实际中Matsuno想要印证的三个波. 分别为**向西和向东传播的重力波, 还有Rossby波**









# 问题汇总

1. ![image-20230518211502263](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230518211502263.png)
2. ![image-20230518222011397](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230518222011397.png)

