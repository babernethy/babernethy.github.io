---
title: 'Silverlight Kata: IFS Fractals: Automating the Transforms'
excerpt: 'Part two of the fractal kata - encapsulating an IFS transform and driving the iterations from code.'
description: 'Part two of the fractal kata - encapsulating an IFS transform and driving the iterations from code.'
date: '2010-02-02T00:53:13+00:00'
category: "development"
tags: ["silverlight", "development", "science"]
redirect_from:
  - /silverlight-kata-ifs-fractals-automating-the-transforms/
---

Now that we have the idea of what IFS Fractals are from [Part 1](/silverlight-kata-ifs-fractals-with-transformgroup-and-messagebus/), we can move on to automating these iterations via code. Our first step is to encapsulate what an IFS Transform is.

```csharp
public class IFSTransform
{
   public double ScaleX { get; set; }
   public double ScaleY { get; set; }
   public double Angle { get; set; }
   public double TransformX { get; set; }
   public double TransformY { get; set; }
   public double Probability { get; set; }
}
```

As detailed [before](/silverlight-kata-ifs-fractals-with-transformgroup-and-messagebus/), an IFS Transform will typically scale the previous iteration (bigger or smaller, and one or both axes), rotate the object, transform/move the object on one or both axes, and will add a probability. The probability is for when the different transformations need to happen more or less often in order to create the desired shape. For example a tree may have many leaves, but less branches; a person may grow more hair than they grow in height. Many of the transforms will be “uniform” and have all the same probability.

It is nice that we can enter our transforms in this concise class, but it would also be nice if we could translate these numbers into a XAML TransformGroup like the ones we manually created in the last post. To do this we’ll add a public method to the IFSTransform to accomplish this.

```csharp
public TransformGroup IFSTransformGroup {

  get {

      var sc = new ScaleTransform { ScaleX = ScaleX, ScaleY = ScaleY };
      var rt = new RotateTransform { Angle = Angle };
      var tt = new TranslateTransform { X = TransformX, Y = TransformY };

      var tg = new TransformGroup();
      tg.Children.Add(sc);
      tg.Children.Add(rt);
      tg.Children.Add(tt);

      return tg;
  }
}
```

That will do nicely, and will help us get started on the XAML IFS Control itself.

[![IFSContentControl](/assets/images/IFSContentControl_thumb.png "IFSContentControl")](/assets/images/IFSContentControl.png)

In order to handle multiple iterations, what we’d really like is a control that contains the object that we are copying, then applies a series of transforms from all the previous iterations.

At the top level we need a control that also has the “smarts” to perform the next iteration. To do this it needs two key things.

First it needs to know all the rules for the iteration. Next it needs to be able to clone/copy itself and apply the next iteration.

We already have a class that represents an individual transform. What would a group of transformations look like. We could just use a generic list of transforms, but the group also needs to be able to return a random transform if the group is probabilistic (i.e. has a need to generate transforms in a non-uniform fashion).

So how can we return a random item from a generic list of transforms based on their individual probabilities (which are represented a a decimal, adding up to 1.0 (hopefully))?

Unfortunately, the C# Random object does not have a “NextDouble” method with a range of values – only the integer method has that ability. We’ll have to turn the doubles into integers for this calculation.

```csharp
public class IFSTransformGroup
{
   public IFSTransformGroup()...

   public List<IFSTransform> Transforms { get; set; }

   public IFSTransform GetRandomTransform
   {
       get {

           var totalProbaility = 0;
           foreach (var t in Transforms) totalProbaility += t.ProbabilityEstimate;
           var rand = new Random();
           var nextIteration = rand.Next(totalProbaility);

           var probablilitySum = 0;
           foreach (var t in Transforms)
           {
               probablilitySum += t.ProbabilityEstimate;
               if (probablilitySum > nextIteration) return t;
           }

           throw new InvalidOperationException("Random number exceeded Probability Total");
       }
   }
}
```

Now we can make our IFSContentControl.

```csharp
public class IFSControl : ContentControl
{
   public IFSTransformGroup IFSTransforms { get; set; }
   public bool IsProbabalistic { get; set; }

   public void DoIteration()...

   private object Copy(ContentControl original)...
}
```

We really just want a “smart” ContentControl, so let’s inherit from that. We can add an IFSTransformGroup, decide if it is probabilistic or not, and add a method to Do the next Iteration, which will need to be able to have a private method that will clone/copy the existing control (most likely several times).

What would need to happen for each iteration?

```csharp
private void DoUniformIteration()
{
  foreach (var ifst in IFSTransforms.Transforms)
  {
      var newControl = new IFSControl
      {
          Content = Copy(this),
          IFSTransforms = this.IFSTransforms,
          RenderTransform = ifst.IFSTransformGroup
      };
   }
 }
```

Let’s look at just the “uniform” iteration first (where all transforms are applied equally). We will need to go through each transform and create a new control that is the existing control with the specific transform applied on “top”. This will create a number of different copies of the existing object which are each different now based on their specific transformation.

What do we do with these new controls? What to we do with the existing controls? That’ll happen in Part 3 when we get into the Messages and the MessageBus.

To finish out today, we need to be able to make a clone/copy of each object, to enable the “Copy” method.

```csharp
private object Copy(ContentControl orig)
{
  if (!(orig.Content is IFSControl || orig.Content is ContentControl))
  {
      var rootControl = new ContentControl
        {
            RenderTransform = orig.RenderTransform,
            Content = new Rectangle[...]
        };
      return rootControl;
  }

  var newControl = new ContentControl
        {
            RenderTransform = orig.RenderTransform,
            Content = Copy((ContentControl) orig.Content)
        };
  return newControl;
}
```

It is always fun to end with a little recursion. We’ll end up walking the control tree down through the previous iterations. So long as we see an IFSControl or ContentControl we’ll add a ContentControl to our new object, carrying over the existing RenderTransform (i.e. TransformGroup) to the new control. When we find something that is not an IFSControl or ContentControl, then we know we’ve reached the source object – in this case a Rectangle.

Coming next, let’s create Messages we can send off to all the wired-up controls to tell them it is time to do the next iteration.

26. [Part 1 – Fractals with TransformGroup and MessageBus](/silverlight-kata-ifs-fractals-with-transformgroup-and-messagebus/)
27. [Part 2 – Automating transformations by creating an IFS Content Control](/silverlight-kata-ifs-fractals-automating-the-transforms/)
28. [Part 3 – Wiring up the Iterations using a basic MessageBus implementation.](/silverlight-kata-ifs-fractals-the-messagebus/)
29. Part 4 – But will it work for a fractal Fern?
30. Part 5 – Lessons Learned (aka limitations of the MessageBus and recursion in Silverlight)
