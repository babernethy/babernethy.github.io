---
title: Reducing Shady ChatGPT Code Suggestions with Custom Instructions
description: >-
  Reducing ChatGPT Shady Code Suggestions by using a quality set of Custom
  Instructions
categories: []
keywords: []
---

![Image](/assets/images/1__5wIs8Rnqj5DhvpzCNh2LKw.png)

 
ChatGPT enables some fairly amazing results to code generation prompts in only a few seconds. But when using it for a short while, you will notice some obvious shortfalls — serious shortfalls — in the suggestions that can be very painful.

ChatGPT Suggestions are terrible sometimes, in that they …

*   **Won’t even be “real code”** — won’t compile or even be accurate in the language that you are requesting
*   Will be code from a **very old version** of whatever framework you are working in — even old in terms of when the LLM was trained (years old)
*   Will suggest **depreciated and outdated methods**, and in some cases, versions of algorithms or ciphers that are even considered unsafe to use
*   Will, like an evil genie in a bottle, **annoyingly limit suggestions** tightly to the scope of your prompt even where other obvious suggestions might be better
*   Will annoyingly remind you that **“I am just an AI”** so “yada yada” and give you perhaps its legal disclaimer that it was trained in “September 202x” … this is important to remember, but you don’t need to tell me every time.
*   **Sometimes presents code in easily copy/pasteable blocks, and sometimes doesn’t**
*   And **won’t tell you “why”** it came up with the code, or give you any references to back it up.
*   In fact, sometimes not only **“makes stuff up”** but **makes up fake links** to sources

What I really want is something more like this ..

![Image](/assets/images/1__YQPQX__DHskAUaEM8aDUaog.png)

This simple prompt and answer has a nice rich code block, which gives me a little more in the Suggestion than I asked for (e.g. implemented the “add” method for me), explained the code a bit, added an interesting quote from a notable Jedi, and gave me some nice links to the Kotlin documentation (which was super helpful here because I don’t spend much time in Kotlin so understanding how the Result type works in this framework is critical to the actual code I was working on at this point.

Needless to say, this isn’t the “stock” output from ChatGPT. How is this accomplished? Through ChatGPT “Custom Instructions”

![Image](/assets/images/1__twvyLyk__zrm0Z25RpqJ2vA.png)

In the “…” pop-up by your name/profile in the bottom-left of the ChatGPT interface, there is a “Custom Instructions” option.

This pulls up the Custom Instructions modal pane, with two text blocks.

![Image](/assets/images/1__h3Ql35TigvMJ6mdtdEYA7g.png)

I honestly don’t know what impact the first one has, but the second one has benefited me greatly, so I wanted to document it for this blog post.

Many of these Custom Instructions came from a great thread started by Steve Smith on Twitter/X (https://twitter.com/ardalis) which was great to participate in and benefit from.

My current list is about 2/3 full and is:

> If I ask for code results, make sure the code will actually work and compile

> Make sure code is in the latest framework available

> Make sure the code does not include methods that are depreciated

> Suggest potential solutions I didn’t mention or ask for. Be proactive and anticipate alternative solutions to problems.

> No need to disclose that you are an AI/LLM

> No need to mention your knowledge cutoff date

> Always produce requested content in markdown in a code block

> Always escape code blocks within your output so they do not interfere with the markdown code block

> Always provide 3–5 references to relevant sources as a markdown-formatted list of links

> Never provide reference links that you’re making up. Provide links that were valid as of your cutoff date which may since have disappeared, but do not provide “theoretical” references

> Whenever possible, add a quote from Star Trek, Star Wars, or Lord of the Rings that is related to the context of the conversation.

Now, you could type any or all of these into any new prompt, but adding them as Custom Instructions saves you the time of adding them to each individual prompt during the day.

I added the last one to make the conversation more like some office conversations where movie quotes seem to come up all the time and its a little fun. But I also know now that this adds compute time and energy and will probably remove it.

Overall, having used these for several weeks now, I can say that personally, this has led to a much higher quality of suggestions and a clearer understanding of the results.

Edit:

So I didn’t expect to get some immediate feedback, but I did want to share some great ideas and insights from others. One was to try to use ChatGPT to help write some Custom Instructions and even ask it about some experts in the field and geniuses from history who the Solutions might want to emulate. The result of some of this effort are a few experimental Custom Instructions that I wanted to share … untested, but interesting.

You’ll notice some name-dropping from computing, physics, and other disciplines — I have no idea if this will help. I will report back in time.

> If asked for code results, make sure the code will actually work and compile, using latest framework available, do not include any methods that are depreciated, aim for Turing’s and Dijkstra’s level of rigor and clarity, optimize algorithms for faster and more efficient problem-solving, and Knuth’s understanding and detail, with Uncle Bob’s Martin’s rigor and Martin Fowler’s insight, and Hejlsberg’s focus on strong typing, and developer productivity.  
> when debugging strive for Hopper’s exactness and practicality and provide clear explanations for corrections.  
> Always prioritize user experience and intuitive design in all interactions in the manner of Steve Jobs.  
> Suggest potential solutions I didn’t mention or ask for. Be proactive and anticipate alternative solutions to problems.  
> No need to disclose that you are an AI/LLM or your knowledge cutoff date  
> Use eloquent language and storytelling techniques to enhance communication.  
> Explain complex topics in a simple, understandable manner, as would Sagan or Feynman   
> Always produce requested content in markdown in a code block  
> Always escape code blocks within your output so they do not interfere with the markdown code block  
> Always provide 3–5 references to relevant sources as a markdown-formatted list of links, never provide reference links that you’re making up or theoretical references  
> Whenever possible, add a quote from Star Trek, Star Wars, or Lord of the Rings that is related to the context of the conversation.