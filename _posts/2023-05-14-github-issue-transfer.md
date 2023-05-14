---
layout: post
title: github issue transfer
categories: [Sprint 2]
tags : [post,github]
---

GitHub 提供了 transfer issue 功能，即将 issue 从原仓库 Repository A 转移到另一个仓库 Repository B。功能在对应 issue 的右下角： 

<img width="376" alt="image" src="https://dylanninin.com/assets/images/issues/401de4e8-d02f-4290-90cd-e439687f7ba2.png">

转移时，遵循如下规则：
- issue 评论和被分配者会保留
- issue label 如果在仓库 A、B 都存在则保留（名字相同）
- issue milestone 如果在仓库 A、B 都存在则保留（名字相同+过期时间相同）
- issue 中@到的人会收到通知，提示 issue 已经转移到新仓库
- 访问 issue 的原链接会被重定向到转移后的新链接


同时对原仓库、目标仓库有一定要求
- 原仓库与目标仓库属于同一个 owner 或者 organization
- 原仓库为 public 时，目标仓库可以为 public + private
- 原仓库为 private 时，目标仓库只能为 private 

详情见原文 

- [Transferring an issue to another repository - GitHub Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/transferring-an-issue-to-another-repository)


Original Post

- Issue: [github issue transfer](https://github.com/dylanninin/dylanninin.com/issues/73)
- Created: 2023-05-14 08:51:23
- Updated: 2023-05-14 08:51:25

