---
icon: lucide/message-circle-question
title: "Using this hub with AI assistants"
description: "How to use AI tools to get more out of this hub: giving your assistant CMI context, ready-made prompts, and honest guidance on what works."
tags:
  - AI
  - Getting started
  - Tools
notes: ""
date_updated: 2026-04-02
---

# Using this hub with AI assistants

*You can ask an AI assistant questions about research data management and get answers grounded in CMI's own guidance. This page explains how to give your assistant the context it needs, offers ready-made prompts for common situations, and is honest about where AI answers are reliable and where they are not.*

## Why this matters

AI assistants work better when they have the right context. Without it, they produce generic answers drawn from broad training data, which may not reflect CMI's institutional context, Norwegian legal requirements, or the specific challenges of multi-country fieldwork. By giving your assistant this hub's content directly, you get answers that draw on the same guidance your colleagues use.

## Give your assistant CMI context

This site publishes a machine-readable version of its full content at:

**[llms-full.txt](llms-full.txt)**

This single file contains every page in the hub, formatted for AI consumption. You can use it in several ways:

- **Paste it into a conversation.** Copy the content of `llms-full.txt` and paste it at the start of a new conversation with your AI assistant. Then ask your questions as follow-ups.
- **Attach it as a file.** Most AI assistants (ChatGPT, Claude, Gemini) let you upload or attach files. Upload `llms-full.txt` and tell the assistant to use it as a reference.
- **Use it in a custom assistant or project.** If your AI tool supports persistent context (such as ChatGPT's custom GPTs or Claude's Projects), add `llms-full.txt` as a knowledge source so it is always available.

There is also a shorter index file, [llms.txt](llms.txt), which lists every page with a one-line description. This is useful if you want to point your assistant at specific pages rather than the entire hub.

!!! warning "Keep your project details out of consumer AI tools"
    Do not paste sensitive project information (participant names, unpublished data, confidential funding details) into AI assistants that are not approved for use with sensitive data. The prompts below are designed to work with the hub's published guidance; they do not require you to share confidential material.

## Ready-made prompts

These prompts are designed to be copied and pasted into a conversation where you have already provided `llms-full.txt` as context. Adjust the bracketed sections to fit your situation.

### Planning a new project

```text
I am planning a research project at CMI that involves [briefly describe
your data: e.g. interviews with government officials in East Africa /
a household survey across three countries / analysis of historical
court records]. Based on CMI's RDM guidance, what should I think about
at the planning stage? Cover data management planning, legal
requirements, and storage.
```

### Checking funder requirements

```text
My project is funded by [funder name: e.g. the Research Council of
Norway / Horizon Europe / Norad]. What does CMI's guidance say about
this funder's data management requirements? What commitments will I
need to make, and what should I budget for?
```

### Storage and security decisions

```text
I need to store [describe your data: e.g. interview recordings with
identifiable participants / survey data with indirect identifiers /
large geospatial datasets]. Based on CMI's guidance, where should I
store this data, and what security measures should I apply?
```

### Preparing a Sikt notification

```text
I am preparing a Sikt notification for a project that [briefly describe:
e.g. collects personal data through interviews in Norway and Tanzania /
uses existing registry data / involves online surveys with no directly
identifiable information]. Walk me through what I need to have ready
and what CMI's standard answers are for each section of the form.
```

### Choosing a repository for publication

```text
My project has produced [describe outputs: e.g. a cleaned survey
dataset and analysis code / qualitative interview transcripts with
restricted access / a combined dataset with both quantitative and
qualitative components]. Based on CMI's guidance, which repository
should I use, and what metadata and licensing decisions do I need
to make?
```

### Understanding GDPR implications

```text
My project involves [describe the personal data situation: e.g.
transferring interview data from a partner institution in Kenya to
CMI in Norway / processing special category data about political
opinions / using a US-based transcription service]. What does CMI's
GDPR guidance say about this situation? What legal basis and
safeguards apply?
```

## What works well, and what does not

AI assistants are good at synthesising information from across the hub, connecting guidance from different lifecycle stages to your specific situation, and summarising long pages into actionable steps. With `llms-full.txt` as context, the answers will reflect CMI's actual recommendations rather than generic advice.

Be cautious with:

- **Legal specifics.** The hub provides interpretive guidance on GDPR and Norwegian data protection law, but an AI assistant cannot replace legal advice for your specific situation. If you are unsure about a legal question, contact CMI's data protection officer.
- **Funder requirements that change.** Funder policies evolve. The hub is updated periodically, but always verify deadlines, form requirements, and policy details against the funder's current documentation.
- **Tool recommendations.** The hub names specific tools and platforms, but availability and pricing change. Confirm that a tool is still available and approved for use at CMI before committing to it.
- **Confidential or internal matters.** The hub covers published institutional guidance. It does not contain information about specific ongoing projects, internal decisions, or unpublished policies.

!!! tip "Verify before you act"
    Use AI-generated answers as a starting point, not a final authority. For anything involving legal obligations, ethical approvals, or funder compliance, read the relevant hub page directly and consult the appropriate CMI contact.

!!! info "Last reviewed: 2 April 2026"
