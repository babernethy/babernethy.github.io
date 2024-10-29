---
title: 'What is hypervideo anyway?'
date: '2010-03-10T00:29:01+00:00'
dsq_thread_id:
    - '382860217'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

If you know me or follow this blog at all you will probably know a few things about me: 1) I really like working with the latest technology and 2) I have a long history with Education and Learning. It just so happens that a project I am working on now, that is using some “cutting edge” technology, takes me back about 18 years to a project I worked on in the summer of 1992. I am talking about “hypervideo”, though in 2010 we are now doing it with streaming high-definition video instead of laserdisc recorders.

## What did “hypertext” do for “text” with HTML?

[![samplehtml](http://www.bruceabernethy.com/wp-content/uploads/samplehtml_thumb.png "samplehtml")](http://www.bruceabernethy.com/wp-content/uploads/samplehtml.png) We are so used to hypertext and the world-wide web, that we really don’t think about the technology and features behind it any more, but let’s take a second to “review the obvious”. The hypertext-markup language (HTML) is the coding behind the world-wide web. It is used to take the raw text and put a structure around the text and within the text. What started as a simple text file now gains things like:

- a “title”,
- “headings”,
- “hyperlinks”,
- navigation,
- sections/anchors,
- a unique identifier (uniform resource identifier (URI)),
- and data-about-the-data or “metadata”.

Users of these pages never really see any of this information, but they do appreciate it and use it all the time. They can enter an address like [www.nbcolympics.com](http://www.nbcolympics.com) and be taken directly to the online Olympic coverage from NBC (and how little most people appreciate how easy this is for them to do now. Users can “bookmark” or “favorite” particular pages and get back to them whenever they want to. Better yet, they can use Google or Bing to type in a few words or a phrase and often find exactly what they are looking for. Search engines use the titles, headings, and metadata in the page in their search routines to find these pages. And let’s not forget those wonderful underlined blue hyperlinks and linked buttons on pages that allow us to jump from page to page, and often find great resources and pages that we never knew that we were even interested in.

The problem with non-text items on web pages is that it is hard for computers to figure out what they are – if you put a picture of your dog on a web page it is still very hard for a browser or search engine to “look” at the picture and file it under “dog.” With words you can often tell what they mean from the context of the words that precede it or follow it; so this helps. Today, images can contain an “alt” attribute where you can describe the picture in words. This was originally though to be for browsers that did not support images or for screen readers for visually impaired users of the web, but now serves very well to help identify images to search engines.

## What if we could do similar things for video?

But what about video? Sites like YouTube, Facebook, and Vimeo enabling the upload of tens of thousands of hours of video. Each video contains a title and description which helps enable search to find the video. But what about what is inside the video. A single video may have many distinct sections or chapters where information is presented logically. In each section there could be textual information describing what is going on in the video (think closed captioning or even the [Descriptive Video Service](http://en.wikipedia.org/wiki/Descriptive_Video_Service)). What if you could not only search to find the video, but also find a particular time-code within the video (e.g. where the bit of text you searched for occurred in the video)? What if you could embed hyperlinks to other videos, other timecodes, other pages or notes, etc. within the video itself, so that they would appear or become available at a particular time when the video was playing?

Well, we can.

## TUVA

My favorite current example of hypervideo ideas is [Project TUVA](http://research.microsoft.com/apps/tools/tuva/) . For one, the main content is Dr. Richard Feynman’s wonderful physics lecture series at Cornell in the ‘60s (and who doesn’t like some good physics every so often). But, for me, it is also nice to know that it is built with Silverlight, which is a toolset that I am very aware of, so I know I could use many of these features myself down the road.

[![tuva1](http://www.bruceabernethy.com/wp-content/uploads/tuva1_thumb.png "tuva1")](http://www.bruceabernethy.com/wp-content/uploads/tuva1.png)

At the core of the player you will see something that looks very common for videos on the internet. There are the standard “VCR” controls, volume, and full-screen buttons – nothing really special so far.

[![tuvadetails](http://www.bruceabernethy.com/wp-content/uploads/tuvadetails_thumb.png "tuvadetails")](http://www.bruceabernethy.com/wp-content/uploads/tuvadetails.png)

But it doesn’t take long to see just how much else can be added to the video player when you start thinking about hypervideo concepts of linking, navigation, chapters, notes, and more.

### Chapters.

The first thing I noticed about the player was the expanded navigation and information timeline on the very bottom (I would really encourage you to open this site if possible because experiencing this live will help you understand this much more than a few static images and my attempt to describe the interactions with words). Each of the seven videos in Feynman’s lecture series are broken up into logical “chapters” with chapter titles like “Newton” and “Electricity”. This provides much the same functionality of HTML headings and anchor tags. You can quickly see the structure of the video and jump to any chapter from this navigation bar.

### Notes / Expert Commentary

Since this player was designed for an educational setting, the ability for the viewer to add their own notes in a left-side panel was added. This allows for anyone watching the video to add a note at a particular time in the video which they will be able to review later. In addition to this, you can load other people’s notes files and see what they were thinking during the video. This feature allows for the addition of “expert commentary” within the video frame – kind of like on a DVD where some allow you to turn on an audio track that includes the director and/or other people involved with the movie. This would also allow a teacher to include their own comments and instructions for students watching the video – and yes, these are also time-stamped so they can become clickable as well to add another layer of navigation.

### Closed Captioning / Transcript

We’ve all seen closed-captioning on television shows where what is being said in a particular show is displayed on the screen for those who are hearing impaired or for situations where the ambient noise in a room is such that the television can’t be heard.

[![tuvatranscript](http://www.bruceabernethy.com/wp-content/uploads/tuvatranscript_thumb.png "tuvatranscript")](http://www.bruceabernethy.com/wp-content/uploads/tuvatranscript.png)

The “Tuva” interface takes closed-captioning one step further and turns it into a full transcript of the talk being given. You can literally read through all the different close captioning entries in a scrollable textbox. Not only can you read through the captioning, but each of the captions itself is now a hyperlink that will take you to the time in the video where that caption was on screen.

But wait. If we have all this text now, linked to the video, can’t we search this too? Yes.

### Search

[![tuvasearch](http://www.bruceabernethy.com/wp-content/uploads/tuvasearch_thumb.png "tuvasearch")](http://www.bruceabernethy.com/wp-content/uploads/tuvasearch.png)

The interactive search box in the “Tuva” interface will allow the user to search the transcripts of all of the chapters of all of the videos for a keyword or phrase. Then all of the “hits” can be displayed, and yes, they are clickable hyperlinks.

### Links / Extras

The other notable feature of this interface is the “Extras” which are shown at the very bottom of the screen. Embedded into the video are bits of metadata which enable the inclusion of “notes” and “links” within the video itself. Each extra can have an associated icon or image which becomes visible in the “Extras” pane on the right at the appropriate time in the video. For a “note” type extra, this can pop-over a panel that includes extra information about a particular topic being discussed. The viewer can click on the icon to read this note, which pauses the video until they are done. Similarly clicking on a “link” extra will take the user to another part of the site or even off of the site to a page that explains a topic in more detail. For example, if Feynman is discussing Albert Einstein, and the viewer knows a lot about Einstein, then they can ignore the picture of Einstein in the Extras panel. If they are less familiar with Einstein, they can click on the icon and be taken to a new page that discusses the works and life of Einstein in detail. When they are ready, the viewer can close the page and return to the video which can then proceed from where they left off.

## NBC Olympics

But how might this technology look in a less “academic” and non-research or prototype situation – how about the 2010 Winter Olympics?

[![nbco1](http://www.bruceabernethy.com/wp-content/uploads/nbco1_thumb.png "nbco1")](http://www.bruceabernethy.com/wp-content/uploads/nbco1.png)

NBC created an online player that would stream live and pre-recorded events to viewers everywhere. They created a nice “blue-ice” themed player with all the functions you would expect from a modern player. A Play/Pause button, Fast Forward, Rewind, Jump Back, Volume, Full-Screen, and even a humorous “Boss” button that filled your screen with a Windows 7 desktop with an open Excel spreadsheet – cute.

But if you look a little closer you will see some components are are not, yet, very typical of video players online.

[![nbc02](http://www.bruceabernethy.com/wp-content/uploads/nbc02_thumb.png "nbc02")](http://www.bruceabernethy.com/wp-content/uploads/nbc02.png)

Clicking on the “Key Events” button for this Snowboarding video pops-up a scrollable list of all of the heats within this pre-recorded event. So that if I scroll through the list and want to find the round with Nick Baumgartner from the USA, I can find him in Heat 8 – clicking on this item takes me directly to that time in the video.

[![nbco3](http://www.bruceabernethy.com/wp-content/uploads/nbco3_thumb.png "nbco3")](http://www.bruceabernethy.com/wp-content/uploads/nbco3.png)

Similarly, the time bar at the bottom of the player has small lines at particular times, that you might not even see if you weren’t looking for them. In this example I was trying to find the quarter-final with Wescott and Holland from the USA – clicking on that bookmark took me directly to that point.

[![nbco4](http://www.bruceabernethy.com/wp-content/uploads/nbco4_thumb.png "nbco4")](http://www.bruceabernethy.com/wp-content/uploads/nbco4.png)

One more interesting use of “metadata” here is the “Play By Play” pane that you can also call up on the player. This allows for you to see interesting details about each event as it occurs. For example here, we can see that the skier has achieved 54.7mph on the ramp before taking off – crazy.

### How is it Done?

So, great, this is a cool technology and I’ve got a bunch of ideas on how it could be used. What tools do I need to start building my own hypervideo projects? Stay tuned for a near future post on this question and some tips to get you started.