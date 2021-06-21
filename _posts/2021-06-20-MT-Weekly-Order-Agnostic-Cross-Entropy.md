---
layout: post
title: "Machine Translation Weekly 84: Order Agnostic Cross-Entropy"
tags: [mt-weekly, en]
lang: en
paperTitle: "Order-Agnostic Cross Entropy for Non-Autoregressive Machine Translation"
paperAuthors: "Cunxiao Du, Zhaopeng Tu, Jing Jiang"
issue: 84
---

I tend to be a little biased against autoregressive models. The way they
operate: say exactly one subword, think for a while, and then say again exactly
one subword, just does not sound natural to me. Moreover, with current models,
a subword can be anything from a single character to a word as long as
["Ausgußreiniger"](https://de.wikipedia.org/wiki/Saugglocke_\(Sanit%C3%A4rtechnik\)).
Non-autoregressive models generate everything in a single step. That does seem
to be really natural either, but at least they offer an interesting
alternative. Hopefully, one day, we can have something in-between these two
extremes. Because the day did not come yet, today, I am going to comment on a
paper that introduces an interesting loss function for non-autoregressive MT,
which might a small step in this direction. The title of the paper is
[Order-Agnostic Cross Entropy for Non-Autoregressive Machine
Translation](https://arxiv.org/abs/2106.05093), it has authors from Tencent AI
Lab and will be published at this year's ICML.

Autoregressive models are trained using the standard cross entropy. In
non-autoregressive MT, it gets more interesting. Two possible alternatives to
standard cross entropy in non-autoregressive models are [Connectionist Temporal
Classification](https://www.aclweb.org/anthology/D18-1336) and [Aligned Cross
Entropy](https://arxiv.org/abs/2004.01655). Both loss functions allow blank
symbols to be inserted between the output tokens, so the output tokens get
better aligned with the decoder states. I hypothesize that this makes
reordering that internally needs to happen within the Transformer layers easier
(although I have no proof for that). Both these alternatives enforce monotonic
alignment between the decoder states and output symbols. After all, if they did
not, would force the model to generate the target tokens in the correct order.

And here comes the trick that they use in this paper. They just use two loss
functions. One is the standard cross-entropy which enforces the monotonic
ordering most straightforwardly. The second one rewards the model for the
correct word choice, regardless of the word order. The trick is to compute the
maximum matching between the output states and embeddings of the target
sentence and align the tokens and the states accordingly. It is nicely
illustrated in Figure 1 (on page 2) of the paper:

![Order agostic cross entropy](/assets/order-agnostic.png)

Indeed, the paper shows improvements in translation quality (otherwise it
probably would not get published these days). But what I liked the most about
this paper is that it returns an old dichotomy in MT: modeling fluency and
adequacy separately but in a very different fashion. Here, the cross-entropy
model fluency (and also adequacy, but it has some issues with it), the order
agnostic cross-entropy only cares about adequacy. However, unlike the old
statistical models, they still have only one model trained end-to-end.
