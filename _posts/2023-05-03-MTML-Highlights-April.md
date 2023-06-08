---
layout: post
title: "Highlights from Machine Translation and Multilinguality in April 2023"
tags: [mtml-highlights, en]
lang: en
---

Here is my monthly summary of what new papers and preprints are liked the most
during the previous month.

## [Multilingual Machine Translation with Large Language Models: Empirical Results and Analysis](https://arxiv.org/abs/2304.04675v1)

Several institutions in China did a thorough evaluation of how large language
models work for machine translation One might think yet another paper like
this, but this one is much better than what Tencent did with ChatGPT and just a
few tests sentences. This paper uses the Flores 101 test set, a pretty standard
large test for 101 languages. Everything is based on promptining: no finetuning
is involved. They test [OPT](https://arxiv.org/abs/2205.01068) (English
GPT3-sized LLM by Meta, claimed to be an open alternative to GPT),
[BLOOMZ](https://arxiv.org/abs/2211.01786) (finetued BLOOM, an open LLM for 40
languages), [XGLM](https://arxiv.org/abs/2112.10668) (multilingual LLM by Meta
AI) and ChatGPT.

At the first glance, BLOOM seem to work really well, but inconsitently. This
led the authors to the suspision that the Flores 101 tests (which are complied
from Wikipedia) must have been in BLOOM's the training data. This got
confirmed, so they made a smaller test from very recent news.

The results are: <center><big>OPT < BLOOMZ < XGLM < ChatGPT</big></center>

## [ChatGPT Beyond English: Towards a Comprehensive Evaluation of Large Language Models in Multilingual Learning](https://arxiv.org/abs/2304.05613v1)

Among the very many papers that try to apply ChatGPT for task XY (typically
without finding anything interesting), this paper clearly stands out. it is
probably the first large-scale  evaluation of what ChatGPT can do
multilingually. They compare it with state-of-the-art approaches that used
finetuned massively multilingual models. Long-story short: zero-shot ChatGPT is
mostly worse than mT5 finetuned for the task doing zero-shot transfer from
English. This holds for:

* Text summarization

* Cloze-style question answering (including
  [IndicNLPSuite](https://aclanthology.org/2020.findings-emnlp.445), which used
  IndicBERT)

* NER (with [DAMO](https://arxiv.org/abs/2203.00545) based on XLM-R and mT5-IL
  finetuned from mT5 base)

The only task where ChatGPT won was POS tagging, where they used XLM-R
(probably large) as a baseline. But who cares about POS tagging in 2023. Not
only is ChatGPT much worse in the target languges, but it most cases, it is
also worse than in English. It is not really a suprising finding, but it is
nice to have it quantified: finetuning of reasonably sized models is still
better than zero-shot with large models.

## [Escaping the sentence-level paradigm in machine translation](https://arxiv.org/abs/2304.12959v1)

Folks from Microsoft try to draw attention to document-level MT and in order to
do so, they prepared strong baselines and show how cool they are. From the
research perspective, they do nothing really new: they use sentence-level
parallel data at the beginning and only add document context during
back-translation. They use as long a context as possible when they train.
At inference time, they use overlapping text windows. The main message is
that doing document-level MT pays off. They show it gets much better
results in sentence-level metrics and contrastive evaluation specifically
designed for document-level evaluation also showed significant impovements.

## [Translate to Disambiguate: Zero-shot Multilingual Word Sense Disambiguation with Pretrained Language Models](https://arxiv.org/abs/2304.13803)

A preprint from the University of Washington introduces a method for
intinsically assessing the cross-lingual language understanding of large
language models that is based on word-sense disambuatuion. They create a
dataset for cross-lingual disambiguation using [Babelnet](https://babelnet.org)
and evaluate the models in the zero-shot setup using tempates like this:

They do templates like this:

```
In the sentence "S" the word "w" is translation into L as ___
```

They compare two models [GPT-NeoX](https://arxiv.org/abs/2204.06745) (an
open-source version of GPT by non-profit EleutherAI) and
[BLOOM](https://arxiv.org/abs/2211.05100) (multilingual LLM for 40 languages by
an international consortium led by Huggingface) and different model sizes. The
English model has performance almost as good as BLOOM. Hard to say if it shows
GPT-NeoX is unexpectedly multilingual or that BLOOM is not as great as it
seems.

## What else is going on...

[WMT announced](http://www2.statmt.org/wmt23) the next round of its general MT
tasks for 8 language pairs, in total there 9 machine-translation-related tasks.

OpenAssistant released its first models, now also available as [Hugging
Chat](https://huggingface.co/chat). I was quite optimistic about its potential
multilingual capabilities, but in Czech and Slovak, it does not work at all (it
generates agrammatical outputs); in German it generates fluent language, but it
makes much more factual errors than in English (I did not measure it, it is
just my subjective impression).
