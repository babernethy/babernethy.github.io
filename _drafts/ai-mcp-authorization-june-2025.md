---
title: "LLMs get their own OWASP Top 10"
excerpt: "An updated list for 2025 of risks and mitigations for LLM applications"
description: "LLMs get their own OWASP Top 10"
category: "ai"
tags: ["ai", "dev"]
comments: true
toc: true
header:
  teaser: /assets/images/llm_owasp.png
  tagline: "LLMs get their own OWASP Top 10"
---

![Image](/assets/images/llm_owasp.png)

June 2025 Updates to the MCP Authorization Framework

The MCP specification is less than a year old, so it will continue to evolve, and an important part of this is the necessary security layers. If you’re building on MCP (Model Context Protocol), or integrating its services into a production system, it’s time to pay close attention to the recent [Authorization Framework update](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization). This June 2025 revision doesn’t just clarify the standard, it also explains a lot better how to secure context-aware services. And if you have created say REST-base APIs, then it feels very familiar.

First, it says that "Authorization is Optional for MCP Implementations" ... let's say that it is optional "for the specification" but really shouldn't be optional for almost any production MCP server.  Even if you have a free and public MCP server you should have folks sign up for a free account and api key/token to use the MCP server.  Then if you do end up tracking negative behavior to a bad actor you can shut them down.  A "free pass" is still a pass that you can control and throttle.

The update also introduces a sharper boundary between Authentication* and Authorization, with clear support for OAuth2-like patterns. The spec now expects developers to explicitly model "who" is performing an action, "on whose behalf", and "with what authority," and gives you the tools to do it.

Here are the parts I found most important when thinking about production:

* **Actors & Delegation:** Every request should now carry explicit actor metadata, meaning your services need to understand and enforce actor identity. This sets the stage for chained delegation—think service A calling B on behalf of user X. The spec calls this out clearly and expects it to be verifiable.

* **Tokens with Context:** MCP now supports scoped *authorization tokens* that aren't just opaque blobs—they carry structured claims that services can interpret. If you’ve worked with JWTs, this will feel familiar. But the twist is the integration with *model scope*, which lets you tie permission not just to a resource type but to the meaning of that resource in your application domain.

* **Trust Requirements:** Services must now declare and enforce their trust model—who they trust to issue tokens, under what conditions, and for which claims. This is big. In production, it's no longer safe to assume that any “valid” token is *appropriate*—services need to understand *why* a token should be honored.

These changes bring the spec closer to production security standards without overburdening developers who are just getting started. You can still prototype easily, but you now have the hooks you’ll need to harden things when real data—and real consequences—enter the picture.

So if you’re working with MCP—or just evaluating it for secure context modeling between services—now’s the time to review how you handle trust boundaries. Ask yourself: *Are your services clear on whose authority they act?* *Can you prove it?* And when the auditors ask how a decision was authorized, will your logs and models tell the same story?

If not—this new Authorization Framework is your chance to tighten that story before someone else does.
