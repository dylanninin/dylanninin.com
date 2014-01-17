---
layout: post
title: Gossip on Router and Push Technology
categories : [Miscellanies, Note, Resource]
tags : [Router, Push, Note, Resource]
---

这两年听得最多的字眼是Oracle，好歹也在Oracle的圈子里混过，先做[Java Web](http://dylanninin.com/blog/2013/10/09/java_resource.html)开发，紧接着做了一年多的[Oracle DBA](http://dylanninin.com/blog/2013/10/26/oracle_dba.html)，维护[Oracle EBS](http://dylanninin.com/blog/2013/10/25/oracle_ebs.html)，也当过[Oracle Linux Administrator](http://dylanninin.com/blog/2013/10/25/linux.html)。第二多的字眼是路由器，听听而已，怎么说我也是路由器圈儿里的人；各位看官请勿笑，也请严肃。

正值年末，总结随处可见，古诗云"千山鸟飞绝，都在写总结；举头望明月，低头写总结；生当做人杰，死亦写总结；远上寒山石径斜，白云深处写总结；垂死病中惊坐起，今天还要写总结。"是也。有的人为了晋升；也有的人纯属无聊。

空闲的时候整理整理资料，顺带来一点Gossips，比如我，今天就是关于路由器的--这听得第二多的字眼，花点时间，将一些信息汇总下，希望能据此引发一些思考，但因生性愚钝，我就不乱发表言论了；另外，贵司有意发展云路由，除了高可用，其中有一个难题是消息推送，为了不致傻眼，断断续续搜集了一些资料以便乘机学习。

##路由器何去何从

关于路由器，听过几个词，罗列一下：

第一弹：极路由。说起这个，首推[极路由HiWiFi](http://www.hiwifi.com/about)，据说内置穿越功能，墙里墙外可畅通无阻；另外还可以给App Store加速，顿时高大上了。但具体该如何评价，尚未有定论。知乎上有一篇[如何评价极路由HiWiFi？](http://www.zhihu.com/question/21034719)可作参考。

第二弹：某XXX也开始做路由器了。XXX大多是互联网公司，居然也涉足路由器的生产制造了，这不是华为、中兴、TP-Link等的看家本领吗？所以极客公园在提问[小米路由器独家首测：它的亮点在哪？](http://www.geekpark.net/read/view/195133?u=9147)之后，也不忘发出一丝忧思：那TP-Link怎么办？你说呢。

第三弹：云路由。[云路由](https://www.google.com.hk/#newwindow=1&q=%E4%BA%91%E8%B7%AF%E7%94%B1)开始流行，相比传统路由，云路由新增了"云管理"、"云关怀"，这不[D-Link](http://www.dlink.com.cn/)连Logo都换成一朵浮云了，见[DIR-605L 云路由](http://www.amazon.cn/D-Link-%E5%8F%8B%E8%AE%AF-DIR-605L-%E4%BA%91%E8%B7%AF%E7%94%B1/dp/B006H02MB2/ref=sr_1_1?ie=UTF8&qid=1389941778&sr=8-1&keywords=%E4%BA%91%E8%B7%AF%E7%94%B1)。当然，这效应很好，正如“云计算”、“大数据”、“互联网思维”一样，很快走红网络，跟风的跟风，烧钱的烧钱... ...

##消息推送的一点了解

因技术知识太有限，故全文摘抄[@hsabby：消息推送的一点了解](http://hsabby.iteye.com/blog/1922612)，希望从此起步开始学习。

###1、消息推送的背景
 
现在选择做消息推送的，一般都是基于移动互联网而言，各种各样的应用，想把消息推送到用户的终端设备上；之前传统的消息推送，更多的是针对Web页面而言（例如实时股票数据显示等）。无论是移动互联网还是传统的web，消息推送，都是用户被动的被接收某些消息，这类消息，和用户主动获取相比，有更好的实时性。换句话说，消息推送，更适合用户对实时性有诉求的场景，同时也适合那些用户不一定会主动获取的场景。

###2、消息推送的技术方案 

无论是移动互联网，还是传统互联网，消息推送方案的本质都是客户端告诉服务端我在这里，并持续告诉服务端，我还活着，服务端有消息时，把哪些客户端还活着查出来，并把消息推送给它们。下面大概分析一下各个方案的优略： 

1) **基于UDP的消息推送**

说实话，这个是笔者想到的第一个方案，实现简单、并且不占用连接资源。客户端发送UDP消息到server，之后定时发送心跳消息到server端维持自己在server端的状态，之后server端就可以源源不断的推送消息到client端了。这个方案最大的缺点就是UDP协议的不确定性，即数据有可能会丢失。如果我们选择的消息推送方案，对于消息的达到率没有太高的要求，我感觉这个方案也不错，尤其是server要面对大并发的要求时。 

2) **HTTP的long-polling模式**

该方式是客户端主动请求的一个升级版；不同之处就在于，long-polling模式下，如果server端当前没有消息推送，server端并不会直接返回无数据的响应，而是会维持这条连接，等到有消息时再返回响应。而客户端这边，如果发现等了一段时间，服务端还没有消息送过来，则会断开连接，随即又重新连接上，再送发送请求继续下一次消息等待。从描述中可以看出来，long-polling实际上还是poll，只不过和普通的polling相比，它比较有耐心，等待的时间long一点。这个方案，应该是当前很多消息推送架构采用的方案，算是比较成熟的实现。只不过笔者有一点不明白，反正都已经连接上了，为什么要断开呢？就继续保持住这个连接，客户端再发送一个请求不行么？（PS：后续阅读发现，可能和浏览器的实现有关；IE浏览器只有在连接断开时，才认为数据接收完整，才能读取数据；如果是自己实现的client，应该就不用断开了） 

3) **HTTP的stream模式**

个人认为该方式是long-polling模式的一个升级版，也就是前面提到的不断连接的模式；只不过，客户端只会发送一次请求，之后就是服务端源源不断的主动发送数据给client端了。需要注意的是，因为HTTP协议要求，请求和响应是一一匹配的，所以我们看见的服务端源源不断的多条通知，在后台都是一条HTTP响应消息，这个响应消息，始终处于未发送完全的状态。这就是为什么有些支持Stream模式的浏览器，小图标一直在转的原因。和上面笔者提出的长连接方案相比，stream的方案少了客户端重复发送请求消息的消耗，只不过从client端看，永远无法接收到完整的HTTP消息 

4）**WebSocket模式**

该方式彻底抛弃了HTTP协议，不再拘泥于它的一收一发，充分利用底层tcp协议的全双工能力，连接建立后，客户端和服务端都能主动的发送消息，不需要费劲心思配合收发了。显然，相比较前面的集中方案，websocket是最先进的方式。只不过当前有很多浏览器不支持。 

5）**XMPP协议**

基于XMPP的消息推送，和websocket差不多；都是维持长连接，并且server端在该长连接上主动发送消息。不同的，应该只是协议的定义。XMPP其实是一种即时消息通信协议，用来完成Server推送消息到client端，绰绰有余，换句话说，未免有点太重了。 

###3、消息推送方案的挑战

推送方案的评价标准：Safe、Stable、Save、Slim；其中最大的挑战应该是Stable和Save的矛盾；既要稳定，又要节省资源；一台服务器能同时支持多少台客户端并发应该是评价一个消息推送方案的核心指标之一。其实，大家基本方案都差不多，都是上面几种模式之一；实现上的差别，应该就是服务器端设计能力的差别了；如果管理并处理好这么多并发连接数，是push方案最大的挑战。 

###3、移动互联网推送的区别

和传统的web相比，移动互联网推送自主的权利大了很多。因为客户端可以完全自己开发，想怎么玩就怎么玩。上面讲得这些方案，基于XMPP的协议就是，应该不会有哪个浏览器会解析XMPP协议的，但是我们自己却可以开发一个客户端来接收。这也就表示，在移动互联网上实现消息推送，可选择范围其实很大。当然，既然能够自己做主了，同时也意味着挑战也来了。移动互联网和传统的web不一样，设计的时候，还需要考虑到网络资源问题。前端时间沸沸扬扬的微信收费事件，就是因为占用太多流量资源导致。如何能够设计少占流量，少耗资源的应用，就是移动推送互联网客户端的挑战。

##延伸阅读

Gossips：

* [Tim：技术晋升的误区](http://timyang.net/tech/career-promotion/)
* [极客公园：路由器](http://www.geekpark.net/tag/%E8%B7%AF%E7%94%B1%E5%99%A8)
* [极客公园：智能路由器](http://www.geekpark.net/tag/%E6%99%BA%E8%83%BD%E8%B7%AF%E7%94%B1%E5%99%A8)
* [极客公园：小米路由器独家首测：它的亮点在哪？](http://www.geekpark.net/read/view/195133?u=9147)
* [知乎：如何评价极路由HiWiFi？](http://www.zhihu.com/question/21034719)

Push：

* [Apple: Apple Push Notification Service](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html#//apple_ref/doc/uid/TP40008194-CH100-SW9)
* [知乎：iOS 和 Android 的后台推送原理各是什么？有什么区别？](http://www.zhihu.com/question/20667886)

Network:

* [Tank：Wireshark基本介绍和学习TCP三次握手](http://www.cnblogs.com/tankxiao/archive/2012/10/10/2711777.html)
* [weiqubo: TCP三次握手四次握手详解](http://blog.csdn.net/weiwangchao_/article/details/7226109)
* [weiqubo: TC/C++网络编程中的TCP保活](http://blog.csdn.net/weiwangchao_/article/details/7225338)
* [weiqubo: TTCP长连接与短连接的区别](http://blog.csdn.net/weiwangchao_/article/details/7225613)
* [weiqubo: TTCP状态迁移图浅析](http://blog.csdn.net/weiwangchao_/article/details/7225652)
* [weiqubo: TTCP四种定时器](http://blog.csdn.net/macrossdzh/article/details/5967676)
* [developerWorks: 使用异步I/O大大提高应用程序的性能](http://www.ibm.com/developerworks/cn/linux/l-async/)
* [陈硕：谈一谈网络编程学习经验](http://www.cnblogs.com/Solstice/archive/2011/06/06/2073490.html)

##维基百科

* [Pull technology](http://en.wikipedia.org/wiki/Pull_technology)
* [Push technology](http://en.wikipedia.org/wiki/Push_technology)
* [Publish-subscribe pattern](http://en.wikipedia.org/wiki/Publish/subscribe)
* [Polling](http://en.wikipedia.org/wiki/Polling_(computer_science))
* [Epoll](http://en.wikipedia.org/wiki/Epoll)
* [Select](http://en.wikipedia.org/wiki/Select_(Unix))
* [HTTP](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
* [WebSocket](http://en.wikipedia.org/wiki/WebSocket)
* [XMPP](http://en.wikipedia.org/wiki/Xmpp)

##参考

* [打喷嚏段子：2011年“总结”篇](http://uni.dapenti.com/blog/more.asp?name=xilei&id=55554)
* [hsabby：消息推送的一点了解](http://hsabby.iteye.com/blog/1922612)
