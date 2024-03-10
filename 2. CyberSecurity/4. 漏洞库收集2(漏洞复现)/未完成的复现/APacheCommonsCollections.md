# ApacheCommonsCollections

这个漏洞简称为: **Apache CC**

号称是 **2015**年影响力最大的漏洞之一.

# 环境配置

> 需要的环境:
>
> 1. jdk 1.7.0_80
> 2. 编辑器的编译环境也需要 设置成 java7
> 3. Apache Commons Collections <= 3.2.1

# 原理介绍

## 前置知识

### 1. java 运行原理



### 2. java 结合框架图



### 3. java反射机制



## 实现原理

这个漏洞主要是由 **Transformer 类**里面的某些子类引起的, 其中最重要的几个就是:

> 1. `InvokeTransformer`    
>
>     利用java反射机制创建类实例( 试问: 如果这里创建的是一个 `能够接收 恶意代码的类实例`呢?)
>
>    
>
> 2. `ChainedTransformer` 
>
>    实现Transformer链式调用, 我们只需要传入一个`Transformer`数组(当然,传一个 元素也行), `ChainedTransformer `就可以实现依次的去调用每个`Transformer`的`transform() `方法
>
>    
>
> 3. `ConstantTransformer` 
>
>    `transform()`返回构造函数的对象.
>
> 4. `TransformedMap`
>
>    使用前面三个(`Transform 子类` 获得的内容)

简单的说, 前三个类主要是得到 `key 和 value ` 的, 最后一个 `TransformedMap` 会使用前三个的 `key`  和  `value`



**具体调用**:

1. 利用 `AnnotationInvocationHandler` 进行**序列化**, 然后交给java **反序列化** 
2. 在进行反序列化的时候会执行 `readObject()`方法, 该方法会调用 `setValue ` , 对变量 `TransformedMap` 的Value 进行修改
3. value 的修改会触发 `TransformedMap` 实例化时传入的参数(也就是`InvokerTransformer`的 `checkSetValue `的`transform()`方法)
4. 被放到Map 里面的是 `InvokeTransformer数组` , `transformer`方法被依次调用执行
5. `InvokerTransformer.transform()` 方法通过反射, 调用 `Runtime.getRuntime.exec("xxxxxx") 函数` , 来执行 **系统命令**

# 漏洞复现

> 暂略

