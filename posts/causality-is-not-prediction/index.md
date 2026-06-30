---
title: "Causality Is Not Prediction"
author:
  - name: Aneesh Sathe
    orcid: 0000-0003-4919-4734
date: "2026-07-06"
categories: [causality, prediction, machine-learning]
image: "malevich-airplane-flying.jpg"
draft: true   # flip to false (or remove) when ready to publish (target 2026-07-06)
---

Prediction and causation feel like the same activity. You have data, you fit a model, a number comes out. They are not the same activity, and confusing them is how confident, well-funded teams drive off a cliff.

Judea Pearl's framing is the clearest I know. Prediction answers *what will I see?* Causation answers *what happens if I act?* He calls it the difference between **seeing** and **doing**. A model trained to predict reads the world exactly as it was recorded. A causal model tells you what changes when you reach in and move something.

## A strong predictor is not a cause

People in gloves and scarves are an excellent predictor of cold weather. Hand that model the lever and it will tell you to ban scarves to stop winter. Funny on the street; not funny when "patients who received drug X died more often" gets read as "drug X kills" — when the truth is that the sickest patients were the ones given drug X in the first place. The predictor is correct. The causal reading is lethally wrong. Gallea's version is worth keeping: *a strong predictor is not necessarily a cause.*

The difference is in the math, not just the attitude. Prediction estimates the probability of an outcome *given that you observe* some variable. Causation estimates the probability of that outcome *given that you set* the variable by intervention. That is a different quantity, equal to the first only when nothing confounds the two. Simpson's paradox is the sharpest reminder: a treatment that helps every subgroup can look harmful in the aggregate, or the reverse. The data alone cannot tell you which number to believe. Only knowledge of what causes what tells you whether to split the groups or pool them.

This is the principle underneath all of it: *no causes in, no causes out.* You must put causal assumptions in to get causal conclusions out, and those assumptions are not in the data — no matter how much of it you pile up. That is the precise sense in which AI cannot replace causal inference. Not because the models are weak, but because prediction and causation are different questions, and scale only makes you better at the one you were already answering.

## The honest part

Here I have to be careful, because the strong version of this claim — "AI can never do causality" — is false, and any statistician will catch you saying it.

Machine learning is now central to *good* causal work. Double machine learning, targeted learning, causal forests — these use flexible models to estimate the messy nuisance pieces while the causal logic does the steering. The pattern, as Gallea describes it, is causal-inference principles first, "then sprinkling a bit of ML on top," not the other way around.

Large language models sit on both sides at once. They are causal parrots — reciting causal claims from their training text without performing the inference — and they are also surprisingly capable knowledge bases of human causal understanding, useful for proposing a graph or surfacing a confounder you forgot. They generate hypotheses well and guarantee nothing. Used as a first draft of the causal graph, reviewed by someone who knows the biology: useful. Used as the oracle: dangerous.

And causal inference is no oracle either. It rests on assumptions you can be wrong about — that you measured the confounders, that the graph is right. Get those wrong and you get a confidently wrong answer dressed in a respectable confidence interval. The discipline does not promise certainty. It promises that you have written your assumptions down where someone can argue with them.

## Match the tool to the question

So the rule is simple, and it belongs on the wall. If the question is *what will happen* — which lead will bind, which patient will relapse — predict, and let the best model win. If the question is *what should we do* — will this change cause that outcome — reach for causal inference. Hand a predictor the lever instead, and it will answer a different question while looking like it answered yours. That is how a forecast gets mistaken for a decision, and how the confident, well-funded team drives off the cliff.

None of this makes AI the enemy. It makes prediction the wrong tool for a causal job — and points straight at the job AI is genuinely good at, which is where this series goes next.

---

<small>Cover: Kazimir Malevich, *Suprematist Composition: Airplane Flying* (1915). Public domain.</small>
