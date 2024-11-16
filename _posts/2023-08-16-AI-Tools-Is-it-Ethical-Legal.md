---
title: 'AI Tools: Is it Ethical? Legal?'
description: >-
  Another of the bigger topics recently is the emergence and use of AI tools
  and, specifically, the use of AI tools in software development.
categories: []
keywords: []
---

Another of the bigger topics recently is the emergence and use of AI tools and, specifically, the use of AI tools in software development. As part of this, there have been a series of questions that have needed answering, which can be summarized as follows:

*   What can the AI tools do? What are devs actually using them for?
*   Which tool(s) are being used and picked? and why? using what criteria?
*   **Is it “cheating”? Is it ethical? or legal?**
*   Is it safe? What are the risks? Am I “leaking” information? How does this fit into my SDLC?
*   Does using AI tools mean my work isn’t “original”? is it copyrightable?
*   Will AI replace my job? or other jobs around me?

All important things to think about and discuss … let’s look at one today.

### Is using AI LLM tools ethical or legal?

![Image](/assets/images/1__R75zNz8W8SnLIZ7qrCLZCw.jpeg)

The short answer on the legal front is “unknown” — that this is still being decided. So let’s look at what the arguments are on both sides. There is some very scenarios from the plaintiffs in one of the current [class action lawsuits](https://clarksonlawfirm.com/wp-content/uploads/2023/06/0001.-2023.06.28-OpenAI-Complaint.pdf) against Open AI and ChatGPT (and there are similar suits against Google and Bard)

> Plaintiff P.M.

> 19\. Plaintiff P.M. is and at all relevant times was a resident of the State of California.

> 20\. Plaintiff P.M. is a **director of information technology** and **software engineer** and began using ChatGPT-3.5 on or about February/March 2023. He is a **current user of ChatGPT-3.5 and ChatGPT-4.0**. Plaintiff P.M. accesses the Products from his personal computer, cellular device, and work computer.

So far, hitting pretty close to home — which helps with the connection. Similar career path, user of similar technologies.

> 21\. Plaintiff P.M. engaged with a variety of websites and social media applications prior to 2021. Plaintiff P.M. has had a **Twitter** account since approximately 2011; using it to post content, and re-post other users’ tweets to save and compile information in line with his interests. For many years Plaintiff P.M. had a **Spotify** account which he frequently used to listen to music and create unique playlists. Approximately five (5) years ago, he transitioned to **YouTube music** and Google Play. Prior to 2021, Plaintiff P.M. regularly viewed videos on YouTube, posted content, and commented on other users’ videos. \[…\]

> 22\. Plaintiff P.M. has posted **photos of himself, his family, and friends** on various websites and social media applications, including photos of his children on **Instagram**. He posted photos of himself and friends on online dating websites, such as **OK Cupid** and **Tinder**, approximately eight (8) years ago. He used these dating websites to post significant amounts of **personal information** and exchange messages with prospective romantic partners. He has been using the United Healthcare Insurance Company web portal for over a decade to find providers and review post-appointment works.

It’s enough to say that this person used the internet in a way that it sounds like a lot of people do, in the recent past, which so far isn’t very interesting.

> 23\. Plaintiff P.M. has also posted online about his political views, as well as frequently asked and **answered technical questions** using his professional knowledge on **Stack Overflow** for the last five (5) years in sporadic sprints to accumulate points on the website.

But this is where it starts, and will get to the point. As a developer, many of us participated and participate in online communities. Posting code to Open Source projects, answering questions on Stack Overflow and similar online discussion forums, write blog posts, etc. And have done this under the existing use agreements and context of those sites and communities. All of this without knowing what was about to happen when the AI models were about to be trained on this very same information.

> 24\. **Plaintiff P.M. is concerned** that Defendants have **taken his skills and expertise**, as reflected in his online contributions, and **incorporated them into Products** that could someday **result in professional obsolescence for software engineers like him**.

> 25\. Plaintiff P.M. **reasonably expected** that the information that he exchanged with these websites prior to 2021 would not be intercepted by any third-party looking to compile and use **all his information and data for commercial purposes**. Plaintiff P.M. **did not consent** to the use of his private information by third parties in this manner. Notwithstanding, Defendants **stole Plaintiff P.M.’s personal data** from across this wide swath of online applications and platforms to **train the Products**

I use this example as it is a very good summary of a lot of the more hypothetical and abstract ideas that have been shared in conversations. This well illustrates those issues.

*   People who posted pictures online of anything — be it themselves, their children, mountains, barns, trees — could not have anticipated, nor consent, to have these pictures become training material for a paid product that would produce on-demand images of “a red barn in front of a mountain.” And even more upsetting would be professional photographers or artists who do this for a career and could “result in professional obsolescence” of people like them.
*   The same with answers to software design and coding questions
*   The same with code posted to open-source projects online — and the specific license models that they were posted under (additional lawsuits pending regarding this as well)
*   The same with the curation of music playlists
*   Professional analysis and recommendations of really any kind

In the class action brief, the background goes through the history of OpenAI from its roots as a non-profit company through its evolution into a for-profit company will a multi-billion-dollar valuation, with its “product” based on models trained on data mined from arguably personal data that was never intended for this purpose, and who’s authors and owners/originators did not give their consent to be part of the product, and are certainly not being compensated. Is this ethical?

BUT, isn’t this the internet? Didn’t Google make billions out of “scraping” the internet and cataloging other people’s web pages, and even copyrighted books and other sources for easy search-and-retrieval? Yes, well, sort of. Doesn’t Netflix and Amazon source other people’s data and profit off of those results? How do existing privacy laws work into this?

The class action suit lists a plethora of existing laws that quite possibly (likely) have been violated by the training of ChatGPT (e.g., Electronic Communications and Privacy Act, Computer Fraud and Abuse Act, California Invasion of Privacy Act, Illinois Biometric Information Privacy Act, etc.) and these are just in the United States.

And yet, if you go through the list of plaintiffs in the suit, you’ll find that most if not all of them are users of OpenAI and ChatGPT — it’s a very valuable and powerful tool, while very possibly being unethically and illegally sourced and trained.

2024 will be a very telling year for the future of OpenAI/ChatGPT and LLMs/AIs in general, and certainly the legal status of their training and impact on personal data and privacy. There is no question of the value and power of the resulting products, but at what cost to the individuals who provided the original data and material on which they were trained?