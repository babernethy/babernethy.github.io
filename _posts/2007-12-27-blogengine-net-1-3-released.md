---
title: 'BlogEngine.NET 1.3 released'
date: '2007-12-27T00:05:58+00:00'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

Well, as of 7:45am I upgraded to v1.3 of BlogEngine.NET.

Staying current is the main reason, though the enhanced Windows LiveWriter support (the blog software I usually post with) is nice, and more customization abilities will also be great (full list of enhancements at the link below).

My only issues were with the database – I use SQL Server 2000 instead of the recommended SQL Server 2005 so I had to remove all the “WITH” statements from the update script (no biggie). The nice thing here was that there were no “breaking” changes in the database upgrade (just some added columns and keys/relationships) so I could migrate on the live database (after a backup).

I also had to migrate all my APP\_Data stuff and Themes stuff, but I remembered this from before.

There is a nice guide here … [http://www.nyveldt.com/blog/post/BlogEngineNET-13-Upgrade-Guide.aspx](http://www.nyveldt.com/blog/post/BlogEngineNET-13-Upgrade-Guide.aspx "http://www.nyveldt.com/blog/post/BlogEngineNET-13-Upgrade-Guide.aspx") if you are upgrading as well.

I need to update my “Talk Like a Pirate” extension soon to make sure it is ready for the fall – Extensions are easier to develop/test/install/configure now.

[BlogEngine.NET 1.3 released](http://www.dotnetblogengine.net/post/BlogEngineNET-13-released.aspx)