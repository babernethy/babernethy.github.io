---
title: 'BlogEngine.NET 1.3 released'
excerpt: 'Upgrading the blog to 1.3, and the one place SQL Server 2000 made me work for it.'
description: 'Upgrading the blog to 1.3, and the one place SQL Server 2000 made me work for it.'
date: '2007-12-27T00:05:58+00:00'
category: "blog"
tags: ["blog", "microsoft"]
redirect_from:
  - /blogengine-net-1-3-released/
---

Well, as of 7:45am I upgraded to v1.3 of BlogEngine.NET.

Staying current is the main reason, though the enhanced Windows LiveWriter support (the blog software I usually post with) is nice, and more customization abilities will also be great (full list of enhancements at the link below).

My only issues were with the database – I use SQL Server 2000 instead of the recommended SQL Server 2005 so I had to remove all the “WITH” statements from the update script (no biggie). The nice thing here was that there were no “breaking” changes in the database upgrade (just some added columns and keys/relationships) so I could migrate on the live database (after a backup).

I also had to migrate all my APP\_Data stuff and Themes stuff, but I remembered this from before.

There is a nice guide here … [http://www.nyveldt.com/blog/post/BlogEngineNET-13-Upgrade-Guide.aspx](http://www.nyveldt.com/blog/post/BlogEngineNET-13-Upgrade-Guide.aspx "http://www.nyveldt.com/blog/post/BlogEngineNET-13-Upgrade-Guide.aspx") if you are upgrading as well.

I need to update my “Talk Like a Pirate” extension soon to make sure it is ready for the fall – Extensions are easier to develop/test/install/configure now.

*BlogEngine.NET 1.3 released* (link is no longer active)