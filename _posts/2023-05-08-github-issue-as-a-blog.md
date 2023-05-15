---
layout: post
title: GitHub Issue as a Blog
categories: [Post]
tags : [post,github]
---

如何使用 GitHub Issues 作为博客，这里介绍一种简单的实现。

--- 
基本概念
- issue：每个 issue 即是一篇博文
- labels：对应博文的 tags
- milestone：对应博文的 categories

主要场景，如文章的发布、更新、删除都可以完成，操作上十分方便
- 写一篇文章时，可以利用 GitHub Issues 强大的编辑功能，支持 Markdown，所见即所得
- 发布文章时，2 步：
    - 1）添加的 label 为 `post`；带有 `post` 标签的 issues 才会导出为博客。
    - 2）关闭 issue，开始博文发布流程。
- 更新文章时，3 步
    - 1）重新打开 issue
    - 2）编辑对应的 issue
    - 3）关闭 issue
- 删除文章时，3 步
    - 1）重新打开 issue
    - 2）移除标签 `post`  
    - 3）关闭 issue

---

实现原理

<img width="1021" alt="image" src="https://dylanninin.com/assets/images/issues/236713780-719c8b09-5e2e-41cf-8818-41d538601659.png.png">

GitHub Pages：[https://pages.github.com/](https://pages.github.com/)，GitHub 提供的静态文件托管服务，开源仓库可以免费使用。

GitHub Actions：[Actions Doc](https://docs.github.com/en/actions)，GitHub 提供的 CI 工具，也是最好用的 CI 工具，开原仓库也可以免费使用。

导出 issue 为文章：[Workflow](https://github.com/dylanninin/dylanninin.github.com/blob/master/.github/workflows/build.yml)，稍微写点[代码](https://github.com/dylanninin/dylanninin.github.com/blob/master/.github/issue.py)就行。

GitHub  仓库中做一些如下设置
- GH_PAT：即 Github Personal Access Token，使用方式见 [Creating a personal access token - GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- GH_REPO：即 issues  所在仓库名，如 [dylanninin/dylanninin.com](https://github.com/dylanninin/dylanninin.com)
设置如图
<img width="1177" alt="image" src="https://dylanninin.com/assets/images/issues/236716380-f5387ea4-67f0-43e4-adbf-ceac35f2a947.png.png">

---

为什么要这样做？

静态博客托管在 GitHub Pages，要发布/更新文章，原始的方式就像编写代码一样编写 markdown，同时需要 commit 之后才能发布，过程较为麻烦；如果遇到一些显示样式问题，或者要重新编辑，也会很繁琐。

GitHub Issues 功能强大，同时提供所见即所得的 markdown 编写体验，能自动保存，还可以分段编辑，使用起来十分方便、友好， 这就是一个天然的编辑器。

同时 GitHub API 非常完善，比如 [Introduction — PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html)，做自动化发布非常容易。

基于 GitHub 提供的各项服务，就可以得到一个既能静态托管、又能所见即所得的编辑、还能提供 API 的博客了，当然还可以多人协同写作。



这篇文章，就是使用 GitHub Issues 作为博客，[原文](https://github.com/dylanninin/dylanninin.github.com/issues/72)。

<img width="1279" alt="image" src="https://dylanninin.com/assets/images/issues/236716094-f06c6fc5-1b60-4ead-a86d-aa1a11050424.png.png">


