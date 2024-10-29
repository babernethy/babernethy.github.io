---
title: 'ImplicitStyleManager &ndash; Hidden Gem in the Silverlight Toolkit November 2008'
date: '2008-10-28T08:05:34+00:00'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

Sure the AutoCompleteBox, Expander, TreeView, Charts, etc. from the new Silverlight Toolkit (<http://www.codeplex.com/Silverlight> ) are cool – and will make some Silverlight apps look even better. But the ImplicitStyleManager (and related Theme classes) will now allow designers to encapsulate their design work into an assembly and xaml resource dictionary, and easily apply the theme to an entire page (or part of a page).

On the surface this is “duh” you could do that before – but not so. You had to “touch” every control and add a Style and/or Template to it and have that StaticResource appear in a generic.xaml or App.xaml somewhere in your app. Now you should be able to “style-up” and entire Page/App in a few declarative steps.

This means that there could be a market for professional looking themes for Silverlight apps that developers could apply for a really polished look in their applications. It also means that custom themes can be created for a company or project that can be easily and consistently applied to many different controls and/or applications.

I am eager to try this out on a larger scale in the next week or so – will report back.

Check it out (with some nifty pre-packaged themes for your use) at [http://www.codeplex.com/Silverlight/Wiki/View.aspx?title=Silverlight%20Toolkit%20Overview%20Part%203&amp;referringTitle=Home&amp;ANCHOR#ImplicitStyleManager](http://www.codeplex.com/Silverlight/Wiki/View.aspx?title=Silverlight%20Toolkit%20Overview%20Part%203&referringTitle=Home&ANCHOR#ImplicitStyleManager)