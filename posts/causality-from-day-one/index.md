---
title: "Causality Belongs in Your Biotech From Day One"
author:
  - name: Aneesh Sathe
    orcid: 0000-0003-4919-4734
date: "2026-06-29"
categories: [causality, biotech, data-science]
image: "kandinsky-composition-viii.jpg"
aliases:
  - "/posts/8 Causality From Day One/Causality Belongs From Day One.html"
---

Every decision in your biotech startup is based on a causal claim: "The compound works." "The assay predicts efficacy." "We should run the bigger study." Scientists often claim to not understand "business" but nothing has a larger effect than the core causal argument. The trouble starts when the people who could check those assumptions (your data science and stats team) are brought in only after the data has been collected. By then, what you are allowed to learn has already been decided.

This is the most expensive mistake I see early biotechs make, and it has nothing to do with talent or tools. It is matter of workflow process and a sequencing.

## Designed in, or lost

Data does not contain causal information nor can you infer it from the patterns you see after the experiment is done. It is something you build into the experiment at the beginning. What you randomize, hold fixed, measured, or discarded as noise — those choices fix the set of questions the data can ever answer. A data scientist handed a finished dataset can only describe what is left. They cannot recover what went down the drain nor simulate an experiment.

Concretely: two arms of an experiment differ in outcome. Was it the treatment — or was it that the treated samples were also the fresher ones, run on the better instrument, by the senior tech? If nobody logged instrument, batch, and operator, that question is now permanently unanswerable \[btw your t-tests can't even try to answer it\]. The confounder is missing from the data because nobody decided, on day one, that it should be there.

## Modeling is craft, not a button

Even with the right data, the work is never a single fit. You don't simply throw it all in a pot and stir it, this isn't witchcraft or [AI](https://xkcd.com/1838/). In their *Bayesian Workflow* paper, Gelman and colleagues are blunt: for any real problem you end up fitting many models. You build a simple one, run it forward to see whether it generates anything like real data, find it embarrassing, expand it, break the computation, fix the model rather than the computer, and go again. They are honest about the intermediate models too — "the hopelessly wrong models and the seriously flawed models are, in practice, unavoidable steps along the way toward fitting the useful models".

This is not a flowchart you can hand to an intern or an API. McElreath's image is the one I keep returning to: a statistical model is a golem — powerful clay that does exactly what you build it to do, and not one thing more. Point it at the wrong question and it will answer the wrong question, confidently, with a tight interval. Someone who understands both the biology and the model has to herd the model and its friends. So, your whole team has to be involved when the experiment is designed, not when the results are due.

## Why an LLM won't save you

The hope, right now, is that a large enough model makes this discipline optional. Feed it everything; let it sort out cause and effect. It cannot — and not because today's models are too small.

Start with the data. Big data is still observational — proxy-ridden, collected for some other purpose, gathered without randomization. Scale multiplies whatever bias you began with. Data is dumb; it has no sense of causality, and more of it is still dumb.

A language model is extraordinary at telling you what tends to follow what in the text it was trained on. That is association. It can recite the causal claims humans have already written down — researchers have a name for a system that talks causality fluently without doing it: a *causal parrot*. What it cannot do is know which variable in *your* assay is a confounder you must adjust for and which is a collider you must leave alone. That call needs domain knowledge (with the right tools AI can be immensely helpful, but only with the right tools) and a causal graph, and it cannot be automated or hand-waved away.

None of this makes the model useless. It means the model can't supply the one thing the work turns on — the causal call itself.

## The fix is a sequencing fix

So put the causal thinking first, and put the people who do it in early. Better yet, learn it yourself, it isn't difficult and enables you to make fun diagrams on a whiteboard! Get the biologists and the data scientists around one whiteboard and draw the graph representing what you believe causes what. It is the cheapest artifact in the building and the most revealing; what you leave off it matters as much as what you put on. The line I would frame from the *Bayesian Workflow* paper: a good model "is not specified from the outside; it emerges from engagement with the application and the available data". That engagement has to begin while the experiment is still on the whiteboard.

A data science team bolted on at the end can only audit a decision that has already been made. A data science team present at the start gets to decide what the company is *able* to learn. Those are not the same job, and only one of them is worth the salary. The golem will build whatever you point it at; someone has to choose the target.

Which raises the question the hype keeps dodging, and the one the next post takes up: if not prediction, then what?

---

<small>Cover: Wassily Kandinsky, *Composition VIII* (1923). Public domain.</small>