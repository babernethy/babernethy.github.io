---
title: 'Silverlight Kata: IFS Fractals: The MessageBus'
date: '2010-02-05T03:20:13+00:00'
dsq_thread_id:
    - '518626049'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

We are almost done with this application. What started with [Part 1 ](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-with-TransformGroup-and-MessageBus.aspx)(intro to Fractals and the Silverlight experiment) and continued with [Part 2](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-Automating-the-Transforms.aspx) (creating the IFSContentControl) now gets a MessageBus to help communicate to and from the different controls

The EventAggregator and MessageBus patterns have been [described as a pattern](http://martinfowler.com/eaaDev/EventAggregator.html) and [discussed for a while](http://www.enterpriseintegrationpatterns.com/MessageBus.html) and recently implemented by several different frameworks within Silverlight. The basic idea is to decouple messages for common functions from specific classes. If there is a common set of Messages, and a shared MessageBus, then objects with access to the bus and messages can “subscribe” to the messages that they want to “hear” and “publish” messages that they want to send out.

A more detailed description of this particular implementation [as described by the Microsoft Patterns &amp; Practices](http://msdn.microsoft.com/en-us/library/ms978583.aspx) group implemented as [EventAggregator](http://msdn.microsoft.com/en-us/library/dd458918.aspx). We will use the EventAggregator for our MessageBus and CompositePresentationEvent from the Microsoft.Practices namespace described here.

## Which Messages?

So, then, what are the messages that we will want to have in this application?

“Iterate” is the big and obvious one. We may, for example, want to press a Button and have it Publish the “Iterate” Message to the MessageBus. Then, we’ll want our IFSContentControls to Subscribe to the “Iterate” message and have them generate the next generation of the fractal.

So to start out we’d have this …

[![messagebus1](http://www.bruceabernethy.com/wp-content/uploads/messagebus1_thumb.png "messagebus1")](http://www.bruceabernethy.com/wp-content/uploads/messagebus1.png)

The IFSContentControl would clone itself and apply each transform (3 in this example). These new controls would then also Subscribe to the “Iterate” Message.

[![messagebus2](http://www.bruceabernethy.com/wp-content/uploads/messagebus2_thumb.png "messagebus2")](http://www.bruceabernethy.com/wp-content/uploads/messagebus2.png)

So the next click of the button that publishes the message will now be “heard” by three different objects ….

[![messagebus3](http://www.bruceabernethy.com/wp-content/uploads/messagebus3_thumb.png "messagebus3")](http://www.bruceabernethy.com/wp-content/uploads/messagebus3.png)

And so on … and so on …

To fully make this work though, we’ll need to (1) get the new controls onto our Container/Canvas. And, in the case of these fractals, the original control does not “survive” the iteration and only “lives” through one generation.

So we’ll add two more Messages: (1) AddIFSControl (to add the new IFSControls to the Container) and (2) RemoveIFSControl (to remove the current control from the Container once the Iteration is complete).

[![messagebus4](http://www.bruceabernethy.com/wp-content/uploads/messagebus4_thumb.png "messagebus4")](http://www.bruceabernethy.com/wp-content/uploads/messagebus4.png)

So our messages end up looking like this …

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:82471b43-0e86-481b-b65c-f91d35aef3bc" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">using</span><span style="color: #000000;"> Microsoft.Practices.Composite.Presentation.Events;

</span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> Messages
{
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> Iterate : CompositePresentationEvent</span><span style="color: #000000;"><</span><span style="color: #0000FF;">bool</span><span style="color: #000000;">></span><span style="color: #000000;"> { }
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> AddIFSControl : CompositePresentationEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">IFSControl</span><span style="color: #000000;">></span><span style="color: #000000;"> { }
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> RemoveIFSControl : CompositePresentationEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">IFSControl</span><span style="color: #000000;">></span><span style="color: #000000;"> { }
}</span>
```

</div>The CompositePresentationEvent is a generic class that takes a strongly typed object. In the case of the “Iterate” message, there really isn’t a type we need to send up (there is no data payload that is needed to process the “Iterate” message). In the case of the AddIFSControl and RemoveIFSControl messages, we will send along the IFSControls themselves in order to be processed.

## Where is the MessageBus?

For this application, it is easiest to implement the MessageBus at the highest point possible in the Application itself. So in our App.xaml.cs file we just add this …

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:65584126-c1d4-4361-a9a9-6b93442bcc4b" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">using</span><span style="color: #000000;"> Microsoft.Practices.Composite.Events;

</span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">partial</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> App : Application
{
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">static</span><span style="color: #000000;"> IEventAggregator MessageBus </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> EventAggregator();</span>
```

</div>Really that is all it takes to set up the MessageBus.

## Publishing the Messages

So, now how do we wire up the Button to publish the iterate event. In the codebehind of the MainPage (or ViewModel if you’ve wired it up) we can add code something like this.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:d2a7e539-e085-4d33-8c6d-37c67e1ba746" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">private</span><span style="color: #000000;"> </span><span style="color: #0000FF;">void</span><span style="color: #000000;"> Button_Click(</span><span style="color: #0000FF;">object</span><span style="color: #000000;"> sender, RoutedEventArgs e)
{
  App.MessageBus.GetEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">Messages.Iterate</span><span style="color: #000000;">></span><span style="color: #000000;">().Publish(</span><span style="color: #0000FF;">true</span><span style="color: #000000;">);
}</span>
```

</div>It is important to notice that there is nothing special

about the “Button” itself – we aren’t using any of its events or properties to do this work or propagate this message. You could just as easily set up a DispatherTimer and have it call “Iterate” every 60 seconds or so …

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:be4ba3f2-1f25-4d7a-83d9-ddf92c449350" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">void</span><span style="color: #000000;"> IterateMe_Tick(</span><span style="color: #0000FF;">object</span><span style="color: #000000;"> sender, EventArgs e)
{
  App.MessageBus.GetEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">Messages.Iterate</span><span style="color: #000000;">></span><span style="color: #000000;">().Publish(</span><span style="color: #0000FF;">true</span><span style="color: #000000;">);
}</span>
```

</div>## Subscribing to the Messages

So now we need to add code to the IFSContentControls to Subscribe to the Iterate Message.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:16d1743b-bd7c-47dc-a037-7958344a813e" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">public</span><span style="color: #000000;"> IFSControl()
{
  App.MessageBus.GetEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">Messages.Iterate</span><span style="color: #000000;">></span><span style="color: #000000;">().Subscribe(DoIteration, </span><span style="color: #0000FF;">true</span><span style="color: #000000;">);</span>
```

</div>To wire this up we need to create a public method that takes the same payload as the message itself – in this case, Iterate sends a boolean. So we need a public method that takes a boolean.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:838eb017-78f4-40a7-8e50-d9496400cf94" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">private</span><span style="color: #000000;"> </span><span style="color: #0000FF;">void</span><span style="color: #000000;"> DoIteration(</span><span style="color: #0000FF;">bool</span><span style="color: #000000;"> isTrue)
{
  </span><span style="color: #0000FF;">foreach</span><span style="color: #000000;"> (var ifst </span><span style="color: #0000FF;">in</span><span style="color: #000000;"> IFSTransforms.Transforms)
  {
      var newControl </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> IFSControl
      {
          Content </span><span style="color: #000000;">=</span><span style="color: #000000;"> Copy(</span><span style="color: #0000FF;">this</span><span style="color: #000000;">),
          IFSTransforms </span><span style="color: #000000;">=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">this</span><span style="color: #000000;">.IFSTransforms,
          RenderTransform </span><span style="color: #000000;">=</span><span style="color: #000000;"> ifst.IFSTransformGroup
      };
      App.MessageBus.GetEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">Messages.AddIFSControl</span><span style="color: #000000;">></span><span style="color: #000000;">().Publish(newControl);
  }
  App.MessageBus.GetEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">Messages.Iterate</span><span style="color: #000000;">></span><span style="color: #000000;">().Unsubscribe(DoIteration);
  App.MessageBus.GetEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">Messages.RemoveIFSControl</span><span style="color: #000000;">></span><span style="color: #000000;">().Publish(</span><span style="color: #0000FF;">this</span><span style="color: #000000;">);
}</span>
```

</div>So IFSControl is now set up to Subscribe to the Iterate event – it will then call DoIteration() when it receives the message. DoIteration() will iterate through all the different transforms, create a new IFSControl which is a clone/copy of the current control, and then Publish the AddIFSControl message with the new control as the payload. In our example this will happen three times for each iteration, so three new controls will be sent in messages.

The last two lines are interesting as well. Once the new controls are created it is time for the current control to request that it be removed from the container – it has done its work and it is time to move on. First we Unsubscribe from the DoIteration Message (always good to not leave loose ends) and then Publish the RemoveIFSControl message with “this” as the payload (i.e., the current control). It is thus requesting to be removed from the container.

## Container Messages

In this example the DataContext of our MainPage will be a class called the IFSStageViewModel. This class encapsulates all the information and logic that will be needed for the user interface of our application.

<div class="wlWriterEditableSmartContent" id="scid:57F11A72-B0E5-49c7-9094-E3A15BD5B5E6:2d53ebce-4a6e-4a98-82fc-79386831ffac" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">```
<span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">class</span><span style="color: #000000;"> IFSStageViewModel : INotifyPropertyChanged
{
   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> Canvas Stage {</span><span style="color: #0000FF;">get</span><span style="color: #000000;">;</span><span style="color: #0000FF;">set</span><span style="color: #000000;">;}

   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">int</span><span style="color: #000000;"> NumStageItems
   {
       </span><span style="color: #0000FF;">get</span><span style="color: #000000;"> { </span><span style="color: #0000FF;">return</span><span style="color: #000000;"> Stage </span><span style="color: #000000;">!=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">null</span><span style="color: #000000;"> </span><span style="color: #000000;">?</span><span style="color: #000000;"> Stage.Children.Count : </span><span style="color: #800080;">0</span><span style="color: #000000;">;  }
   }

   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> IFSStageViewModel()
   {
       App.MessageBus.GetEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">Messages.AddIFSControl</span><span style="color: #000000;">></span><span style="color: #000000;">().Subscribe(AddIFSControl, </span><span style="color: #0000FF;">true</span><span style="color: #000000;">);
       App.MessageBus.GetEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">Messages.RemoveIFSControl</span><span style="color: #000000;">></span><span style="color: #000000;">().Subscribe(RemoveIFSControl, </span><span style="color: #0000FF;">true</span><span style="color: #000000;">);
       App.MessageBus.GetEvent</span><span style="color: #000000;"><</span><span style="color: #000000;">Messages.Iterate</span><span style="color: #000000;">></span><span style="color: #000000;">().Subscribe(Iterate, </span><span style="color: #0000FF;">true</span><span style="color: #000000;">);
   }

   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">void</span><span style="color: #000000;"> Iterate(</span><span style="color: #0000FF;">bool</span><span style="color: #000000;"> isIteration)
   {
       OnPropertyChanged(</span><span style="color: #800000;">"</span><span style="color: #800000;">NumStageItems</span><span style="color: #800000;">"</span><span style="color: #000000;">);
   }

   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">void</span><span style="color: #000000;"> AddIFSControl(IFSControl newIFS)
   {
       Stage.Children.Add(newIFS);
   }

   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">void</span><span style="color: #000000;"> RemoveIFSControl(IFSControl oldIFS)
   {
       Stage.Children.Remove(oldIFS);
   }

   </span><span style="color: #0000FF;">protected</span><span style="color: #000000;"> </span><span style="color: #0000FF;">virtual</span><span style="color: #000000;"> </span><span style="color: #0000FF;">void</span><span style="color: #000000;"> OnPropertyChanged(</span><span style="color: #0000FF;">string</span><span style="color: #000000;"> propertyName)
   {
       </span><span style="color: #0000FF;">if</span><span style="color: #000000;"> (</span><span style="color: #0000FF;">string</span><span style="color: #000000;">.IsNullOrEmpty(propertyName)) </span><span style="color: #0000FF;">return</span><span style="color: #000000;">;

       </span><span style="color: #0000FF;">if</span><span style="color: #000000;"> (PropertyChanged </span><span style="color: #000000;">!=</span><span style="color: #000000;"> </span><span style="color: #0000FF;">null</span><span style="color: #000000;">)
       {
           PropertyChanged(</span><span style="color: #0000FF;">this</span><span style="color: #000000;">, </span><span style="color: #0000FF;">new</span><span style="color: #000000;"> PropertyChangedEventArgs(propertyName));
       }
   }

   </span><span style="color: #0000FF;">public</span><span style="color: #000000;"> </span><span style="color: #0000FF;">event</span><span style="color: #000000;"> PropertyChangedEventHandler PropertyChanged;
}</span>
```

</div>It starts with a XAML Canvas called “Stage” which will be assigned to the Canvas on the MainPage where we want the fractal to appear. There is also an integer called NumStageItems – this will be bound to a TextBlock to simply display the current number of IFSContentControls are currently contained in the “Stage”.

In the constructor you will see that three different Messages are subscribed to – that is, all three Messages that we have defined.

For AddIFSControl the ViewModel will simply add the sent control to the Canvas. Likewise for RemoveIFSControl the sent control will be removed from the Stage.

For Iterate all we end up doing is calling OnPropertyChanged for NumStageItems. Because of the binding in Silverlight, and because our ViewModel implements INotifyPropertyChanged, this will cause the TextBlock in our View/MainPage to be refreshed with the new “get” value, which is simply the number of children in the “Stage” Canvas.

Next we will see how this works for the Serpinski Triangle / Gasket – and see if it will work for a more complex set of iterations a Barnsley Fern.

45. [Part 1 – Fractals with TransformGroup and MessageBus](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-with-TransformGroup-and-MessageBus.aspx)
46. [Part 2 – Automating transformations by creating an IFS Content Control](http://blog.bruceabernethy.com/post/Silverlight-Kata-IFS-Fractals-Automating-the-Transforms.aspx)
47. Part 3 – Wiring up the Iterations using a basic MessageBus implementation.
48. Part 4 – But will it work for a fractal Fern?
49. Part 5 – Lessons Learned (aka limitations of the MessageBus and recursion in Silverlight)