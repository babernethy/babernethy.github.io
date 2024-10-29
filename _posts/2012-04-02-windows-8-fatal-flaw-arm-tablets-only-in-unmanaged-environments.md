---
title: 'Windows 8 Fatal Flaw &#8211; ARM Tablets only in Unmanaged Environments?'
date: '2012-04-02T10:01:52+00:00'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

I know that many that have been following the development and previews of Windows 8 have many opinions about the new operating system. And while many are very positive, some have people quite concerned (e.g. the “Lack of the Start Menu” or “Metro as the default interface / can’t disable”). But I think the fatal flaw from a business/corporate perspective may probably be the fact that the tablet/mobile/ARM versions may not be able to be centrally managed or secured by joining a domain.

I had heard rumors/tweets about this but wanted to “get it from the source” and I did find a link to the [Windows 8 Consumer Preview Product Guide for Business](http://www.microsoft.com/download/en/details.aspx?id=28970). This 16-page guide is worth a read if you are interested in such things.

I was pleased to read on Page 4 in the “Line-of-business app development” section that …

> “Enterprise developers can create Windows 8 apps that are critical for their business and feel confident that they maintain control over the deployment and access to their apps. Businesses can load their Windows 8 apps onto their domain-joined PCs running Windows 8 Consumer Preview, bypassing the Windows Store. An app that is created in an enterprise can stay within the corporate firewall and be centrally managed, updated, and distributed.”

This is very good. When you have to manage and support 10, 100, 1000, or more computers, it is important to be able to “manage, update, and distribute” to them easily and hopefully at the level of the operating system.

A little later, Page 6 “Choice in form factors” we learn …..

> “32-bit and 64-bit tablet computers that run Windows 8 can also integrate into your existing management infrastructure. These tablets can be managed in the same way as traditional desktops and laptops, so IT professionals can ensure that these devices can easily be added to any business.”

Again, positive, and getting cautiously optimistic, so it looks like tablets are in on the management and can be “easily be added to any business”.

But, only a paragraph later ….

> “ARM-based tablets running Windows 8 are ideal for workers who are constantly on the go and need a long-lasting battery. ARM-based tablets use less power than 32-bit and 64-bit devices and workers can rely on the extended uptime of these devices. Although the ARMbased version of Windows does not include the same manageability features that are in 32-bit and 64-bit versions, businesses can use these power-saving devices in unmanaged environments.”

What? The “ARM-based tablets” (i.e. the lightweight mobile devices, ala the “iPads” running Windows 8) for “workers who are constantly on the go” … yes … yes … but this “version of Windows does not include the same manageability features” but “businesses can use these power-saving devices in unmanaged environments”. What?

So these can be used, just without the capability to secure, deploy, or manage the devices or applications on the devices? Um. So. What?

People want their mobile devices; people want their tablets; people want an iPad but many are waiting to see, in a corporate environment, what Window 8 may deliver in this area. But if they wait it out, and loose all of the “manageability”, “security”, “updates/distribution/apps”, then the biggest value, in my opinion, of these devices may be lost. Many business features that rely on role-based security, managed environments, compliance requirements (e.g. PCI, PII, HIPAA), rely on these features.

While third-parties may step in and fill this gap, as they have started to do on the iPad and Android tablets, to have these functions not be part of the core functionality of Windows 8 will be a major issue. Tablets need to be able to be centrally staged, secured, and have software/patches deployed and updated, in order to meet many of these needs. Hopefully enough people will ask questions about this to encourage a change on this direction.