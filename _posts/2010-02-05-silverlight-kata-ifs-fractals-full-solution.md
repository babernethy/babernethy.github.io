---
title: 'Silverlight Kata: IFS Fractals: Full Solution'
date: '2010-02-05T09:23:28+00:00'
dsq_thread_id:
    - '477582954'
category: "development"
tags: ["silverlight", "development", "science"]
redirect_from:
  - /silverlight-kata-ifs-fractals-full-solution/
---

If you have been following along with [Part 1](/silverlight-kata-ifs-fractals-with-transformgroup-and-messagebus/), [Part 2](/silverlight-kata-ifs-fractals-automating-the-transforms/), and [Part 3](/silverlight-kata-ifs-fractals-the-messagebus/), then you know we have described basically what the IFS Fractal “quest” is, how we did the rotatation/translation/scale transforms, and how we wired up the MessageBus to send our messages.

## Complete Code Solution

So we are ready to put it all together: \[ *Download Source Code (if desired) IFSContentControl.zip (1.4Mb)* *{missing-file:IFSContentControl.zip}* \]

And, since you’ve been so patient, here is a live demo of the application.

## Live Demo (Requires Silverlight 3)

 *{missing-embed:live Silverlight IFS fractal demo — Silverlight is no longer supported}*

## Pulling it Together

So, once we had the idea, the IFSContentControl, and the MessageBus wired up, pulling the rest of the Solution together is pretty straightforward. You will see the typical Silverlight Solution structure of a Silverlight project and the hosting Web Application project.

In “polishing” this up a little I did add a few more Messages.

```csharp
public class SetStartupIFSControl : CompositePresentationEvent<IFSControl> { }
public class SelfDestruct : CompositePresentationEvent<DateTime> { }
```

Adding SetStartupIFSControl let me add the ability to have the three buttons at the bottom with different “starter” IFS Objects.

The “Serpinski Triangle / Gasket” that I’ve been showing since Part 1 was defined like this …

```csharp
public static IFSControl StarterSerpinski()
{
  var starter = new IFSControl
                    {
                        IsProbabalistic = false,
                        Background = new SolidColorBrush(Colors.LightGray),
                        XOffset = 25,
                        Age = 1
                    };

  starter.Content = starter.MyRootControl;

  starter.IFSTransforms.Transforms.Add(new IFSTransform(.5, .5, 0, 0, 0, 1));
  starter.IFSTransforms.Transforms.Add(new IFSTransform(.5, .5, 0, 200, 0, 1));
  starter.IFSTransforms.Transforms.Add(new IFSTransform(.5, .5, 0, 100, 200, 1));

  return starter;
}
```

The more complex “Barnsley Fern” looks like this …

```csharp
public static IFSControl BarnsleyFern()
{

  var starter = new IFSControl
                    {
                        IsProbabalistic = false,
                        Background = new SolidColorBrush(Colors.Black),
                        XOffset = 100,
                        Age = 1
                    };

  starter.RectangleTemplate = new Rectangle
                                  {
                                      Height = 400,
                                      Width = 200,
                                      Stroke = new SolidColorBrush(Colors.Green),
                                      Fill = new SolidColorBrush(Color.FromArgb(200, 128, 255, 128)),
                                      StrokeThickness = 8
                                  };

  starter.Content = starter.MyRootControl;

  starter.IFSTransforms.Transforms.Add(new IFSTransform(.01, .16, 0, 0, 0, 1));
  starter.IFSTransforms.Transforms.Add(new IFSTransform(.34, .3, -50, 2, 50, 7));
  starter.IFSTransforms.Transforms.Add(new IFSTransform(.36, .28, 40, -2, 50, 7));
  starter.IFSTransforms.Transforms.Add(new IFSTransform(.85, .85, -3, -0, 50, 75));

  return starter;
}
```

These are both in the StarterIFSObjects static class.

The RectangleTemplate allowed for different shape Rectangles (which the “fern” required”) and also gave me a place to put the foreground and background colors – which is nice. I added “Age” so I could tell how many iterations each object had gone through (surfaces as a ToolTip).

## How well does it work?

For the Serpinski Triangle / Gasket, I was very pleased:

[![triangle8it](/assets/images/triangle8it_thumb.png "triangle8it")](/assets/images/triangle8it.png)

After 8 iterations, we have a fine (nearly textbook) example of what we were looking for.

For the “Checkered ‘X’”, also very nice:

[![cross5it](/assets/images/cross5it_thumb.png "cross5it")](/assets/images/cross5it.png)

More predictable, in my opinion, than the triangle, but after only 5 iterations we have the multi-layered self-similar “X”

But for the Barnsley Fern:

[![fern7it](/assets/images/fern7it_thumb.png "fern7it")](/assets/images/fern7it.png)

Not what I was hoping for. Even after 7 iterations (creating 16384 IFSContentControls), this is only starting to look like what I was hoping for. Iterating one more time left the browser “Not Responding” and was not generally a good idea.

The fern has many intricate details that do not surface well with this algorithm. There are “bitmap” algorithms that create very nice ferns in a short amount of time (“classic” GDI+ routines) …

[![bitmapfern](/assets/images/bitmapfern_thumb.png "bitmapfern")](/assets/images/bitmapfern.png)

But these do not track each translation and each message going out, which was what I was hoping to learn about from this.

So, the goal last weekend (which turned in to a goal to blog about it before “next” weekend (i.e. tomorrow)) was to learn more about TransformGroups and to see how much I could stress the EventAggregator/MessageBus without it caving. More about that in the last installment.

32. [Part 1 – Fractals with TransformGroup and MessageBus](/silverlight-kata-ifs-fractals-with-transformgroup-and-messagebus/)
33. [Part 2 – Automating transformations by creating an IFS Content Control](/silverlight-kata-ifs-fractals-automating-the-transforms/)
34. [Part 3 – Wiring up the Iterations using a basic MessageBus implementation.](/silverlight-kata-ifs-fractals-the-messagebus/)
35. Part 4 – But will it work for a fractal Fern?
36. Part 5 – Lessons Learned (aka limitations of the MessageBus and recursion in Silverlight)
