---
title: 'Mouse Mischief: Multiple Mouse Support in PowerPoint with the MultiPoint Mouse SDK'
excerpt: 'Multiple mice in one PowerPoint, no programming required - a Saturday morning worth spending.'
description: 'Multiple mice in one PowerPoint, no programming required - a Saturday morning worth spending.'
date: '2010-02-06T04:15:05+00:00'
category: "tech"
tags: ["microsoft", "education", "presentations"]
redirect_from:
  - /mouse-mischief-multiple-mouse-support-in-powerpoint-with-the-multipoint-mouse-sdk/
---

I am trying to spend the early hours of Saturday morning experimenting and learning about something that interests me, with the only requirement being that is has no immediate practical value other than learning (i.e. it is not linked to work or other side projects). If it seems interesting enough, I’ll blog it. This was fun. Also, this post will be much less technical than the last set, no programming needed for this one, in fact anyone with PowerPoint will be able to take advantage and use the tools here. There may be a follow on post that will be more technical, but I wanted to alternate between tech anyone can use, and tech that really only developers could appreciate.

Back on January 18th, [Scott Hansleman](http://twitter.com/shanselman) tweeted about the new *Windows MultiPoint Mouse SDK* (link is no longer active) by teasing “Want your application to support TWO mice at a time?” This is something I remember doing waaay back with the early Macintosh computers having multiple students with different mice interacting with a single HyperCard stack. Now we can do this again, in code wit, and with a cool PowerPoint plugin called “Mouse Mischief”.

Then on January 26th woot.com had $.99 refurbished mice for sale on a Woot-Off – why would anyone buy three mice that had been returned and refurbished? For just such an experiment.

Disclaimer: This is beta technology and should only be used by people who aren’t easily frustrated and don’t expect a final/polished result. This technology will be final soon – if you want it to be more tested and full-functioned, come back in a few months and try this out.

The Mouse Micschief PowerPoint 2007 plugin can be found on [Microsoft Connect](http://connect.microsoft.com). You will need a Microsoft Live ID and register with Microsoft Connect. This is a great place to stay current on Microsoft technology and participate in beta programs. But, again, it is not for everyone.

Once installed, “Mouse Mischief” will show up as a PowerPoint ribbon control.

[![mm1](/assets/images/mm1_thumb.png "mm1")](/assets/images/mm1.png)

There will be a new item up in the tabs, which reveals the “Mouse Mischief” ribbon. Also note the “pptPlex” tab that is still up there. This is another cool PowerPoint plugin that makes your presentations use a “DeepZoom” look and feel which makes the very “Silverlighty”, but that is/was another post.

[![mm2](/assets/images/mm2_thumb.png "mm2")](/assets/images/mm2.png)

The ribbon adds some new slide types “Yes/No” and “Multiple Choice” and an important button “Play”. If you insert the new slide types and play the slides the “normal” way in PowerPoint, there will be no new functionality in the slides. If you launch the slides using the play button in the ribbon you will get the multi-mouse functionality.

![mm3](/assets/images/mm3.png "mm3")

When you first start your “Mischievous” presentation you will notice a slide you didn’t add yourself. This allows for one (or more) mice to “register” itself as the presenter/teacher (this specific tool is education oriented, but has many uses outside of education as well). If you move other mice at this point you will see multiple mice moving independently on the screen – very cool. Previous to this, if the different mice had been moved, they would all have controlled the single cursor on the screen.

![mm4](/assets/images/mm4.png "mm4")

This next screen show that the designers of this are expecting a massive number of different mice – perhaps a classroom full – we only have four (teacher/presenter and three for feedback).

[![mm5](/assets/images/mm5_thumb.png "mm5")](/assets/images/mm5.png)

When we get to a screen that has one of the Yes/No or Multiple Choice questions, then the different mice become active and they get to pick one of the answers. When everyone has answered, or the teacher/presenter chooses to move on, we get a summary screen.

![mm6](/assets/images/mm6.png "mm6")

This provides instant feedback for presenters and/or checks for comprehension from the audience. The multiple choice slide has other options.

[![mm7](/assets/images/mm7_thumb.png "mm7")](/assets/images/mm7.png)

Notice that only the presenter/teacher mouse has the ability at the bottom to move the presentation to the next or previous slide, or to end the interaction early. In addition to giving feedback on open-ended questions like this one, you can also pre-pick the “correct” answer on the slide and show how many had the correct answer, and who was first to respond.

[![mm9](/assets/images/mm9_thumb.png "mm9")](/assets/images/mm9.png)

When the presentation is complete, you need to end the presentation with the presenter/teacher mouse (i.e. audience/class members can’t end or control the flow of the presentation.

![mm8](/assets/images/mm8.png "mm8")

The ability to use multiple mice on once screen is great – and this “Mouse Mischief” plug-in tool for PowerPoint gets you started right away.

In Part 2 of this series, I will show how a developer can add multi-mouse support to their own applications using the MultiPoint Mouse SDK – if you want to get started early, check out the *MultiPoint Mouse SDK Developer* (link is no longer active) Info page.