---
layout: post
title: "Machine Translation and Multilinguality 03/2022"
tags: [mt-weekly, en]
lang: en
---

Here is a monthly summary of what I found most interesting on arXiv this month
from machine translation and mutlilinguality. This month was the camera-ready
deadline for ACL 2022, so many of the interesting papers are accepted to ACL.

### Overlapping BPE

When training, BPE merges actually do not have to follow the simple objective
of merging the most frequent token pair. In massively multilingual models,
there is an imbalance between languages, and some of them got segmented almost
down to characters. Therefore, we might want to have a higher vocabulary
overlap between languages. A [paper from IIT Bombay and
Google](https://arxiv.org/abs/2203.01976) that will appear at ACL suggests
mixing the interpolate the bigram frequency with a factor telling in how many
languages the particular merge would appear. This leads to a higher token
overlap between languages and in turn also to better zero-shot transfer when a
multilingual model is pretrained with this tokenization.

### Linguistic segmentation may sometimes pay off

Another paper (that will appear in Findings of ACL) that [discusses input
segmentation](https://arxiv.org/abs/2203.08954) shows that linguistically
meaningful segmentation can sometimes be better than heuristically learned
subwords. The task in the paper was machine translation between Spanish and
four polysynthetic languages (Nahuatl, Raramuri, Shipibo-Konibo, and Wixarika).
The best segmentation method was a [variant of Morfessor called
LMVR](https://arxiv.org/abs/1707.09879).

### Multilingual BERT as a knowledge base

Some people hope that pre-trained language models could be used for distilling
factual knowledge (when prompted correctly). A [pre-print from the University
of Copenhagen](https://arxiv.org/abs/2203.11552) shows that when try does it
with pre-trained multilingual models, the factual answers are neither correct
nor consistent across languages.

### BERT is good with metaphors

A [paper accepted to ACL from the University of
Tehran](https://arxiv.org/abs/2203.14139) probes contextual embeddings for the
presence of metaphors. Long story short: it is indeed possible to detect
metaphors relatively well and it is consistent across datasets and most
importantly across languages.

### Cultural values in contextual embeddings

Another [preprint from the University of
Copenhagen](https://arxiv.org/abs/2203.13722) studies cultural value in
multilingual models using the so-called Hofstede's value survey. By using
prompts like `Having time for family is [MASK]`, where the `[MASK]` token can
be either replaced with important or unimportant, they try to evaluate how well
correlated the probabilities from the models with surveys on the same sets of
questions done in different countries. The result is that there is no
consistent pattern, the results even seem to be pretty random.

### Better likelihood means better translation

There is an ongoing discussion on whether the standard beam search decoding
(and maximum a posteriori inference in general) in machine translation makes
sense, or in general, what is the best way to get good output from a model that
models well conditional probabilities of individual tokens. A recent [paper
from the University of Zurich](https://arxiv.org/abs/2203.15721) shows that for
machine translation, it indeed roughly holds that the higher the likelihood
from the model, the better the translation is according to human evaluation
(even though, e.g., a [pre-print from Google from the last
November](https://arxiv.org/abs/2111.09388) claims the opposite). In other
tasks (such as story generation), is the relation between the likelihood in the
model and human evaluation of the generated text.
