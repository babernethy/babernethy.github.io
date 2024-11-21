# Blog Moved to GitHub Pages and Jekyll

It's time again to move and update the blog. Long-story-short: WordPress is in the middle of public "family problems," and I like Medium well enough, but there is always the pressure to put posts behind their "paywall" and they prompt visitors to join the paid tier, even for public posts.  So what to move to?

After doing some research on things that are available today, I decided to move my personal blog to GitHub Pages and to utilize the open source Jekyll system and framework.  It met a bunch of my criteria right away, and after experimenting with it for a while it really grew on me.  For example ...

* No ads or annoying pop-ups from a commercial product trying to entice anyone reading a post.
* Works with my blog custom domain name - bruceabernethy.com, etc.
* A path to migrate all my existing posts from WordPress and Medium pretty easily
* Nicely scriptable to automate some work and posts
    * Some Ruby and Python integrations
    * GitHub Actions enable publishing updates on merging Pull Requests on the site
* Nice pre-made Themes and templates 
    * for reactive screens that work nicely with desktop and mobile readers
    * meta tagging for different social media and community sites
    * robust RSS feeds built with rich support data
* Build posts in Markdown format which is very compatible with other simply styled documents I'm alerady writing
* Comments are nice - to enable conversations
* Basic post analytics - what to write more about 

# Static Rendered Content

What's different about GitHub Pages and Jekyll is it seems to be a bit of a "throwback" to the early days of web/blog publishing, in that the "final product" of publishing a web site, is a static set of web pages and images that can be published to any web server.

# GitHub Pages

[GitHub Pages](https://pages.github.com/) GitHub customers have an option to create and use GitHub Pages.  If you create a repository called **{github-username}.github.io** then GitHub will create that custom web site subdomain for you (if it isn't taken already - which it shouldn't be).  Then, you can define a particular branch in this repository to be your "pubilshing branch" and when you merge to that branch, a GitHub Action will auto-deploy your updates.  So ...

* Create a GitHub repo with your username.github.io
* Pick a publishing branch (custom or main)
* You can register a custom domain for this web site.
* GitHub will also get (and maintain) the SSL certificate for your custom domain

# Jekyll

[Jekyll](https://jekyllrb.com/) - I'm becoming a big fan of this framework.  It is a framework for creating static web sites, and has wonderful support for blogging specicially (but also works nicely for static pages and other uses (e.g. portfolio, business information, etc.)).  It also has been adopted and supported by the [GitHub Pages Jekyll Integration](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll) which makes it perfect for this purpose.  This makes it very straightforward to get Jekyll and GitHub Pages working nicely together.

## "Minimal Mistakes" - Theme for Jekyll

Jekyll has great support for Themes and Templates and Extensions - and the community around many of these is quite strong.  I tried a few different Themes, and ended up with the [Minimal Mistakes - Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/) by Michael Rose (and contributors).  I was looking for a very minimal and clean theme, but one that would support a reactive/adaptive design so posts would be readable either on a desktop or mobile browser.

Minimal Mistakes is also designed to be nicely extendable by implementing a model where the stylesheets Saas/SCSS/CSS are really easy to customize.  In a very similar way you can use the templates that come with the theme, but it is easy to update or change one or more if you want to do something more (or less).

It also is designed, up front, to work with blog comment services (e.g. Disqus) and analytics (e.g. Google Analytics) frameworks - and all are optional, but work wihtout having to add additional extensions.

## WordPress to Jekyll

How to move posts from your current blog into Jekyll when the formats are so different?  Thankfully, many other folks have done this before me.  There is a great [WordPress to Jekyll Exporter](https://wordpress.org/plugins/jekyll-exporter/) plugin.  And this worked for me with minimal "tweaking" of the resulting Markdown content.

**Note:** the server I was exporting from was minimally powered and timedout a number of times when I was trying this export.  I ended up backing up the site and running a local Docker container for WordPress in order to get really nice local performance and completed a relatively large export.

## Medium to Jekyll

This was actually much easier.  Medium has a feature (that they hide pretty well in submenus) to Export all of your content from their platform.  From this compiled .zip file, you can extract the folders representing your posts.  Then there is a great utility (nodejs I believe) called [medium-2-md](https://github.com/gautamdhameja/medium-2-md) that converts all these posts into a Markdown format that is directly compatible with Jekyll.

I did have to do more clean-up of these files as the filename had some "slug" content and an underscore that didn't seem to work well with Jekyll.  And the tool added a "slug" meta-data/front-matter into the posts which disrupted the flow of how the other pages were being rendered. Most of these were mass-updatable, but took some time.