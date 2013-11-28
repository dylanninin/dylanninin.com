---
layout: post
title: Python Resource
category: Miscellanies
tags: [Python, Libs, NoSQL, Resource]
---

[Python](http://www.python.org/)是在工作期间零零碎碎学习起来的。当时正值部门申购图书，鉴于Python的动态、快速等特性，就申请买了一本[《Python核心编程》](http://book.douban.com/subject/3112503/)，内容可谓全面，但翻译实在太差，有些概念看了几遍也没弄清楚，所以只匆匆翻阅完了解一个大概。
后来在豆瓣上看了下评分，不到8分的样子，顺便做了下简评“只能说看这本书省去了初学者看电脑的眼疲劳，可以快速浏览一窥全貌。不过相比公开课，或者网上的教材，太不适合入门；尽管我还是硬着头皮差不多看完，也差不多入门”。

对Python有所了解之后，断断续续写了一些简单的程序，按先后顺序汇总如下：

* BBS账户批量导入工具：基于Discuz！，数据库为MySQL，直接读取Excel中的数据批量导入即可；当时正好在找代码片段分享的网站，就贴在[snipplr](http://snipplr.com/view/68951.85279/)上，这应该是我的第一个可以用的Python程序。

* 复杂密码生成工具：关于这个还有一段趣事，见本站[Complex Password Utility](http://dylanninin.com/blog/2013/01/18/complex_password.html)，源代码[PasswordGen on Github](https://github.com/dylanninin/utils/blob/master/passwdgen.py)。

* 邮件测试工具：碰到的Java程序员们连一个简单的[SMTP](http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)测试用例都懒得写，所以整了一个Python版，参考[email: Examples](http://docs.python.org/2/library/email-examples.html)；用[Telnet](http://en.wikipedia.org/wiki/Telnet)当然也可以，见本站[Telnet Introduction](http://dylanninin.com/blog/2013/03/21/telnet.html)。

* LDAP 账户查找工具：那时公司出了所谓的内网导航，提供查找员工的电话、邮件等信息，但后来残了，邮件地址不再显示（在一个靠邮件来沟通的公司，可见这种残会有多残），所以写了一个脚本自己用，见源代码[LDAPSearch on Github](https://github.com/dylanninin/utils/blob/master/ldapsearch.py)。

* Java Service接口测试用例生成工具：在[For Rails](http://dylanninin.com/blog/2013/11/11/for_rails.html)中提到过，思路见模板[jUnit TestCase Gist](https://gist.github.com/dylanninin/7426041)。

* Markdown Blog程序：使用[Web.py](http://webpy.org/)开发的Blog程序，自动渲染Markdown格式成HTML，见[Blog on Github](https://github.com/dylanninin/blog/)，在线demo [http://ec2-54-251-227-120.ap-southeast-1.compute.amazonaws.com](http://ec2-54-251-227-120.ap-southeast-1.compute.amazonaws.com)。

* 单词排行程序：同学在邮件中提到[Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/)，手上正好有Oracle Database 11g的全部文档，所以动手统计了一下词频，不知道每年的高考、考研的英语高频词汇是不是这样统计出来的。

以上大概是自学Python以来写过的一些程序，大部分代码还在，从中可见Python代码写得很不成熟；分析起来无非就是Python基础不过关、对标准库第三方库不熟练、受时间精力约束程序缺少锤炼、阅读源代码太少等之类的原因；当然，也很业余。

##为什么是Python

前段时间写[For Rails](http://dylanninin.com/blog/2013/11/11/for_rails.html)时，稍微概括了下自己的工作，这里再提一下：我是一枚Java攻城狮，工作两年多，主要做[Java Web](http://dylanninin.com/blog/2013/10/09/java_resource.html)开发，期间转去做了一年多的[Oracle DBA](http://dylanninin.com/blog/2013/10/26/oracle_dba.html)，维护[Oracle EBS](http://dylanninin.com/blog/2013/10/25/oracle_ebs.html)，也当过[Linux Administrator](http://dylanninin.com/blog/2013/10/25/linux.html)。似乎涉猎的东西太多太浅，有点样样稀松的嫌疑。

那么，为什么要学Python呢？我觉得可以先看看Peter的[Teach Yourself Programming in Ten Years](http://www.norvig.com/21-days.html)，中文翻译见[十年学会编程](http://daiyuwen.freeshell.org/gb/misc/21-days-cn.html)。

关于语言的选择，这里直接抄录[十年学会编程](http://daiyuwen.freeshell.org/gb/misc/21-days-cn.html)：

不少人问我，他们首先该学哪种编程语言。没有绝对的答案，不过请考虑以下几点：

* 用你的朋友的。当被问起“我该用哪种操作系统，Windows，Unix， 还是Mac？”，我总是回答：“你朋友用什么，你就用什么。” 你从朋友那能学到知识，这种优势可以抵销不同操作系统或语言之间本质的差异。也考虑你将来的朋友：程序员社区 — 你将成为它的一部分如果你继续往前走的话。你选择的语言是否有一个成长中的社区，还是人数不多、即将消亡？有没有书籍、网站、在线论坛回答你的问题？你喜欢论坛里的那些人吗？

* Keep it simple, stupid. 象C++和Java这样的语言是为经验丰富的程序员组成的团队进行专业开发而设计的，他们专注于代码运行时的效率。因此，这些语言有些部分非常复杂。而你关注的是如何编程，不需要那些复杂性。你需要的是这样的语言： 对单个的编程新手来说，它易学易记。

* 练习。你偏爱哪种学弹钢琴的方式：通常的交互式的方式，你一按下琴键就能听到音符；还是“批量”模式，你只有弹完整首曲子才能听到音符？ 显然，用交互模式学习弹钢琴更容易些，编程也一样。坚持用交互模式学习并使用一种语言。

有了上面的准则，我推荐的第一个编程语言是[Python](http://python.org/)或[Scheme](http://www.schemers.org/)。因人而异，还有其它好的选择。如果你的年纪是10岁以下，你可能更喜欢Alice。关键是你要选择并开始实践。

正如文中提到的一样，我学习Python很大一部分原因就是朋友的介绍；经过一些练习之后，你会发现自己越来越喜欢Python的简洁。印象最深的一次，要属部门一次关于[Web Service](http://en.wikipedia.org/wiki/Web_service)的技术交流会，主持人用Java来演示[XML RPC](http://en.wikipedia.org/wiki/XML-RPC)、[JSON RPC](http://en.wikipedia.org/wiki/JSON-RPC)、[SOAP](http://en.wikipedia.org/wiki/SOAP)，不说混杂着各种[Annoation](http://en.wikipedia.org/wiki/Java_annotation)，连这些协议都未所有触及，就疯狂的演示各种语言的客户端程序了。鉴于此，我花了几天时间看了下wiki，然后用Python做了几个原型，还附加地看了[REST](http://en.wikipedia.org/wiki/Representational_state_transfer)，这时你会发现用Python来解释会更加简明，这大概就是[奥卡姆剃刀](http://zh.wikipedia.org/wiki/%E5%A5%A5%E5%8D%A1%E5%A7%86%E5%89%83%E5%88%80)所讲的简单有效原理吧。

##一点Python编程资料

因为Python学习得很业余，所以想加强理解，提高编程技能；在工作之余顺手收藏了一些Python相关的资料，有一些看了一部分就搁置了，但时常还是会想起来是不是该抽点时间继续看看。基于以上原因，就动手整理一份Python编程的资料作为索引，以后会陆续更新。

###入门和基础

Python有Python 2.x 和Python 3.x 之分，争论很多，见[Python2orPython3](https://wiki.python.org/moin/Python2orPython3)。初学者不用考虑这个问题，可以从Python 2.x入门，之后再讨论会多一些理性。

* [洪强宁：Python于Web 2.0网站的应用](http://www.slideshare.net/hongqn/qcon2010-3881323)：豆瓣网洪强宁在QCon北京2010中的技术分享，若不能访问，请自备梯子；另外，豆瓣的[阿北](http://www.douban.com/people/ahbei/)很值得关注。

* [A Byte of Python](http://swaroopch.com/notes/python/)：即简明Python教程，边看边练习就对Python有基本的了解，可以轻松存活。

* [Google's Python Lessons](http://blog.hartleybrody.com/google-python/)：Google出品的Python教程，值得信赖。

* [Python Documentation](http://www.python.org/doc/)：Python在线文档，若嫌枯燥，可以直接看[Python Standard Lib](http://docs.python.org/2/library/)。

* [42区：python入门指引](http://matrix.42qu.com/10757179)：江湖人称[张教主](http://zuroc.42qu.com/)的Python入门指引，除开[《Python核心编程》](http://book.douban.com/subject/3112503/)。严格来说，这是张教主的一份Python资料索引。

* [CS61A: SICP with Python](http://www-inst.eecs.berkeley.edu/~cs61a/fa11/61a-python/content/www/index.html)：作为计算机相关人士，[SICP](http://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs)都不了解，实在很惭愧，所以来还债了。这应该是起源于[MIT的SICP](http://mitpress.mit.edu/sicp/)教程，一个用Python，一个用Scheme。

* [看到一个有趣的python的招聘测试](http://www.douban.com/group/topic/28872729/)：同学发的一个贴，总结了一下应聘中遇到的问题，并给出了相应的资料来学习。如果想检测下自己的Python水平，请自觉移步[北京视讯天下的开发测试](http://www.video-tx.com/devtest/test.html#/home)。

* MOOC们：在线公开课很多，见[课程图谱](http://coursegraph.com/search_results/python)；仅在[Codecademy](http://www.codecademy.com/tracks/python)上学了一点；现在希望能够每天跟进一些感兴趣的课程，多多学习。

* 书：去年6月份一同事离职，我买了两本[黑客与画家](http://book.douban.com/subject/6021440/)，一本送给他(博客[一起去看海](http://www.ooobj.com))，另一本给部门老大；他回送了一本[Python源代码剖析](http://book.douban.com/subject/3117898/)，看书名就知道是讲底层原理的，有机会啃啃。

* 源代码：直接到[Github](https://github.com/search?q=python&ref=cmdform)上去找吧。

###Python与数据库

在项目开发中，数据库应用必不可少。这里汇总下目前接触过的数据库和使用教程。

SQL，计算机出身的人应该都学过，若有疑问可以参考[Wikipedia SQL](http://en.wikipedia.org/wiki/SQL)，并使用SQLite做下练习。

* [PEP249: DB API](http://www.python.org/dev/peps/pep-0249/)：数据库访问接口规范，当时还做了一份[笔记](http://dylanninin.com/blog/2012/11/16/python_pep249.html)。

* [SQLite](http://www.sqlite.org/)：教程见[SQLite Python Tutorial](http://www.tutorialspoint.com/sqlite/sqlite_python.htm)；若要深入了解，推荐[The Definitive Guide to SQLite](http://book.douban.com/subject/5392299/)；看此书时，做了一些好句子、段落的摘要，见[Sentences in SQLite 3](http://dylanninin.com/blog/2013/11/10/sentences_in_sqlite.html)。

* [MySQL](http://www.mysql.com/)：教程见[Python MySQL Database Access](http://www.tutorialspoint.com/python/python_database_access.htm)。

* [Oracle Database](http://www.oracle.com/us/products/database/overview/index.html)：有可能这是最庞大的数据库，所以需要专职的DBA。官方教程[The Mastering Oracle+Python Series](http://www.oracle.com/technetwork/articles/dsl/mastering-oracle-python-1391323.html)，快速入门教程[cx_Oracle Quick Start](http://dbaportal.eu/sidekicks/sidekick-cx_oracle-code-paterns/)。

* [SQLAlchemy](http://www.sqlalchemy.org/)：Python的ORM标准和框架，解决面向对象编程和关系数据库模式不匹配的问题。

数据库理论除了SQL，还有另一派NoSQL。

关于NoSQL，先上一段笑话：“Big data is like teenage sex: everyone talks about it, nobody really knows how to do it, everyone thinks everyone else is doing it, so everyone claims they are doing it.” [Big Data](http://en.wikipedia.org/wiki/Big_data)和[NoSQL](http://en.wikipedia.org/wiki/NoSQL)紧密相连，Big Data为甚？目前我没有多少理解和认识，所以先来看看NoSQL，在[NoSQL Database](http://nosql-database.org/)上的定义和介绍：

NoSQL DEFINITION: Next Generation Databases mostly addressing some of the points: being **non-relational**, **distributed**, **open-source** and **horizontally scalable**.

The original intention has been modern web-scale databases. The movement began early 2009 and is growing rapidly. Often more characteristics apply such as: schema-free, easy replication support, simple API, eventually consistent / BASE (not ACID), a huge amount of data and more. So the misleading term "nosql" (the community now translates it mostly with "not only sql") should be seen as an alias to something like the definition above.

关于常见NoSQL产品的比较见[Main NoSQL Database Comparison](http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis)；若果需要一些NoSQL的理论知识和基本概念，见[The NoSQL Ecosystem](http://www.aosabook.org/en/nosql.html)、[Big Data与NoSQL](http://www.slideshare.net/pavlobaron/big-data-nosql-efs11-pavlo-baron)。目前仅用过[MongoDB](http://www.mongodb.org/)和[Redis](http://redis.io/)。

* MongoDB：如果熟悉SQL，MongDB的学习成本会很低；相关资料见[Python Language Center in MongoDB](http://docs.mongodb.org/ecosystem/drivers/python/)；用过的两个驱动：1）[PyMongo](http://api.mongodb.org/python/current/)，提供了类似Mongo Shell的接口；2）[MongoEngine](http://mongoengine.org/): A Python Object-Document-Mapper for working with MongoDB，即MongoDB的'ORM'框架，此时变成了'ODM'，[MongoEngine on Github](https://github.com/hmarr/mongoengine)。

* Redis：Redis需要一些学习成本，入门推荐[The Little Redis Book](http://openmymind.net/2012/1/23/The-Little-Redis-Book/)；用过的Python客户端驱动[Redis-py](https://github.com/andymccurdy/redis-py)；更多客户端见[Redis Clients](http://redis.io/clients)。

* NoSQL建模：SQL发展了几十年，有很成熟的建模技术，那么NoSQL呢，见[陈皓：NoSQL数据建模技术](http://coolshell.cn/articles/7270.html)，原文[NoSQL Data Modeling Techniques](http://highlyscalable.wordpress.com/2012/03/01/nosql-data-modeling-techniques/)。

* 更多资料：NoSQL英文站点见[NoSQL Database](http://nosql-database.org/)；NoSQL中文论坛见[NoSQL Fan：关注NoSQl相关的新闻和技术](http://blog.nosqlfan.com/)。NoSQL Fan中，MongoDB和Redis资料很多，已经形成了资料专题，包括介绍、内部实现、应用与优化、新闻等，总能发现你想要的东西：1）[NoSQL Fan：Redis资料汇总专题](http://blog.nosqlfan.com/html/3537.html)；2）[NoSQL Fan: MongoDB资料汇总专题](http://blog.nosqlfan.com/html/3548.html)。

###Python与Web开发

Python的Web框架众多，见[Web Frameworks for Python](https://wiki.python.org/moin/WebFrameworks)，总有一款适合你或你的项目，实在不行，请动手打造自己的框架；为什么会有这么多框架呢，见[Why so many Python wen frameworks?](http://bitworking.org/news/Why_so_many_Python_web_frameworks)。

* [Web.py](http://webpy.org/)：已故[Aaron Swartz](http://www.aaronsw.com/)的框架。一句话介绍"web.py is a web framework for Python that is as simple as it is powerful. web.py is in the public domain; you can use it for whatever purpose with absolutely no restrictions."。接触的第一个Web框架，后来模仿MovableType，写了一个简单的博客，见[Blog on Github](https://github.com/dylanninin/blog/)，在线demo [http://ec2-54-251-227-120.ap-southeast-1.compute.amazonaws.com](http://ec2-54-251-227-120.ap-southeast-1.compute.amazonaws.com)；碰到的坑点是模板中嵌套Python代码一直有缩进问题。

* [Flask](http://flask.pocoo.org/)：一句话介绍"Flask is a lightweight web application framework written in Python and based on the Werkzeug WSGI toolkit and Jinja2 template engine. It is BSD licensed.
Flask is called a microframework because it keeps the core simple but extensible"。因为工作变动，练习过一段时间的Flask，以便熟悉开发的工具链；如果没有Rails，我想这才是自己首选的Web开发框架: simple but extensible and for fun。实战教程[The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)。

* [Django](https://www.djangoproject.com/)：一句话介绍"Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design."，接触不多，作为全栈式框架，听说它的组件都是Made in Django。更多资料见[Django资料](http://haoluobo.com/trac/wiki/Django)。

###IDE

* [Vim](http://www.vim.org/) + [Python Mode](https://github.com/klen/python-mode)。目前就用这个方案，很方便，直接引用同学的[效果图](http://www.douban.com/photos/photo/1975213817/)。关于Vim资料和讨论，请移步[Vim资料大全](http://wiki.hotoo.me/Vim.html)；关于Vim更多插件和演示，请移步[k-vim on Github](https://github.com/wklken/k-vim)；关于Git，Github，请移步本站[Free Blog with Github Pages](http://dylanninin.com/blog/2013/11/02/free_blogs.html)。

###社区

* [啄木鸟社区](http://wiki.woodpecker.org.cn/moin/)
* [42区：网站开发.漫游指南](http://matrix.42qu.com/)
* [Python on V2EX](https://www.v2ex.com/go/python)
* [Python4cn](http://www.simple-is-better.com/)
* [豆瓣Python小组](http://www.douban.com/group/python/)
* [哲思社区](http://www.zeuux.com/)

###周刊

* [Python Weekly](http://www.pythonweekly.com/)：每周更新，包括Python相关的文章、教程、演讲、书籍、项目、工作等。
* [Pycoder's Weekly](http://www.pycoders.com/)：与Python Weekly类似，两者可以互为补充，了解过去一周动态。
* [码农周刊](http://weekly.manong.io/): [developerWorks](http://weibo.com/developerworks)出品的周刊，来自国人的分享。可以先看[为什么要做《码农周刊》？](http://blog.manong.io/why-create-a-weekly-newsletter-for-programmers/)；接着[《码农周刊》用到的一些技术](http://blog.manong.io/technologies-we-use/)；
再接着[周刊回顾](http://weekly.manong.io/issues/)。这里不仅仅是Python。

##Reference

* [十年学会编程](http://daiyuwen.freeshell.org/gb/misc/21-days-cn.html)
