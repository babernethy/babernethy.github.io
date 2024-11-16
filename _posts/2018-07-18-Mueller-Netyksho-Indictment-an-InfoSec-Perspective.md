---
title: Mueller “Netyksho” Indictment — an InfoSec Perspective
description: >-
  This isn’t a political post — I think you can find enough of those online from
  whatever perspective you like the best. But the most recent…
categories: []
keywords: []
---

![Image](/assets/images/1__fp6Vp2qS3RnJCH7ElLrSqQ.png)

This isn’t a political post — I think you can find enough of those online from whatever perspective you like the best. But the most recent [Mueller Indictment document](https://www.justice.gov/file/1080281/download) is a fascinating read from a technical and InfoSec perspective. It also reads like an old James Bond “Cold War” movie script (early draft), in fact it is almost “too vanilla/formula” to be believable.

**TL;DR** — But if you’re willing to stick with it for a few minutes, there are some good computer security lessons to learn (or hopefully review) about phishing emails, and being careful what you click on (especially if you have something to keep secret or private).

### The “GRU”

![Image](/assets/images/1__Po0tDlgwuYRu4ipbLhn6tg.png)

The hackers in this are the Russian “GRU” Units **26165** and **74455** “engaged in cyber operations” to get incriminating documents to harm candidates they didn’t like. In this case the targets were the Democratic Congressional Campaign Committee (“DCCC”) and Democratic National Committee (“DNC”) … oh, and if you read until the end, the Republican National Committee (“RNC”) as well.

### Spearphishing

![Image](/assets/images/1____xtGAZ2NC2__PXXHuUT0zrw.png)

You have probably heard of regular old phishing e-mail attacks (sending an e-mail out to a group of people, pretending to be from someone trusted (e.g. your bank, social media, e-commerce site, etc.) to trick you into responding and divulging information that they can then leverage to get more access.

“Spearphishing” is a highly-targeted version of this tactic that focuses on a small number, or even one, person. If you know enough about someone, you can probably create an e-mail that will get their attention.

### Spoofing

![Image](/assets/images/1____xtGAZ2NC2__PXXHuUT0zrw.png)

Once you have you target’s attention, then you want to get something useful from them — most commonly a userid and password to a system you want access to. In this case getting access to the target’s Gmail account.

> **BOOM**

> Honestly, the story could end here — with the **50,000** or so e-mails they got access to, there was enough compromising information to release to do a lot of damage. Just by a phishing attack that compromised their password

> **LESSON:** know the signs to look for that an e-mail is authentic. Check the address it is from, check the link that they are sending you to, think if there what is being asked for in the e-mail makes sense. If a link sends you back to Google and it asks you to login — weren’t you already logged in — does the login page look a little different. Why are you still not using **multi-factor authentication?** …

### One-Off E-mail Address

![Image](/assets/images/1__wHdZ__F__C9it1WsqVjkNobA.png)

So if you get an e-mail from me and it is **bruce.abernethy@gmail.com** … that’s cool, respond and everything is ok …

But then you get an e-mail from me and it’s _bruce.abernathy@gmail.com_ … well that’s the same … no … just one letter different … what about _bruce.adernethy@gmail.com_ … or _bruce.abermethy@gmail.com_ …

The hackers used the second most common trick in the book, using an address that looks like someone they should trust and see a lot and hope that they are just busy enough today to not look closely at the address and will just click on a link or open a document that was included.

An alternate would be to send you and e-mail from an actual compromised e-mail address but then send you to something like www.qooqle.com (Google, but not really — look closely) — and don’t open that site, I am not sure even where it goes.

### Malware: X-Agent / X-Tunnel

![Image](/assets/images/1__8F9eucMh5UhZ9rpSLClI0Q.png)

But what if you want more than just e-mails? What if you want documents or even to watch the computer “live”? Just need to install some malware on their computer — and if they’ve got your credentials and got you clicking on links and attachments, installing the malware takes just a few steps. Once you have it installed, you have a lot of additional capabilities

#### Keylogger / Screenshot

Imagine if someone was watching every key you typed and could take a screenshot at anytime of what you were currently doing on your machine. This would (and did) lead to a lot of other information that helped get even deeper into the system.

#### Takeover / Exfiltration

If they can watch your screen, they know when you are away, and they can take over your machine. In one such scenario the hackers searched the machine for “Benghazi Investigations” found files, and were able to exfiltrate (send them out over the internet) the files, which then ended up “leaked” onto the Internet.

### Caught by “Company 1”

![Image](/assets/images/1__WvjTZUSBFu2VniKDJQ3Z0A.png)

The best hackers are the ones you never see, and never catch, because they finish their work and remove all traces that they were present. These hackers were not successful at leaving undetected. When alert staff noticed things weren’t right and got suspicious that they were being hacked, they called in a security firm “Company 1” to help them out. While it took them months to completely secure the systems, I believe it was because of them that we have the evidence in order to put this story together.

### The RNC too

![Image](/assets/images/1__TQt1WDoUoWDQEzkuEcC__MQ.png)

This didn’t come out in most news stories, but some of the documents the hackers released did not come from the DCCC or DNC hacking efforts. Some of the documents could only have come from inside the opposition RNC servers, from previous hacking attempts. It seems they were equal-opportunity hackers, but selective on what and when to release documents.

### One more thing — the hacker/developer’s username …

![Image](/assets/images/1__wZFG2NB0w__dYuc1RGA5LBQ.png)

In all seriousness, none of this is funny — serious business, damaging leaks, a lot more to come as an outcome of all of these events. But in all of this it is interesting to note the username that the developer used at times online — “**blablabla1234565.**”