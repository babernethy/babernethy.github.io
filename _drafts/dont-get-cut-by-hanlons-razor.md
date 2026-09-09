---
title: "Don't Get Cut by Hanlon's Razor"
excerpt: "Hanlon's Razor tells us not to assume malice. Dreyfus, Dunning, and Kruger tell us what to assume instead."
description: "Hanlon's Razor tells us not to assume malice. Dreyfus, Dunning, and Kruger tell us what to assume instead."
category: "jobs"
tags: ["leadership", "thinking", "jobs"]
comments: true
toc: true
header:
  teaser: /assets/images/dont-get-cut-by-hanlons-razor-light.svg
  tagline: "Hanlon's Razor tells us not to assume malice. Dreyfus, Dunning, and Kruger tell us what to assume instead."
---

<picture>
  <source srcset="/assets/images/dont-get-cut-by-hanlons-razor-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/assets/images/dont-get-cut-by-hanlons-razor-light.svg" alt="A straight razor whose blade is the gap between the competence and confidence curves.">
</picture>

You are in a meeting when someone makes a confident statement about a complicated problem.

They have the answer. They may even seem surprised that everyone else cannot see it. Yet the people who have lived with the problem the longest are hesitant. They qualify their answers, identify exceptions, and ask for more information.

Who sounds more credible?

Too often, we confuse confidence with competence. The person who speaks decisively sounds knowledgeable, while the person who sees five possible failure modes sounds uncertain. When the discussion becomes tense, we may go further and assign motives: *They are being difficult. They are protecting their territory. They do not care about the outcome. They are deliberately slowing us down.*

That is where Hanlon's Razor can cut us.

Hanlon's Razor asks us not to attribute to malice what error, ignorance, or misunderstanding adequately explains. It is usually credited to a Robert J. Hanlon, by way of a joke book, which is a fitting origin for a rule of thumb rather than a law. It is a useful corrective, but it is not enough by itself. Telling someone what *not* to assume leaves the more important question open: what should we assume instead?

If we combine the razor with the Dreyfus model of skill acquisition, the Dunning–Kruger research on self-assessment, and a concept I call the **Razor Gap**, we get a more useful answer.

The goal is not to diagnose or label people. It is to become slower to judge motives, more curious about capability, and more honest about our own certainty.

These ideas have been with me for a long time. In 2007, I wrote about [the Dreyfus model of skill acquisition]({% post_url 2007-08-18-the-dreyfus-model-of-skills-acquisition %}) and then about Kruger and Dunning's paper, ["Unskilled and Unaware of It"]({% post_url 2007-08-18-unskilled-and-unaware-of-it %}). Even then, I was asking what happens when someone at the novice end of a skill believes they are much farther along. Nearly two decades later, after many more software projects, architecture decisions, mentoring conversations, and difficult meetings, I find myself returning to the same question — but with a greater appreciation for what the mismatch does to everyone else in the room.

## Three ideas and one razor

### Dreyfus: competence develops through stages

The Dreyfus model describes skill acquisition as a progression through five stages: **novice, advanced beginner, competent, proficient, and expert**.[^1]

Dreyfus and Dreyfus describe the underlying movement this way:

> "as the student becomes skilled, he depends less on abstract principles and more on concrete experience."[^1]

A novice depends heavily on rules and instructions. An advanced beginner starts recognizing recurring situations but may struggle to decide which details matter. A competent practitioner can plan, prioritize, and accept responsibility for choices. A proficient practitioner sees situations more holistically. An expert recognizes meaningful patterns and responds fluidly, while still slowing down when the situation is unfamiliar or anomalous.

This is not simply the accumulation of more facts. Expertise changes how a person sees the problem. What appeared to be one straightforward decision becomes a network of context, tradeoffs, precedents, and consequences.

### Dunning and Kruger: self-assessment can be poorly calibrated

The original Dunning–Kruger studies found that low performers often substantially overestimated their performance. One proposed explanation is metacognitive: some of the knowledge required to perform well is also required to recognize what good performance looks like. As Kruger and Dunning put it:

> "the skills that engender competence in a particular domain are often the very same skills necessary to evaluate competence in that domain"[^2]

There is an important caution here. The famous internet curve — with its dramatic peak, crash, and gradual recovery — is not a graph produced by Dunning and Kruger. The size and interpretation of the effect are also debated, including whether part of the observed pattern can be explained statistically.[^3] I use the rise-and-fall shape in my illustration as a **storytelling model**, not as a precise scientific curve.

The durable insight is simpler: our ability to judge our own competence is imperfect, and it is least reliable exactly when we lack the context to see our own mistakes.

### The Razor Gap: confidence relative to competence

The Dreyfus model describes the development of competence. Dunning and Kruger explored the accuracy of self-assessment. I use **the Razor Gap** as a visual metaphor connecting those ideas:

> **Razor Gap (Δ) = expressed confidence − demonstrated competence**

This is not a new scientific measure or a replacement for either model. It is a practical name for the space that opens when demonstrated competence and expressed confidence do not align. Like the gap between a razor's blade and its safety bar, a wider opening allows a more aggressive — and more damaging — cut.

![A conceptual line chart of competence and confidence across the five Dreyfus stages, with the space between them shaded as the Razor Gap.](/assets/images/dreyfus-confidence-competence.svg)

*Figure 1. Competence rises through the Dreyfus stages while confidence follows a less direct path. The shading takes the color of whichever line is on top, so it shows which way the gap runs without implying that either direction is the healthy one. The curves and gaps are illustrative, not measured values.*

When the gap is positive, confidence exceeds competence. When it is near zero, the two are aligned. When it is negative, competence exceeds expressed confidence.

Notice that neither direction is automatically the problem. A large positive gap can make an inexperienced person reckless. A large negative gap can keep a capable person silent, which is its own kind of failure — the room loses the one perspective it most needed. The goal is **calibrated confidence**: enough to act, enough humility to see uncertainty, and enough self-awareness to know when another perspective is needed.

In my illustration, the novice begins with a wide positive gap. The advanced beginner's confidence drops as the landscape becomes visible. Confidence and competence align around the competent stage. The proficient and expert stages show a modest negative gap — not because experts lack confidence, but because they understand boundary conditions and can see how much remains uncertain.

That is a pattern I have observed, not a claim that every person follows the same path.

## How Hanlon's Razor cuts the wrong thing

Imagine a discussion at SWIVEL about retrying a failed instant payment.

Someone new to the domain might say, "If it fails, retry it. That is what retries are for." The statement is simple, confident, and not obviously irrational. In most systems, it would even be correct.

Someone with deeper payments experience starts asking questions. Did the request fail before submission, or did the response disappear afterward? Could the payment already have been accepted? Is the operation idempotent? What do the network rules permit? How will duplicate risk, settlement, posting, and reconciliation be handled?

The expert's answer sounds less decisive because the expert can see more of the system. The hesitation *is* the expertise. But hesitation is not what a room under time pressure rewards.

Several bad assumptions can now enter the conversation:

- We may mistake the newcomer's confidence for competence.
- We may mistake the expert's qualifications for indecision.
- We may interpret questions as resistance rather than risk discovery.
- We may interpret a wrong answer as laziness, arrogance, or bad intent.
- We may use Hanlon's Razor dismissively — "they just do not understand" — rather than helping them understand.

That last one is worth sitting with. The razor is supposed to protect the person you are judging. Used carelessly, it becomes a more polite way of writing them off.

Hanlon's Razor should reduce moral judgment, not eliminate accountability. Ignorance may explain an initial mistake. It does not excuse repeated negligence, refusal to learn, concealed incentives, or behavior that continues after clear feedback.

The razor is most useful as a pause:

> *Before I assign a motive, what differences in knowledge, experience, context, incentives, or confidence could also explain what I am seeing?*

That question creates room for curiosity without requiring naivety.

## What leaders can do

### 1. Stop using confidence as a proxy for competence

Confidence is information, but it is not verification. Ask what evidence, experience, assumptions, and constraints support a position. A confident answer with a weak foundation should not outweigh a qualified answer built on years of relevant experience.

At the same time, tenure and title are not proof either. Experts can be wrong, domains change, and expertise does not transfer automatically from one subject to another.

### 2. Ask questions that reveal the reasoning

Instead of asking only, "What do you recommend?" try:

- What assumptions does this recommendation depend on?
- Which parts are well understood, and which remain uncertain?
- What failure modes have we considered?
- What evidence would change your mind?
- Have you seen this situation before, or are you reasoning from analogy?

These questions make the Razor Gap visible without putting anyone on trial.

### 3. Match support to the person's stage

Novices need clear rules, examples, feedback, and safe boundaries. Advanced beginners need help separating important signals from distracting details. Competent practitioners need ownership and consequential decisions to make. Proficient and expert practitioners need room to exercise judgment — and a culture where raising an unusual risk is treated as a contribution rather than an obstruction.

Giving everyone the same kind of direction ignores how skills actually develop.

### 4. Protect qualified speech

Leaders often reward the cleanest answer in the room. Complex systems rarely produce clean answers.

Phrases such as "under these assumptions," "my confidence is moderate," or "I need to validate one dependency" are not signs of weakness. They are usually signs that someone understands the limits of the available evidence.

Make it safe to say, "I do not know yet." Then expect the speaker to explain how they will find out.

### 5. Correct without humiliating

If limited knowledge already makes self-assessment difficult, embarrassment only makes learning harder. Publicly diagnosing someone with the Dunning–Kruger effect is rarely helpful — and carries a certain irony, since confidently labeling another person's competence from the outside is precisely the move the research warns about.

Challenge the claim. Test the assumptions. Provide evidence. Invite revision. Leave the person's dignity intact.

## What participants can do

Leaders are not the only people responsible for keeping confidence and competence aligned. Everyone in the room can help narrow the Razor Gap.

### Separate what you know from how sure you feel

Try using distinct language:

- "I know this because…"
- "My current interpretation is…"
- "I suspect…"
- "I am confident about X but uncertain about Y."
- "I have not worked directly in this part of the domain."

This is especially valuable in software architecture, where the same person can be an expert in distributed systems and a novice in payment-network operations during a single conversation.

### Treat discomfort as information

That moment when a simple problem becomes complicated can feel like failure. It is usually evidence of growth. You have crossed from not seeing the landscape to seeing enough of it to feel overwhelmed.

Think about your own career. Can you remember a time when learning more briefly made you feel less capable? That drop in confidence may have been painful, but it was also the beginning of better judgment.

Curiosity is what helps us stay in that uncomfortable stage long enough to grow through it.

### Make updating visible

When new evidence changes your position, say so plainly: "I was assuming the timeout meant the payment failed. I now understand the outcome may be unknown, so I am changing my recommendation."

That is not losing a debate. It is demonstrating calibration — and narrowing the Razor Gap in public, where it does the most good.

### Do not weaponize the models

The Dreyfus stages are not a hierarchy of human worth. Dunning–Kruger is not a sophisticated way to call someone stupid. Hanlon's Razor is not permission to ignore harmful patterns.

We are all novices somewhere, and we occupy different stages within the same project. The expert in application architecture may be the advanced beginner in compliance. The payments expert may be the novice in observability. Healthy collaboration begins when people can contribute expertise without pretending it is universal.

## A short Razor Gap check

Before a consequential decision or a heated debate, ask the group four questions:

1. **What do we know?** Identify evidence and relevant experience.
2. **What are we assuming?** Surface the invisible premises.
3. **How confident should we be?** Calibrate certainty to the strength of the evidence.
4. **What else could explain this?** Apply Hanlon's Razor before assigning motives.

These questions will not eliminate disagreement. They will make disagreement more productive.

## Use the razor on assumptions, not people

The most dangerous gap is not always between two people's opinions. It may be the gap between what I know and how certain I feel — or between what another person says and the motives I assign to them.

Dreyfus reminds us that competence develops. Dunning and Kruger remind us that self-assessment is imperfect. The Razor Gap reminds us to compare confidence against evidence. Hanlon's Razor reminds us to hesitate before turning incomplete understanding into a moral judgment.

Together they encourage a better posture for leadership and collaboration: curious but not gullible, accountable but not condemning, confident but still teachable.

The next time a conversation becomes tense, pause before deciding what another person's confidence — or caution — means. Ask what they see. Ask what you might be missing. Then use the razor to cut away the assumption rather than cutting down the person.

---

[^1]: Stuart E. Dreyfus and Hubert L. Dreyfus, "[A Five-Stage Model of the Mental Activities Involved in Directed Skill Acquisition](/assets/mirror/dreyfus-model.pdf)," Operations Research Center, University of California, Berkeley, February 1980.
[^2]: Justin Kruger and David Dunning, "[Unskilled and Unaware of It: How Difficulties in Recognizing One's Own Incompetence Lead to Inflated Self-Assessments](https://doi.org/10.1037/0022-3514.77.6.1121)," *Journal of Personality and Social Psychology* 77, no. 6 (1999): 1121–1134. ([mirror, 498KB](/assets/mirror/1999-kruger.pdf))
[^3]: For examples of the methodological debate, see Gilles E. Gignac and Marcin Zajenkowski, "[The Dunning–Kruger Effect Is (Mostly) a Statistical Artefact](https://research-repository.uwa.edu.au/en/publications/the-dunning-kruger-effect-is-mostly-a-statistical-artefact-valid-/)," *Intelligence* 80 (2020), and Jan R. Magnus and Nikita Peresetsky, "[A Statistical Explanation of the Dunning–Kruger Effect](https://pmc.ncbi.nlm.nih.gov/articles/PMC8992690/)," *Frontiers in Psychology* 13 (2022).
