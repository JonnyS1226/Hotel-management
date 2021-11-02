# hotel-management

数据库课设-宾馆管理系统-python3.7+pyqt5



## 简介

* 大二数据库课程设计（3-4天工作量）的项目，登录界面的ui设计参考了他人成果，其余ui以及所有后端部分全部独立完成，详细功能见功能模块图
* 使用python+pyqt5，数据库使用MySQL5.7（使用了触发器技术）

## 待解决和完善
- [ ] 房间检索还需要手动重置查询结果
- [ ] 报表的中文显示问题
- [ ] 输入信息的检查，拟采用正则匹配方式
- [ ] 拟增加会员功能

## 运行方法

1. 在数据库中创建一个数据库，库名自定，与dbConfig中的配置一致即可
2. 在DBMS（如navicat）或MySQL中导入hotelManagement.sql，即可生成需要用的所有表，表内数据可自行修改，但是要注意参照完整性约束。
3. 在HotelManagement/dao/dbConfig中修改有关数据库配置（账号密码等）
4. 将文档内/pictures文件夹移动至D:，这是因为前端Qt StyleSheet中许多图片采用的绝对地址--D:/pictures/xxx
5. 运行Main.py即可


## 依赖库

* pyqt5：可视化展示
* pymysql：python3与mysql连接
* matplotlib：用于生成报表
* xlwt：用于将数据写入excel
以上使用pip安装即可

## 功能

![image-20200109132129113](https://github.com/JonnyS1226/hotel-management/blob/master/%E6%88%AA%E5%9B%BE/function.png)

## 项目截图

![image-20200109132059633](https://github.com/JonnyS1226/hotel-management/blob/master/%E6%88%AA%E5%9B%BE/chart.png)

![image-20200109132214605](https://github.com/JonnyS1226/hotel-management/blob/master/%E6%88%AA%E5%9B%BE/main.png)

![image-20200109132156385](https://github.com/JonnyS1226/hotel-management/blob/master/%E6%88%AA%E5%9B%BE/login.png)

![image-20200109132214605](https://github.com/JonnyS1226/hotel-management/blob/master/%E6%88%AA%E5%9B%BE/backup.png)

![image-20200109132214605](https://github.com/JonnyS1226/hotel-management/blob/master/%E6%88%AA%E5%9B%BE/room.png)

