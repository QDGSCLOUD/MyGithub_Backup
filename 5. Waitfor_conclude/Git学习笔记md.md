---
Git学习笔记
---



> 声明:本人通过哔哩哔哩的狂神说来学习的, 相关内容也是通过公众号看到的.

# 1. 版本控制

## 版本控制是啥?

一个项目不断的迭代, 不断的更新, 为了保留和利用之前的项目版本, 就需要版本控制

## 版本控制作用

1. 实现跨区域多人协同开发
2. 追踪和记载一个或者多个文件的历史记录
3. 组织和保护你的源代码和文档
4. 统计工作量
5. 并行开发、提高开发效率
6. 跟踪记录整个软件的开发过程
7. 减轻开发人员的负担，节省时间，同时降低人为错误

## 版本控制工具有哪些

- **Git**
- **SVN**（Subversion）
- **CVS**（Concurrent Versions System）
- **VSS**（Micorosoft Visual SourceSafe）
- **TFS**（Team Foundation Server）
- Visual Studio Online

**现在影响力最大且使用最广泛的是Git与SVN**

## 版本控制分类

1. **本地版本控制**

> 自己写的项目自己看, 保存到本地机器上.

1. **集中版本控制  SVN**

> SVM 就是将所有人的项目文件都保存到一个中心, 如果这个中心挂了, 那么大家就只能看到自己完成的那部分项目, 而不能看到其他人的了, 并且如果有人没备份, 那么这个项目可能就完了

1. **分布版本控制Git**

> 不仅有一个保存所有人写的项目的文件, 而且每个人通过**拉取,** 都能获得完整的项目文件, 这样即使即使那个保存所有项目的中心挂了, **每个人也都可以有一个相对完整的备份**, 项目就可以继续写啦!!!

# 2. Git诞生

Git诞生要从linux的管理来说, 绝大多数的 Linux 内核维护工作都花在了提交补丁和保存归档的繁琐事务上(1991－2002年间)。到 2002 年，整个项目组开始启用一个专有的分布式版本控制系统 BitKeeper 来管理和维护代码. 但是BitKeeper是收费的, 2005年的时候, 开发 BitKeeper 的商业公司同 Linux 内核开源社区的合作关系结束，他们收回了 Linux 内核社区免费使用 BitKeeper 的权力。这就迫使 Linux 开源社区(特别是 Linux 的缔造者 Linus Torvalds)基于使用 BitKeeper ，开发出自己的版本系统（2周左右！） **也就是后来的 Git！**

# 4. 安装Git

> 上网搜索就行(不要忘记配置环境变量)

# 5.Git账号配置

1. 查看是否有账号, 输入:

```git
# 查看所有的配置文件(里面有账号)
git config -l

# 查看系统的配置文件
git config --system --list

# 查看本地的配置文件(如果已经配置好的话, 可以直接看到账号和密码)
git config --global --list
```

2. 配置账号 和 邮箱

```
git config --global user.name "自己起个站好名字(最好是英文)"
```

```
git config --global user.email 填写一个自己的邮箱(例如:xx@qq.com)
```

去查看是否成功,  例如: 下方是已经配置好账号的:

![image-20230331205846011](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230331205846011.png)

**注意: 所谓的配置文件其实就是在某个文件文件中写入一些内容, 可以通过下方的目录来查看配置文件:**

```
Git\etc\gitconfig  # 查看的是系统级别的配置

C:\Users\你的电脑登录账号名字\ .gitconfig    只适用于当前登录用户的配置  --global 全局
```

3. 本地电脑绑定远程仓库

   >  首先在电脑上找到 `.ssh` 文件夹

```

# 一般的windows电脑 , 进入 C:\Users\用户名\.ssh 目录
# 在生成git公钥(-t命令指的是采用哪种加密算法), 在git中执行:
ssh-keygen -t rsa 
```

接着, **多次回车后, 就生成了`公钥 和私钥`文件, 再电脑中打开生成的public key **, 将里面的内容放到, github 或者 gitee 的ssh里面就行

> 注意: 我们要用的是公钥, 有`文件名字里面pub`

> 以Gitee为例: 
>
> 1. 打开gitee, 右上角的那里, 有 **账号设置**, 点击进入
> 2. 在左边栏中, 下面有个 **SSH公钥**, 点击进入

![image-20230331215950463](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230331215950463.png)

# 5. Git基本流程

**该本内容了解即可, 本人在为学习git的时候, 也不知道这些东西, 但是照样使用git**

## 工作区介绍

1. **Workspace：工作区**，就是你平时存放项目代码的地方
2. **Index / Stage：暂存区**，用于临时存放你的改动，事实上它只是一个文件，保存即将提交到文件列表信息
3. **Repository：仓库区（或本地仓库）**，就是安全存放数据的位置，这里面有你提交到所有版本的数据。其中HEAD指向最新放入仓库的版本
4. **Remote：远程仓库**，托管代码的服务器，可以简单的认为是你项目组中的一台电脑用于远程数据交换

```
# 1. 在工作目录中, 添加修改的文件
git add . 

# 2. 将添加的文件推送到本地的暂存区
git commit -m '推送描述'

# 3. 将暂存区的文件提交到git仓库
git push origin 当前分支名
```

## git管理文件的三种状态

1. 已修改(modified)
2. 已暂存(staged)
3. 已提交(committed)

## 文件操作的状态

1. Untracked: 未跟踪, 此文件在文件夹中, 但并没有加入到git库, 不参与版本控制. 通过git add 状态变为Staged.
2. Unmodify: 文件已经入库, 未修改, 即版本库中的文件快照内容与文件夹中完全一致. 这种类型的文件有两种去处, 如果它被修改, 而变为Modified. 如果使用git rm移出版本库, 则成为Untracked文件
3. Modified: 文件已修改, 仅仅是修改, 并没有进行其他的操作. 这个文件也有两个去处, 通过git add可进入暂存staged状态, 使用git checkout 则丢弃修改过, 返回到unmodify状态, 这个git checkout即从库中取出文件, 覆盖当前修改 !
4. Staged: 暂存状态. 执行git commit则将修改同步到库中, 这时库中的文件和本地文件又变为一致, 文件为Unmodify状态. 执行git reset HEAD filename取消暂存, 文件状态为Modified

# 6. Git使用中用到的命令

1. 建立本地仓库, 初始化git仓库

```
git init

# 也可以直接克隆一个仓库
git clone 克隆地址
```

>  注意:** 生成的`.git` 文件夹, 是隐藏文件夹.

> 克隆地址:

![image-20230331212459774](https://raw.githubusercontent.com/QDGSCLOUD/BJYH_picture/main/img/image-20230331212459774.png)



2. 查看为跟踪文件

> 所谓的 **未跟踪**, 指的就是 刚建立的文件, 没有执行`git add .`的那些文件

```
git status
```

如果没有被跟中, 执行`git add . ` 就行



3. 忽略文件

通过在项目的某个文件夹下定义**.gitignore文件**，在该文件中定义相应的忽略规则，来管理当前文件夹下的文件的Git提交行为。.gitignore 文件是可以提交到公有仓库中，这就为该项目下的所有开发者都共享一套定义好的忽略规则。在.gitingore 文件中，遵循相应的语法，在每一行指定一个忽略规则。如：

1. `\*.log`
2. `\*.temp`
3. `/vendor`

**忽略配置和 忽略规则, 参考:https://cloud.tencent.com/developer/article/1831680**

还有其他的命令: 

```
# 列出所有本地分支
git branch

# 列出所有远程分支
git branch -r

# 新建一个分支，但依然停留在当前分支
git branch [branch-name]

# 新建一个分支，并切换到该分支
git checkout -b [branch]

# 合并指定分支到当前分支
$ git merge [branch]

# 删除分支
$ git branch -d [branch-name]

# 删除远程分支
$ git push origin --delete [branch-name]
$ git branch -dr [remote/branch]
```

