---
title: "The Prudent Use of AI: Find the Evidence, Then Reason"
author:
  - name: Aneesh Sathe
    orcid: 0000-0003-4919-4734
date: "2026-07-13"
categories: [AI-agents, causality, biotech]
image: "boccioni-dynamism-of-a-cyclist.jpg"
draft: true   # flip to false (or remove) when ready to publish (target 2026-07-13)
---

If prediction is the wrong tool for causal questions, and a language model can't supply your causal assumptions, the real question is what AI is actually *for* in a serious lab. The answer is not "nothing." It is a different job than the one the hype is selling.

The hype sells an **oracle**: ask the model, receive the truth. The useful version is an **orchestrator**: a model that knows which validated tool, dataset, or paper answers your question, calls it correctly, and hands the result back to a human who can check it. Same model, opposite epistemics. The oracle invents an answer from its own memory. The orchestrator goes and fetches one from a source you already trust.

## What an orchestrator looks like

ToolUniverse, from Marinka Zitnik's lab at Harvard Medical School (arXiv:2509.23426, *"Democratizing AI scientists using ToolUniverse,"* 2025), is a clean instance. It connects a language model to more than six hundred validated scientific resources — models, datasets, APIs, and packages spanning drug discovery, target and disease research, multi-omics, and the literature — and the public repository has since grown past a thousand. The model's job is not to remember pharmacology. Its job is to find the right tool, call it with the right arguments, compose the results, and keep a human expert in the loop. The reasoning is grounded in resources you can audit, not in the model's parametric guesswork.

That is the line between prudent and reckless AI in science. Reckless: the model is the source of truth, and you discover it was confidently wrong after you have ordered the synthesis. Prudent: the model is a fast, tireless research assistant that retrieves from validated sources and shows its work, while your scientists — and your causal models — do the judging. The pattern is not free to stand up; someone has to curate the tools, wire the interfaces, and decide what "validated" means for your science. That cost is the point — it is where your domain expertise gets encoded, and it is not something you can buy off the shelf.

## Retrieval first, judgment after

AI's real job sits in front of the causal work, not on top of it. Use it to get to the right information — the relevant assay, the prior study, the public dataset, the package that runs the analysis. Then use causal reasoning to decide what the information *means* and what to do about it. Retrieval is a prediction-flavored task, and AI is excellent at it. Deciding what causes what, and what to intervene on, stays with the people and the causal models. The two are not in competition; they run in sequence.

There is one more prudent habit the hype actively discourages: measuring whether your AI is doing anything at all. Gallea's line belongs taped to the monitor — *"Saying that it works is clearly not enough."* A model that makes your scientists *feel* faster is not the same as a model that makes your science *better*, and the only way to tell the difference is a causal evaluation: deploy it, and measure the effect against a real counterfactual. One AI-first fintech made headlines in 2025 for cutting its marketing team, then re-hired months later, having decided it wasn't such a good idea after all.

## The actual edge

Put the three posts together and you get the advantage that never shows up in a demo. It starts with causal thinking on day one, so the data can answer the questions that matter. It keeps prediction in its lane, so a forecast never gets mistaken for a decision. And it points AI at the one thing it does better than any person — finding and connecting the right evidence, fast — instead of asking it to be the scientist.

The science stays yours, and so do the causes you are trying to find. The machine just gets you to the evidence faster. Done honestly, that is plenty.

---

<small>Cover: Umberto Boccioni, *Dynamism of a Cyclist* (1913). Public domain.</small>
