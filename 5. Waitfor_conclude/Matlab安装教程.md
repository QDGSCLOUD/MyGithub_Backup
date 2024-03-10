1. 环境

   1. 需要确定自己的linux系统有 `jdk` 和 `xserver`

      在没有的情况下, **我们可以再  `CentOs` 上安装**

      ```
      sudo yum install java-devel
      
      #  查看是否成功     java -version
      
      sudo yum groupinstall "X Window System"
      sudo systemctl start graphical.target          # 开启服务 , 可能要等一会
      
      # 开启服务也可以直接用   startx
      
      sudo systemctl enable graphical.target         # 设置开机自启
      
      # 重启机器
      sudo  reboot
      ```

      ok, 接下来 直接进入到解压出来的matlab文件夹中

      ```
      sudo  ./install
      ```

      正常就行, 账号和邮箱就是注册的账号和邮箱