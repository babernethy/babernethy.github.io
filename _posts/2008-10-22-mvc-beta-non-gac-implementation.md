---
title: 'MVC Beta &ndash; Non-GAC implementation'
excerpt: 'Referencing the MVC beta DLLs locally, and the one property that makes it actually work.'
description: 'Referencing the MVC beta DLLs locally, and the one property that makes it actually work.'
date: '2008-10-22T00:21:01+00:00'
category: "development"
tags: ["microsoft", "development"]
redirect_from:
  - /mvc-beta-non-gac-implementation/
---

Another “geek post”, sorry.

We’ve been updating some of our MVC apps to the beta and were relying on the non-GAC implementation of MVC (i.e. we didn’t want to have to physically install the MVC .dlls on the shared dev and live servers – we’ll do this for RTW but not the betas).

However, even when we copied the DLLs locally and referenced those .dlls we were still getting a “yellow screen” error that the assemblies could not be found.

It turns out that there is a little-known property on the References themselves that is needed to accomplish the task of copying and referencing these .DLLs. Select one of the References to the .dlls (say System.Web.Routing) and look at the properties. You must set the “Copy Local” property to “True” in order to reference the local copy.

Took a little while to find this – hope to save others a little time.