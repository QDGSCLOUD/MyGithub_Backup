

1. 使用 `conda` 生成配置文件

```
jupyter notebook --generate-config
```



2. 找到 生成的`jupyter_notebook_config.py` 中的 `c.NotebookApp.notebook_dir = ''` ,  在单引号中放入路径就行,

   例如:`c.NotebookApp.notebook_dir = 'D:\GithubRepository\编程\Python_program'`



3. 设置 `快捷键`的 `属性`

**想要设置的默认打开的路径:**

D:\GithubRepository\编程\Python_program*



将下方的  `"%USERPROFILE%/" ` 改为 `"D:/GithubRepository/编程/Python_program/"`  

D:\myAnaconda_base\python.exe D:\myAnaconda_base\cwp.py D:\myAnaconda_base D:\myAnaconda_base\python.exe D:\myAnaconda_base\Scripts\jupyter-notebook-script.py "%USERPROFILE%/"



**一定要注意斜杠的方向!!!!**



OK啦!

