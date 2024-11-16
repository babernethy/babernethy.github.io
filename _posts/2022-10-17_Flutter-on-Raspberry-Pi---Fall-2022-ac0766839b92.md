---
title: Flutter on Raspberry Pi — Fall 2022
description: >-
  I didn’t see this all together in one place elsewhere, so wanted to compile
  and share.
date: '2022-10-17T16:28:19.709Z'
categories: []
keywords: []
slug: /@bruce-abernethy/flutter-on-raspberry-pi-fall-2022-ac0766839b92
---

I didn’t see this all together in one place elsewhere, so wanted to compile and share.

With the advances in Flutter and the Raspberry Pi platform, I wanted to see if the process for getting Flutter to run on the Raspberry Pi had gotten easier, and one I’d be willing to promote in some trainings and for folks getting started in this tech.

TL;DR — Yes, initial thoughts and evidence are that Flutter has arrived for regular use on Raspberry Pi

![Image](/assets/images/0__dGPZ37j91lVBS1pf.jpg)

Ingredients for the Recipe:

Thanks to the recent Amazon Prime Days, there were some nice deals on the parts I wanted, not too many.

*   Eviciv Raspberry Pi 7 Inch Touchscreen Display Screen HDMI with Rear Housing -1024x600
*   A nice all-in-one unit with a power supply, fans, touch screen, housing, etc. that could just mount the Raspberry Pi 4
*   Raspberry Pi 4 Model B 2019 Quad Core 64 Bit WiFi Bluetooth
*   64Gb PNY MicroSDHC Elite Class 10 U1 Flash Memory Card

### Assemble the Parts

This I didn’t document or photograph but it was just adding a couple jumpers for the touch screen, HDMI, and USB-C and screwing the RPi into the housing.

### Install Raspberry Pi OS

I flashed the SD card with _Raspberry Pi OS 64-bit (5.15) released 9/22/22_

> I don’t know if this is important or not, but it’s nice to have the 64 bit Pi 4 and 64 bit OS — all nice and aligned and released (not beta).

### First boot Raspberry Pi OS

All the typical set up, country, language, initial user.

### Terminal

> sudo apt update

Make sure apt libs/packages are up to date.

> sudo apt install snapd

We’re going to use “snap” which I have not used before, but was recommended for initial install of flutter on Raspberry Pi

[https://snapcraft.io/docs/installing-snap-on-raspbian](https://snapcraft.io/docs/installing-snap-on-raspbian)

> sudo snap install core

This gets the core libraries of snap installed for our use.

> sudo snap flutter — classic

[**Install Flutter on Linux | Snap Store**  
_Get the latest version of Flutter for Linux - Flutter SDK_snapcraft.io](https://snapcraft.io/flutter "https://snapcraft.io/flutter")[](https://snapcraft.io/flutter)

This is a snap for Flutter on Linux which includes some of the glue needed to make things work in this environment. I am all for shortcuts created by the team.

> sudo apt install code

[**Running Visual Studio Code on Linux**  
_See the Download Visual Studio Code page for a complete list of available installation options. By downloading and…_code.visualstudio.com](https://code.visualstudio.com/docs/setup/linux "https://code.visualstudio.com/docs/setup/linux")[](https://code.visualstudio.com/docs/setup/linux)

VS Code is a favorite IDE for Flutter (and other coding). Will be an app on Raspberry Pi UI menu (or just type “code”)

### What do we NOT need to install

*   chromium-browser already installed
*   git already installed

### Flutter doctor

Issuing the first “flutter” command after installing with snap seems to kick off the actual install of flutter and dart and building of the toolset. But it does put you on “master” which I’d like to change to “stable” for the projects I am working on, so I’ll make that change right off the bat.

> flutter doctor

> flutter channel stable

> flutter upgrade

Now we seem to be ready

> flutter create flutterpi

> cd flutterpi

> flutter run

![Image](/assets/images/0__YHNLqvOlNYSFMMiQ.jpg)

It just sort of worked — took a little while to compile, but not crazy long and ran native. In the past I had to rig a bunch of different things to get Flutter apps to run on RPi and compile them elsewhere to even get them to run on the Pi. Now you can do it all in one place — even the editing if you want (but probably not).

### Set up ‘chromium-browser’ as “Chrome” for Flutter Web debugging (optional)

Update to .bashrc to target chromium-browser as “chrome executable”

```
export CHROME_EXECUTABLE = '/usr/bin/chromium-browser'
```

This will tell flutter to use Chromium as your Chrome debugging browser.

![Image](/assets/images/0__GXzczPcBgZp2PHaQ.jpg)

That is about it — going to do more experimenting with what works nicely on RPiOS native and what doesn’t (Firebase :-( ) … more soon.