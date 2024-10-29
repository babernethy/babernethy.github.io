---
title: 'Silverlight Certification Test &#8211; Passed'
date: '2011-07-12T15:33:54+00:00'
dsq_thread_id:
    - '357240483'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
image: /wp-content/uploads/2011/07/70506.png
---

Microsoft released it’s long awaited (very long awaited) Silverlight Certification (MCTS 70-506) earlier this year. It was reportedly held up several times as Silverlight transitioned from version 2-&gt;3-&gt;4. There was enough new in Silverlight 4 that the wait was worth it and now the test is out. Having been working on Silverlight projects for years, there has really been no certification test to take as a credential, though I took the WPF 70-502 test as it was the closest technology to Silverlight that was available. But even having been through the WPF test previously, and working in Silverlight for several years, there are still some details that are worth reviewing before you take the test. If you are thinking about taking the test, here are some things that I found that were helpful in studying and passing the test.

p.s. Why might you want to take the test? First you can personally get a MCTS Silverlight (which is nice to have a current certification), also if you are a Microsoft Partner, this fulfills part of the Mobility Competency (along with the 70-599: Pro exam for WP7 – which is supposed to be out by now?), and most importantly, you gain depth – I always learn several things when studying for an exam which I am able to use fairly soon afterwards.

The Prometric/Microsoft testing agreement prohibits publishing actual test questions or summaries of the test itself, so I really should have written this yesterday while I was still preparing. I will try to recall the info without sharing anything that would violate the NDA on the test. Good resources to review:

1\) [Microsoft’s information](http://www.microsoft.com/learning/en/us/exam.aspx?ID=70-506) – this is a good review of the information and sections of the test

- **Laying Out a User Interface (15%)** – this is a section on laying out the UI, you should know the XAML for the elements mentioned – this is very “core” stuff, don’t lose any points here
- **Enhancing the User Interface (14%)** – styles, templates (know the difference), transformations, animations, visual state – again, review the syntax and know what is required and optional
- **Implementing Application Logic (16%)** – handling events, services, background workers, dependency properties, and the SL 4 ICommand interface
- I was worried that doing so much MVVM would hurt in doing things “old school” on the test, but they did a good job of respecting the pattern without using any of the frameworks outside of stock SL4.
- Also, make sure you are comfortable with setting up event handlers as class methods but also as statement lambdas (i.e.. the ” += (s, args) = &gt; { } ” syntax).
- If you have to learn some anonymous .NET delegates/functions at the same time as writing the test, it could add some complexity.
- I realized that I was using a lot of the shortcuts/helpers in Visual Studio 2010 and ReSharper to help implement dependency properties – which is fine for daily use – but make sure you know how to do it “from scratch” as well.

- **Working with Data (17%)** – formatting, data binding, value converters, data validation
- formatting and data binding are fairly common, value converters (especially the annoying boolean-to-visibility converter) are fairly common, but are largely templated (review the templates),
- and data validation is used but not as common. The data validation, especially, got a lot of “love” in later versions of Silverlight – review this.

- **Interacting with a Host Platform (11%)** – printing, out-of-browser applications, isolated storage, HTML DOM interaction, clipboard, read/write files from the host.
- Do yourself a favor – set up a quick OOB SL4 application that reads a file from the computer, combines that info with text on the clipboard, and prints out the result from Silverlight – it won’t take long and what you learn will be very helpful (and useful).

- **Structuring Applications (13%)** – I lost a question here somewhere – probably in the “localization” area (I’ve never done that in production). Review how to write and merge resource dictionaries, localize/globalize and application, and handle application-level events.
- **Deploying Applications (13%)** – review the HTML &lt;object&gt; code structure, initparms, etc. how to dynamically load resources (zip file, fonts, etc.) and use what you find, and the client-access policy file (where does it go, what should be in it, etc.)

<div>2) Preparation Materials – nada, there are no online learning, books or practice tests that I could find yet – by the time these get out we’ll be at Silverlight 5 – bummer</div><div>3) The guys at Silverlight Show did a g[ood 7-part blog series](http://www.silverlightshow.net/items/Getting-ready-for-the-exams-Part-1.aspx) on preparing for the test – this was quite helpful to review. They have been going over a prep guide for 70-599 (WP7) test as well which I plan to read and take soon.</div><div>I am debating my next test, but I do have a summer goal of taking one more – probably WCF to fill out the MCPD certification. Anyone who is interested in the WCF or WP7 tests, that wants to study together (online or in person), let me know in the next couple weeks.</div>