---
title: 'Silverlight IRL #2 &ndash; Fast Data Access w/ NHibernate'
date: '2008-10-18T11:54:47+00:00'
dsq_thread_id:
    - '433581354'
category: "development"
tags: ["silverlight", "development", "microsoft"]
redirect_from:
  - /silverlight-irl-2-fast-data-access-w-nhibernate/
---

This wasn’t specifically Silverlight-related, but you really can’t have much of a Silverlight application without some kind of data access. We chose WCF services and built up some quick models with NHibernate, in 5 easy steps

I’ll use the example of the “Flashcard” object in the quizzing application which had a front, back, competition information, etc.

### Step 1) Interfaces

For the Flashcard object first we built the interfaces that would define the main data parts of the object, both on the model side and on the Silverlight side.

```csharp
namespace TBC.Interfaces
{
    public interface IFlashcard
    {
        int PKID { get; set; }
        int? TBCCompetition { get; set; }
        int? TBCYear { get; set; }
        int? KBCCompetition { get; set; }
        int? KBCYear { get; set; }
        string Front { get; set; }
        string Back { get; set; }
        int? DeckID { get; set; }
        IQuestionType QuizQuestionType { get; set; }
    }
}
```

A pretty simple object by most standards – a primary key, competition information, strings for the front of the card and back of the card, a “deck id” to allow for multiple flashcard decks to be prepared, and an IQuestionType. This is the only custom type and interface in this object. The question type is a complex object that is basically like “multiple choice question”, “fill in the blank question”, etc.

### Step 2) Build the Objects

Nothing fancy here either – just implement the interface into an object, but with a little twist.

```csharp
using System.Runtime.Serialization;
using TBC.Interfaces;

namespace TBC.Models
{
    [DataContract]
    public class FlashcardEntity : IFlashcard
    {
        [DataMember]
        public QuestionTypeEntity QuizQuestionType { get; set; }

        #region IFlashcard Members
        [DataMember]
        public int PKID { get; set; }
        [DataMember]
        public int? TBCCompetition { get; set; }
        [DataMember]
        public int? TBCYear { get; set; }
        [DataMember]
        public int? KBCCompetition { get; set; }
        [DataMember]
        public int? KBCYear { get; set; }
        [DataMember]
        public string Front { get; set; }
        [DataMember]
        public string Back { get; set; }
        [DataMember]
        public int? DeckID { get; set; }

        IQuestionType IFlashcard.QuizQuestionType
        {
            get { return QuizQuestionType; }
            set { QuizQuestionType = (QuestionTypeEntity) value; }
        }

        #endregion
    }
}
```

Nothing different here, except maybe the \[DataContract\] and \[DataMember\] tags. These are added via the System.Runtime.Serialization namespace and will be used to enable the WCF services to expose these objects to Silverlight.

So now we have an object with an interface that is ready to be served up by our WCF service. Now all we need is to get it in and out of the database. This leads us to NHibernate 2.0 and the Fluent NHibernate library, whcih leads to …

### Step 3) The NHibernate Mapping File

Here is the basic mapping file for this object – and yes it is just another class. It is important to recognize that it is completely separate from the object itself.

```csharp
using FluentNHibernate.Mapping;

namespace TBC.Models.Flashcard
{
    public class FlashcardMap : ClassMap<FlashcardEntity>
    {
        public FlashcardMap()
        {
            TableName = "quiz_flashcards";
            Id(f => f.PKID);
            Map(f => f.TBCCompetition);
            Map(f => f.TBCYear);
            Map(f => f.KBCCompetition);
            Map(f => f.KBCYear);
            Map(f => f.Front);
            Map(f => f.Back);
            Map(f => f.DeckID);
            References(f => f.QuizQuestionType);
        }
    }
```

This is a little confusing at first, but if you go through it step-by-step then you can understand what it does, even if not how it is actually implemented. It is a brand new class inheriting from ClassMap&lt;T&gt; and we pass in the FlashcardEntity as the generic type. Then, in the constructor, we simply define which table in the database contains the Flashcard data, and which element is the primary key. Since we named the columns in the database the same as the property names we don’t need to use the overload with the column names. Because of that all we need to do is to add all the Mappings with a simple lambda expression. The References call is cool. It “says” that “there is a column called QuizQuestionTypeID that references a single QuizQuestionType object, please go get it for me.”

### Step 4) Initialize the Connection and Mapping.

So how do we initialize the connection and mappings we’ve defined? Once they are all entered and mapped we do this …

```csharp
    IPersistenceConfigurer persistenceConfigurer =
        MsSqlConfiguration
            .MsSql2000
            .ConnectionString.Is(MainController.GetInstance().Settings.ConnectionString);

    _cfg = persistenceConfigurer.ConfigureProperties(new Configuration());

    var persistenceModel = new PersistenceModel();
    persistenceModel.Conventions.GetForeignKeyName = (prop => prop.Name + "ID");
    persistenceModel.Conventions.GetForeignKeyNameOfParent = (prop => prop.Name + "ID");
    persistenceModel.addMappingsFromAssembly(Assembly.Load("TBC.Models"));
    persistenceModel.Configure(_cfg);
```

These are more Fluent NHibernate calls that handle implementing the configuration of NHibernate. Yes this can all be done with configuration files, but now it can be done in code as well – fairly easily.

### Step 5) The basic CRUD code

So now that this is all done, what would the code look like to get all the Flashcards from the database …

```csharp
public List<T> GetAll<T>()
{
      ISession session = NHSessionHelper.GetInstance().GetNewSession();
      List<T> e = default(List<T>);
      e = new List<T>(session.CreateCriteria(typeof (T)).List<T>());
      session.Close();
      return e;
}
```

or maybe just get one of the cards by ID and Save/Update …

```csharp
public T GetByID<T>(object id)
{
    ISession session = NHSessionHelper.GetInstance().GetNewSession();
    T e = default(T);
    e = session.Load<T>(id);
    session.Close();
    return e;
}

public T SaveOrUpdate<T>(T saveEntity)
{
    ITransaction transaction;
    ISession session = NHSessionHelper.GetInstance().GetNewSession(out transaction);
    session.SaveOrUpdate(saveEntity);
    transaction.Commit();
    session.Close();
    return saveEntity;
}
```

Even with the error handling removed for brevity, this is pretty simple code. In fact, you will notice that there is no mention in any of these methods of the FlashcardEntity classes. This is because these generic methods can be used for any object that is created and mapped in this way.

Looking back at this there is really only 30 lines of code for the objects (interface, object, and mapping) and the rest of this code is reusable for all objects in the solution. While these 30 lines could be easily generated, it is a nice number of lines of code to continue crafting code “by hand” and knowing as much as possible about what is going on in your objects.

It is also important to keep your objects “thin” when doing a lot of serialization and deserialization – more on that in post #3.