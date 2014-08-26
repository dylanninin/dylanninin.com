---
layout: post
title: Phabricator Introduction
categories: [Dev, Management]
tags: [Worlflow, Nginx, Git, Markdown, Phabricator]
---

##写在前面的话

今年工作中的第一个项目，就是Phabricator的调研和定制。目前Phabricator已经在团队引入并使用近半年，整体来说体验不错；尽管核心的代码审查功能一直无人问津。另外，用Vagrant + Virtualbox搭建了一个个人日常使用的版本，在记录日常事务处理的同时，也作一些体验，比如代码审查，个性化，新功能体验等，工作流有了很大的优化，这种体验与使用Alfred颇有相通之处。

这里简单介绍下Phabricator的安装与配置过程，以及一些定制需求和实现。


##1.安装与配置

Phabricator安装/配置导图：

![phabricator-index](http://dylanninin.com/assets/images/2014/phabricator/index.png)

###要求

* OS: Redhat/Ubuntu 
* Web Server: nginx + php-fpm
* App: Phabricator(from facebook)
* PHP: >= 5.2
* Database: MySQL

###安装步骤

1. Network(hostname & ip, optional)

		sudo echo "phabricator.egolife.com" > /etc/hosts

2. Install Required Packages

		bash <(wget -qO- http://www.phabricator.com/rsrc/install/install_ubuntu.sh)

		sudo apt-get install nginx php5-fpm
		
	install mail server(optional)

		sudo apt-get install postfix

3. Nginx
	
	configuration file `phabricator.conf` references [Phabricator Configuration Guide](https://secure.phabricator.com/book/phabricator/article/configuration_guide/).
	
		sudo cp phabricator.conf /etc/nginx/sites-available`
	
		sudo ln -s /etc/nginx/sites-available/phabricator.conf /etc/nginx/sites-enabled

	
4. MySQL

	1) username/password: root/secret, phabricator/secret

	2) create database and tables using root
	
		./bin/storage upgrade --user root --password secret
		
	3) create a privileged user for Phabricator.
	
		create user phabricator@localhost identified by 'secret';
	
		grant all privileges on *.* to 'phabricator'@'localhost';

	
5. Phabricator config for MySQL (go to phabricator home first)

		./bin/config set mysql.host localhost
	
		./bin/config set mysql.user phabricator
	
		./bin/config set mysql.pass secret
	
		./bin/config set mysql.port 3306

6. Phabricator config for URI
		
		phabricator.base-uri your_url

7. Start Phabricator (go to phabricator home)

		./bin/phd start			#strat habricator daemons
	
		sudo service mysql start
	
		sudo service nginx start

8. 目录结构


	8.1. Top directories:

		/home/sponia/phabricator	#Phabricator Home
		├── bin						
		├── conf					#configuration for dev/prod/local
		├── externals
		├── LICENSE
		├── NOTICE
		├── README
		├── resources
		├── scripts
		├── src
		├── support
		└── webroot					#Web Root Path


	8.2. Main utils/scripts

	1) global configuration(settings will be saved in `./conf/local/local.json`)
	
		./bin/config list|get|set|delete|help
	
	2) database
	
		./bin/storage databases|destroy|dump|probe|status|upgrade|help
	
	3) phabricator daemons

		./bin/phd debug|launch|list|log|restart|start|status|stop|help


9. 配置

	9.1. `phabricator.conf` for nginx

	    #phabricator.conf
	    server {
	      listen 80 default;
	      #server_name phabricator.egolife.com;
	
	      root      /home/egolife/phabricator/webroot;
	      try_files $uri $uri/ /index.php;
	
	      location / {
	        index   index.php;
	
	        if ( !-f $request_filename )
	        {
	          rewrite ^/(.*)$ /index.php?__path__=/$1 last;
	          break;
	        }
	      }
	
	      location /index.php {
	        fastcgi_pass   localhost:9000;
	        fastcgi_index  index.php;
	
	        #required if PHP was built with --enable-force-cgi-redirect
	        fastcgi_param  REDIRECT_STATUS    200;
	
	        #variables to make the $_SERVER populate in PHP
	        fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;
	        fastcgi_param  QUERY_STRING       $query_string;
	        fastcgi_param  REQUEST_METHOD     $request_method;
	        fastcgi_param  CONTENT_TYPE       $content_type;
	        fastcgi_param  CONTENT_LENGTH     $content_length;
	
	        fastcgi_param  SCRIPT_NAME        $fastcgi_script_name;
	
	        fastcgi_param  GATEWAY_INTERFACE  CGI/1.1;
	        fastcgi_param  SERVER_SOFTWARE    nginx/$nginx_version;
	
	        fastcgi_param  REMOTE_ADDR        $remote_addr;
	      }
	    }
	    
---

##2.问题

1. magic_quotes_gpc should be disabled to run Phabricator.

	Error message when visiting phabricator:

		Your server is configured with PHP 'magic_quotes_gpc' enabled. This feature is 'highly discouraged' by PHP's developers and you must disable it to run Phabricator. Consult the PHP manual for instructions.

	Solution reference [Overriding php configuration in php-fpm pool](https://thedotproduct.org/setting-or-overriding-php-configuration-in-php-fpm-pool-configurations/): 
	
	edit `/etc/php5/fpm/pool.d/www.conf`, adding a new line: 
		
		php_admin_value[magic_quotes_gpc]=On

2. MySQL strict_all_tables mode should be enabled

	edit `/etc/mysql/my.cnf`, add a new line in `[mysqld]` module:
	
		 sql-mode=STRICT_ALL_TABLES

3. Server Timezone

	edit `/etc/php5/fpm/php.ini`, add a new line:

 		date.timezone = Asia/Shanghai

4. Repositories path does not set

	create the repository path & change its owner:
	
		sudo mkdir /var/repo && sudo chown www-data:www-data /var/repo

---

##3.定制需求


###3.1 Phabricator与Github的集成

根据[Diffusion User Guide: Repository Hosting](https://secure.phabricator.com/book/phabricator/article/diffusion_hosting/)上的描述，对于Git/HG/SVN等代码托管，目前有两种方案：

* 方案1：由phabricator自身托管（新功能，目前处于beta版），此时开发者可以向本代码库推送更新，但phabricator不能从其他地方拉取更新。
* 方案2：从其他地方（如Github.Bitbucket等）导入代码库，此时phabricator会启动daemon进程从远程代码库拉取更新以保持同步，但开发者不能向phabricator提交更新。

####导图

Phabricatory提供了代码库托管功能(自身托管，或者从外部导入),在此功能上，可以结合phabricatory中的其他应用如Feed/Herald/Diffusion等来进行代码的浏览、评审、任务追踪的操作，提供了一个高度统一的项目管理平台。

关于phabricator与github集成调研初步信息如下(其中标出序号的为重点项，下文将进行简单描述)：

![phabricator_github](http://dylanninin.com/assets/images/2014/phabricator/with_github.png)

1. daemon

	phabricator将启动一些daemon守护进程，负责拉取远程代码库的更新，并将代码库的更新历史等信息存放到数据库中（官方的说法时，相比直接从文件系统获取代码库历史信息，从数据库中查询速度更快）。

	因为启动的daemon守护进程是异步拉取更新，再加上网络条件，代码的同步可能会存在一定的延时；另外，phabricator管理的代码库较多时，对这些daemon的调优很有必要。

2. remote

	远程代码库，即github/bitbucket等其他代码库，phabricator从这里拉取更新。

3. mirrors

	phabricator提供了代码库镜像的功能，一个代码库可以有多个镜像(镜像可以在本地、远程)，phabricator会自动推送更新到这些镜像代码库。

4. action

	主要是Notify/Action功能，即通知和动作。动作功能主要体现在Herald应用中，可定义好一些规则(如代码提交者、标签、项目等)和动作(发送邮件通知、标记提交、触发审计、运行构建计划等)，当代码库有更新并匹配某些规则时将触发预定义的动作，使得整个流程更加自动化。

5. browser

	主要是浏览浏览、评论功能，有Diffusion应用提供。

6. 模型

	代码托管计划从bitbucket(hg)迁移到github(git)上，phabricator提供了导入这些代码库的功能，还可以进行代码审查、任务/bug追踪等，这部分具体的需求以及工作流程暂未确定下来。这部分涉及到的服务器比较多，如phabricator，github，还可以加上开发机、测试机，在需求确定下来后，可以构建几个可靠的模型，方便理解这些系统之间的关系。

![phabricator_github_model](http://dylanninin.com/assets/images/2014/phabricator/with_github_model.png)


####3.2 Git Commits与Maniphest Task关联

1 . Task关联

**需求**：Associate Git commit to Maniphest task。在Diffusion查看Repository的某一次提交时，提供了"Edit Maniphest Tasks"的选项，可以手动将Commits关联到某些任务，但这种方式不够自动化。

**解决**：目前Phabricator提供了以下方式，在commit时填写一些指定的message，即可以自动触发以上关联动作。

- 仅引用task，在commit message中添加 "Ref T1" 即可将此次提交关联到Task 1。
- 引用且改变Task状态，在commit message中添加"Resolve T1"，在Ref T1的同时会将Task 1的状态改为"Resoveld"。

在改变Task状态时，需要参考预定义的Task的statuses。

2 . 提交规范

git commits可以和task进行关联，接下来就是规范开发者的提交，目前有两种处理方式：

* 严格控制。即要求开发者提交的代码必须关联Task，否则不允许提交。可以通过git提供的一些列hooks来实现，如使用pre-push在client-side控制(此时开发者拥有自主决定权)；或pre-receive在server-side控制(具有强制性)。几种解决方法：
	* 情形1：在client-side添加pre-push，具有通用性，但脚本分散，开发者拥有自主决定却；
	* 情形2：在server-side添加pre-receive，需要server支持pre-receive，脚本可以集中管理；
	* 情形3：github尽管提供了很多Web/Service Hooks，但不支持pre-receive，此时暂未想到很好的解决方法。

* 非严格控制，即仅针对没有关联Task的提交发送邮件通知给相关人员。几种解决方法：
	* 情形1：在phabricator的repositories中添加post-receive，检查commit message，若没有关联task，则发送邮件给相关人员；
	* 情形2：在phabricator的herald中添加commit rules，但phabricator没有提供检查commit message的接口。
	* 情形3：github提供了Email Service Hook，但无法检查commit message决定是否发送邮件。
	* 情形4：github提供了Web Hook，此时需要搭建Web Hook的API服务，自行检查commit message，再发送邮件通知。

综上，使用github+phabricator,目前简单可行的方法如下：

* 严格控制：情形1，在client-side添加pre-push
* 非严格控制，邮件通知：情形1，在phabricator的repositories中添加post-receive，检查commit message，若没有关联task，则发送邮件给相关人员；

###3.3 搜索功能增强（集成ElasticSearch）

目前PH的搜索功能有限，如不支持搜索按name搜索task，也不支持中文搜索等，现希望对PH的搜索进行一些增强。

初步查阅资料：

- 字段查询
 - 目前支持的查询字段有限，见Phabricator的Advanced Search
 - 定制化搜索功能，增加一些常用的字段，提高检索的有好性
- 中文检索
 - 默认的MySQL fulltext engine (如MyISAM)，不支持非拉汀语言
 - 替换MySQL的搜索引擎，如Lucene/SOLR/ElasticSearch，使PH支持中文检索

参考

- [T1695 Support Chinese character search.](https://secure.phabricator.com/T1695)
- [T2632 MyISAM fulltext does not support non-latin languages and we don't warn you about it](https://secure.phabricator.com/T2632)
- [T355 Build a Lucene/SOLR backing engine as an alternative to the MyISAM Fulltext Index](https://secure.phabricator.com/T355)

####集成ElasticSearch

Phabricator内置支持ElasticSearch作为搜索引擎，需要做的几件事：

- 配置Phabricator要使用的ElasticSearch地址 `search.elastic.host`
- 微调代码，将field改为match，支持模糊匹配 [⚙ D9321 T4446: Fix Elasticsearch support for 1.0 and above](https://secure.phabricator.com/D9321)
- 搭建ElasticSearch服务，参见[Elasticsearch.org Download ELK | Elasticsearch](http://www.elasticsearch.org/overview/elkdownloads/)
- 为Phabricator手动建立索引：`./bin/search index --all`

注意:

- Phabricator需要启动 `./bin/phd`服务，做一些后台任务，在这里即同步索引数据
- 目前ElasticSearch没有额外添加分词库，中文搜索结果会按最大匹配进行排序
- ElasticSearch需要添加一些中文分词库，中文搜索的效果会更好，可再后续逐步迭代实现
- 若要取消ElasticSearch，只还原 `search.elastic.host` 设置即可。


参考：

- [Queries in ElasticSearch](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl-queries.html)

---

##4.备份

1. MySQL databases

	Backup:

	 	./bin/storage dump | gzip > backup.sql.gz

	Restore:

		gunzip -c backup.sql.gz | mysql


2. Uploaded files

	Storage Engine

	* Default/MySQL: Backup of database will include all files.
	* Amazon S3: ...
	* Local Disk: set `storage.local-disk.path`，than tar a copy.

3. Configuration files

	* tar a copy to somewhere else.
	* create a private reporisoty

---

##参考

* [Phabricator Official Site](http://phabricator.org/)
* [Phabricator on Github](https://github.com/facebook/phabricator/)
* [Phabricator Installation Guide](https://secure.phabricator.com/book/phabricator/article/installation_guide/)
* [Phabricator Configuration Guide](https://secure.phabricator.com/book/phabricator/article/configuration_guide/)
* [◉ Remarkup Reference](https://secure.phabricator.com/book/phabricator/article/remarkup/)
* [Diffusion User Guide](https://secure.phabricator.com/book/phabricator/article/diffusion/)
* [Diffusion User Guide: Repository Hosting](https://secure.phabricator.com/book/phabricator/article/diffusion_hosting/)
* [Phabricator - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Phabricator)
* [Phabricator - 热门问答 - 知乎](http://www.zhihu.com/topic/19745675)
* [借助 Alfred 2 的 Workflows 功能可以做哪些好玩的事情？ - 知乎](http://www.zhihu.com/question/20656680)