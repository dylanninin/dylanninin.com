---
layout: post
title: WeChat Favorite Exporter
categories: [WeChat]
tags : [post,wechat]
---

微信里导出图文消息的现状：微信导出图文消息时，先多选消息收藏，后导出笔记，最后复制时图片会全部丢失。

难道只能人工一条一条的复制、黏贴吗？对于日常在微信运营、编辑的重度用户来说十分不便。

如下图。

<img width="506" alt="image" src="https://dylanninin.com/assets/images/issues/53e01491-1cac-4566-9ef1-c374b6831949.png">

对于非文本的消息类型，如图片、视屏、文件均会出现类似情况，或图片丢失，或视屏比例变形。


解决方案

除了人工一条条复制、黏贴，技术上有没有自动化工具，提高效率？

1. 微信接口相关的开发工具，要么有些不能用了，要么就是用长了会被提醒封号，程序上要用起来还是有很高门槛的。具体见 [微信接口开发工具](https://dylanninin.com/blog/2023/05/07/wechat-api-libraries.html)，个人均已测试过。

2. 第三方工具性产品，要么功能上不满足需求，要么会泄露个人隐私，因为大概率他们会存档你转发的消息内容。
- 小程序，如聊天文件快速保存，功能上不满足需求
- [Cubox - 微信转发收藏](https://help.cubox.pro/save/ecf6/) 

3. 开源工具，[GitHub 上搜索"微信导出"](https://github.com/search?q=%E5%BE%AE%E4%BF%A1%E5%AF%BC%E5%87%BA&type=repositories)，从数量上看需求还挺多，但各种微信版本不一样，逆向坑也多，很多都年久失修了。

4. 自己写一个？不是不可能，满足需求的同时，还要保护用户隐私，不存档任何聊天数据。