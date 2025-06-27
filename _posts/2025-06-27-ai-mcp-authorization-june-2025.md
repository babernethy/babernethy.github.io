---
title: "MCP Security Framework - June 2025 Updates"
excerpt: "MCP Security, Authentication, Authorization, Best Practices, updated June 2025"
description: "MCP Security Framework - June 2025 Updates"
category: "ai"
tags: ["ai", "dev", "security"]
comments: true
toc: true
header:
  teaser: /assets/images/ai-mcp-june-2025-header.png
  tagline: "MCP Security Framework - June 2025 Updates"
---

![Image](/assets/images/ai-mcp-june-2025-header.png)

# MCP Security Framework - June 2025 Updates

The MCP specification is less than a year old, so it will continue to evolve, and an important part of this is the necessary security layers. If you’re building on MCP (Model Context Protocol), or integrating its services into a production system, it’s time to pay close attention to the recent [Authorization Framework update](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization). This June 2025 revision doesn’t just clarify the standard, it also explains a lot better how to secure context-aware services. And if you have created say REST-base APIs, then it feels very familiar.

First, it says that "Authorization is Optional for MCP Implementations" ... let's say that it is optional "for the specification" but really shouldn't be optional for almost any production MCP server.  Even if you have a free and public MCP server you should have folks sign up for a free account and api key/token to use the MCP server.  Then if you do end up tracking negative behavior to a bad actor you can shut them down.  A "free pass" is still a pass that you can control and throttle.

The update also introduces a sharper boundary between Authentication* and Authorization, with clear support for OAuth2-like patterns. The spec now expects developers to explicitly model "who" is performing an action, "on whose behalf", and "with what authority," and gives you the tools to do it.

Here are the parts I found most important when thinking about production:

## Actors & Delegation

Every request should now carry explicit actor metadata, meaning your services should understand and enforce actor identity. This is another big difference between "just REST APIs" and MCP in that MCP services are often used in a group or chain together in one query or request.  So think of service A calling B on behalf of user X. The spec calls this out clearly and expects it to be verifiable. What happens if the difference MCP servers are secured by different tokens?

## Tokens with Context

MCP now supports scoped *authorization tokens* that carry structured claims that services can interpret. If you’ve worked with JWTs (e.g. OAuth/OIDC), this will feel familiar. But the twist is the integration with *model scope*, which lets you tie permissions not just to a resource type but to the meaning of that resource in your application domain. There is more detail in the spec itself [Authorization Framework update](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization), but the flows should look similar to OpenID Connect flows with OAuth but with some extra metadata.

![Image](/assets/images/ai-mcp-authorization-flow.png)

## Trust Requirements

Services must now declare and enforce their trust model which includes who they trust to issue tokens, under what conditions, and for which claims. This is new and not something I've seen with OIDC/REST APIs. In production, it's no longer safe to assume that any “valid” token is *safe* or correct to be used for a particular call. Services need to understand more about "why" a token should be honored and the business rules behind the situations that the tokens are valid.

These changes bring the spec closer to production-ready security standards without overburdening developers who are just getting started. You can still prototype easily (without security - but don't do this for long), but you now have the hooks you’ll need to harden things very soon.

## So Get Started

So if you’re working with MCP, or just evaluating it for secure context modeling between services, now’s the time to review how you handle trust boundaries. Ask yourself: *Are your services clear on whose authority they act?* *Can you prove it?* And when the auditors ask how a decision was authorized, will your security and application logs tell the same story?
