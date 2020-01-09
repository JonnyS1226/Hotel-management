# hotel-management

数据库课设-宾馆管理系统-python3.7+pyqt5



## 简介

* 两周数据库课程设计（实际大概4天左右写完的）的项目，登录界面前端设计参考了他人成果，其余部分全部独立完成，详细功能见功能模块图
* 使用python+pyqt5，数据库使用MySQL5.7



## 运行方法

1. 在数据库中创建一个数据库，库名自定，与dbConfig中的配置一致即可
2. 在DBMS（如navicat）或MySQL中导入hotelManagement.sql，即可生成需要用的所有表，表内数据可自行修改
3. 在HotelManagement/dao/dbConfig中修改有关数据库配置（账号密码等）
4. 将文档内/pictures文件夹移动至D:，这是因为前端Qt StyleSheet中许多图片采用的绝对地址--D:/pictures/xxx
5. 运行Main.py即可



## 依赖库

pyqt5，pymysql，matplotlib，xlwt

以上使用pip install xxx即可安装



## 项目截图

![image-20200109132059633](C:\Users\Sjy\AppData\Roaming\Typora\typora-user-images\image-20200109132059633.png)

![image-20200109132129113](C:\Users\Sjy\AppData\Roaming\Typora\typora-user-images\image-20200109132129113.png)

![image-20200109132156385](C:\Users\Sjy\AppData\Roaming\Typora\typora-user-images\image-20200109132156385.png)

![image-20200109132214605](C:\Users\Sjy\AppData\Roaming\Typora\typora-user-images\image-20200109132214605.png)
