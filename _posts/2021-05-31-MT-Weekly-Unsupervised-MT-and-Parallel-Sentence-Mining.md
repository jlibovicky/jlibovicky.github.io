---
layout: post
title: "Machine Translation Weekly 81: Unsupervsied MT and Parallel Sentence Mining"
tags: [mt-weekly, en]
lang: en
paperTitle: "Unsupervised Multilingual Sentence Embeddings for Parallel Corpus Mining"
paperAuthors: "Ivana Kvapilıkova, Mikel Artetxe, Gorka Labaka, Eneko Agirre, Ondřej Bojar"
issue: 81
---

This week I am going to briefly comment on a paper that uses unsupervised
machine translation to improve unsupervised scoring for parallel data mining.
The title of the paper is [Unsupervised Multilingual Sentence Embeddings for
Parallel Corpus Mining](https://arxiv.org/pdf/2105.10419.pdf), it has authors
from Charles University and the University of the Basque Country and will
appear at this year's ACL student research workshop.

The idea of the paper is quite simple. They took XLM, a BERT-like model that
was trained for 100 languages using masked language modeling objective
(randomly masking words in the input and predicting what the missing word is).
In such a setup nothing forces the model to represent parallel sentences
similarly, although it partially happens. This property dramatically improves
when the model is provided with parallel sentences and trained in the same way.
The model has a chance to find a translation of the masked word in the parallel
sentence which forces it to represent the sentences similarly across languages.
This paper basically shows that this type of supervision does not have to be
really strong – synthetic data from unsupervised machine translation (which is
always of rather low quality) is enough to get a large improvement.

One of the big problems of unsupervised machine translation is that it requires
large amounts of monolingual data and for languages for which we have such an
amount of monolingual data, there are certainly parallel to (to at least
several languages) as well. This would probably be a reason to think that this
paper does not show anything particularly useful. However, Table 4 of the paper
shows a really interesting result. The finetuning of XLM on the synthetic
parallel data improved the parallel data retrieval for other language pairs as
well. This is a really interesting property. It almost seems like that the
representations are almost language-neutral, waiting for the slightest training
signal to align them together. What a pity that the paper does not explore this
result in more detail.
