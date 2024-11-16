---
title: The Case for Flutter — Mobile-Oriented Architecture
description: This is the second post in a series on “The Case for Flutter”
categories: []
keywords: []
---

![Image](/assets/images/1__8Vnv9__PqjUdC5jGiDh8ghQ.png)

> _This is the second post in a series on “_[_The Case for Flutter_](https://medium.com/@bruce.abernethy/the-case-for-flutter-72af3f2df8bb)_”_

![Image](/assets/images/1__y84HNreVJc0YVCpWQbPE7w.png)

In evaluating the viability of Flutter, and how it compares to other options, it helps to have a framework for making evaluations and determinations. I found that I was making unconscious decisions about things related to mobile development and architecture. But when pressed as to “_why this feature is ‘cool’?_” it is more helpful to have some tangible reason that can be explained — something I’ll call “_Mobile-Oriented Architecture” (yes, stealing from SOA, but it works)_

What makes mobile development different than desktop, back-end, web, mobile-web, embedded? What are the unique challenges and expectations for a mobile app? How do we have to design, architect, and build differently for mobile? How does all of this impact how we choose a mobile framework?

![Image](/assets/images/1__XTK__uZeoBzXJCFp3aQDQVQ.jpeg)

Mobile phones are the most personal devices yet — they are almost part of us. The majority of people sleep with them beside their beds, have the phones with them at all times (most admit to using them while driving and in the bathroom). Mobile phone users can even psychologically/physiologically face significant anxiety when their batteries are near empty (or fail!!!). We put pictures of our children and grandchildren and most precious moments on them — share our deepest secrets in messages or live communication. We share financial and other personal information with our phones. Most people would not share their unlocked phones with even close friends or family for any length of time.

Developing for mobile phones is therefore different in nature that other types of development — what are the unique aspects of a “_Mobile-Oriented Architecture_”? Here are a few high-level categories that we’ll look at more deeply while evaluating the Flutter (or any) mobile framework.

*   [Users and their devices are omnipresent, ADD, and temporal](#75d4)
*   [All data is “live data” and FOMO](#8a75)
*   [“Time-to-market” expectations of mobile apps is exponentially decreasing](#e466)
*   [Natural and accessible user interface](#d66b)
*   [All apps are expected to be secure and private](#1257)
*   [Apps need to be able to be monetized](#6661)

#### Users and their devices are **omnipresent**, **ADD**, and **temporal**

Nothing existential or quantum-mechanical here — just a few observations. Mobile apps can be anywhere at anytime. The phone will usually be connected, at a decent bandwidth, unless it’s not. Sometimes my bandwidth might drop to 300 baud modem speeds, or disconnect altogether.

![Image](/assets/images/1__9HLjO7mNfJIicbH__Bzu__Xw.jpeg)

I open the app. Quick background the app — I got a call. Open it back up. Scroll down a little — need to go away now, remember where I was at. Actually I have two phones — one for work, one personal phone — I’d really like the same app on both phones, with the same data, oh and one phone is an Android and one is an iPhone — and the Android phone is older than my six-year-old cat — _squirrel_. Battery died.

New iPhones — at least once a year. New Android phones come out probably every week. These phones have different screen resolutions, OS versions, and capabilities. Phones are retired just as often. Customers are constantly updating/upgrading their phones. Just in a small beta test of my first Flutter app, we had a group with Android phones ranging from an old Motorola Android “_Lollipop_” phone, up to a Pixel 2 “moving from _Oreo_ to ‘_P_’ soon” — had an iPhone 4s through iPhone X (iOS 9–11).

In addition, phone screens get cracked/replaced, bought/sold, and people are “starting from scratch” or backup all the time. You need to be able to start from bare metal and get people into your app and back to where they were previously (with their previously fully loaded and functional phone) _ASAP_.

Oh, and I expect your app to load instantly and work flawlessly through all of this.

Oh, BTW, you’ll need to QA all of those scenarios. _Get to work._

_Keep this in mind a few posts from now when we look at the Flutter rendering engine and Redux development pattern and how that helps so much here._

#### All data is **“live data”** and **FOMO**

If you look at the most popular apps, they live on “live data” — yesterday’s news stories, weather, viral videos, chat messages, social media posts, etc. are almost out of our minds already — and forget about last week. Today, tonight, the last few hours, matter, and if anything changes we want to know immediately. The “Fear Of Missing Out” (FOMO) is almost epidemic as people want to be the first to find out anything and not be “out of the loop”.

![Image](/assets/images/1__5i1F7kynHTDtmDBwvr20vg.jpeg)

Today’s apps are more like an live interconnected neural-network of devices than a classic client-server application — they don’t “pull” data from a central source they are “pushed” data from a multitude of different sources. Data flows all-day all-night every-day.

I want the app to update in front of my eyes whenever something new happens — I live for the little red badge to appear or increment — a new message, story, picture, or update animates/dissolves into existence.

Even if I’m not using the app, or the phone for that matter, the app doesn’t stop needing new data. I want the ability for my phone to use optional Notifications to let me know there is a significant update that needs my attention and bring me back into the app and immediately show me what the changes are.

I may be traveling in the Michigan Upper Peninsula or in the basement lecture hall of a college and have no usable cellphone or wifi connection. I still want to be able to use as much of the app as possible. Show me what was going on before I lost connectivity. Let me interact with the app and “do things”. And as soon as I’m online again, sync up the updates like a sluice gate of data flow.

The data needs to be feel faster than actually possible, using [optimistic user interfaces](https://www.smashingmagazine.com/2016/11/true-lies-of-optimistic-user-interfaces/), [polyglot persistence](https://www.martinfowler.com/bliki/PolyglotPersistence.html), and caching latency-impacting data and resources wherever possible. I don’t want “[jank](https://en.wiktionary.org/wiki/jank)” to impact my experience (and we’ll talk more about “avoiding jank in Flutter” a little later).

_Keep this in mind when we talk about Flutter + Dart 2 + Firebase + Google Cloud ecosystem and how they organically interweave with one-another._

#### **Time-to-market** expectations for mobile apps are exponentially decreasing

This is in no way unique to mobile — but it’s still true about mobile. There is pressure to release high-quality software, as fast as possible.

![Image](/assets/images/1__PQAyDeLr1deBR__IylY7B__A.jpeg)

*   Any mobile framework needs to be able to “deliver working secure code daily”.
*   Work in a Continuous Integration and Continuous Delivery system — integrate well with DevOps frameworks.
*   Be able to have non-trivial additions and updates occur with as little friction as possible
*   Have a scalable team, from one to a hundred people, working, coding, merging, building, testing, and deploying
*   Provide automated test capability across the entire “[Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html)”
*   For mobile this includes automatically pushing builds on specific branches immediately to alpha and beta testers
*   And once approved automatically build and stage production releases

#### Natural and accessible user interface

Mobile apps that require training or documentation have already failed in usability in many users eyes (or new-user “Walkthroughs”, and I just did this in my Flutter app). [Don’t make me think](https://www.sensible.com/dmmt.html). The app should work in an obvious and natural way. I want to touch/tap/swipe/talk/shake in the way I’ve learned that other apps work. I don’t want to read a lot (unless its a reading app), and if you make me use a keyboard for any length of time I get cranky.

![Image](/assets/images/1__VBl8c8oaQdbxDsur4a8M0w.jpeg)

My eyes are getting old (true story) and I don’t want to wear glasses to use your app. The app should work with with big fonts, or I want to use the Accessibility options on my phone to read-out-loud sections of your app in a way that makes sense to me. I may use a big font on a large screen and want my “big phone” to work like a “small phone” only bigger — thanks.

I has been shown that when apps use [Universal Design](https://www.washington.edu/doit/what-difference-between-accessible-usable-and-universal-design) principles (i.e. designing for use by all users and abilities) actually increases overall usability and user experience for all users.

#### All apps are expected to be secure and private

Again, not unique to mobile development, but at a heightened level. Some of my most personal, financial, private, critical, confidential, information is in (or travels through) my phone. The information must be kept secure and private.

![Image](/assets/images/1__2q7prQ4SLnf9yDPlNxgKBg.jpeg)

There is a fundamental expectation that security is not an “add-on” feature to any app, but should be “baked-in” from the core of the application and framework.

#### Apps need to be able to be monetized

![Image](/assets/images/1____METLDKovkx3yQVf2sesvg.jpeg)

The typical “real cost” of an app that reaches the AppStore is difficult to accurately estimate, but I have seen believable numbers from $50,000 to $500,000 depending on the complexity of the application. This is almost all labor cost, so having a friend or family member that does graphic/ui/ux design and/or development work reduces your cost (like a good friend to knows how to fix your car) — but if you are the idea person paying for the work to be done, there is a non-trivial out-of-pocket expense.

Unless your project is funded by other means, this up-front cost needs to not only be recouped but exceeded (by a decent multiplier) to ever realize a profit for your efforts. Some of the most common ways to monetize an application are …

*   AppStore app purchase
*   Micropayments — in-app purchases
*   Subscriptions
*   Ecommerce
*   Advertising

Any mobile framework will need to be able to utilize one or more (or all) of these capabilities.

### Wrap Up

We’ve had some fun talking about some of our unique functional and architectural challenges with mobile applications — next we’ll see how this plays out in concrete application examples, and very soon we’ll actually look at how Flutter handles these challenges, where it really has innovated and is doing things as well (or better) than others, and some places where there is still work to be done.

### Next

Next [**“The ~8 Mobile Meta Apps”**](https://medium.com/@bruce.abernethy/this-is-the-third-post-in-a-series-on-the-case-for-flutter-1ab6849a8802)

_All images licensed via — stock-graphics.com_