---
title: 'Silverlight Kata: IFS Fractals with TransformGroup and MessageBus'
date: '2010-02-01T02:36:23+00:00'
dsq_thread_id:
    - '384044579'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
image: /wp-content/uploads/2010/02/fractal_it7_thumb.png
---

At the CodeMash conference this year many things stuck with me, and two have been bugging me enough to do something about them this last weekend. One was the idea that programmers need to practice and refine their skills, which was probably best described in the ideas of [“Code Katas”](http://en.wikipedia.org/wiki/Kata_(programming)) ala Dave Thomas in the [Pragmatic Programmer](http://www.pragprog.com/). The other was my recent concentration on all-things-Silverlight, specifically looking at the power of the platform and the emerging patters (e.g. MVVM).

So if I can find an hour or two to “practice my craft” without expecting this will ever result in production code – just for learning – what should I tackle? It hit me – “Fractals!!!”. It seems like every computer system and programming environment that I’ve gotten since the late 80s I have seen what I could do with some of the now-classic fractal algorithms. Inspiration for this also came from Corey Hanes great feature summary of another classic, the “[Game of Life](http://github.com/coreyhaines/practice_game_of_life)”.

This post isn’t intended to be a detailed primer on fractals, and specifically fractals resulting from an [“iterated function system” or IFS](http://en.wikipedia.org/wiki/Iterated_function_system), but here are the basics. Many systems in nature exhibit features that look very similar to each other. That is, leaves on a tree, mountains, crystal structures, cells, snowflakes, etc. How can we try to simulate these patterns in a simple system to generate complex results. The IFS routines in these systems are kind of like DNA in a cell. Each element in the current generation of a system doesn’t know where it came from, but does know how to create the next generation in the system. How about an example.

Start with a square.

[![fractal_it1](http://www.bruceabernethy.com/wp-content/uploads/fractal_it1_thumb.png "fractal_it1")](http://www.bruceabernethy.com/wp-content/uploads/fractal_it1.png)

The shape you start with really doesn’t matter. What you end up with is making a “collage” of whatever shape you start with, a square is simple and fills the space nicely (which will be important later).

Now we need to add some simple transformation rules. We’ll do a “classic” Serpinski triangle or “gasket”.

A transformation rule generally has four parts: Scale, Rotation, Translation, and Probability.

In this case each of the three translations will scale 50% on both axes and have no rotation (0 degrees).

1. The first will not move at all (i.e. translate (0,0)).
2. The second will be a full width horizontally away (width, 0).
3. The third will be a full width vertically away and a half-width horizontally away (width/2, width)

[![fractal_it2](http://www.bruceabernethy.com/wp-content/uploads/fractal_it2_thumb.png "fractal_it2")](http://www.bruceabernethy.com/wp-content/uploads/fractal_it2.png)

These then are the simple rules that this system will run by. Each square in the system will know these rules and know how to apply them to themselves. So when told to “iterate” each square should execute each rule by creating a clone of itself, and applying the rule to it. After the iteration, the original square(s) should self-destruct as their short life is now over.

So what would happen with the next iteration?

[![fractal_it3](http://www.bruceabernethy.com/wp-content/uploads/fractal_it3_thumb.png "fractal_it3")](http://www.bruceabernethy.com/wp-content/uploads/fractal_it3.png)

And so on and so on. What if we did this 7 times?

[![fractal_it7](http://www.bruceabernethy.com/wp-content/uploads/fractal_it7_thumb.png "fractal_it7")](http://www.bruceabernethy.com/wp-content/uploads/fractal_it7.png)

Starts looking far different that you might have expected.

So how might we start to tackle this in Silverlight?

Actually, this should be far easier to do in Silverlight than in previous platforms because graphics and transformations are built in to Silverlight “out-of-the-box”.

So “Iteration 0” will be easy (just a Rectangle).

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:45b099f2-6155-4188-925f-f438c1edbe75" style="margin: 0px; display: inline; float: none; padding: 0px;">```
<span style="color: #0000ff;"><</span><span style="color: #800000;">Rectangle </span><span style="color: #ff0000;">Fill</span><span style="color: #0000ff;">="Red"</span><span style="color: #ff0000;"> Height</span><span style="color: #0000ff;">="400"</span><span style="color: #ff0000;"> Width</span><span style="color: #0000ff;">="400"</span><span style="color: #0000ff;">/></span>
```

</div>Now we could create a rectangle with half the height, width, and translate it in XAML, but we want to be able to automate this, so perhaps there is a better way.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:b219750e-5ecf-45c8-9e30-054f6336197d" style="margin: 0px; display: inline; float: none; padding: 0px;">```
<span style="color: #0000ff;"><</span><span style="color: #800000;">Rectangle </span><span style="color: #ff0000;">Fill</span><span style="color: #0000ff;">="Blue"</span><span style="color: #ff0000;"> Height</span><span style="color: #0000ff;">="400"</span><span style="color: #ff0000;"> Width</span><span style="color: #0000ff;">="400"</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">Rectangle.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">ScaleTransform </span><span style="color: #ff0000;">ScaleX</span><span style="color: #0000ff;">=".5"</span><span style="color: #ff0000;"> ScaleY</span><span style="color: #0000ff;">=".5"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">RotateTransform </span><span style="color: #ff0000;">Angle</span><span style="color: #0000ff;">="0"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TranslateTransform </span><span style="color: #ff0000;">X</span><span style="color: #0000ff;">="0"</span><span style="color: #ff0000;"> Y</span><span style="color: #0000ff;">="0"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"></</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">Rectangle.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">Rectangle</span><span style="color: #0000ff;">></span>
```

</div>We can take the original Rectangle and use the RenderTransform to handle all of the scaling, rotating, and translating of the Rectangle. This works pretty well and is starting to get promising. What would the other two “rules” look like?

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:5e26f68d-40be-405a-87c3-0c26ae924d30" style="margin: 0px; display: inline; float: none; padding: 0px;">```
<span style="color: #0000ff;"><</span><span style="color: #800000;">Rectangle </span><span style="color: #ff0000;">Fill</span><span style="color: #0000ff;">="LightBlue"</span><span style="color: #ff0000;"> Height</span><span style="color: #0000ff;">="400"</span><span style="color: #ff0000;"> Width</span><span style="color: #0000ff;">="400"</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">Rectangle.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">ScaleTransform </span><span style="color: #ff0000;">ScaleX</span><span style="color: #0000ff;">=".5"</span><span style="color: #ff0000;"> ScaleY</span><span style="color: #0000ff;">=".5"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">RotateTransform </span><span style="color: #ff0000;">Angle</span><span style="color: #0000ff;">="0"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TranslateTransform </span><span style="color: #ff0000;">X</span><span style="color: #0000ff;">="200"</span><span style="color: #ff0000;"> Y</span><span style="color: #0000ff;">="0"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"></</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">Rectangle.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">Rectangle</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">Rectangle </span><span style="color: #ff0000;">Fill</span><span style="color: #0000ff;">="AliceBlue"</span><span style="color: #ff0000;"> Height</span><span style="color: #0000ff;">="400"</span><span style="color: #ff0000;"> Width</span><span style="color: #0000ff;">="400"</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">Rectangle.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">ScaleTransform </span><span style="color: #ff0000;">ScaleX</span><span style="color: #0000ff;">=".5"</span><span style="color: #ff0000;"> ScaleY</span><span style="color: #0000ff;">=".5"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">RotateTransform </span><span style="color: #ff0000;">Angle</span><span style="color: #0000ff;">="0"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TranslateTransform </span><span style="color: #ff0000;">X</span><span style="color: #0000ff;">="100"</span><span style="color: #ff0000;"> Y</span><span style="color: #0000ff;">="200"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"></</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">Rectangle.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">Rectangle</span><span style="color: #0000ff;">></span>
```

</div>But now we have a problem. This works well for Iteration 1, but not for subsequent Iterations. We need to be able to do transformations on top of existing transformations (on top of other existing transformations, etc.). Rectangle alone will not get us there.

What is a very simple XAML object that can contain another object? The ContentControl is just such a basic object. Its basic job is to contain one other object (which itself could contain other objects), and it just so happens to also inherit from UIElement, which means it has RenderTransform as well. What does this mean.

It means that we can do something like this …

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:941370a3-96db-4311-8ded-d3297704e43b" style="margin: 0px; display: inline; float: none; padding: 0px;">```
<span style="color: #0000ff;"><</span><span style="color: #800000;">ContentControl</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">ContentControl.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">ScaleTransform </span><span style="color: #ff0000;">ScaleX</span><span style="color: #0000ff;">=".5"</span><span style="color: #ff0000;"> ScaleY</span><span style="color: #0000ff;">=".5"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">RotateTransform </span><span style="color: #ff0000;">Angle</span><span style="color: #0000ff;">="0"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TranslateTransform </span><span style="color: #ff0000;">X</span><span style="color: #0000ff;">="0"</span><span style="color: #ff0000;"> Y</span><span style="color: #0000ff;">="0"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"></</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">ContentControl.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">Rectangle </span><span style="color: #ff0000;">Fill</span><span style="color: #0000ff;">="Green"</span><span style="color: #ff0000;"> Height</span><span style="color: #0000ff;">="400"</span><span style="color: #ff0000;"> Width</span><span style="color: #0000ff;">="400"</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">Rectangle.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"><</span><span style="color: #800000;">ScaleTransform </span><span style="color: #ff0000;">ScaleX</span><span style="color: #0000ff;">=".5"</span><span style="color: #ff0000;"> ScaleY</span><span style="color: #0000ff;">=".5"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">RotateTransform </span><span style="color: #ff0000;">Angle</span><span style="color: #0000ff;">="0"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"><</span><span style="color: #800000;">TranslateTransform </span><span style="color: #ff0000;">X</span><span style="color: #0000ff;">="0"</span><span style="color: #ff0000;"> Y</span><span style="color: #0000ff;">="0"</span><span style="color: #0000ff;">/></span><span style="color: #0000ff;"></</span><span style="color: #800000;">TransformGroup</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">Rectangle.RenderTransform</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">Rectangle</span><span style="color: #0000ff;">></span><span style="color: #0000ff;"></</span><span style="color: #800000;">ContentControl</span><span style="color: #0000ff;">></span>
```

</div>… which, if you look at it, is the first rule in Iteration 2. That is, apply the first rule to an object that already had the first rule already applied to it. Now we’ll get a rectangle that is half the size of a half-sized rectangle (25%) and hasn’t rotated or moved from the origin at (0,0).

\[End of Part 1\]

Two more parts to this coming in the next few days:

- Part 1 – Fractals with TransformGroup and MessageBus
- [Part 2 – Automating transformations by creating an IFS Content Control](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-Automating-the-Transforms.aspx)
- [Part 3 – Wiring up the Iterations using a basic MessageBus implementation.](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-The-MessageBus.aspx)
- Part 4 – But will it work for a fractal Fern?
- Part 5 – Lessons Learned (aka limitations of the MessageBus and recursion in Silverlight)

Ironically(?) It will end up taking 3-4 times as long to blog this as it actually took to code it, but there is learning in the blogging as well, so more coming soon.