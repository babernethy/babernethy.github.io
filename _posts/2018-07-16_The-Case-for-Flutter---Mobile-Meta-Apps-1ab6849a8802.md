---
title: The Case for Flutter — Mobile Meta Apps
description: This is the third post in a series on “The Case for Flutter”
date: '2018-07-16T20:33:49.614Z'
categories: []
keywords: []
slug: >-
  /@bruce-abernethy/this-is-the-third-post-in-a-series-on-the-case-for-flutter-1ab6849a8802
---

![Image](/assets/images/1__8Vnv9__PqjUdC5jGiDh8ghQ.png)

> This is the third post in a series on “[The Case for Flutter](https://medium.com/@bruce.abernethy/the-case-for-flutter-72af3f2df8bb)”

![Image](/assets/images/1__klCBwLwNiBteYNyvEi4iNg.png)

### When evaluating a mobile framework, what are be some good test cases for apps that we should be able to build (e.g. our “Hello World” app on up)? What are the most common features in mobile apps? If we were learning a new mobile framework, what types of apps would we want to be able to build and test out?

Further, once we have these meta apps, can we evaluate them …

*   How well was the solution implemented? Is there anything obviously missing?
*   How long did it take to create? Start-to-finish
*   How complex is the solution that was created? Could it be easily handed off to others or continued and expanded?

In addition to suggesting what some good “mobile meta apps” to test are in general, I’ll try to be better about making “the case for Flutter”. To get a flavor for some of these, I’ll try to include some starter links for existing Flutter examples. It’s always helpful for me to read “real code” and you can get the git repo(s) and read the code in any editor without even committing to installing the full Flutter framework.

Here is a proposed list of apps that will help us “kick the tires” on a new mobile framework.

1.  [Hello World](#14f9)
2.  [Make a List](#63fe)
3.  [Remote Data / API](#cd81)
4.  [Live Data](#fd07)
5.  [Phone Features](#e74c)
6.  [Monetize](#9afa)
7.  [Game](#8bd4)
8.  [Emerging / Differentiating Tech](#b8b4)

![Image](/assets/images/1__y84HNreVJc0YVCpWQbPE7w.png)

### Hello World

The “hello world” app for mobile is the least amount of code you need to write to get something demonstrable running on an emulator or connected device. It would meet these criteria …

*   Runs on a mobile phone (iOS or Android — bonus points for both)
*   Some text in a title bar and main body
*   An action can be user-initiated, probably using a button
*   This action can be tied to a change in the UI
*   Bonus points to be able to flavor the UI with some color, images, icons.

As with most current frameworks, Flutter creates this level of app automatically when you create a new Flutter project — either through your favorite IDE or “`flutter create`” from the CLI.

![Image](/assets/images/1__wJBzoxK7SJcxWbGg__7M__AQ.png)

The code Flutter creates is well documented and commented so you can get a feel for the basics. If you’ve got a device connected when you create your new app, a simple “`flutter run`” will build and run the solution. When you’re ready to set up and try out Flutter, there are getting started instructions at the [Flutter project page](http://flutter.io).

### Make a List

A next obvious step is a app that displays a formatted list of items — perhaps allowing for a master-detail approach to picking an item and getting more information about it. Examples could be a “shopping list”, “to-do-list”, “baseball card list”, “checklist”, etc.

*   Create a model for the items in the list
*   Create a list of models to be maintained in the state of the app (bonus points to persist these items locally, between app sessions)
*   Create a UI to display one of the items
*   Create a UI to display a list of the items (and scroll through them)
*   Create the action/interaction necessary to pop-up a detail view of an item, and return to the list.

There are a number of good “To-do” list example in Flutter (code and walkthrough videos). My favorites are (yes multiple) in Brian Eagan’s “[Flutter Architecture Examples](https://github.com/brianegan/flutter_architecture_samples)”

![Image](/assets/images/1__poo__UvLQhXDZPe7oRQlRdQ.png)

### Remote Data / API

Most mobile apps need to be able to load and interact with data from locations across the internet and off of the device. A logical next step is to load data from an API and render it in your application. This includes …

*   Setting up, authenticating, and calling the API (probably REST)
*   Parsing the result (probably JSON) into an object or collection of objects
*   Using this data to fill a list and master-detail screen
*   App data is stored in some type of state/view-model and rendered on the screen.
*   Data can be pulled and refreshed by the user.

If you have an existing API from a previous project, this is a great way to demonstrate the power of the mobile app, and the reason you took the time to build an API. Note, this may also be a database that exposes itself as a REST API, or even something like Firebase that enables most API features without an explicit API.

If you don’t have an existing API, there are a bunch of free/open APIs out there to choose from (news, weather, etc.) — most social media platforms have an available API.

![Image](/assets/images/1__qpjliA3VuvkquSUfBCceBQ.png)

A good simple-API example from Flutter is the [Dad jokes](https://proandroiddev.com/a-new-flutter-app-from-flutter-create-to-the-app-store-e6c2dee17c1a) app that Tim Sneath wrote about in April — it also includes good basic info on taking a simple app all the way to the AppStore

### Live Data

I tried to make the case in the Mobile-Oriented Architecture post, that modern mobile apps rely on “live data” (pushed to the app vs. all app-initiated pulls) to help satisfy user FOMO (fear of missing out). Creating an application that will auto-update based on live data being pushed to the app is an important next step. The features of this app would be …

*   App data can be obtained from a back-end and stored in some type of state (the starting point)
*   When server data is updated, the server can initiate communication with the app to update the data
*   Updated data can instantly update the user-interface (when appropriate)
*   Data from the app can be pushed to the server and then forwarded out to other applications who subscribe to that specific data.

An obvious starter for a “live data” meta app is a **“chat app”** where multiple users can add chat items simultaneously with all phones being updated.

To complete this meta app you’ll need a remote data source that is capable of pushing data (sockets/websockets or equivalent). In the Google world, an obvious source for this data is Google’s Firebase and Cloud solutions. The “memechat” app published by Emily Fortuna.

[**efortuna/memechat**  
_memechat - playing with flutter_github.com](https://github.com/efortuna/memechat "https://github.com/efortuna/memechat")[](https://github.com/efortuna/memechat)

> **Flutter Packages**

> On the Flutter front, many of the higher-level meta apps require additional functionality that is outside the base Flutter framework. These [Flutter Packages](https://pub.dartlang.org/flutter) are written by many different groups, from the Flutter team itself to individuals or groups in the community. A daily-growing list of these is available at [https://pub.dartlang.org/flutter](https://pub.dartlang.org/flutter).

One of these packages in the “live data” category is [Firebase Messaging](https://pub.dartlang.org/packages/firebase_messaging). This package allows for platform-specific push notifications to be sent to devices. These messages can be received (whether the app is open or not) and can trigger actions to help route and guide users to the appropriate part of the application.

### Common Phone Features

No mobile app is an island — integration with the phone OS and hardware itself and other applications is expected in any mobile framework.

*   The application can use native features of the phone, when available.
*   This may require UI updates
*   This may only be updates to the “back-end” of the mobile application
*   This may enable integrations outbound to other applications

Some examples of these type of integrations are … (and some [Flutter packages](https://pub.dartlang.org/flutter))

*   Capture camera or photo gallery pictures from the phone (Flutter Package: _image\_picker_)
*   Call up a map with locations and pins with callbacks to the main application (Flutter Package: _map\_view_)
*   Get the current location of the phone in GPS coordinates (Flutter Package: _geolocation_, _geolocator_)
*   Launch a web page in a browser on the phone (Flutter Package: _url\_launcher_) — this will launch the phone’s default browser to a particular URL. **Note**: there is not currently a Flutter package/widget (that I know of) that will embed a web page into a Flutter page/view.
*   Play a full-screen video (Flutter Package: _video\_player_)
*   Share content from the application to other applications (e.g. mail, messaging, Facebook, Twitter, etc.) (Flutter Package: _share_)

### Monetize

You’ve got to pay the bills. If you’re going to go to the trouble of writing a mobile app, it should at least pay for itself, if not turn a nice profit. What do app developers do to monetize their apps? A number of things …

*   Charge for installing app — including just for completeness
*   Authenticate users — have a security system in place for users
*   E-commerce features —product and search API, build a “cart”, call a payment API.
*   Serve advertisements (and get paid for them)
*   Support in-app payments (subscriptions, “freemium” options (start at the free level, then pay to go further — permanently (new levels) or consumable (buy some in-app currency/coins/etc.)).

![Image](/assets/images/1____METLDKovkx3yQVf2sesvg.jpeg)

Some helpful Flutter packages

*   There are a good number of Flutter [Packages featuring payment](https://pub.dartlang.org/flutter/packages?q=payment&sort=top)
*   [firebase\_admob](https://pub.dartlang.org/packages/firebase_admob) — “supports loading and displaying banner, interstitial (full-screen), and rewarded video ads”
*   [flutter\_iap](https://pub.dartlang.org/packages/flutter_iap)\- enables in-app-payments from Google Play and AppStore

### Game

The bulk of the paid applications in AppStores are games. Some of these stand-alone, and others integrate to back-end systems that enable play with another player, a handful of other players, or can even integrate into massive systems of thousands or tens-of-thousands of players.

Many of these games offer amazing 3D graphics and sound that rivals console gaming systems. Others are simpler abstract puzzle games that take a different part of the brain. I won’t try to itemize what features make a “game” because of the wide variety, but will try to give some examples.

One example that caught my attention this spring was the 2048 app, which started more as an experiment with coordinated animations.

![Image](/assets/images/1__2Zu0gEpTeHsmxba4DZRP7Q.png)

[**Animation Management with Flutter and Flux/Redux**  
_Edit description_medium.com](https://medium.com/flutter-io/animation-management-with-flutter-and-flux-redux-94729e6585fa "https://medium.com/flutter-io/animation-management-with-flutter-and-flux-redux-94729e6585fa")[](https://medium.com/flutter-io/animation-management-with-flutter-and-flux-redux-94729e6585fa)

One apparent deficit in the Flutter framework (compared to platform native options) is the ability to access rich and responsive 3D graphics (many times using frameworks like OpenGL). But, as I understand it, **this is by design in Flutter**. Flutter is heavily-engineered for 2D optimization using the Skia graphics engine, for very fluid and performant 2D graphics, effects, and animations. Creating high-quality 2D games is very possible in Flutter — you can control literally every pixel on every screen at a very high frame rate. But if your app is a 3D platformer game, Flutter is not designed for this purpose.

### Differentiating / Emerging Features

This really isn’t a meta-app in the same sense of the others, but it is something that people trying out a new framework get to fairly quickly — the hottest new features. The smartphone industry is built on people buying new phones on a regular cadence — every year (subscriptions) or two to stay “current”. In addition to more storage, better screens/cameras, faster processors, etc., there are emerging brand new features that sell users on buying a new phone. And since the average phone costs more than my first car now, they want to use these features and will be attracted to apps that enable them.

Examples of emerging technologies include features like: biometrics, machine-learning, augmented reality, virtual reality, voice integration, smart home integration, etc.

There are some good Flutter examples of cross-platform new smartphone features, like biometrics. For example there is the “[local\_auth](https://pub.dartlang.org/packages/local_auth)” package that will ask for increased local security (e.g. TouchID/FaceID on iOS or fingerprint APIs on Android)

![Image](/assets/images/1__1IFKh__siWbba__yUDu2reFw.jpeg)

It makes sense that Flutter, being developed by Google, has more initial support for emerging technologies from Google. So if you want to do experiment with some machine-learning capabilities such as reading text on images, recognizing faces, scan barcodes, etc. there is an [MLKit](https://pub.dartlang.org/packages/mlkit)integration package and [MLVision](https://pub.dartlang.org/packages/firebase_ml_vision) package for example.

There are a number of emerging platform features of phones that do not currently have Flutter packages or integrations (on iOS noticeably: ARKit, 3D Touch, HomeKit, Siri API).

> **Roll your own Flutter Plugins**

> But, if you want a missing cutting-edge feature in your Flutter application, and have an aspiring iOS or Android developer handy, Flutter is very extensible and offers a well-documented platform on [Using and Writing Flutter Packages](https://flutter.io/using-packages/). So take a shot, write a nice integration, publish it on GitHub (please) and you may be able to build a group of similarly-interested developers who can help build-up and mature the package.

> **Integrate Flutter into Android or iOS platform native app**

> And if you’re really brave, there is some experimental support for [embedding Flutter views into other Android and iOS applications](https://github.com/flutter/flutter/wiki/Add-Flutter-to-existing-apps). This feature would allow for Flutter views to be created for primary 2D/UIs/Interactions but then allow the platform native application to control the cutting-edge content that is only/best supported in the native tools. I’ve never tried this or seen it work, but the capability is very interesting.

### Wrapping up

From “**Hello World”** to “**Virtual Reality”,** there are a number of meta applications that we’ll want to test out in any mobile framework. The speed and quality of these solutions helps build the case for any mobile framework.

Even at the beta/pre-release stage of Flutter, it has good answers for most of the primary meta-apps. For those features that require a full front-end-back-end-ecosystem, it is understandable that the best out-of-the-box integrations and packages today are with other Google products (e.g. Firebase, Google Cloud) but a widening list of platforms and projects is emerging.

For the scenarios of 3D/action games and emerging tech on iOS (ARKit, 3D Touch, HomeKit, etc.) using the platform/native Xcode solutions are still a better option.

### Next

Next (will be) What do Developers Want in a Mobile Framework …