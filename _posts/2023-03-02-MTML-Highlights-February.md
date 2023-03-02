---
layout: post
title: "Highlights from Machine Translation and Multilinguality in February 2023"
tags: [mtml-highlights, en]
lang: en
---

There were plenty of interesting pre-prints on arXiv in February. Here is a
brief summary of three that I think are cool but could get lost in the hundreds
of papers that went public.

### [The unreasonable effectiveness of few-shot learning for machine translation](https://arxiv.org/abs/2302.01398v1)

Folks from Google experimented with few-shot MT based on language-model.
Instead of using one of the cool huge language models we all know, they train
their smaller ones. They prepare specific bi- and tri-lingual LMs (8B
parameters; BERT has 110M, GPT-2 has 1.5B, GPT-3 175B). At inference time, they
retrieve 5 random examples from the train set and use them as a prompt to the
model. It works better than Google Translate and is comparable to the best WMT
submissions.  However, it is hard to say how fair the comparison is (and what a
fair comparison would be). WMT submissions typically do ensembling and several
iterations of back-translation, which is an unfair advantage compared to the
few-shot setup. On the other hand, the models in this paper are 35× bigger than
Transformer Big, typically used in WMT submissions.


### [Efficiently Upgrading Multilingual Machine Translation Models to Support More Languages](https://arxiv.org/abs/2302.03528v1)

An EACL paper from Meta shows practical tips on adding new languages to
existing multilingual models. During finetuning, they need to increase the
model capacity to avoid forgetting what the model already knows. They invent
two tricks:

1. Widening the FF layers to double the original size. They initialize the new
   broader layer by concatenating the original weight matrix with a noisy copy
   of itself.

2. They add new layers and initialize them by averaging the parameters of the
   already existing layers.

And indeed, it works better than not doing it.

### [Exploring Segmentation Approaches for Neural Machine Translation of Code-Switched Egyptian Arabic-English Text](https://arxiv.org/abs/2210.06990)

A paper accepted to EACL 2023 from Cairo, Stuttgart, and Abu Dhabi studies the
effect of tokenization on code-switched Arabic-to-English translation. Because
I generally do not like how BPE tokens look (no objective reason, I just think
it is annoying that they mostly do not make much linguistic sense), I am glad
there is yet another paper that might bring BPEs down. In the paper, they
experiment with different tokenizers for Arabic-to-English translation with
plenty of English on the source side.  BPE is the best in almost all setups (to
my disappointment). However, the very best setup was supervised morphological
segmentation for Arabic combined with BPE for English. The difference got
bigger when they used less training data, which confirms the importance of
morphological segmentation in low-resource scenarios.

### What else is going on...

Several new large language models were released. Most importantly, LLaMA by
[Meta AI](https://arxiv.org/abs/2302.01398) promises GPT-3 performance with
just a fraction of GPT-3's parameters. Microsoft released
[KOSMOS](https://arxiv.org/abs/2302.14045), a GPT-2 sized multimodal language
model with some language-only instruction finetuning.

The [OpenAssistant](https://open-assistant.io) initiative is gaining momentum.
It is an attempt to replicate ChatGPT with open-source tools. They are
currently collecting data from volunteers, and it seems to go well. The good
thing is that the data they collect is not only in English but also in Spanish,
German, and Russian.
