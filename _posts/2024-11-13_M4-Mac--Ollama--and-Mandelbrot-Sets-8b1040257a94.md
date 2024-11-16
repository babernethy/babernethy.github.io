---
title: 'M4 Mac, Ollama, and Mandelbrot Sets'
description: Local AI/LLM goodness for Developers
date: '2024-11-13T15:08:47.997Z'
categories: []
keywords: []
---

I was trying to think of how to put a new home machine through some stress testing to see how fast the processors really are, and what types of features are enabled by that power. My mind immediately went to two things.

*   Run a local decently powered AI LLM (or two) in real-time, and see how the results compared to “the big guys” (e.g., ChatGPT and GitHub CoPilot)
*   Render some fractals — my favorite being the Mandelbrot set and Julia sets. Been running these on personal computers since the late 1980s, so it’d be great to compare the new power to the runs that took hours/overnight “back then.”
*   Why not put these two ideas together?

### Mac Mini M4 Pro

I didn’t go with the entry-level Mac Mini M4, but also not the highest-end — somewhere in the middle. Got the M4 Pro configuration, but with 48Gb of memory so thats: 12-Core _CPU_, 16-Core _GPU_, 16-Core _Neural Engine_ capable of “performing up to 38 trillion operations per second” — so we need to try that out.

![Image](/assets/images/1__BLOyL7lyx4V0J7aso__k9gg.png)
![Image](/assets/images/1__J__qHzupyBLE0UxIBQXKPnw.png)

### Ollama

One of the local LLM platforms I’ve been wanting to try out was [Ollama](https://ollama.com/). So I downloaded the Mac app from the distribution website.

Once this is installed and configured in the shell I could pull the three models I wanted to try out initially:

*   **llama3.2** — a general purpose LLM like ChatGPT (but smaller) — (3.1 has more power, but I wanted to limit the model to 32b (billion) parameters as I need to reserve some memory for other apps I want to run.
*   **qwen1.5coder** — a model trained more specifically to software development and coding in 40 different languages.
*   **llava** — the first “vision” model I found that was compatible to help describe and identify image contents.

> ollama pull llama3.2

> ollama pull qwen2.5-coder

> ollama pull llava

### Command Line

First, lets just try to run something from the command line … a simple quicksort in C#.

![Image](/assets/images/1__CsdpujBOPLSfK7hGCTcnDg.png)

… literally “count to 5” and the code is generated.

### What about a Graphical UI / Web Page?

There is a handy GUI for the ollama models that can be installed quite easily using a Docker container. This is the [_open-webui_](https://docs.openwebui.com/) package.

> docker pull ghcr.io/open-webui/open-webui:main

> docker run -d -p 3000:8080 -v open-webui:/app/backend/data — name open-webui ghcr.io/open-webui/open-webui:main

Then you get a nice web-based UI at localhost 8080 …

![Image](/assets/images/1__3qtgbNV2HBJ4vt0Fpz__oNA.png)

… with access to all your installed ollama models …

![Image](/assets/images/1__4w37ivzUe3NRU9__71YYidw.png)

### What about the Mandelbrot set — how about Flutter?

What if I could combine my favorite fractal with my favorite/easy front-end UI framework — a Mandelbrot set in Flutter. Ask _qwen2.5-coder:32b_ …

> “Can you help me write an app that would render a Mandelbrot set in Flutter”

Full disclosure — it got one line of code wrong. It tried to do a canvas.drawPoint (singular) when the actual/current method is canvas.drawPoints (a set). So I got to write five lines of code and update one. The result was pretty impressive, built as a native MacOS app.

![Image](/assets/images/1__GEQyrbALYNw8S6ioVsJsMQ.png)

Impressive because (1) the code works, but also (2) it rendered the entire image in about 1–2 seconds — the power of the LLM and the new Mac Mini. I changed the default zoom level to “2”, and scaled the app to fill by biggest 36" monitor, and then had to wait a good 5–6 seconds for …

![Image](/assets/images/1__kg6RBrIbq8IsvkPbTrpbrw.png)

I found this to be very satisfying. I added the ability to change the “center” with a mouse click, use the mouse wheel to “zoom” the image, and fix the aspect ratio to fit the current window. All with some subsequent _qwen-coder_ prompts. About 20 minutes of work for something that took me weeks — many years ago.

**Will this all run in the IDE — VS Code?**

It turns out there are several VS Code Extensions that will enable integration of ollama models with the IDE. The one documented (perhaps recommended) by Ollama itself is [_Continue_](https://docs.continue.dev/getting-started/overview) _…_

![Image](/assets/images/1__trufJtWcXSShEcRlZ19CsQ.png)

… enabling _Chat_, _Autocomplete_, and _Edit_ AI/code-assistant capabilities.

![Image](/assets/images/0__IwFcsr6sXNGdG1Fo.gif)

### Conclusions / What’s Next?

I currently have both ChatGPT and GitHub CoPilot subscriptions — wouldn’t it be nice not to have to pay for that but get 80% or more of the features? AND, not have to think/worry about what OpenAI or GitHub/Microsoft does with my prompts and suggestions?

I plan to run these side-by-side with the Commercial BigAICompany versions and see their differences for a few weeks. We’ll see how it goes.