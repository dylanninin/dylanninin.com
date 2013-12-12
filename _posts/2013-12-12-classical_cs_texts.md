---
layout: post
title: Classical CS Texts
categories: [Theory, Resource]
tags: [Theory, Resource]
---

从[g9yuayon](http://blog.csdn.net/g9yuayon)上偶然看到的一篇博客，因为个人理论很薄弱，所以有意地去瞅瞅，仅看过一两篇，惭愧。刚看了一遍[No Silver Bullet: Essence and Accidents of Software Engineering](http://www-inst.eecs.berkeley.edu/~maratb/readings/NoSilverBullet.html)，你懂的，相见恨晚，g9说“地球人都知道。不用俺多嘴了”，大学时确实听说过，但不记得自己有认真看过；所以你懂得，继续还债。

全文转载，希望抽时间一一拜读；另外，以正常的上网方式，部分链接似乎已经找不到了，稍后顺手汇总备份一份到Google Drive(HTML转PDF)，地址见文末。

##计算机科学经典论文

从Jao的[Programming Musing](http://jaortega.wordpress.com/) 看到的：[Babar Kazar](http://www.zafar.se/bkz/Articles/ClassicCompScienceTexts)整理了一堆经典论文。Jao强烈建议每个严肃的程序员读每篇论文，说它们都或多或少有意思。粗粗扫了一下，很多论文都没读过。挑了些俺多少知道一点的介绍。

1 . [An axiomatic basis for computer programming](http://www.spatial.maine.edu/~worboys/processes/hoare%20axiomatic.pdf) C. A. R. Hoare

Tony Hoare名下的公理化语义（Axiomatic Semantics）。著名的Hoare Triples, P{C}Q, 就是从这里来的。论文不长，双列6页。前辈们就是这样的，6页纸就能开宗立派。不像俺，6页纸连介绍部分都写不周全。哪位老大想知道怎么证明程序正确。前置条件，不变条件，后置条件的妙用，可以用这篇论文开牙。

2 . [Communicating Sequential Processes (CSP)](http://www.usingcsp.com/) C. A. R. Hoare

Hoare, 又见Hoare。其实也正常。牛人之牛，就在于成就深广。链接的文档应该不算论文，而算专著。260页。从1985年推出到现在20多年过去，这本书的引用率在CS历史上排名第三，可见其影响之深。对并发编程有强烈兴趣的老大可以去钻研一把。我没读过。

3 . [Call-by-name, call-by-value, and the lambda calculus](http://homepages.inf.ed.ac.uk/gdp/publications/cbn_cbv_lambda.pdf) Gordon Plotkin

没读过。只见LtU介绍过。Gordon老大这篇论文的要点之一是要想顺利地对程序进行推导，就需要有合适的lambda理论。想深入理解call-by-name，call-by-value，和lambda算子的老大们可以上了。

4 . [Towards a theory of type structure](ftp://ftp.cs.cmu.edu/user/jcr/theotypestr.pdf) John C. Reynolds

号称经典中的经典。不过也没读过。类型系统一直是编程语言研发的热点，也是非常有趣的方向――类型系统的编程好比让机器证明一系列定理。Reynolds在论文里讨论了什么才是正确的类型结构，和句法正确必须独立于任何具体的类型表达形式，并且给出了带类型的lambda算子的一种扩展，允许他描述用户自定义类型和多态函数。满篇公式，有勇气去读的老大要有心理准备。

5 · [Structured Programming with go to Statements](http://pplab.snu.ac.kr/courses/adv_pl05/papers/p261-knuth.pdf) Donald E. Knuth

这篇论文详细结构化编程时讨论了什么时候用goto，什么时候不用goto。高爷爷精细务实的态度非常值得学习。高老太爷用了一辈子goto(MIX和MMIX程序里没了Goto怎么玩儿得转嗫？)，岂能轻易被Dijkstra对goto的批评吓退？他仔细探讨了几种不同的程序，考察goto用在那些程序里的利弊。最后得出结论，goto在某些程序里仍然高效实用。虽然论文是30年前的，但里面的分析手法和利用goto的优化技术至今可用。

6 · [Definitional interpreters for higher-order programming languages](ftp://ftp.cs.cmu.edu/user/jcr/defint.ps.gz) John C. Reynolds

这篇文章俺喜欢。”Metacircular”这个性感的概念就是在这篇论文里首次提出的。想深入了解用一门语言写出的解释器定义这门语言自身的神奇理念，这篇论文是必读材料。有兴趣的老大可以先读SICP的第四章。 

![hands](http://p.blog.csdn.net/images/p_blog_csdn_net/g9yuayon/77d4acdbcd854554a4eb504ed337f317.png)

7 · [An APL Machine 1970](http://www.slac.stanford.edu/pubs/slacreports/slac-r-114.html) Philip S. Abrams

只知道APL是门有历史意义的语言。顺便说一句，APL这个名字太土了。A Programming Language ＝＝APL。象什么话嘛。

8 · [The Anatomy of a Large-Scale Hypertextual Web Search Engine](http://www-db.stanford.edu/pub/papers/google.pdf) Sergey Brin and Lawrence Page

网络是个大的矩阵(transition probability matrix of Markov Chain)。网页的声誉(page rank)就是这个巨大矩阵的principle eigenvector的某个元素。嗯，反正我只有佩服的份儿。

9 · [No Silver Bullet: Essence and Accidents of Software Engineering](http://www-inst.eecs.berkeley.edu/~maratb/readings/NoSilverBullet.html) Frederic P. Brooks, Jr.

地球银都知道。不用俺多嘴了。

10 · [A Mathematical Theory of Communication](http://www.unil.ch/webdav/site/ling/shared/ElementStatText/Shannon1948.pdf) Claude Shannon

Bell实验室当年辉煌一时。出了名的叫人做A，结果发明了B。香农老大就是其中杰出代表。香农进了Bell实验室后，居然没人吩咐他干嘛。香农老大转念一想，自己喜欢数学，Bell的生意尽在通讯，干嘛不看看把数学应用到通讯上有什么结果呢？于是1948年这篇论文问世乐。搞通讯的人崩溃乐。现代信息理论就诞生乐。

11 · [Bayesian Networks without Tears](http://www.cs.ubc.ca/~murphyk/Bayes/Charniak_91.pdf)

贝叶斯理论热了好几年了。估计还会继续热下去。现在信息越来越多，我们已经审美疲劳。大家渴望的不是信息，而是知识。靠个人的力量把信息提炼成知识太慢，我们需要机器的帮忙。机器学习不热都难，而贝叶斯理论在机器学习里有很好的应用。这篇文章行为浅显，可以轻松读完。对了，那个人人喝骂的微软回形针的智能引擎就是用贝叶斯网络实现的。

12 · [A Universal Algorithm for Sequential Data Compression](http://www.stanford.edu/class/ee398a/resources/ziv:77-SDC.pdf)

没读过。无耻地找个借口：我们系开信息理论课的时候，俺刚好毕业。

13 · [A Relational Model of Data for Large Shared Data Banks 1970](http://www.cs.duke.edu/~junyang/cps216/papers/codd-1970.pdf) Edgar F. Codd

没有关系代数，人类将会怎样？Codd划时代的论文奠定了现代数据库的基础。嘿嘿，其实俺也没有读过这篇论文。顺便说一句，现在的ORM试图把data schema和对象系统映射起来。问题是，data schema只是对关系的一种表达方式而已，还和具体的系统实现有关。也许把对象间的结构和关系映射起来才是正道。

14 · [Let's Build a Compiler 1988-1995](http://compilers.iecc.com/crenshaw/)

教你一步一步写出一坨编译器。不算论文吧。一篇相当不错的指南。

15 · [Gauging Similarity via N-Grams: Language-Independent Sorting... Marc Damashek](http://gnowledge.sourceforge.net/damashek-ngrams.pdf)

第一次听说

16 · [Worse Is Better](http://www.dreamsongs.com/WorseIsBetter.html) Richard P. Gabriel

网上脍炙人口的文章。很有教育意义。简单说，worse is better包括下面几点：

--简单：设计要简单。但如果接口和实现不能两全，追求实现的简单。文章里给出的Unix vs Multics的例子非常有意思。

--正确：程序必须在所有可见的方面正确。其它地方，如果简单和正确不能两全，追求简单。

--一致性：程序不能太不一致。但为了简单，可以在少数地方不一致。

-- 完备性：程序应该尽可能照顾到重要的地方，但是不能牺牲简洁。

强烈推荐。

17 · [Hints on Programming Language Design](http://www.cs.berkeley.edu/~necula/cs263/handouts/hoarehints.pdf) C.A.R. Hoare

Hoare对设计语言的经验总结。这些经验至今有效。文章很容易读，读后绝对增长程序设计的功力。

18 · [Why Functional Programming Matters](http://www.math.chalmers.se/~rjmh/Papers/whyfp.pdf) John Hughes

为普通程序员准备的大餐，所以写得通俗。没有公式，也没有拗口的术语。着重展示了Fold和Map的强大抽象能力。不由想到我在大学里修的一门课，编程语言。课是好课，老师是一流老师。课上我们学习了浅显的程序语言理论，重点学习了函数编程（用Common Lisp）和逻辑编程（用Prolog）。这门课彻底改变我对编程的理解，明白了imperative programming和OO programming外还有精彩世界。至今想来都觉得幸运。那门课的作业也很有意思，实现一个驻留内存的数据库，支持关系代数里的常见操作。

19 · [On the Expressive Power of Programming Languages](http://www.ccs.neu.edu/scheme/pubs/scp91-felleisen.ps.gz) Matthias Felleisen

没读过。待读。

20 · [The Early History Of Smalltalk](http://www.metaobject.com/papers/Smallhistory.pdf) Alan Kay

还有什么好说的呢？Alan Kay这个名字说明一切。30年前Alan Kay就做出来Smalltalk，现在想来仍然让人惊叹。引一段文章Alan Kay评述Smalltalk的话：

> In computer terms, Smalltalk is a recursion on the notion of computer itself. Instead of dividing "computer stuff" into things each less strong than the whole--like data structures, procedures, and functions which are the usual paraphernalia of programming languages--each Smalltalk object is a recursion on the entire possibilities of the computer. Thus its semantics are a bit like having thousands and thousands of computer all hooked together by a very fast network. Questions of concrete representation can thus be postponed almost indefinitely because we are mainly concerned that the computers behave appropriately, and are interested in particular strategies only if the results are off or come back too slowly.

21 · [Computer Programming as an Art](http://fresh.homeunix.net/~luke/misc/knuth-turingaward.pdf) Donald E. Knuth

高老太爷在1974年图灵奖仪式上的致词。真是顶尖geek的风范啊。高太爷在文章里解释了问什么他的书取名为《编程的艺术》。明显他对人们谈到编程时把科学置于艺术之上很不了然。高爷爷追溯“艺术”的词源，说艺术的本意就是技能，也是技术和技巧两次的起源。从这里开始，他开始讨论艺术和科学的关联，讨论艺术在编程里的表现形式和意义。用他的话说，他作为教育者和作者的毕生目标就是叫人写美妙的程序。读起来让人心潮彭湃的说。

22 · [The next 700 programming languages](http://www.cs.utah.edu/~wilson/compilers/old/papers/p157-landin.pdf) Peter J. Landin

42年前的论文，影响深远。Peter在论文里描述的函数语言ISWIM（If You See What I Mean）现在没有几个人知道了。但他对lambda算子的推崇和对函数语言的论述影响了后来的函数语言设计。

23 · [Recursive Functions of Symbolic Expressions and their Computation by Machine (Part I) 1960](http://www-formal.stanford.edu/jmc/recursive.html) John McCarthy

47年前提出LISP的那篇著名论文。没读过。动态类型检查，Garbage Collection, 递归函数，S-expression, 程序及数据。。。可谓贡献辉煌。

24 · [FORTH - A Language for Interactive Computing](http://www.cs.wisc.edu/~bolo/shipyard/4th_1970/4th_1970.html) Charles H.Moore 

只知道Forth是一门stack oriented的编程语言，影响了后来的一些语言，比如CAT。其它的就不知道了。

25 · [Teach Yourself Programming in Ten Years 2001](http://www.norvig.com/21-days.html) Peter Norvig

大牛之所以为大牛，原因之一就是目光深远。这篇文章批评那些《24秒学会C＋＋》之类教材的无稽，讨论了学习编程，从菜鸟变成鲲鹏的方法。中文版已经传得满世界都是，赶快找来看吧。Peter Norvig的网站上还有很多高质量的文章。强烈推荐一读。

26 · [The Definition and Implementation of a Computer Language based on constraints](ftp://publications.ai.mit.edu/ai-publications/500-999/AITR-595.ps) Guy Lewis Steele Jr.

好像是Guy Steels的硕士论文。没读过。

27 · [Growing a Language](http://www.cs.umbc.edu/331/resources/papers/gls-grow-lang.pdf) Guy Lewis Steele Jr.

好文！G老大在OOPSLA 98上的主题演讲。G老大主张应该采取渐进的方式设计一门可以被自由扩展的语言（LISP圈子里的牛人们多半都持这种观点吧？）。这篇演讲稿针对该观点做了精练地论述。说起进化的观点，可以参看另外一篇好文章，SICP作者之一，Jay Sussman的[近作](http://swiss.csail.mit.edu/classes/symbolic/spring07/readings/robust-systems.pdf)。

28 · [Epigrams on Programming](http://www-pu.informatik.uni-tuebingen.de/users/klaeren/epigrams.html) Alan J. Perlis

A老大发表的一系列关于编程的格言。幽默而深刻。每读必笑。笑后必哭。嗯嗯嗯，夸张一下。不要当真。

29 · [The Complexity of Theorem Proving Procedures](http://www.cs.helsinki.fi/u/gionis/cc05/cook.pdf) Stephen A. Cook

仙风道骨的库克爷爷的成名作。这篇文章一出，好比有人在加州荒漠里发现第一块狗头金，立刻掀起开发加州的狂潮。计算复杂性理论迅速遍地开花。相比这篇论文开创性的贡献，库克因此得到图灵奖不过小小点缀。NP-Complete在这篇论文里被严格定义。更重要的是，库克证明了第一个NP-Complete的问题，SAT(Boolean Satisfiability Problem)。有了SAT，再加上折磨了无数学生的Polynomial Reducibility，无数的NPC问题就出现乐。。。别看俺在这里唾沫横飞，当年做有关计算理论的证明题还是相当吃力的，没有少熬夜。奇怪的是，某一天我给同学讲解我的解法，NPC的相关定义突然变得清晰起来。当初让我绞尽脑汁的证明竟然变得相当机械。后来知道，给人讲解（包括写作）是非常有效地学习方法。怀着备课的目标读文章，假设自己给别人讲解正在读的文章，有助快速理解所读内容。SAT的证明相当复杂，我反正没有耐心读完。

30 · [Steps Toward Artificial Intelligence](http://web.media.mit.edu/~minsky/papers/steps.html) Marvin Minsky

AI的奠基论文。不过我没读过。

31 · [The Original 'Lambda Papers'](http://library.readscheme.org/page1.html) Guy Steele and Gerald Sussman

一系列讲解lambda算子和scheme设计的经典论文。学scheme时读过，对理解scheme的设计理念很有帮助。

32 · [The UNIX Time-Sharing System](http://cm.bell-labs.com/cm/cs/who/dmr/cacm.html) Dennis Ritchie and Ken Thompson

作者不用介绍了吧？这篇文章里介绍的Unix特性早为人熟知。不过第八部分(VIII Perspective)讨论了作者的设计理念，仍然值得一读。

Reference:

* [g9：计算机科学经典论文](http://blog.csdn.net/g9yuayon/article/details/1512851)
