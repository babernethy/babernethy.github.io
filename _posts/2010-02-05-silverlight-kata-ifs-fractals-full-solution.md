---
title: 'Silverlight Kata: IFS Fractals: Full Solution'
date: '2010-02-05T09:23:28+00:00'
dsq_thread_id:
    - '477582954'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

If you have been following along with [Part 1](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-with-TransformGroup-and-MessageBus.aspx), [Part 2](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-Automating-the-Transforms.aspx), and [Part 3](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-The-MessageBus.aspx), then you know we have described basically what the IFS Fractal “quest” is, how we did the rotatation/translation/scale transforms, and how we wired up the MessageBus to send our messages.

## Complete Code Solution

So we are ready to put it all together: \[ [Download Source Code (if desired) IFSContentControl.zip (1.4Mb)](http://blog.bruceabernethy.com/mirror/IFSContentControl.zip) \]

And, since you’ve been so patient, here is a live demo of the application.

## Live Demo (Requires Silverlight 3)

 <object data="data:application/x-silverlight-2," height="600" type="application/x-silverlight-2" width="475"><param name="source" value="http://blog.bruceabernethy.com/ClientBin/SerpinskiMessage.xap"></param><param name="onError" value="onSilverlightError"></param><param name="background" value="white"></param><param name="minRuntimeVersion" value="3.0.40624.0"></param><param name="autoUpgrade" value="true"></param>[ ![Get Microsoft Silverlight](http://go.microsoft.com/fwlink/?LinkId=108181) ](http://go.microsoft.com/fwlink/?LinkID=149156&v=3.0.40624.0)</object>

## Pulling it Together

So, once we had the idea, the IFSContentControl, and the MessageBus wired up, pulling the rest of the Solution together is pretty straightforward. You will see the typical Silverlight Solution structure of a Silverlight project and the hosting Web Application project.

In “polishing” this up a little I did add a few more Messages.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:e98a13a2-7119-41fe-8b01-5b5258ffb613" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> SetStartupIFSControl : CompositePresentationEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">IFSControl</span><span style="color: #000000;">></span><span style="color: #000000;"> { }
</span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> SelfDestruct : CompositePresentationEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">DateTime</span><span style="color: #000000;">></span><span style="color: #000000;"> { }</span>
```

</div>Adding SetStartupIFSControl let me add the ability to have the three buttons at the bottom with different “starter” IFS Objects.

The “Serpinski Triangle / Gasket” that I’ve been showing since Part 1 was defined like this …

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:b7514783-b11c-4935-954b-34de72decb7a" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">static</span><span style="color: #000000;"> IFSControl StarterSerpinski()
{
  var starter </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSControl
                    {
                        IsProbabalistic </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">false</span><span style="color: #000000;">,
                        Background </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> SolidColorBrush(Colors.LightGray),
                        XOffset </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #800080;">25</span><span style="color: #000000;">,
                        Age </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #800080;">1</span><span style="color: #000000;">
                    };

  starter.Content </span><span style="color: #000000;">=</span><span style="color: #000000;"> starter.MyRootControl;

  starter.IFSTransforms.Transforms.Add(</span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSTransform(.</span><span style="color: #800080;">5</span><span style="color: #000000;">, .</span><span style="color: #800080;">5</span><span style="color: #000000;">, </span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">1</span><span style="color: #000000;">));
  starter.IFSTransforms.Transforms.Add(</span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSTransform(.</span><span style="color: #800080;">5</span><span style="color: #000000;">, .</span><span style="color: #800080;">5</span><span style="color: #000000;">, </span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">200</span><span style="color: #000000;">, </span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">1</span><span style="color: #000000;">));
  starter.IFSTransforms.Transforms.Add(</span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSTransform(.</span><span style="color: #800080;">5</span><span style="color: #000000;">, .</span><span style="color: #800080;">5</span><span style="color: #000000;">, </span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">100</span><span style="color: #000000;">, </span><span style="color: #800080;">200</span><span style="color: #000000;">, </span><span style="color: #800080;">1</span><span style="color: #000000;">));

  </span><span style="color: #0000FF;">return</span><span style="color: #000000;"> starter;
}</span>
```

</div>The more complex “Barnsley Fern” looks like this …

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:15709a58-47eb-4a94-9d1d-c343f5c2cfa3" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">static</span><span style="color: #000000;"> IFSControl BarnsleyFern()
{

  var starter </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSControl
                    {
                        IsProbabalistic </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">false</span><span style="color: #000000;">,
                        Background </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> SolidColorBrush(Colors.Black),
                        XOffset </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #800080;">100</span><span style="color: #000000;">,
                        Age </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #800080;">1</span><span style="color: #000000;">
                    };

  starter.RectangleTemplate </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> Rectangle
                                  {
                                      Height </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #800080;">400</span><span style="color: #000000;">,
                                      Width </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #800080;">200</span><span style="color: #000000;">,
                                      Stroke </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> SolidColorBrush(Colors.Green),
                                      Fill </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> SolidColorBrush(Color.FromArgb(</span><span style="color: #800080;">200</span><span style="color: #000000;">, </span><span style="color: #800080;">128</span><span style="color: #000000;">, </span><span style="color: #800080;">255</span><span style="color: #000000;">, </span><span style="color: #800080;">128</span><span style="color: #000000;">)),
                                      StrokeThickness </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #800080;">8</span><span style="color: #000000;">
                                  };

  starter.Content </span><span style="color: #000000;">=</span><span style="color: #000000;"> starter.MyRootControl;

  starter.IFSTransforms.Transforms.Add(</span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSTransform(.</span><span style="color: #800080;">01</span><span style="color: #000000;">, .</span><span style="color: #800080;">16</span><span style="color: #000000;">, </span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">1</span><span style="color: #000000;">));
  starter.IFSTransforms.Transforms.Add(</span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSTransform(.</span><span style="color: #800080;">34</span><span style="color: #000000;">, .</span><span style="color: #800080;">3</span><span style="color: #000000;">, </span><span style="color: #000000;">-</span><span style="color: #800080;">50</span><span style="color: #000000;">, </span><span style="color: #800080;">2</span><span style="color: #000000;">, </span><span style="color: #800080;">50</span><span style="color: #000000;">, </span><span style="color: #800080;">7</span><span style="color: #000000;">));
  starter.IFSTransforms.Transforms.Add(</span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSTransform(.</span><span style="color: #800080;">36</span><span style="color: #000000;">, .</span><span style="color: #800080;">28</span><span style="color: #000000;">, </span><span style="color: #800080;">40</span><span style="color: #000000;">, </span><span style="color: #000000;">-</span><span style="color: #800080;">2</span><span style="color: #000000;">, </span><span style="color: #800080;">50</span><span style="color: #000000;">, </span><span style="color: #800080;">7</span><span style="color: #000000;">));
  starter.IFSTransforms.Transforms.Add(</span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSTransform(.</span><span style="color: #800080;">85</span><span style="color: #000000;">, .</span><span style="color: #800080;">85</span><span style="color: #000000;">, </span><span style="color: #000000;">-</span><span style="color: #800080;">3</span><span style="color: #000000;">, </span><span style="color: #000000;">-</span><span style="color: #800080;">0</span><span style="color: #000000;">, </span><span style="color: #800080;">50</span><span style="color: #000000;">, </span><span style="color: #800080;">75</span><span style="color: #000000;">));



  </span><span style="color: #0000FF;">return</span><span style="color: #000000;"> starter;
}</span>
```

</div>These are both in the StarterIFSObjects static class.

The RectangleTemplate allowed for different shape Rectangles (which the “fern” required”) and also gave me a place to put the foreground and background colors – which is nice. I added “Age” so I could tell how many iterations each object had gone through (surfaces as a ToolTip).

## How well does it work?

For the Serpinski Triangle / Gasket, I was very pleased:

[![triangle8it](http://www.bruceabernethy.com/wp-content/uploads/triangle8it_thumb.png "triangle8it")](http://www.bruceabernethy.com/wp-content/uploads/triangle8it.png)

After 8 iterations, we have a fine (nearly textbook) example of what we were looking for.

For the “Checkered ‘X’”, also very nice:

[![cross5it](http://www.bruceabernethy.com/wp-content/uploads/cross5it_thumb.png "cross5it")](http://www.bruceabernethy.com/wp-content/uploads/cross5it.png)

More predictable, in my opinion, than the triangle, but after only 5 iterations we have the multi-layered self-similar “X”

But for the Barnsley Fern:

[![fern7it](http://www.bruceabernethy.com/wp-content/uploads/fern7it_thumb.png "fern7it")](http://www.bruceabernethy.com/wp-content/uploads/fern7it.png)

Not what I was hoping for. Even after 7 iterations (creating 16384 IFSContentControls), this is only starting to look like what I was hoping for. Iterating one more time left the browser “Not Responding” and was not generally a good idea.

The fern has many intricate details that do not surface well with this algorithm. There are “bitmap” algorithms that create very nice ferns in a short amount of time (“classic” GDI+ routines) …

[![bitmapfern](http://www.bruceabernethy.com/wp-content/uploads/bitmapfern_thumb.png "bitmapfern")](http://www.bruceabernethy.com/wp-content/uploads/bitmapfern.png)

But these do not track each translation and each message going out, which was what I was hoping to learn about from this.

So, the goal last weekend (which turned in to a goal to blog about it before “next” weekend (i.e. tomorrow)) was to learn more about TransformGroups and to see how much I could stress the EventAggregator/MessageBus without it caving. More about that in the last installment.

32. [Part 1 – Fractals with TransformGroup and MessageBus](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-with-TransformGroup-and-MessageBus.aspx)
33. [Part 2 – Automating transformations by creating an IFS Content Control](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-Automating-the-Transforms.aspx)
34. [Part 3 – Wiring up the Iterations using a basic MessageBus implementation.](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-The-MessageBus.aspx)
35. Part 4 – But will it work for a fractal Fern?
36. Part 5 – Lessons Learned (aka limitations of the MessageBus and recursion in Silverlight)