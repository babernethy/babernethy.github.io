---
title: '64-bit Vista Oddness'
date: '2007-08-17T06:48:00+00:00'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

If you aren't running (or thinking of running) a 64-bit Vista OS (or don't know what that means) stop reading this post now, and have a nice day.

<font face="courier new,courier">&lt;geekspeak&gt;</font>

<font face="courier new,courier">A few "gotchas" in 64-bit stuff.</font>

> <font face="courier new,courier">1) Two "Program Files" folders – /Program Files and /Program Files (x86) – this is pretty obvious if you look in the root of the drive, but some programs have hard coded their path to "Program Files" and don't like being in the "Program Filex (x86) folder.</font>
> 
>  <font face="courier new,courier">2) Two "regedit" apps – yes a 64-bit version and a 32-bit version. So if you are using the 64-bit regedit you will see a weird root key called "Wow6432Node" which contains all your 32-bit keys. So if you (or a 64-bit program) is looking where the keys "used to be" in 32-bit-land, they are now in a sub-key of "Wow6432Node" (interesting naming – wonder how they got there? – [KB Article here](http://support.microsoft.com/kb/896459 "KB Article here").)  
>  </font>
> 
>  <font face="courier new,courier">3) Some 32-bit APIs want full control, and won't run in 64-bit. Most notably, and unfortunate, here is XNA. So if you are looking forward to doing some cool game programming and/or interacting with game controllers, etc. don't go 64-bit yet. This may stay this way for a while because the XBox 360 is not going 64-Bit (probably ever). </font>

<font face="courier new,courier">&lt;/geekspeak&gt;</font>