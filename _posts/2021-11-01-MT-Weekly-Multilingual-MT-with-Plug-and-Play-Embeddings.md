---
layout: post
title: "Machine Translation Weekly 92: Multilingual Machine Translation with Plug-and-Play Embeddings"
tags: [mt-weekly, en]
lang: en
paperTitle: "Continual Learning in Multilingual NMT via Language-Specific Embeddings"
paperAuthors: "Alexandre Berard"
issue: 92
---

Deep learning models are prone to so-called catastrophic forgetting when
finetuned on slightly different data than they were originally trained on.
Often, they also badly generalize when confronted with data that do not exactly
look like those they were trained on. On the other hand, there are more and
more tricks on how to just reuse a part of a model that was trained for
something else and it just works.  I could hardly believe when [Tom Kocmi and
Ondřej Bojar](https://aclanthology.org/W18-6325) took some trained models, used
them as initialization for totally unrelated languages and it worked much
better than initializing the models randomly. Recently, a new similar "recipe
paper" appeared on arXiv, advising to re-trained just word embedding and keep
the other weights frozen. The title of the paper is [Continual Learning in
Multilingual NMT via Language-Specific
Embeddings](https://arxiv.org/abs/2110.10478), is from Naver Labs Europe and
will appear at [this year's WMT](http://www.statmt.org/wmt21).

The task the paper deals with is adding another language into an existing
multilingual machine translation model. If we do want to end up having multiple
models, it would require re-training the model from scratch with the new
language pair mixed in the training data. The papers suggest something in
between having a single multilingual model and models for each language pair.
What they propose is: keep all parameters of the model frozen and just re-train
a new embedding table for the new language — as if the model was some universal
machine and replacing the embeddings would be just loading a different program
into it.

This works well on the encoder side, i.e., for translation from a new language.
Adding a language on the decoder seems to be more tricky. (After all,
understanding a language is usually easier than speaking a language.) On the
decoder side, it requires adding [adapter
layers](https://aclanthology.org/2020.emnlp-demos.7) (if you don't know what
adapters are, read more about them, they are really cool). Actually, adapter
layers also help on the encoder side, which sort of breaks my story about the
model being a universal language processor with plug and play embeddings
layers.

The story of the paper seems to me to be in principle similar to a paper about
the [adaptation of GPT-2 for other
languages](https://aclanthology.org/2021.findings-acl.74) that I briefly
mentioned two weeks ago. They also start with replacing the embeddings does
most of the job and the "body" of the model only needs to be slightly
finetuned. This brings me back to my obsessive idea of the "model body" being a
universal processor and embeddings a program. Could it be so, or am I just
fabricating conspiracies?
