---
title: '64-bit Vista Oddness'
excerpt: 'A few gotchas worth knowing about before you move to a 64-bit version of Vista.'
description: 'A few gotchas worth knowing about before you move to a 64-bit version of Vista.'
date: '2007-08-17T06:48:00+00:00'
category: "tech"
tags: ["microsoft", "development"]
redirect_from:
  - /64-bit-vista-oddness/
---

If you aren't running (or thinking of running) a 64-bit Vista OS (or don't know what that means) stop reading this post now, and have a nice day.

`<geekspeak>`

A few "gotchas" in 64-bit stuff.

> 1) Two "Program Files" folders – /Program Files and /Program Files (x86) – this is pretty obvious if you look in the root of the drive, but some programs have hard coded their path to "Program Files" and don't like being in the "Program Filex (x86) folder.
>
>  2) Two "regedit" apps – yes a 64-bit version and a 32-bit version. So if you are using the 64-bit regedit you will see a weird root key called "Wow6432Node" which contains all your 32-bit keys. So if you (or a 64-bit program) is looking where the keys "used to be" in 32-bit-land, they are now in a sub-key of "Wow6432Node" (interesting naming – wonder how they got there? – [KB Article here](http://support.microsoft.com/kb/896459 "KB Article here").)
>
>  3) Some 32-bit APIs want full control, and won't run in 64-bit. Most notably, and unfortunate, here is XNA. So if you are looking forward to doing some cool game programming and/or interacting with game controllers, etc. don't go 64-bit yet. This may stay this way for a while because the XBox 360 is not going 64-Bit (probably ever).

`</geekspeak>`
