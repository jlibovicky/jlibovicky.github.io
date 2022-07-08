---
layout: post
title: "Machine Translation and Multilinguality in May and June 2022"
tags: [mt-weekly, en]
lang: en
---

After a while, here is a dump of what I found most interesting on arXiv about
machine translation and multilinguality, covering May and June of this year.

Google Research published a [pre-print of their NAACL
paper](https://arxiv.org/abs/2205.00704): SCONES (Single-label Contrastive
Objective for Non-Exclusive Sequences). The paper is about a simple trick:
they replace softmax with binary classifiers with a sigmoid output and use the
sum of binary cross-entropies as their loss function. It gets a slightly better
BLEU and BLEURT score on WMT19, it does not suffer from the beam search curse
that much and it is slightly faster because it does not have to normalize the
logits of the output vocabulary in every time step.

Folks from UNC Chapell Hill, Meta AI, and Microfost made an [empirical study on
how to best use SentencePiece](https://arxiv.org/abs/2204.14268) in
multilingual machine translation models. They experiment with different
language proportions in training data for SentencePiece estimation. The more
balanced the data is, the better the translation. Byte-fallback does not make a
difference.

Google shared a [white paper on MT for another 1k
languages](https://arxiv.org/abs/2205.03983). There are no modeling
innovations, it is mostly a story about getting parallel data from the Internet
and cleaning the data.

Huawei Noah’s Ark Lab published a [pre-print of their paper from the Findings
of NAACL](https://arxiv.org/abs/2206.06586) about a cross-lingual model
transfer. The conclusions are that knowledge distillation, translate-train, and
paraphrasing at distillation time are better than translating the inputs at
inference time. That sounds cool, but I always thought zero-shot language
transfer is there primarily for low-resource languages where both translation
and paraphrasing would be poor.

A [pre-print from the Hebrew University of
Jerusalem](https://arxiv.org/abs/2206.09860) makes an astounding observation:
the bigger model, the bigger chance of gender bias. More parameters create more
opportunities for memorization, so the models can memorize more stereotypical
cases from the training data. At the same time, it can also solve the tasks
better, but it does not overweight the memorization problem (certainly a good
candidate for the [Inverse Scaling
Prize](https://twitter.com/EthanJPerez/status/1541454949397041154)).
