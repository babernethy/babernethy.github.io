---
title: 'Silverlight IRL #2 &ndash; Fast Data Access w/ NHibernate'
date: '2008-10-18T11:54:47+00:00'
dsq_thread_id:
    - '433581354'
et_enqueued_post_fonts:
    - 'a:2:{s:6:"family";a:3:{s:12:"et-gf-roboto";s:91:"Roboto:100,100italic,300,300italic,regular,italic,500,500italic,700,700italic,900,900italic";s:22:"et-gf-roboto-condensed";s:59:"Roboto+Condensed:300,300italic,regular,italic,700,700italic";s:17:"et-gf-roboto-slab";s:51:"Roboto+Slab:100,200,300,regular,500,600,700,800,900";}s:6:"subset";a:7:{i:0;s:9:"latin-ext";i:1;s:5:"greek";i:2;s:9:"greek-ext";i:3;s:10:"vietnamese";i:4;s:8:"cyrillic";i:5;s:5:"latin";i:6;s:12:"cyrillic-ext";}}'
---

This wasn’t specifically Silverlight-related, but you really can’t have much of a Silverlight application without some kind of data access. We chose WCF services and built up some quick models with NHibernate, in 5 easy steps

I’ll use the example of the “Flashcard” object in the quizzing application which had a front, back, competition information, etc.

### Step 1) Interfaces

For the Flashcard object first we built the interfaces that would define the main data parts of the object, both on the model side and on the Silverlight side.

<div class="csharpcode">```
<span class="lnum">   1:  </span><span class="kwrd">namespace</span> TBC.Interfaces
```

```
<span class="lnum">   2:  </span>{
```

```
<span class="lnum">   3:  </span>    <span class="kwrd">public</span> <span class="kwrd">interface</span> IFlashcard
```

```
<span class="lnum">   4:  </span>    {
```

```
<span class="lnum">   5:  </span>        <span class="kwrd">int</span> PKID { get; set; }
```

```
<span class="lnum">   6:  </span>        <span class="kwrd">int</span>? TBCCompetition { get; set; }
```

```
<span class="lnum">   7:  </span>        <span class="kwrd">int</span>? TBCYear { get; set; }
```

```
<span class="lnum">   8:  </span>        <span class="kwrd">int</span>? KBCCompetition { get; set; }
```

```
<span class="lnum">   9:  </span>        <span class="kwrd">int</span>? KBCYear { get; set; }
```

```
<span class="lnum">  10:  </span>        <span class="kwrd">string</span> Front { get; set; }
```

```
<span class="lnum">  11:  </span>        <span class="kwrd">string</span> Back { get; set; }
```

```
<span class="lnum">  12:  </span>        <span class="kwrd">int</span>? DeckID { get; set; }
```

```
<span class="lnum">  13:  </span>        IQuestionType QuizQuestionType { get; set; }
```

```
<span class="lnum">  14:  </span>    }
```

```
<span class="lnum">  15:  </span>}
```

</div><style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>A pretty simple object by most standards – a primary key, competition information, strings for the front of the card and back of the card, a “deck id” to allow for multiple flashcard decks to be prepared, and an IQuestionType. This is the only custom type and interface in this object. The question type is a complex object that is basically like “multiple choice question”, “fill in the blank question”, etc.

### Step 2) Build the Objects

Nothing fancy here either – just implement the interface into an object, but with a little twist.

<div class="csharpcode">```
<span class="lnum">   1:  </span><span class="kwrd">using</span> System.Runtime.Serialization;
```

```
<span class="lnum">   2:  </span><span class="kwrd">using</span> TBC.Interfaces;
```

```
<span class="lnum">   3:  </span> 
```

```
<span class="lnum">   4:  </span><span class="kwrd">namespace</span> TBC.Models
```

```
<span class="lnum">   5:  </span>{
```

```
<span class="lnum">   6:  </span>    [DataContract]
```

```
<span class="lnum">   7:  </span>    <span class="kwrd">public</span> <span class="kwrd">class</span> FlashcardEntity : IFlashcard
```

```
<span class="lnum">   8:  </span>    {
```

```
<span class="lnum">   9:  </span>        [DataMember]
```

```
<span class="lnum">  10:  </span>        <span class="kwrd">public</span> QuestionTypeEntity QuizQuestionType { get; set; }
```

```
<span class="lnum">  11:  </span> 
```

```
<span class="lnum">  12:  </span>        <span class="preproc">#region</span> IFlashcard Members
```

```
<span class="lnum">  13:  </span>        [DataMember]
```

```
<span class="lnum">  14:  </span>        <span class="kwrd">public</span> <span class="kwrd">int</span> PKID { get; set; }
```

```
<span class="lnum">  15:  </span>        [DataMember]
```

```
<span class="lnum">  16:  </span>        <span class="kwrd">public</span> <span class="kwrd">int</span>? TBCCompetition { get; set; }
```

```
<span class="lnum">  17:  </span>        [DataMember]
```

```
<span class="lnum">  18:  </span>        <span class="kwrd">public</span> <span class="kwrd">int</span>? TBCYear { get; set; }
```

```
<span class="lnum">  19:  </span>        [DataMember]
```

```
<span class="lnum">  20:  </span>        <span class="kwrd">public</span> <span class="kwrd">int</span>? KBCCompetition { get; set; }
```

```
<span class="lnum">  21:  </span>        [DataMember]
```

```
<span class="lnum">  22:  </span>        <span class="kwrd">public</span> <span class="kwrd">int</span>? KBCYear { get; set; }
```

```
<span class="lnum">  23:  </span>        [DataMember]
```

```
<span class="lnum">  24:  </span>        <span class="kwrd">public</span> <span class="kwrd">string</span> Front { get; set; }
```

```
<span class="lnum">  25:  </span>        [DataMember]
```

```
<span class="lnum">  26:  </span>        <span class="kwrd">public</span> <span class="kwrd">string</span> Back { get; set; }
```

```
<span class="lnum">  27:  </span>        [DataMember]
```

```
<span class="lnum">  28:  </span>        <span class="kwrd">public</span> <span class="kwrd">int</span>? DeckID { get; set; }
```

```
<span class="lnum">  29:  </span> 
```

```
<span class="lnum">  30:  </span>        IQuestionType IFlashcard.QuizQuestionType
```

```
<span class="lnum">  31:  </span>        {
```

```
<span class="lnum">  32:  </span>            get { <span class="kwrd">return</span> QuizQuestionType; }
```

```
<span class="lnum">  33:  </span>            set { QuizQuestionType = (QuestionTypeEntity) <span class="kwrd">value</span>; }
```

```
<span class="lnum">  34:  </span>        }
```

```
<span class="lnum">  35:  </span> 
```

```
<span class="lnum">  36:  </span>        <span class="preproc">#endregion</span>
```

```
<span class="lnum">  37:  </span>    }
```

```
<span class="lnum">  38:  </span>}
```

</div><style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>Nothing different here, except maybe the \[DataContract\] and \[DataMember\] tags. These are added via the System.Runtime.Serialization namespace and will be used to enable the WCF services to expose these objects to Silverlight.

So now we have an object with an interface that is ready to be served up by our WCF service. Now all we need is to get it in and out of the database. This leads us to NHibernate 2.0 and the Fluent NHibernate library, whcih leads to …

### Step 3) The NHibernate Mapping File

Here is the basic mapping file for this object – and yes it is just another class. It is important to recognize that it is completely separate from the object itself.

<div class="csharpcode">```
<span class="lnum">   1:  </span><span class="kwrd">using</span> FluentNHibernate.Mapping;
```

```
<span class="lnum">   2:  </span> 
```

```
<span class="lnum">   3:  </span><span class="kwrd">namespace</span> TBC.Models.Flashcard
```

```
<span class="lnum">   4:  </span>{
```

```
<span class="lnum">   5:  </span>    <span class="kwrd">public</span> <span class="kwrd">class</span> FlashcardMap : ClassMap<FlashcardEntity>
```

```
<span class="lnum">   6:  </span>    {
```

```
<span class="lnum">   7:  </span>        <span class="kwrd">public</span> FlashcardMap()
```

```
<span class="lnum">   8:  </span>        {
```

```
<span class="lnum">   9:  </span>            TableName = <span class="str">"quiz_flashcards"</span>;
```

```
<span class="lnum">  10:  </span>            Id(f => f.PKID);
```

```
<span class="lnum">  11:  </span>            Map(f => f.TBCCompetition);
```

```
<span class="lnum">  12:  </span>            Map(f => f.TBCYear);
```

```
<span class="lnum">  13:  </span>            Map(f => f.KBCCompetition);
```

```
<span class="lnum">  14:  </span>            Map(f => f.KBCYear);
```

```
<span class="lnum">  15:  </span>            Map(f => f.Front);
```

```
<span class="lnum">  16:  </span>            Map(f => f.Back);
```

```
<span class="lnum">  17:  </span>            Map(f => f.DeckID);
```

```
<span class="lnum">  18:  </span>            References(f => f.QuizQuestionType);
```

```
<span class="lnum">  19:  </span>        }
```

```
<span class="lnum">  20:  </span>    }
```

</div><style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>This is a little confusing at first, but if you go through it step-by-step then you can understand what it does, even if not how it is actually implemented. It is a brand new class inheriting from ClassMap&lt;T&gt; and we pass in the FlashcardEntity as the generic type. Then, in the constructor, we simply define which table in the database contains the Flashcard data, and which element is the primary key. Since we named the columns in the database the same as the property names we don’t need to use the overload with the column names. Because of that all we need to do is to add all the Mappings with a simple lambda expression. The References call is cool. It “says” that “there is a column called QuizQuestionTypeID that references a single QuizQuestionType object, please go get it for me.”

### Step 4) Initialize the Connection and Mapping.

So how do we initialize the connection and mappings we’ve defined? Once they are all entered and mapped we do this …

<div class="csharpcode">```
<span class="lnum">   1:  </span>    IPersistenceConfigurer persistenceConfigurer =
```

```
<span class="lnum">   2:  </span>        MsSqlConfiguration
```

```
<span class="lnum">   3:  </span>            .MsSql2000
```

```
<span class="lnum">   4:  </span>            .ConnectionString.Is(MainController.GetInstance().Settings.ConnectionString);
```

```
<span class="lnum">   5:  </span> 
```

```
<span class="lnum">   6:  </span>    _cfg = persistenceConfigurer.ConfigureProperties(<span class="kwrd">new</span> Configuration());
```

```
<span class="lnum">   7:  </span> 
```

```
<span class="lnum">   8:  </span>    var persistenceModel = <span class="kwrd">new</span> PersistenceModel();
```

```
<span class="lnum">   9:  </span>    persistenceModel.Conventions.GetForeignKeyName = (prop => prop.Name + <span class="str">"ID"</span>);
```

```
<span class="lnum">  10:  </span>    persistenceModel.Conventions.GetForeignKeyNameOfParent = (prop => prop.Name + <span class="str">"ID"</span>);
```

```
<span class="lnum">  11:  </span>    persistenceModel.addMappingsFromAssembly(Assembly.Load(<span class="str">"TBC.Models"</span>));
```

```
<span class="lnum">  12:  </span>    persistenceModel.Configure(_cfg);
```

</div><style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>These are more Fluent NHibernate calls that handle implementing the configuration of NHibernate. Yes this can all be done with configuration files, but now it can be done in code as well – fairly easily.

### Step 5) The basic CRUD code

So now that this is all done, what would the code look like to get all the Flashcards from the database …

<div class="csharpcode">```
<span class="lnum">   1:  </span><span class="kwrd">public</span> List<T> GetAll<T>()
```

```
<span class="lnum">   2:  </span>{
```

```
<span class="lnum">   3:  </span>      ISession session = NHSessionHelper.GetInstance().GetNewSession();
```

```
<span class="lnum">   4:  </span>      List<T> e = <span class="kwrd">default</span>(List<T>);
```

```
<span class="lnum">   5:  </span>      e = <span class="kwrd">new</span> List<T>(session.CreateCriteria(<span class="kwrd">typeof</span> (T)).List<T>());
```

```
<span class="lnum">   6:  </span>      session.Close();
```

```
<span class="lnum">   7:  </span>      <span class="kwrd">return</span> e;
```

```
<span class="lnum">   8:  </span>}
```

</div><style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>or maybe just get one of the cards by ID and Save/Update …

<div class="csharpcode">```
<span class="lnum">   1:  </span><span class="kwrd">public</span> T GetByID<T>(<span class="kwrd">object</span> id)
```

```
<span class="lnum">   2:  </span>{
```

```
<span class="lnum">   3:  </span>    ISession session = NHSessionHelper.GetInstance().GetNewSession();
```

```
<span class="lnum">   4:  </span>    T e = <span class="kwrd">default</span>(T);
```

```
<span class="lnum">   5:  </span>    e = session.Load<T>(id);
```

```
<span class="lnum">   6:  </span>    session.Close();
```

```
<span class="lnum">   7:  </span>    <span class="kwrd">return</span> e;
```

```
<span class="lnum">   8:  </span>}
```

```
<span class="lnum">   9:  </span> 
```

```
<span class="lnum">  10:  </span><span class="kwrd">public</span> T SaveOrUpdate<T>(T saveEntity)
```

```
<span class="lnum">  11:  </span>{
```

```
<span class="lnum">  12:  </span>    ITransaction transaction;
```

```
<span class="lnum">  13:  </span>    ISession session = NHSessionHelper.GetInstance().GetNewSession(<span class="kwrd">out</span> transaction);
```

```
<span class="lnum">  14:  </span>    session.SaveOrUpdate(saveEntity);
```

```
<span class="lnum">  15:  </span>    transaction.Commit();
```

```
<span class="lnum">  16:  </span>    session.Close();
```

```
<span class="lnum">  17:  </span>    <span class="kwrd">return</span> saveEntity;
```

```
<span class="lnum">  18:  </span>}
```

</div><style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>Even with the error handling removed for brevity, this is pretty simple code. In fact, you will notice that there is no mention in any of these methods of the FlashcardEntity classes. This is because these generic methods can be used for any object that is created and mapped in this way.

Looking back at this there is really only 30 lines of code for the objects (interface, object, and mapping) and the rest of this code is reusable for all objects in the solution. While these 30 lines could be easily generated, it is a nice number of lines of code to continue crafting code “by hand” and knowing as much as possible about what is going on in your objects.

It is also important to keep your objects “thin” when doing a lot of serialization and deserialization – more on that in post #3.