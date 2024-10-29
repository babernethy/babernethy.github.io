---
title: 'Confusion and FUD around Silverlight PDC Announcements'
date: '2009-12-01T04:49:35+00:00'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

Anytime I answer a question from three or more different sources, I want to write it up and refer the next people to this (and update as necessary).

There are two myths/exaggerations/tall tales surrounding announcements related to Silverlight last week at the PDC.

1\) Silverlight is running on the iPhone with Apple’s help.

2\) Silverlight 4 is breaking cross-platform compatibility and focusing on Windows over Mac and Linux.

As most good rumors/lies do, these both contain a smidgeon of truth (&lt;1%) and a whole lot of speculation, “analysis” and FUD (fear, uncertainty, and doubt).

### Silverlight on the iPhone

The “truth part” of this is the Silverlight Smooth Streaming technology that enables smooth high-definition video to play in Silverlight has been made compatible for streaming video to the iPod. This is a server-side technology that is integrated with IIS server. This does not mean that Silverlight applications run on the iPhone. If and when this happens this will be a big deal. For now, what this means for video content providers is that they can have a single solution to provide high-quality streaming video to both the desktop computer and the iPhone. Why the confusion here? I think a few poorly titled “news” articles/releases and blog posts and a bunch of trolls latching on to it.

### Silverlight Ending Cross-Platform Development

The Silverlight runtime is becoming available on a number of new platfroms from desktops (Win/Mac &amp; Linux with Moonlight), to hand-held devices, to TV-top and game consoles. Across all of these platforms there is a core Silverlight that runs 100% the same in each environment. But with each environment also comes some critical and desired functionality that is unique to that environment. On the XBOX you’ll want to be able to access game controllers (perhaps multiple), for touch screens you’ll want to be able to support touch and multi-touch capability, on a phone you will want to be able to dial the phone, if there is a GPS or accelerometer in the device you’ll be want to access that as well. These are all unique to specific devices and don’t exist on the other devices. Supporting one or more of these would not mean that Silverlight was not “cross-platform”, just that it enabled high-value specialized capability where it exists.

The “truth part” of this false accusation is the announced support for COM interaction in Silverlight on the Windows platform. What this means is that Silverlight will be able to call out to certain external code on machines if they exist. This means that a datagrid on the Silverlight screen could be easily sent to Excel, or an appointment could be sent to Outlook, a chart could be exported as a report to Word, etc. The grid, appointment and chart will exist cross-platform for all environments. The only difference is, if you happen to be on Windows with the right software installed there is additional functionality that can be quite useful. This is an example of a request from developers who are creating Silverlight applications for Enterprise Business customers who are requesting these types of features.

Why the confusion here? I think there is a small group of people who believe that cross-platform has to mean “least common denominator” – that is, if a feature/function can’t be used in 100% of the places where the software runs, then it isn’t “cross-platform”. In the iPhone world this would mean that applications couldn’t use the GPS or dialer because the apps might be used on the iPod Touch (where these don’t exist), or applications couldn’t support touch-screens because most people don’t have them. It will be up to the developers to make sure that their applications work well in all situations, but this shouldn’t prevent them from taking advantage of added features where they exist.