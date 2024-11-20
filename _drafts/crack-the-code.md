---
title:  "Interesting Links for the Week of Monday, November 11, 2024"
date: 2024-11-18
categories: links
header:
  teaser: /assets/images/crack-the-code-original.png
categories: ["development", "flutter"]
keywords: []
toc: true
comments: true
---

Inspired by a Brain Teaser from a few weeks ago … got a brain-worm to “sove this in code” …

![Image](/assets/images/crack-the-code-original.png)

# Donald Knuth Algorithm (1977) - the “5 guess” algorithm

## Generate a list of all the possible Guesses

Start with an initial guess - there are “better than other guesses” but I wanted to start with a random guess (which is not optimal) to generate random “puzzles” so might not get it in “5” guesses (more on that in a second).

## Evaluate the guess (how many “correct”, and how many “well placed”)

If 4 are “well placed” you are done!!!

Otherwise remove any other guesses that would not return the same output from the remaining guesses. The ones that match the output will match the code, the others will not match the code.

Pick the guess with the least numeric value of the remaining guesses for ideal guess, but I wanted to pick the next random one for more random puzzles.

I wanted to retain any “puzzles” that had exactly 5 “guesses” - some had less, some had more so recurse through this until I found exactly 5, which is actually the most common number.

This was actually pretty easy - felt like an Advent of Code. But then how to make it into a Flutter app?

How to make this happen when the page loads?

Add the generative function to a Riverpod FutureProvider and call it from the Page State initial build and load it when it is complete.  This works for adding config values, reading a file, calling an API, or any non-immediate value that needs to be added to state when it first starts up.

# Guess Entry Widget

Need to be able to enter each number, 

only once, 

and keep track of which numbers have been picked 

and not reuse those numbers,

ideally, visually represent which numbers have been picked

allow people to change their mind

be able to submit the number, but only once four numbers have been picked

only be able to pick 4 numbers

the entry widget will need its own state

I’d like to reuse this widget two different ways, so be able to “return” the guess from the widget to the containing widget/form as a callback

hmmm

## Simple Animation

Not always obvious that numbers are updating

Not always obvious that guess clears between guesses

Do a quick “flip” and “fade in/out” animation

Flutter has “Transform” and “Opacity”

Template/Sample Animation Widget

Onboarding / Quickstart

Wanted to try out the QuickStart/Onboarding package to help new users start using the app

Two tabs for two types of games

5 Guesses

5 Clues

Highlights where tab is and gives in instructions and animates/pulses where to click to go next.

Create a FocusNode() array “overlayKeys” in global area (app.dart),

Add onboardingKey to MyApp GlobalKey<OnboardingState> 

Onboarding “script” of List<OnboardingSteps> in global area (today.dart),

Wrap today.dart in Onboarding() widget in routes.dart, 

and “start” call, in “Instructions” widget “Quick Start” elevated button “onboarding.show()”, 

adding Focus nodes to areas where highlights need to occur

## Web Assembly

Why not

In the “stable” branch if you do flutter build web --wasm --release you'll get the bits using the experimental Web Assembly GC bits, so I did.

I also updated the index.htm file to have an alternate root to work on my coder.camp site

And added meta tags to have it have a nicer stub/renderer in things like Teams or other social media, etc.

