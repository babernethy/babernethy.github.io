---
title: 'Silverlight Kata: IFS Fractals: The MessageBus'
date: '2010-02-05T03:20:13+00:00'
dsq_thread_id:
    - '518626049'
category: "development"
tags: ["silverlight", "development"]
redirect_from:
  - /silverlight-kata-ifs-fractals-the-messagebus/
---

We are almost done with this application. What started with [Part 1 ](/silverlight-kata-ifs-fractals-with-transformgroup-and-messagebus/)(intro to Fractals and the Silverlight experiment) and continued with [Part 2](/silverlight-kata-ifs-fractals-automating-the-transforms/) (creating the IFSContentControl) now gets a MessageBus to help communicate to and from the different controls

The EventAggregator and MessageBus patterns have been [described as a pattern](http://martinfowler.com/eaaDev/EventAggregator.html) and [discussed for a while](http://www.enterpriseintegrationpatterns.com/MessageBus.html) and recently implemented by several different frameworks within Silverlight. The basic idea is to decouple messages for common functions from specific classes. If there is a common set of Messages, and a shared MessageBus, then objects with access to the bus and messages can “subscribe” to the messages that they want to “hear” and “publish” messages that they want to send out.

A more detailed description of this particular implementation [as described by the Microsoft Patterns &amp; Practices](http://msdn.microsoft.com/en-us/library/ms978583.aspx) group implemented as [EventAggregator](http://msdn.microsoft.com/en-us/library/dd458918.aspx). We will use the EventAggregator for our MessageBus and CompositePresentationEvent from the Microsoft.Practices namespace described here.

## Which Messages?

So, then, what are the messages that we will want to have in this application?

“Iterate” is the big and obvious one. We may, for example, want to press a Button and have it Publish the “Iterate” Message to the MessageBus. Then, we’ll want our IFSContentControls to Subscribe to the “Iterate” message and have them generate the next generation of the fractal.

So to start out we’d have this …

[![messagebus1](/assets/images/messagebus1_thumb.png "messagebus1")](/assets/images/messagebus1.png)

The IFSContentControl would clone itself and apply each transform (3 in this example). These new controls would then also Subscribe to the “Iterate” Message.

[![messagebus2](/assets/images/messagebus2_thumb.png "messagebus2")](/assets/images/messagebus2.png)

So the next click of the button that publishes the message will now be “heard” by three different objects ….

[![messagebus3](/assets/images/messagebus3_thumb.png "messagebus3")](/assets/images/messagebus3.png)

And so on … and so on …

To fully make this work though, we’ll need to (1) get the new controls onto our Container/Canvas. And, in the case of these fractals, the original control does not “survive” the iteration and only “lives” through one generation.

So we’ll add two more Messages: (1) AddIFSControl (to add the new IFSControls to the Container) and (2) RemoveIFSControl (to remove the current control from the Container once the Iteration is complete).

[![messagebus4](/assets/images/messagebus4_thumb.png "messagebus4")](/assets/images/messagebus4.png)

So our messages end up looking like this …

```csharp
using Microsoft.Practices.Composite.Presentation.Events;

public class Messages
{
   public class Iterate : CompositePresentationEvent<bool> { }
   public class AddIFSControl : CompositePresentationEvent<IFSControl> { }
   public class RemoveIFSControl : CompositePresentationEvent<IFSControl> { }
}
```

The CompositePresentationEvent is a generic class that takes a strongly typed object. In the case of the “Iterate” message, there really isn’t a type we need to send up (there is no data payload that is needed to process the “Iterate” message). In the case of the AddIFSControl and RemoveIFSControl messages, we will send along the IFSControls themselves in order to be processed.

## Where is the MessageBus?

For this application, it is easiest to implement the MessageBus at the highest point possible in the Application itself. So in our App.xaml.cs file we just add this …

```csharp
using Microsoft.Practices.Composite.Events;

public partial class App : Application
{
   public static IEventAggregator MessageBus = new EventAggregator();
```

Really that is all it takes to set up the MessageBus.

## Publishing the Messages

So, now how do we wire up the Button to publish the iterate event. In the codebehind of the MainPage (or ViewModel if you’ve wired it up) we can add code something like this.

```csharp
private void Button_Click(object sender, RoutedEventArgs e)
{
  App.MessageBus.GetEvent<Messages.Iterate>().Publish(true);
}
```

It is important to notice that there is nothing special

about the “Button” itself – we aren’t using any of its events or properties to do this work or propagate this message. You could just as easily set up a DispatherTimer and have it call “Iterate” every 60 seconds or so …

```csharp
void IterateMe_Tick(object sender, EventArgs e)
{
  App.MessageBus.GetEvent<Messages.Iterate>().Publish(true);
}
```

## Subscribing to the Messages

So now we need to add code to the IFSContentControls to Subscribe to the Iterate Message.

```csharp
public IFSControl()
{
  App.MessageBus.GetEvent<Messages.Iterate>().Subscribe(DoIteration, true);
```

To wire this up we need to create a public method that takes the same payload as the message itself – in this case, Iterate sends a boolean. So we need a public method that takes a boolean.

```csharp
private void DoIteration(bool isTrue)
{
  foreach (var ifst in IFSTransforms.Transforms)
  {
      var newControl = new IFSControl
      {
          Content = Copy(this),
          IFSTransforms = this.IFSTransforms,
          RenderTransform = ifst.IFSTransformGroup
      };
      App.MessageBus.GetEvent<Messages.AddIFSControl>().Publish(newControl);
  }
  App.MessageBus.GetEvent<Messages.Iterate>().Unsubscribe(DoIteration);
  App.MessageBus.GetEvent<Messages.RemoveIFSControl>().Publish(this);
}
```

So IFSControl is now set up to Subscribe to the Iterate event – it will then call DoIteration() when it receives the message. DoIteration() will iterate through all the different transforms, create a new IFSControl which is a clone/copy of the current control, and then Publish the AddIFSControl message with the new control as the payload. In our example this will happen three times for each iteration, so three new controls will be sent in messages.

The last two lines are interesting as well. Once the new controls are created it is time for the current control to request that it be removed from the container – it has done its work and it is time to move on. First we Unsubscribe from the DoIteration Message (always good to not leave loose ends) and then Publish the RemoveIFSControl message with “this” as the payload (i.e., the current control). It is thus requesting to be removed from the container.

## Container Messages

In this example the DataContext of our MainPage will be a class called the IFSStageViewModel. This class encapsulates all the information and logic that will be needed for the user interface of our application.

```csharp
public class IFSStageViewModel : INotifyPropertyChanged
{
   public Canvas Stage {get;set;}

   public int NumStageItems
   {
       get { return Stage != null ? Stage.Children.Count : 0;  }
   }

   public IFSStageViewModel()
   {
       App.MessageBus.GetEvent<Messages.AddIFSControl>().Subscribe(AddIFSControl, true);
       App.MessageBus.GetEvent<Messages.RemoveIFSControl>().Subscribe(RemoveIFSControl, true);
       App.MessageBus.GetEvent<Messages.Iterate>().Subscribe(Iterate, true);
   }

   public void Iterate(bool isIteration)
   {
       OnPropertyChanged("NumStageItems");
   }

   public void AddIFSControl(IFSControl newIFS)
   {
       Stage.Children.Add(newIFS);
   }

   public void RemoveIFSControl(IFSControl oldIFS)
   {
       Stage.Children.Remove(oldIFS);
   }

   protected virtual void OnPropertyChanged(string propertyName)
   {
       if (string.IsNullOrEmpty(propertyName)) return;

       if (PropertyChanged != null)
       {
           PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
       }
   }

   public event PropertyChangedEventHandler PropertyChanged;
}
```

It starts with a XAML Canvas called “Stage” which will be assigned to the Canvas on the MainPage where we want the fractal to appear. There is also an integer called NumStageItems – this will be bound to a TextBlock to simply display the current number of IFSContentControls are currently contained in the “Stage”.

In the constructor you will see that three different Messages are subscribed to – that is, all three Messages that we have defined.

For AddIFSControl the ViewModel will simply add the sent control to the Canvas. Likewise for RemoveIFSControl the sent control will be removed from the Stage.

For Iterate all we end up doing is calling OnPropertyChanged for NumStageItems. Because of the binding in Silverlight, and because our ViewModel implements INotifyPropertyChanged, this will cause the TextBlock in our View/MainPage to be refreshed with the new “get” value, which is simply the number of children in the “Stage” Canvas.

Next we will see how this works for the Serpinski Triangle / Gasket – and see if it will work for a more complex set of iterations a Barnsley Fern.

45. [Part 1 – Fractals with TransformGroup and MessageBus](/silverlight-kata-ifs-fractals-with-transformgroup-and-messagebus/)
46. [Part 2 – Automating transformations by creating an IFS Content Control](/silverlight-kata-ifs-fractals-automating-the-transforms/)
47. Part 3 – Wiring up the Iterations using a basic MessageBus implementation.
48. Part 4 – But will it work for a fractal Fern?
49. Part 5 – Lessons Learned (aka limitations of the MessageBus and recursion in Silverlight)
