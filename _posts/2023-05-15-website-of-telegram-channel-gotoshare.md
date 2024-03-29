---
layout: post
title: Website of Telegram Channel gotoshare
categories: [Telegram]
tags : [post,telegram]
---

耗子叔维护的 telegram channel [程序员资源分享频道](t.me/gotoshare)，沉淀了很多有价值的分享（接近1k分享，16k订阅者），打算导出弄成一个网页版，浏览器即可访问、搜索，受众应该会更广，也能帮助到更多的开发者。

<img width="564" alt="image" src="https://dylanninin.com/assets/images/issues/5d32eef2-7349-4457-8c7e-d373b20b7aff.png">

将该频道内容网站化，添加分类、评论系统、订阅等方式，受众可能更广？
- 内容来源，官方 channel
- 内容转化为结构化数据，tg 机器人
- 内容自动发布到网站，自动化 + 编辑


---

tg 机器人识别内容之基础信息

telebot 可以自动从消息中识别出 entity，包括 url、mention 等数据结构

<img width="663" alt="image" src="https://dylanninin.com/assets/images/issues/5111ffba-7426-48c7-bb09-4b534169e90b.png">

<img width="652" alt="image" src="https://dylanninin.com/assets/images/issues/0948f1d1-c435-4a5c-936e-a97bd696e2b8.png">

参考 
- [eternnoir/pyTelegramBotAPI: Python Telegram bot api.](https://github.com/eternnoir/pyTelegramBotAPI)

---

tg 机器人识别内容之 link preview

主要是针对 url，进行内容元信息的识别，达到 telegram link previews 的效果

<img width="675" alt="image" src="https://dylanninin.com/assets/images/issues/2468cc63-9e18-44e3-9404-9d2529c89a8c.png">

元信息

- title
- date
- author
- summary
- content
- tags 
- cover
- video

等

GitHub 上找了一圈 Article Extractor 相关的开源库，功能上基本都有欠缺，跟 Telegram 的 Link Preview 无法比。其中 js 版本的试用起来效果还不错，可以先用上。

参考

- [meyt/linkpreview: Get link preview in python](https://github.com/meyt/linkpreview)
- [grangier/python-goose: Html Content / Article Extractor, web scrapping lib in Python](https://github.com/grangier/python-goose)
- [Article Extractor](https://github.com/extractus/article-extractor)

---

tg 机器人识别内容之初始化

- 如何快速导入频道中所有历史消息？
- 后续进行增量更新即可

方案 1：批量导出消息，支持输出 json+html格式，试了下最新的 macOS 客户端，没找到功能入口

- [Chat Export Tool, Better Notifications and More](https://telegram.org/blog/export-and-more)

方案 2：bot 方式，只有管理员有权限添加 bot，同时历史消息无法获取

方案 3：利用 MTProto protocol 编写 app，即可获取所有消息

- [api - Can a Telegram bot subscribe to a channel? - Stack Overflow](https://stackoverflow.com/questions/48152731/can-a-telegram-bot-subscribe-to-a-channel)
-  [MTProto protocol](https://core.telegram.org/mtproto) 
- [LonamiWebs/Telethon: Pure Python 3 MTProto API Telegram client library, for bots too!](https://github.com/LonamiWebs/Telethon)

试了下 Telethon，真好用！

---

关于 Telethon 

GitHub  主页介绍：Pure Python 3 MTProto API Telegram client library, for bots too!

得益于 Telegram MTProto API 与其开放性，开发者可以基于 MTProto 编写第三方 Telegam 客户端，当然还可以写机器人。


测试

试了下，正如官方 Telegram 客户端里 UI 显示效果一样，获取的信息很齐全，还有 webpage 字段，即 link preview 的数据，十分惊喜，这下不用额外再写 link preview 库了。

<img width="1308" alt="image" src="https://dylanninin.com/assets/images/issues/8a40aaf2-8dfc-40df-be81-610a0223d6ef.png">

PS

既然现有的一些 article extractor 很难用，将 telegram link preview 的效果封装成一个对外的 API 服务，或许是一个好主意。

参考

- [LonamiWebs/Telethon: Pure Python 3 MTProto API Telegram client library, for bots too!](https://github.com/LonamiWebs/Telethon)
- [﻿MTProto Mobile Protocol](https://core.telegram.org/mtproto)


---

关于博客系统

基本要求
- 支持 markown
- 支持嵌入视频
- 支持 tags 
- 支持搜索
- 静态话部署，如 github pages
- 支持评论
- GA 统计
- About 页面
- Archive 页面

同时支持较灵活的定制化，如布局、样式、功能等。

参考
- [Tailwind NextJS Blog](https://github.com/timlrx/tailwind-nextjs-starter-blog)


---

将程序员资源分享频道网站化，调研一番整体上可行，剩下的主要是一些细节问题，如分享资料的多样性（文件、视频、链接等），最终呈现的效果，等等，这方面估计要花更多的时间。

现在就开始行动！