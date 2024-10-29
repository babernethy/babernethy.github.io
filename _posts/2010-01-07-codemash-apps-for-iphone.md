---
title: 'CodeMash Apps for iPhone'
date: '2010-01-07T03:35:23+00:00'
dsq_thread_id:
    - '430893019'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

The CodeMash conference is next week – it is a regional “software developer smörgåsbord” covering topics on a wide variety of technologies, patterns and processes. There are times when all 650ish attendees are together for keynotes and meals, but at other times there are 5-6+ different sessions going on throughout the conference center.

Traditional methods for getting information to attendees at conferences such as this is a printed program with all the tracks, sessions, speaker info, and location maps with all the rooms that sessions are taking place. This year, the organizers of CodeMash made available a set of web services using industry standard protocols that included all of this information. Then they left it up to the CodeMash community to come up with creating great applications to use this data.

At this time there are apps using many different platforms and technologies, but I wanted to focus on the iPod/iPhone apps (because that is the mobile device that I have) – see the CodeMash main site for more info <http://www.codemash.org>

Our team is taking five members to CodeMash this year, so we are getting together today to go over the schedule and decide which sessions we should try to all get to together and which ones we could “divide and conquer”, so I added the 3 iPod applications that I could find today to my Touch.

[![threeicons](http://www.bruceabernethy.com/wp-content/uploads/threeicons_thumb.png "threeicons")](http://www.bruceabernethy.com/wp-content/uploads/threeicons.png)

The three apps I could find for the iPhone were iCodeMash, MobiMash, and a “CodeMash 2010 Scheduler”. The first is a web offline HTML application, and the other two are available in the AppStore (search on CodeMash). I was wondering if the offline HTML application would be able to have the same functionality as a “full iPhone application” and I have to say that I was really impressed with how much can be done using the tools available.

This will really not be a review/recommendation for these applications – they are all free of charge and I will have all of them on my iPod for the conference. Rather, I wanted to review how the different authors and teams implemented features and see how many things were the same, but some features were innovative and even surprising. I won’t go application-by-application then, but feature by feature and show how all three were implemented.

## Splash Screen

[![IMG_0042](http://www.bruceabernethy.com/wp-content/uploads/IMG_0042_thumb.png "IMG_0042")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0042.png) [![IMG_0043](http://www.bruceabernethy.com/wp-content/uploads/IMG_0043_thumb.png "IMG_0043")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0043.png) [![IMG_0051](http://www.bruceabernethy.com/wp-content/uploads/IMG_0051_thumb.png "IMG_0051")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0051.png)

I only mention this “feature” because it was interesting how similar things were, using the same source material.

## Home / Start Screen

[![IMG_0035](http://www.bruceabernethy.com/wp-content/uploads/IMG_0035_thumb.png "IMG_0035")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0035.png) [![IMG_0044](http://www.bruceabernethy.com/wp-content/uploads/IMG_0044_thumb.png "IMG_0044")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0044.png) [![IMG_0052](http://www.bruceabernethy.com/wp-content/uploads/IMG_0052_thumb.png "IMG_0052")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0052.png)

Other than the obvious different color palettes, this is where the applications (with the same back-end data) start to diverge.

The iCodeMash application is very conscious of the “above the fold” region of the different areas of the app. It is also seems to be written to be used “at” the conference as well as “before” the conference. It automatically highlights the next session and has a quick-link to your favorites. Because this is not a full iPhone application, the button bar at the bottom is not used. iCodeMash approaches the schedule from primarily a day/time standpoint. The “next step” from this start screen would be to go view the next session, list of favorites, or review the schedule by day/time.

MobiMash starts with a news feed from CodeMash which is updated regularly. This may be updated during the conference as well, so this would be a good way to get late-breaking news at the top-level of the application. From this screen, you can view a list of all of the sessions, review those you have tagged as favorites, see a map of the venue. The More button reveals access to Speaker info, a Twitter feed of the #CodeMash hashtag (nice feature) as well as a “Right Now” and “Next” functionality which will be functional in the future.

The Scheduler application starts with a menu featuring links to sessions, but adds the ability to filter by Level and Track which may be helpful in finding topics that are attendee-appropriate. The button bar provides a “My Sessions” button that displays sessions that have been added to your favorites, and a News button which shows the CodeMash news feed.

## Pick Sessions

[![IMG_0036](http://www.bruceabernethy.com/wp-content/uploads/IMG_0036_thumb.png "IMG_0036")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0036.png) [![IMG_0037](http://www.bruceabernethy.com/wp-content/uploads/IMG_0037_thumb.png "IMG_0037")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0037.png) [![IMG_0038](http://www.bruceabernethy.com/wp-content/uploads/IMG_0038_thumb.png "IMG_0038")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0038.png)

iCodeMash approaches the sessions from a day/time standpoint. You need to pick a day (Thursday or Friday) and then you will see a list of all the titles of sessions at that time. If you pick a session title, then you will see the details for that session. If you select the “star” symbol on the description then this one will become a selection/favorite (very much like many Google apps use). Also in the description is a link to the room that this session is taking place in, with the specific room highlighted with a blue dot. This is a nice feature for when moving between sessions at the conference. I could not find a way to filter by level or track or access the speaker/bio information.

[![IMG_0045](http://www.bruceabernethy.com/wp-content/uploads/IMG_0045_thumb.png "IMG_0045")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0045.png) [![IMG_0046](http://www.bruceabernethy.com/wp-content/uploads/IMG_0046_thumb.png "IMG_0046")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0046.png)

MobiMash provides a complete list of all the sessions. The session abstract is included as well as the location and level of the session. The speaker’s name is a hyperlink to the speaker/bio information. A hyperlink by the session title enables you to add/remove the session from your list of favorites. This screen feels and works much like a web page. At the bottom of the session description is a unique feature to rate the session if you have attended it. I am not sure where this information surfaces, but it takes the application into the feedback/recap part of the process

[![IMG_0053](http://www.bruceabernethy.com/wp-content/uploads/IMG_0053_thumb.png "IMG_0053")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0053.png) [![IMG_0056](http://www.bruceabernethy.com/wp-content/uploads/IMG_0056_thumb.png "IMG_0056")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0056.png)

Scheduler provides either a complete list or a filtered list (level/track) of the sessions. From the formatted description you can access the speaker/bio information or Add the session to your My Sessions list.

## Review / Track Your Selections

Viewing the list of sessions and their descriptions is a great feature (and would really be “enough” for any of these to be useful at the conference), but all add the ability to tag sessions you are interested in attending and review those selections later.

[![IMG_0040](http://www.bruceabernethy.com/wp-content/uploads/IMG_0040_thumb.png "IMG_0040")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0040.png) [![IMG_0047](http://www.bruceabernethy.com/wp-content/uploads/IMG_0047_thumb.png "IMG_0047")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0047.png) [![IMG_0057](http://www.bruceabernethy.com/wp-content/uploads/IMG_0057_thumb.png "IMG_0057")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0057.png)

iCodeMash continues to provide data in a day/time format in reviewing your session Favorites. This is most helpful in this view as this is probably how you will be using the data at the conference.

MobiMash and Scheduler provide a list of those items you have selected; MobiMash gives them to you, I believe, in the order you selected them, while Scheduler sorts them by day/time ascending and includes the times in the list.

## Additional Features

All three apps do a good job of implementing the “big 3” for conference sessions: finding, tagging, and reviewing. I would expect anyone at CodeMash with an iPhone/Touch to take advantage of one or more of these. Beyond these features were a few unexpected bonuses.

[![IMG_0039](http://www.bruceabernethy.com/wp-content/uploads/IMG_0039_thumb.png "IMG_0039")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0039.png) [![IMG_0048](http://www.bruceabernethy.com/wp-content/uploads/IMG_0048_thumb.png "IMG_0048")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0048.png)

Maps – iCodeMash and MobiMash both a venue map of the Kalahari conference center. MobiMash enables this on the button bar at the bottom. iCodeMash includes a link from the session description. iCodeMash goes one step more and includes a little blue dot highlighting the room that the selected session which is very thoughtful.

[![IMG_0050](http://www.bruceabernethy.com/wp-content/uploads/IMG_0050_thumb.png "IMG_0050")](http://www.bruceabernethy.com/wp-content/uploads/IMG_0050.png)

Twitter – MobiMash includes a current sampling of Twitter postings using the #CodeMash hashtag. This is also quite cool and may be the way to find the most current info from the cloud at the Conference

## Ideas While Reviewing

This is the first year that CodeMash has made the conference data available for public consumption as web services. I have to say that all of these developers and groups have done a real service in pulling these applications together. I hope this is the first of many years that CodeMash, and other conferences, will offer information like this for applications.

I couldn’t help but think of what the next-generation applications might try to take on in future releases – what might be the most useful and interesting things to add?

**Additional Mashups – Twitter, Blog, LinkedIn, Google Group, Facebook, etc.**

I liked what MobiMash started with the integration of Twitter feeds with the #CodeMash hashtag. Why not extend this and include links from the speaker/bio information to their personal Twitter feeds (can learn a lot about someone from their feed). Why stop there? Integrate an RSS/Atom feed from their blog into the application as well. Basic information from LinkedIn might also be useful. In addition to bringing in the news feed from CodeMash, why not also include a summary feed from the Google Group where interesting conversations and threads are taking place.

**Backchannel – During the Sessions/Conference**

The Twitter feeds are a good start of this, but wouldn’t it be nice if there was a place where people could post comments, ideas, questions, etc. that were session-specific? Speakers could get an idea of how their audience is responding, and people outside the session could get an idea of what happened in the session or even if they should gracefully exit their session and join an ongoing discussion.

**Followup – After**

Many/most speakers who have PowerPoint decks or code samples as part of their session will create a blog post and attach these resources to the post. Comments on these posts can serve to give the speaker feedback and continue the conversation. MobiMash had the idea of a 5-star rating system for sessions that you attended – this is a start. But if the applications could contain access to follow-up posts and comments from the session then they would have value even after the conference was over.

**Framework**

And then you end up saying “If this can be done for CodeMash, couldn’t there be a framework or platform that could be used at the 1000s of conferences that go on every year?” Wouldn’t it be cool if a standard schema could be agreed on for sessions, speakers, venues, news, etc. that the major conferences, even just technology conferences, could all use so that all the work these developers have put into these apps could “pay if forward” and be used beneficially in the future.

In summary, great job to all the developers – Jonathan Penn (<http://wavethenavel.com>) for iCodeMash, SRT Solutions with Jay Wren ([http://jrwren.wrenfam.com/blog/](http://jrwren.wrenfam.com/blog/ "http://jrwren.wrenfam.com/blog/") <http://mobimash.org> ) for MobiMash, and QuickSolutions (<http://www.quicksolutions.com>) for CodeMash iPhone Scheduler. Thanks for creating great resources and inspiring others with your implementations.

**Connected / Disconnected**

All applications were tested online and offline – all worked well offline which is key since WiFi is iffy at big conferences.

**UPDATE:** updated some details, MobiMash author Jay Wren