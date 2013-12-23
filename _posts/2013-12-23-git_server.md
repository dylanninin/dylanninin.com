---
layout: post
title: Set Up a Minimal Git Server
categories: [Linux, Dev]
tags: [Git, Linux, Windows]
---

[Github](https://github.com) is well-known and we are enjoying it, but now I will set up a minimal Git server on Ubuntu according to [Git on the Server](http://www.git-scm.com/book/en/Git-on-the-Server) for some reason you have to set up your own hosting repositories, and it really works well.

##Minimal Git Server

Get server information: Kernel and IP address.

	me@ubuntu:~$ uname -a
	Linux ubuntu 3.8.0-19-generic #29-Ubuntu SMP Wed Apr 17 18:19:42 UTC 2013 i686 i686 i686 GNU/Linux

	me@ubuntu:~$ sudo ifconfig
	eth0      Link encap:Ethernet  HWaddr 00:0c:29:e2:b7:55  
	          inet addr:192.168.1.111  Bcast:192.168.1.255  Mask:255.255.255.0
	          inet6 addr: fe80::20c:29ff:fee2:b755/64 Scope:Link
	          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
	          RX packets:18521 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:15017 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:1000 
	          RX bytes:13819275 (13.8 MB)  TX bytes:4889250 (4.8 MB)
	          Interrupt:19 Base address:0x2000 
	
	lo        Link encap:Local Loopback  
	          inet addr:127.0.0.1  Mask:255.0.0.0
	          inet6 addr: ::1/128 Scope:Host
	          UP LOOPBACK RUNNING  MTU:65536  Metric:1
	          RX packets:72 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:72 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:0 
	          RX bytes:17632 (17.6 KB)  TX bytes:17632 (17.6 KB)

1 . Create user

First, create a `git` user for your git repositories.

	$ sudo adduser git

2 . Generate SSH Keys

Generate ssh keys for users, dylan for example.

	git@ubuntu:~$ ssh-keygen 
	Generating public/private rsa key pair.
	Enter file in which to save the key (/home/git/.ssh/id_rsa): /home/git/.ssh/id_rsa.dylan
	Enter passphrase (empty for no passphrase): 
	Enter same passphrase again: 
	Your identification has been saved in id_rsa.dylan.
	Your public key has been saved in id_rsa.dylan.pub.
	The key fingerprint is:
	e5:f7:49:15:6d:39:0a:6e:02:57:4f:6b:c9:e3:d9:c0 git@ubuntu
	The key's randomart image is:
	+--[ RSA 2048]----+
	|          .. . .o|
	|       . . .= oo+|
	|        o o .E..o|
	|         + oo.=. |
	|        S + .o.. |
	|           . o . |
	|              o  |
	|                 |
	|                 |
	+-----------------+

3 . Setting Up the Server

Now, append the public keys into the `authorized_keys` file.

	git@ubuntu:~$ cd .ssh
	
	git@ubuntu:~/.ssh$ ls -l
	total 40
	drwx------ 2 git git 4096 Dec 23 10:26 ./
	drwxr-xr-x 7 git git 4096 Nov 18 18:04 ../
	-rw------- 1 git git    0 Nov 18 17:49 authorized_keys
	-rw------- 1 git git 1679 Dec 23 10:22 id_rsa.dylan
	-rw-r--r-- 1 git git  392 Dec 23 10:22 id_rsa.dylan.pub
	-rw------- 1 git git 1675 Dec 23 10:26 id_rsa.gandhi
	-rw-r--r-- 1 git git  392 Dec 23 10:26 id_rsa.gandhi.pub
	-rw------- 1 git git 1679 Dec 23 10:26 id_rsa.mandela
	-rw-r--r-- 1 git git  392 Dec 23 10:26 id_rsa.mandela.pub
	-rw------- 1 git git 1679 Dec 23 10:26 id_rsa.suukyi
	-rw-r--r-- 1 git git  392 Dec 23 10:26 id_rsa.suukyi.pub

	git@ubuntu:~/.ssh$ cat *.pub >> authorized_keys 


Then, initialize a bare git repository.

	git@ubuntu:~$ cd repositories/
	git@ubuntu:~/repositories$ ls -l
	total 8
	drwxrws--- 2 git git 4096 Nov 18 17:49 ./
	drwxr-xr-x 5 git git 4096 Dec 23 10:34 ../

	git@ubuntu:~/repositories$ mkdir web.git
	git@ubuntu:~/repositories$ cd web.git/
	git@ubuntu:~/repositories/web.git$ git --bare init
	Initialized empty Git repository in /home/git/repositories/web.git/

	git@ubuntu:~/repositories/web.git$ ls -l
	total 40
	drwxrwsr-x 7 git git 4096 Dec 23 11:15 ./
	drwxrws--- 3 git git 4096 Dec 23 11:15 ../
	drwxrwsr-x 2 git git 4096 Dec 23 11:15 branches/
	-rw-rw-r-- 1 git git   66 Dec 23 11:15 config
	-rw-rw-r-- 1 git git   73 Dec 23 11:15 description
	-rw-rw-r-- 1 git git   23 Dec 23 11:15 HEAD
	drwxrwsr-x 2 git git 4096 Dec 23 11:15 hooks/
	drwxrwsr-x 2 git git 4096 Dec 23 11:15 info/
	drwxrwsr-x 4 git git 4096 Dec 23 11:15 objects/
	drwxrwsr-x 4 git git 4096 Dec 23 11:15 refs/

4 . Client Test

First, get the ssh private key from the server, `id_rsa.dylan` for example.

	git@ubuntu:~/.ssh$ sz id_rsa.dylan
	*B00000000000000

Start a git-bash window on the client, and move `id_rsa.dylan` to `id_rsa`:

	$ ~ mv id_rsa.dylan ~/.ssh/id_rsa

	dev$ ~ ls
	id_rsa

Configure your global git options: 

	$ git config --global user.name "Dylanninin Gogh"
	$ git config --global user.email "dylanninin@gmail.com"

	$ git config -l
	user.name=Dylanninin Gogh
	user.email=dylanninin@gmail.com
	color.ui=true
	core.editor=vim

Create a new git repository and push to the remote git server：

	$ cd /f/Workspace/web

	$ git init
	Initialized empty Git repository in f:/Workspace/web/.git/

	$ git add .

    dev$ git commit -m 'initial commit'
	[master (root-commit) a8c85ac] initial commit
	 14 files changed, 15063 insertions(+)
	 create mode 100644 1.html
	 create mode 100644 css/todos.css
	 create mode 100644 js/app.js
	 create mode 100644 js/lib/backbone-edge.js
	 create mode 100644 js/lib/backbone-min.js
	 create mode 100644 js/lib/backbone.js
	 create mode 100644 js/lib/backbone.localStorage.js
	 create mode 100644 js/lib/jquery.js
	 create mode 100644 js/lib/json2.js
	 create mode 100644 js/lib/underscore.js
	 create mode 100644 js/models/todos.js
	 create mode 100644 js/demo.js
	 create mode 100644 todos.html
	 create mode 100644 ws_client.html

	$ git remote add origin git@192.168.1.111:~/repositories/web.git

	$ git push origin master
	Counting objects: 20, done.
	Delta compression using up to 2 threads.
	Compressing objects: 100% (17/17), done.
	Writing objects: 100% (20/20), 192.52 KiB, done.
	Total 20 (delta 1), reused 0 (delta 9)
	To git@192.168.1.111:~/repositories/web.git
	 * [new branch]      master -> master

Show git log on the server:

	git@ubuntu:~/repositories/web.git$ git log
	commit 27e266eb7b67514ae00d7c1aba4539b43ca60680
	Author: dylanninin <dylanninin@gmail.com>
	Date:   Mon Dec 23 11:21:53 2013 +0800
	
	    initial commit
	git@ubuntu:~/repositories/web.git$ 

5 . Security

For extra precaution, you can easily restrict the 'git' user to only doing Git activities with a limited shell tool called `git-shell` that comes with Git.

	me@ubuntu:~$ sudo whereis git-shell
	git-shell: /usr/bin/git-shell /usr/bin/X11/git-shell /usr/share/man/man1/git-shell.1.gz
	me@ubuntu:~$ sudo usermod -s /usr/bin/git-shell git


Shell into the machine will get a login rejection:

	me@ubuntu:~$ sudo su - git
	fatal: Interactive git shell is not enabled.
	hint: ~/git-shell-commands should exist and have read and execute access.

Client side:

	$ ssh git@192.168.1.111

	Welcome to Ubuntu 13.04 (GNU/Linux 3.8.0-19-generic i686)
	
	 * Documentation:  https://help.ubuntu.com/
	
	  System information as of Mon Dec 23 09:20:33 HKT 2013
	
	
		New release '13.10' available.
	Run 'do-release-upgrade' to upgrade to it.
	
	Last login: Mon Dec 23 11:39:20 2013 from 192.168.1.1
	
	fatal: Interactive git shell is not enabled.
	hint: ~/git-shell-commands should exist and have read and execute access.
	Connection to 192.168.1.111 closed.

6 . GitWeb

You may want to set up a simple web-based visualizer. Git comes with a CGI script called `GitWeb` that is commonly used for this.

![git.kernel](http://www.git-scm.com/figures/18333fig0401-tn.png)

For further details, continue reading [GitWeb](http://www.git-scm.com/book/en/Git-on-the-Server-GitWeb).

##Others

* Local Repositories: Interally supported as Git is designed for distributed development.

* [GitLab](https://github.com/gitlabhq/gitlabhq): Project management and code hosting application powered by Ruby on Rails.

* [GitBucket](https://github.com/takezoe/gitbucket): The easily installable Github clone powered by Scala.

* [Github](https://github.com): Build software better, together.

##Reference

* [Git on the Server](http://www.git-scm.com/book/en/Git-on-the-Server)
* [Free Blog with Github Pages](http://dylanninin.com/blog/2013/11/02/free_blogs.html)
