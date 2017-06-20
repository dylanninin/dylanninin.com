---
layout: post
title: Install pyenv with ansible
categories: [DevOps, Python]
tags: [Ansible, Python, pyenv]
---

不知大家是如何安装 pyenv，以及 pyenv-virtualenv 的。

昨天看到 [说说我对 Python 装饰器的理解 - V2EX 后](https://www.v2ex.com/t/369581)，打算重新搭建下 Python 开发环境。之前工作中用 virtualenv + virtualenvwrapper 较多，自从 Ruby 环境管理工具从 rvm 更换到 rbenv 后，想一想也是时候使用 pyenv 了。

现在 DevOps 已全面往 ansible 迁移，对 rbenv 也熟悉，所以想着直接用 Ansible 来安装初始化；意外的是，遇到的问题还挺多（相反，使用 [ansible-rbenv](https://github.com/zzet/ansible-rbenv-role) 就没有遇到什么问题）。特此发贴，希望对大家有所帮助。

#### 使用 ansible-pyenv

GitHub 上搜索到 https://github.com/dirn/ansible-pyenv 这个项目，最近更新是 2 年以前，问题多到不可用，现在做了修复，Travis-CI 也跑通了（只是慢得无法仍受）。

目前暂未合并，要使用可以按以下步骤：

```shell
$ # 1. clone ansible-pyenv into your roles, and name dirn.pyenv
$ git clone https://github.com/dylanninin/ansible-pyenv /path/to/your/ansible/roles/dirn.pyenv
$
$ # 2. add python playbook, see python.yml
$ cat python.yml
#!/usr/bin/env ansible-playbook
---
- name: deploy python env
  hosts: all
  roles:
    # https://github.com/dirn/ansible-pyenv
    - role: dirn.pyenv
      pyenv_runcom: ~/.bashrc
      pyenv_versions:
        - 2.7.11
        - 3.5.3
      pyenv_default_versions:
        - 3.5.3
      pyenv_project_versions:
        - 3.5.3
$
$ # 3. edit your inventory, see inventory
$ cat inventory
[vagrant]
vagrant-1404
vagrant-1604

[local]
localhost ansible_connection=local
$
$ # 4. layout of current directory
$ tree -L 2
.
├── inventory
├── python.yml
└── roles
    └── dirn.pyenv

2 directories, 2 files
$ # 5. just play it with specified host, localhost as example
$ ansible-playbook python.yml -l localhost
```

这样就可以自动化安装 pyenv、pyenv-virtualenv 了。当然，事先需要安装 [Ansible](https://www.ansible.com/)。

另外，dirn.pyenv 中可能有一些不合理的地方，欢迎大家提建议。

#### 题外话

https://github.com/pyenv/pyenv 上安装 pyenv 已经足够简单，似乎不足以使用 Ansible 等自动化工具，但 Ansible 带来的变化其实非常大，主要是：

- 自动化。这可能是最明显、最可感知的收效，一两个服务器配置无所谓，一旦多起来了就会重复操作。现在可以自动化，还可以多台机器并行执行。
- 标准化。『每一片雪花都独一无二』，同样适用于服务器、开发人员；人工操作总会有差异性，规模化之后会很难维护，但『雪崩后没有一片雪花觉得自己有责任』。现在可以做到『标准化』，避免此类问题。
- 思维变化。ansible 帮助重新理解 provisioning/configuring 等，以前 手工操作、使用 shell script、使用 Dash 的 snippets 等，中间可能会遇到各类问题和中断，都不能保证服务器抵达某一种『状态』。现在可以做到了，而且是『一致性状态』。

有机会专门介绍下 Ansible。

#### 参考

- https://github.com/rbenv/rbenv
- https://github.com/pyenv/pyenv
- [Update pyenv by dylanninin · Pull Request #7 · dirn/ansible-pyenv](https://github.com/dirn/ansible-pyenv/pull/7)
- https://github.com/dylanninin/ansible-pyenv
