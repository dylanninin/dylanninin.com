---
layout: post
title: MySQL Multiple Instances
category: Database
tags: [DBA, MySQL]
---

上周五下午，同事问到一个关于MySQL Multiple Instances的问题，参考一些教程配置后只能启动一个实例。当时正好要参加一个会议，晚上又是一年一度的晚会加抽奖环节（实际上我是奔着抽奖去的，无奈再次无缘），所以当天没有来得及处理。今天参考同事的配置进行测试，中间也遇到过一些错误，但感觉基础和关键都在MySQL的基本概念；最后同事发现问题所在，很快就解决了。

另外，前几天正好看到阮一峰的[PostgreSQL新手入门](http://www.ruanyifeng.com/blog/2013/12/getting_started_with_postgresql.html)，开篇即提到“自从MySQL被Oracle收购以后，PostgreSQL逐渐成为开源关系型数据库的首选”，不是黑Oracle，我只想说，即使不是为了逐渐去IOE化，也应该试试PostgreSQL；另外，时下从MySQL迁移到各类NoSQL数据库的案例正在逐步增加。

这儿简单记录下配置过程，同时做几点延伸：

* 对MySQL虽没有深究，但说不定以后会用到，所以我也来折腾下；
* 顺便推荐一些关于MySQL的延伸阅读，以作收藏和扩散；
* 最后，借此机会学习下如何提问，做好做足自身的准备工作，见[How To Ask For Help](http://dylanninin.com/blog/2013/12/30/ask_for_help.html)。

##MySQL多实例配置

###MySQL基本环境

1 . 主要信息

* OS: Ubuntu 13.04 i386
* MySQL: 5.5.34

2 . MySQL规划

MySQL Server使用apt-get安装，单实例使用默认配置，具体如下：

* 配置文件： `/etc/mysql/my.cnf`
* 数据库目录: `/var/lib/mysql`
* 日志目录：`/var/log/mysql`

MySQL Multiple Instances，参考MySQL单实例目录结构(两个实例，分别为mysql1，mysql2)，具体如下：

* 配置文件： `/etc/mysql/my_multi.cnf`
* 数据库目录: `/var/lib/mysql1`，`/var/lib/mysql2`
* 日志目录：`/var/log/mysql1`, `/var/lib/mysql2`

###MySQL Single Instance

一般情况下我们安装MySQL Server后，即默认启动一个MySQL实例，并绑定3306端口。主要步骤如下：

安装数据库，自动添加mysql用户/用户组。

    root@ubuntu:# apt-get install -y mysql-server

安装客户端

    root@ubuntu:# apt-get install -y mysql-client

主要配置

	root@ubuntu:# cat /etc/mysql/my.cnf 
	[mysqld]
	character-set-server=utf8
	datadir=/var/lib/mysql
	socket=/var/lib/mysql/mysql.sock
	user=mysql
	# Disabling symbolic-links is recommended to prevent assorted security risks
	symbolic-links=0
	log-error=/var/log/mysql/error.log
	log-bin=/var/log/mysql/update.log
	general_log-file=/var/log/mysql/all.log
	
	[mysqld_safe]
	pid-file=/var/run/mysqld/mysqld.pid
	
启动MySQL

    root@ubuntu:# service mysql start

客户端测试

	root@ubuntu:#mysql -uroot -p
	... ...

###MySQL Multiple Instances

有时需要在一台主机上运行多个MySQL实例，以便充分利用服务器资源。以两个实例mysql1，mysql2为例，主要步骤如下：

创建必须的目录结构，并分配权限。

	#数据文件目录
    root@ubuntu:#  mkdir /var/lib/mysql1 && chown mysql:mysql /var/lib/mysql1
    root@ubuntu:#  mkdir /var/lib/mysql2 && chown mysql:mysql /var/lib/mysql2
    
	#日志目录
    root@ubuntu:#  mkdir /var/log/mysql1 && chown mysql:mysql /var/log/mysql1
    root@ubuntu:#  mkdir /var/log/mysql2 && chown mysql:mysql /var/log/mysql2

安装数据库
 
    root@ubuntu:# mysql_install_db --datadir=/var/lib/mysql1 --user=mysql
    root@ubuntu:# mysql_install_db --datadir=/var/lib/mysql2 --user=mysql

编辑多实例参数配置

	root@ubuntu:# cat /etc/mysql/my_multi.cnf 
	[mysqld_multi]
	mysqld = /usr/bin/mysqld_safe
	mysqladmin = /usr/bin/mysqladmin
	user = root
	password = root
	
	[mysql1]
	ledir = /usr/sbin
	socket = /var/lib/mysql1/mysql1.sock
	port = 3301
	server-id = 1
	pid-file = /var/lib/mysql/mysql1.pid
	datadir = /var/lib/mysql1
	log-bin=/var/lib/mysql1/mysql1_update.log
	log_slave_updates
	expire_logs_days=7
	general_log-file = /var/log/mysql1/all.log
	log-error = /var/log/mysql1/error.log
	slow-query-log-file=/var/lib/mysql1/slow.log
	user = mysql
	
	[mysql2]
	ledir = /usr/sbin
	socket = /var/lib/mysql2/mysql2.sock
	port = 3302
	server-id = 2
	pid-file = /var/lib/mysql2/mysql2.pid
	datadir = /var/lib/mysql2
	log-bin=/var/lib/mysql2/mysql2_update.log
	log_slave_updates
	expire_logs_days=7
	general_log-file = /var/log/mysql2/all.log
	log-error = /var/log/mysql2/error.log
	slow-query-log-file=/var/lib/mysql2/slow.log
	user = mysql

启动多个实例

    mysqld_multi --defaults-file=/etc/mysql/my_multi.cnf start 1,2

检查实例运行状态

	root@ubuntu:# mysqld_multi report
	Reporting MySQL servers
	MySQL server from group: mysql1 is running
	MySQL server from group: mysql2 is running

###MySQL的几个异常

1 . `mysql`命令未找到

使用mysql客户端程序进行连接测试，发现mysql命令找不到，但是mysql-client已经安装。

	root@ubuntu:~# mysql -uroot -p -P3301
	The program 'mysql' is currently not installed. You can install it by typing:
	apt-get install mysql-client-core-5.5

	root@ubuntu:~# apt-get install -y mysql-client-core-5.5
	Reading package lists... Done
	Building dependency tree       
	Reading state information... Done
	mysql-client-core-5.5 is already the newest version.
	0 upgraded, 0 newly installed, 0 to remove and 7 not upgraded.

	root@ubuntu:~# apt-get install -y mysql-client
	Reading package lists... Done
	Building dependency tree       
	Reading state information... Done
	mysql-client is already the newest version.
	0 upgraded, 0 newly installed, 0 to remove and 7 not upgraded.
	
	root@ubuntu:~# whereis mysql
	mysql: /etc/mysql /usr/lib/mysql /usr/share/mysql
	root@ubuntu:~# locate mysql

先留着吧，看啥时候解决。

2 . 同事遇到的错误

因办公地点的物理阻隔，没有面对面的沟通，只是使用邮件在缓慢传递，一段时间后还没有解决，正准备使用SSH远程过去看看时，同事看出问题所在了，原来创建多个实例时定义的`datadir`定义有误，具体如下。

错误的定义：

	/var/lib/mysql/mysql1
	/var/lib/mysql/mysql2
	/var/lib/mysql/mysql3

现在改为：

	/var/lib/mysql1
	/var/lib/mysql2
	/var/lib/mysql2

重启即正常。

原来`/var/lib/mysql`为MySQL默认数据库的数据文件目录，在`/etc/mysql/my.cnf`中有定义，在此目录下，有类似如下的目录结构：

	root@ubuntu:~# ls -l /var/lib/mysql
	total 28700
	-rw-r--r-- 1 mysql mysql        0 Dec 30 10:23 debian-5.5.flag
	-rw-rw---- 1 mysql mysql 18874368 Dec 30 14:03 ibdata1
	-rw-rw---- 1 mysql mysql  5242880 Dec 30 14:06 ib_logfile0
	-rw-rw---- 1 mysql mysql  5242880 Dec 30 09:30 ib_logfile1
	drwx------ 2 mysql mysql     4096 Dec 30 10:24 mysql
	-rw-rw---- 1 mysql mysql        5 Dec 30 10:51 mysqld1.pid
	-rw-rw---- 1 mysql mysql        6 Dec 30 10:37 mysqld2.pid
	-rw-r--r-- 1 mysql mysql       91 Dec 30 09:44 mysqld_multi.log
	srwxrwxrwx 1 mysql mysql        0 Dec 30 14:06 mysql.sock
	drwx------ 2 mysql mysql     4096 Dec 30 10:23 performance_schema
	drwx------ 2 mysql mysql     4096 Dec 30 09:39 test
	-rw-rw---- 1 mysql mysql        5 Dec 30 14:06 ubuntu.pid

其中，目录`mysql`，`performance_schema`，`test`为启动MySQL的默认数据库。

以上即为此次配置过程，不管对错，以后再做深究；或许是用不做深究。

##延伸阅读

* YY哥理解MySQL系列博文：[架构与概念](http://www.cnblogs.com/hustcat/archive/2009/10/18/1585626.html)，[索引与优化](http://www.cnblogs.com/hustcat/archive/2009/10/28/1591648.html)，[复制Replication](http://www.cnblogs.com/hustcat/archive/2009/12/19/1627525.html)，[并行数据库与分区Partition](http://www.cnblogs.com/hustcat/archive/2009/12/24/1631674.html)
* [《High Performance MySQL》](http://book.douban.com/subject/1495763/)，[中文版](http://book.douban.com/subject/4241826/)
* [何登成的技术博客](http://hedengcheng.com/)

##参考

* [Oracle MySQL Blogs](https://blogs.oracle.com/MySQL/)
* [MySQL 5.5 Reference](http://dev.mysql.com/doc/refman/5.5/en/)
