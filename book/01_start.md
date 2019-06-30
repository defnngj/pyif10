

#### 环境搭建

1、安装python 

下载地址：https://www.python.org/downloads/release/python-373/

2、配置环境变量

```
C:\python37;C:\python37\Scripts;
``` 

3、安装编辑器/IDE

* 编辑器推荐：VS code 

* IDE推荐：pycharm 

4、安装Django

```
pip install django==2.2.2
```

#### django项目

1、创建```mysite```项目

```shell
> django-admin startproject mysite
```

2、创建```sign```应用

```shell
> cd mysite
> python startapp sign 
```

#### 练习

1、根据django官方教程，完成投票系统。

https://docs.djangoproject.com/en/2.2/intro/tutorial01/