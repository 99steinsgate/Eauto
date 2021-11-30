# Eauto
E浙理自动打卡

本项目仅用于浙江理工大学学生E浙理打卡使用

#### 注1：本程序默认用户安装了python环境

#### 注2：本程序只支持Google浏览器

#### 注3：驱动安装教程转载自https://blog.csdn.net/dingding_ting/article/details/116671013

#### 注4：本仓库内置对应96.0.4664.45版本的Google驱动chromedriver.exe，若版本不匹配请根据教程自行更改

#### 操作流程

一、在目录下打开终端，运行以下命令安装依赖

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

二、将账号密码写入“acc_pass.txt”中，请务必确保账号密码填写正确。

三、请务必确保安装了相应的驱动，并且**放在和程序相同的目录下**。

​	1.检查浏览器版本
以Chrome浏览器为例，点击.菜单栏->帮助->关于 Google Chrome 查看。版本号比较长，主要版本号是第三个点号的前几位，最后的93为小版本，暂不考虑。

![å¨è¿éæå¥å¾çæè¿°](https://img-blog.csdnimg.cn/20210511212808359.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RpbmdkaW5nX3Rpbmc=,size_16,color_FFFFFF,t_70)


2. 下载对应版本驱动
    下载地址为：https://www.selenium.dev/documentation/en/webdriver/driver_requirements/，页面如下所示：

  ![å¨è¿éæå¥å¾çæè¿°](https://img-blog.csdnimg.cn/20210511213539208.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RpbmdkaW5nX3Rpbmc=,size_16,color_FFFFFF,t_70)

点击Downloads,页面如下所示：选择版本号90.0.4430

![å¨è¿éæå¥å¾çæè¿°](https://img-blog.csdnimg.cn/20210511213702475.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RpbmdkaW5nX3Rpbmc=,size_16,color_FFFFFF,t_70)

再选择window环境包：

![å¨è¿éæå¥å¾çæè¿°](https://img-blog.csdnimg.cn/20210511213812754.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RpbmdkaW5nX3Rpbmc=,size_16,color_FFFFFF,t_70)

