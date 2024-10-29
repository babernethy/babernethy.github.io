---
title: 'Silverlight Proof-of-Concept &ndash; Top 10 Questions to Be Answered'
date: '2008-07-07T07:27:04+00:00'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

I am getting a chance to do something I’ve wanted to do for a while – that is, get paid to do some Silverlight development.

That being said there is a lot to prove to our customer and ourselves that Silverlight is the right choice, and is at the right level of development, to be used as the platform for running day-to-day operations for a multi-million dollar business. So we are undertaking a process to evaluate Silverlight and prove out some of the “unknowns” of Silverlight.

Other options are out there for the User Interface for this application:

(1) A “fat” installed app (WPF or WinForm) – the current app is a fat Windows 3.11/95-looking application with decent performance (especially when it was designed on PC’s with 1/10 the power of today’s applications). But this app will be widely deployed (50+ sites) and tech support is limited and costly to overhead. Web applications, or at least web-deployed applications, are preferred.

(2) An Ajax-enabled Web Site. There is a lot of “magic” you can do with a little Ajax and some custom Javascript coding. But, having done several of these sites, you end up feeling that you are making a web page do something “unnatural” (i.e. something it wasn’t designed to do). And supporting and debugging these applications can be complicated. Plus there is an inherent performance issue with even the best designed web application. This is especially true when coming from a very performant Windows application to a new browser-based application.

(3) Flash/Flex. In addition to this Silverlight POC, at CQL we are working on a Flash and a Flex-based application from two other companies. We’re updating a Flash-based application that gets a lot of XML-based data from simple web services, and we’re writing the services to support a modern site-wide Flex-based application. There are other RIA options out there, and the two different design firms have much more experience with the Adobe products than Silverlight. To their credit they have heard of and have used the basic Silverlight tools already, but never anything “production.” So we need to prove to our clients and our design partners that this is a good idea.

So, what needs to be proven and how are we going to go about proving it out.

## Here is the start of the list – this will build over the next few weeks.

1\) Automated testing – how to test the front-end Silverlight controls using automated testing tools

2\) Web Service calls / Databinding – using secure web service calls for data routines. Pull-type calls for common actions/methods. Also Publish/Subscribe type services that could push important data to subscribed controls. How to handle disconnected concurrency issues?

3\) Security / Roles – encrypted traffic. Working in the same security context as the containing web application (i.e. login, roles, etc.)

4\) Dynamic Control Loading – app needs to perform very well and should only load the components that are needed at any one time.

5\) Keyboard/Keystroke/Hot-Keys – many of the current functions of the system have assigned key shortcuts than enable staff members to quickly access common features. Can this be reproduced in Silverlight?

6\) Stress/Load Testing – How does the load of an application that is mainly web service based differ from that of a get/post HTML web application? Many small messages vs. less frequent bigger messages.

7\) Real-world ability to work with designers – We’ve all seen the PowerPoint slides showing how easy it is to work with XAML between developers and designers. Is it true? Does it work in real life?

8\) Uploading a file – can it be done in Silverlight or will we need some Ajax/Web Page interaction?

9\) Drag-and-Drop – part of the app is a scheduling calendar – can appointments be rescheduled via drag-and-drop?

10\) Controls – are there enough now for what we need in beta 2? Are any third-party controls worth using/buying? Can we do common data-entry validation (e.g. masked-edit textbox)?