---
title: 'MVC Beta &ndash; Non-GAC implementation'
date: '2008-10-22T00:21:01+00:00'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

Another “geek post”, sorry.

We’ve been updating some of our MVC apps to the beta and were relying on the non-GAC implementation of MVC (i.e. we didn’t want to have to physically install the MVC .dlls on the shared dev and live servers – we’ll do this for RTW but not the betas).

However, even when we copied the DLLs locally and referenced those .dlls we were still getting a “yellow screen” error that the assemblies could not be found.

It turns out that there is a little-known property on the References themselves that is needed to accomplish the task of copying and referencing these .DLLs. Select one of the References to the .dlls (say System.Web.Routing) and look at the properties. You must set the “Copy Local” property to “True” in order to reference the local copy.

Took a little while to find this – hope to save others a little time.