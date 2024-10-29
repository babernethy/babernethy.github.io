---
title: 'Rebooting the blog in WordPress'
date: '2011-06-30T18:21:49+00:00'
dsq_thread_id:
    - '448831577'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
image: /wp-content/uploads/2011/07/be2wp.png
---

I had a goal to get my blog up and running again by the end of June – so I figured I’d get a head start today ![Smile](http://www.agileeducation.net/myblog/wp-content/uploads/2011/06/wlEmoticon-smile.png)

I’ve been away from blogging for a while – first because of a major technical snafu at my previous hosting provider (WebHost4Life – ironic name), but then because of my lack of time and focus regarding blog posts. Recently there has been so much going on and nowhere to blog, so I decided to start blogging again.

I’ve opted for WordPress this time mainly for two reasons: 1) the previously mentioned “time factor” – WordPress is a two-click install and will automatically update itself when new versions come out (as 3.1.4 did today to handle some security issues), and 2) there are a bunch of really powerful (and mostly free) plugins and themes than those available in the BlogEngine.NET community. I still operate a few BlogEngine.NET blogs for groups and clients, and where tighter control and easy customization is needed I’ll still go to BlogEngine for that (they have a shiny new version too). But for my personal blog I am going with WordPress so I can (hopefully) focus more on the content and less on keeping things up to date and up and running.

**UPDATE:**

The migration is going well – first major hurdles are taken care of.

I have really liked Windows Live Writer as a blogging platform so I wanted to try to continue using that with WordPress. Got that set up and posted some initial posts for testing – worked well.

Found a helpful resource here: <http://merill.net/2009/01/migrating-from-blogenginenet-to-wordpress/> which covers the major points in migration from BlogEngine.NET to WordPress.

\#1 Exporting the old blog posts

- Exported using the BlogML format, from the settings in the admin of BlogEngine.NET

\#2 Find/replace the image tags

- Moving image links from the .axd in BlogEngine.NET to the wp-content/uploads directory

\#3 Importing the BlogML into WordPress

- <http://wordpress.org/extend/plugins/blogml-importer/>
- This crashed midway through the process so I need to find out if there are any missing posts – but the results do look pretty good.

\#4 Finding the missing images – my “backup” from WebHost4Life doesn’t look like it has all the images. I am going to try to track them down on the backup drive and home computer – recreate or remove any I can’t find

Overall pretty seamless – more content soon.

**UPDATE 2:**

Missed this the first time through: The blog categories come over from BlogEngine in the BlogML as the long GUIDs (e.g. 74d4ef66-f7ce-4f9f-9286-b32b8e294a4a) what we really want is the human-readable name (e.g. Development). The easiest way to fix this (looks weird to users and writers otherwise) is to import as normal, and then edit each Category in WordPress. Copy the GUID and then search the BlogML for the code. There will be a code element something like this …

```
    <span class="kwrd"><</span><span class="html">category</span> <span class="attr">id</span><span class="kwrd">="74d4ef66-f7ce-4f9f-9286-b32b8e294a4a"</span> <span class="attr">date-created</span><span class="kwrd">="0001-01-01T00:00:00"</span> <span class="attr">date-modified</span><span class="kwrd">="0001-01-01T00:00:00"</span> <span class="attr">approved</span><span class="kwrd">="true"</span> <span class="attr">parentref</span><span class="kwrd">="0"</span><span class="kwrd">></span>
      <span class="kwrd"><</span><span class="html">title</span> <span class="attr">type</span><span class="kwrd">="text"</span><span class="kwrd">><!</span>[CDATA[Development]]<span class="kwrd">></</span><span class="html">title</span><span class="kwrd">></span>
    <span class="kwrd"></</span><span class="html">category</span><span class="kwrd">></span>
```

Match the category id to the text inside the CDATA of the Title and you are back in business.