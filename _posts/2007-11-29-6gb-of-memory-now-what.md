---
title: '6Gb of memory &#8211; Now What?!?'
date: '2007-11-29T15:11:49+00:00'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

Thanks to Chris for the heads-up on the $50 (after rebate) “cyber-Monday” memory deal at NewEgg – arrives on Thursday, can’t beat that.

[![6gig](http://www.bruceabernethy.com/wp-content/uploads/WindowsLiveWriter/6Gbofmemorynowwhat_13BE3/6gig_thumb.png)](http://www.bruceabernethy.com/wp-content/uploads/WindowsLiveWriter/6Gbofmemorynowwhat_13BE3/6gig_2.png)

2 2Gb sticks brings me to 6Gb.

[![vista_sidebar](http://www.bruceabernethy.com/wp-content/uploads/WindowsLiveWriter/6Gbofmemorynowwhat_13BE3/vista_sidebar_thumb.png)](http://www.bruceabernethy.com/wp-content/uploads/WindowsLiveWriter/6Gbofmemorynowwhat_13BE3/vista_sidebar_2.png) It is strange how much pressure I feel now having a system I could only dream about even 3-4 years ago. It is a lot of responsibility having so much raw computing power.

I spend the majority of the time reading and writing which my Windows 98 computer did just fine with an old Pentium 3.

To make it worse I have the Vista Sidebar gadget going that monitors CPU performance. Most of the time I have one of the four guys chugging along or spiking for a second or two while the other three take a nap. They seem to spread out the work pretty well sometimes, but other times a couple team up on a task and leave the others out of the game.

It’s weird (and cool) that today when I’m wondering what to do with the extra power, Microsoft announces their new [Parallel Extension to the .NET Framework](http://blogs.msdn.com/somasegar/archive/2007/11/29/parallel-extensions-to-the-net-fx-ctp.aspx). This enables programmers to explicitly design and code for extra processing power. There are parallel ways to do loops (for/foreach), parallel data access (with LINQ even), and more.

I downloaded the samples and started playing with them tonight, and they are very cool. The examples are classic CPU-intensive tasks like matrix-math, ray-tracing, searching, sorting, solving Soduku puzzles (some are very hard).

[![parallel](http://www.bruceabernethy.com/wp-content/uploads/WindowsLiveWriter/6Gbofmemorynowwhat_13BE3/parallel_thumb.png)](http://www.bruceabernethy.com/wp-content/uploads/WindowsLiveWriter/6Gbofmemorynowwhat_13BE3/parallel_2.png)

It is satisfying to see all the processors spike and the memory get eaten up (still haven’t crossed the 4Gb threshold yet. Tonight was all about making processors “dance”.

| [![processor_dance](http://www.bruceabernethy.com/wp-content/uploads/WindowsLiveWriter/6Gbofmemorynowwhat_13BE3/processor_dance_thumb.png)](http://www.bruceabernethy.com/wp-content/uploads/WindowsLiveWriter/6Gbofmemorynowwhat_13BE3/processor_dance_2.png) | I’m guessing the processor in the bottom-right had the primary application thread in it and the others were open for the parallel processing. |
|---|---|

I have a project right now that this would be terribly useful on, but the OS and hardware are already in place – lowly 2Gb dual-core server 🙂 – and you need .NET Framework 3.5 (plus these CTP (i.e. pre-release) extensions) to make it work. Maybe next time.

Now I just need something practical (not that computing pi to 1,000,000 places isn’t interesting) to code for practice – any ideas? I know I can always help fold proteins and search for hidden space aliens, but I want to create something to test the technology and learn it for myself.