# Python 通过rpy2调用 R语言

**系统环境**

```
python 2.7.4  32bit
R 3.0.1  i386-w64-mingw32/i386 (32-bit)
rpy2 2.3.7  32bit
windows 8  64bit
```

### 安装方法

rpy2 官方不支持windows了，python 2.7安装官方版本会报错。

下面的地址安装非官方的 rpy2 

安装地址：[http://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2](http://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2)

注意：（这里没有测试，因为我之前安装了numpy 和 vc++ 2008，如果安装出错这里也许有帮助）
>Many binaries depend on Numpy-MKL 1.7 and/or the Microsoft Visual C++ 2008 (64 bit or 32 bit, for CPython 2.6 to 3.2) redistributable packages.

rpy2的文档在[这里](http://rpy.sourceforge.net/rpy2/doc-2.3/html/index.html)

需要设置环境变量：
    
    path :安装路径\bin  #例如 C:\R-3.0.1\bin
    R_Home :安装路径  #例如 C:\R-3.0.1
    R_User ：可以也设置为安装路径  #例如 C:\R-3.0.1\bin

简单的例子：

    import rpy2
    from rpy2 import robjects as ro
    r=ro.r
    r("pi")

[example](https://github.com/kalelfc/rpy2/tree/master/example)文件夹中将给出各种例子

### 参考资料

- [sourceforge.net](http://sourceforge.net/mailarchive/forum.php?set=custom&viewmonth=&viewday=&forum_name=rpy-list&style=nested&max_rows=75&submit=Change+View)
- [www.blogosfera.co.uk](http://www.blogosfera.co.uk/2012/06/install-rpy2-on-windows7-64bit-for-python-2-7/)
- [Github--bwallace/OpenMeta-analyst-](https://github.com/bwallace/OpenMeta-analyst-/wiki/Setting-up-a-development-environment)
