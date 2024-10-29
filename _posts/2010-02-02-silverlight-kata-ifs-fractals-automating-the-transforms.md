---
title: 'Silverlight Kata: IFS Fractals: Automating the Transforms'
date: '2010-02-02T00:53:13+00:00'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

Now that we have the idea of what IFS Fractals are from [Part 1](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-with-TransformGroup-and-MessageBus.aspx), we can move on to automating these iterations via code. Our first step is to encapsulate what an IFS Transform is.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:a091dd59-6504-48b8-bf19-49aa67f8cb93" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> IFSTransform
{
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">double</span><span style="color: #000000;"> ScaleX { </span><span style="color: #0000FF;">get</span><span style="color: #000000;">; </span><span style="color: #0000FF;">set</span><span style="color: #000000;">; }
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">double</span><span style="color: #000000;"> ScaleY { </span><span style="color: #0000FF;">get</span><span style="color: #000000;">; </span><span style="color: #0000FF;">set</span><span style="color: #000000;">; }
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">double</span><span style="color: #000000;"> Angle { </span><span style="color: #0000FF;">get</span><span style="color: #000000;">; </span><span style="color: #0000FF;">set</span><span style="color: #000000;">; }
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">double</span><span style="color: #000000;"> TransformX { </span><span style="color: #0000FF;">get</span><span style="color: #000000;">; </span><span style="color: #0000FF;">set</span><span style="color: #000000;">; }
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">double</span><span style="color: #000000;"> TransformY { </span><span style="color: #0000FF;">get</span><span style="color: #000000;">; </span><span style="color: #0000FF;">set</span><span style="color: #000000;">; }
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">double</span><span style="color: #000000;"> Probability { </span><span style="color: #0000FF;">get</span><span style="color: #000000;">; </span><span style="color: #0000FF;">set</span><span style="color: #000000;">; }
}</span>
```

</div>As detailed [before](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-with-TransformGroup-and-MessageBus.aspx), an IFS Transform will typically scale the previous iteration (bigger or smaller, and one or both axes), rotate the object, transform/move the object on one or both axes, and will add a probability. The probability is for when the different transformations need to happen more or less often in order to create the desired shape. For example a tree may have many leaves, but less branches; a person may grow more hair than they grow in height. Many of the transforms will be “uniform” and have all the same probability.

It is nice that we can enter our transforms in this concise class, but it would also be nice if we could translate these numbers into a XAML TransformGroup like the ones we manually created in the last post. To do this we’ll add a public method to the IFSTransform to accomplish this.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:d9281aaf-47e2-4927-b4b5-41f44429d5d0" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">public</span><span style="color: #000000;"> TransformGroup IFSTransformGroup {

  </span><span style="color: #0000FF;">get</span><span style="color: #000000;"> {

      var sc </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> ScaleTransform { ScaleX </span><span style="color: #000000;">=</span><span style="color: #000000;"> ScaleX, ScaleY </span><span style="color: #000000;">=</span><span style="color: #000000;"> ScaleY };
      var rt </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> RotateTransform { Angle </span><span style="color: #000000;">=</span><span style="color: #000000;"> Angle };
      var tt </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> TranslateTransform { X </span><span style="color: #000000;">=</span><span style="color: #000000;"> TransformX, Y </span><span style="color: #000000;">=</span><span style="color: #000000;"> TransformY };

      var tg </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> TransformGroup();
      tg.Children.Add(sc);
      tg.Children.Add(rt);
      tg.Children.Add(tt);

      </span><span style="color: #0000FF;">return</span><span style="color: #000000;"> tg;
  }
}</span>
```

</div>That will do nicely, and will help us get started on the XAML IFS Control itself.

[![IFSContentControl](http://www.bruceabernethy.com/wp-content/uploads/IFSContentControl_thumb.png "IFSContentControl")](http://www.bruceabernethy.com/wp-content/uploads/IFSContentControl.png)

In order to handle multiple iterations, what we’d really like is a control that contains the object that we are copying, then applies a series of transforms from all the previous iterations.

At the top level we need a control that also has the “smarts” to perform the next iteration. To do this it needs two key things.

First it needs to know all the rules for the iteration. Next it needs to be able to clone/copy itself and apply the next iteration.

We already have a class that represents an individual transform. What would a group of transformations look like. We could just use a generic list of transforms, but the group also needs to be able to return a random transform if the group is probabilistic (i.e. has a need to generate transforms in a non-uniform fashion).

So how can we return a random item from a generic list of transforms based on their individual probabilities (which are represented a a decimal, adding up to 1.0 (hopefully))?

Unfortunately, the C# Random object does not have a “NextDouble” method with a range of values – only the integer method has that ability. We’ll have to turn the doubles into integers for this calculation.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:df291476-dba3-485d-b233-c2c3b51e1dc2" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> IFSTransformGroup
{
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> IFSTransformGroup()...

   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> List</span><span style="color: #000000;"><</span><span style="color: #000000;">IFSTransform</span><span style="color: #000000;">></span><span style="color: #000000;"> Transforms { </span><span style="color: #0000FF;">get</span><span style="color: #000000;">; </span><span style="color: #0000FF;">set</span><span style="color: #000000;">; }

   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> IFSTransform GetRandomTransform
   {
       </span><span style="color: #0000FF;">get</span><span style="color: #000000;"> {

           var totalProbaility </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #800080;">0</span><span style="color: #000000;">;
           </span><span style="color: #0000FF;">foreach</span><span style="color: #000000;"> (var t </span><span style="color: #0000FF;">in</span><span style="color: #000000;"> Transforms) totalProbaility </span><span style="color: #000000;">+=</span><span style="color: #000000;"> t.ProbabilityEstimate;
           var rand </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> Random();
           var nextIteration </span><span style="color: #000000;">=</span><span style="color: #000000;"> rand.Next(totalProbaility);

           var probablilitySum </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #800080;">0</span><span style="color: #000000;">;
           </span><span style="color: #0000FF;">foreach</span><span style="color: #000000;"> (var t </span><span style="color: #0000FF;">in</span><span style="color: #000000;"> Transforms)
           {
               probablilitySum </span><span style="color: #000000;">+=</span><span style="color: #000000;"> t.ProbabilityEstimate;
               </span><span style="color: #0000FF;">if</span><span style="color: #000000;"> (probablilitySum </span><span style="color: #000000;">></span><span style="color: #000000;"> nextIteration) </span><span style="color: #0000FF;">return</span><span style="color: #000000;"> t;
           }

           </span><span style="color: #0000FF;">throw</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> InvalidOperationException(</span><span style="color: #800000;">"</span><span style="color: #800000;">Random number exceeded Probability Total</span><span style="color: #800000;">"</span><span style="color: #000000;">);
       }
   }
}</span>
```

</div>Now we can make our IFSContentControl.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:b1b6b8fb-099c-45bc-9141-e3888661f4b6" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> IFSControl : ContentControl
{
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> IFSTransformGroup IFSTransforms { </span><span style="color: #0000FF;">get</span><span style="color: #000000;">; </span><span style="color: #0000FF;">set</span><span style="color: #000000;">; }
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">bool</span><span style="color: #000000;"> IsProbabalistic { </span><span style="color: #0000FF;">get</span><span style="color: #000000;">; </span><span style="color: #0000FF;">set</span><span style="color: #000000;">; }
   
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">void</span><span style="color: #000000;"> DoIteration()...
   
   </span><span style="color: #0000FF;">private</span><span style="color: #000000;"> </span><span style="color: #0000FF;">object</span><span style="color: #000000;"> Copy(ContentControl original)...
}</span>
```

</div>We really just want a “smart” ContentControl, so let’s inherit from that. We can add an IFSTransformGroup, decide if it is probabilistic or not, and add a method to Do the next Iteration, which will need to be able to have a private method that will clone/copy the existing control (most likely several times).

What would need to happen for each iteration?

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:33f726af-315f-4fb9-a92f-806fb9401772" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">private</span><span style="color: #000000;"> </span><span style="color: #0000FF;">void</span><span style="color: #000000;"> DoUniformIteration()
{
  </span><span style="color: #0000FF;">foreach</span><span style="color: #000000;"> (var ifst </span><span style="color: #0000FF;">in</span><span style="color: #000000;"> IFSTransforms.Transforms)
  {
      var newControl </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSControl
      {
          Content </span><span style="color: #000000;">=</span><span style="color: #000000;"> Copy(</span><span style="color: #0000FF;">this</span><span style="color: #000000;">),
          IFSTransforms </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">this</span><span style="color: #000000;">.IFSTransforms,
          RenderTransform </span><span style="color: #000000;">=</span><span style="color: #000000;"> ifst.IFSTransformGroup
      };
   }
 }</span>
```

</div>Let’s look at just the “uniform” iteration first (where all transforms are applied equally). We will need to go through each transform and create a new control that is the existing control with the specific transform applied on “top”. This will create a number of different copies of the existing object which are each different now based on their specific transformation.

What do we do with these new controls? What to we do with the existing controls? That’ll happen in Part 3 when we get into the Messages and the MessageBus.

To finish out today, we need to be able to make a clone/copy of each object, to enable the “Copy” method.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:8fa887fc-f4c8-496b-93bf-a3135a60967b" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">private</span><span style="color: #000000;"> </span><span style="color: #0000FF;">object</span><span style="color: #000000;"> Copy(ContentControl orig)
{
  </span><span style="color: #0000FF;">if</span><span style="color: #000000;"> (</span><span style="color: #000000;">!</span><span style="color: #000000;">(orig.Content </span><span style="color: #0000FF;">is</span><span style="color: #000000;"> IFSControl </span><span style="color: #000000;">||</span><span style="color: #000000;"> orig.Content </span><span style="color: #0000FF;">is</span><span style="color: #000000;"> ContentControl))
  {
      var rootControl </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> ContentControl 
        {
            RenderTransform </span><span style="color: #000000;">=</span><span style="color: #000000;"> orig.RenderTransform,
            Content </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> Rectangle[...]
        };
      </span><span style="color: #0000FF;">return</span><span style="color: #000000;"> rootControl;
  }

  var newControl </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> ContentControl
        {
            RenderTransform </span><span style="color: #000000;">=</span><span style="color: #000000;"> orig.RenderTransform,
            Content </span><span style="color: #000000;">=</span><span style="color: #000000;"> Copy((ContentControl) orig.Content)
        };
  </span><span style="color: #0000FF;">return</span><span style="color: #000000;"> newControl;
}</span>
```

</div>It is always fun to end with a little recursion. We’ll end up walking the control tree down through the previous iterations. So long as we see an IFSControl or ContentControl we’ll add a ContentControl to our new object, carrying over the existing RenderTransform (i.e. TransformGroup) to the new control. When we find something that is not an IFSControl or ContentControl, then we know we’ve reached the source object – in this case a Rectangle.

Coming next, let’s create Messages we can send off to all the wired-up controls to tell them it is time to do the next iteration.

26. [Part 1 – Fractals with TransformGroup and MessageBus](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-with-TransformGroup-and-MessageBus.aspx)
27. [Part 2 – Automating transformations by creating an IFS Content Control](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-Automating-the-Transforms.aspx)
28. [Part 3 – Wiring up the Iterations using a basic MessageBus implementation.](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-The-MessageBus.aspx)
29. Part 4 – But will it work for a fractal Fern?
30. Part 5 – Lessons Learned (aka limitations of the MessageBus and recursion in Silverlight)