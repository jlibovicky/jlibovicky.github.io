---
layout: post
title: "Machine Translation Weekly 10: Massively Multilingual Neural Machine Translation"
tags: [mt-weekly, en]
lang: en
---

The holiday period is over and I almost settled in my new place of operation
which is the Ludwig-Maximilian University of Munich. This means I can continue
with weekly reports on what is new in the world of machine translation and
natural language processing.

This week it will be two related papers that recently popped up on arXiv. The
papers were written by quite an overlapping group of authors from Google and
both of them deal with massively multilingual translation models. The first one
is accepted to [EMNLP 2018](https://emnlp-ijcnlp2019.org) and is called
[Investigation Multilingual NMT Representations at
Scale](https://arxiv.org/abs/1909.02197), the second one is called [Evaluating
the Cross-Lingual Effectiveness of Massively Multilingual Neural Machine
Translation](https://arxiv.org/abs/1909.00437).

Both of the papers probe sentence representations that emerge in two newly
developed machine translation models. One of them is capable of translating
from English into 102 different languages, the other one works the other way
round. The drop of the translation quality compared to language-specific models
(which means 204 translation models, each of them several gigabytes large) is
only 0.25 [BLEU](https://en.wikipedia.org/wiki/BLEU) on average. It mostly
drops for high-resource languages whereas for low-resourced languages it
usually increases. This itself is an amazing achievement.

The main finding of the first paper is that the vector representations cluster
according to language families as can be seen in a 2D projection below. They
took vectors (of 512 dimensions!) from the encoder part of the network, compute
the average over sentences and drew a 2D projection that more or less preserves
the distances in the original space.

![Language clusters](/assets/MT-Weekly-10/clusters.png)

In the first layers of the models, the representations tend to cluster based on
what scripts the languages use. In the later layers, it seems the network
abstracts away from this and captures more the similarity based on language
families phylogenetic distances. Isn't it fascinating? These structures arise
in the network without explicitly teaching them to do so. It just, by the way,
emerges while learning to translate from 102 languages into English.

The second paper explores options to use the sentence representations from the
multilingual models in other natural language tasks. To be honest, the results
are not so exciting as in the first one. The first reason is that many of the
tasks are rather artificial: part-of-speech-tagging in many languages at once,
multilingual exercise from predicate logic called natural language inference,
etc. The second reason is that the representations seem to be similarly good as
Multilingual BERT. Unlike the machine translation model, BERT is trained to
predict masked-out neighboring words, the model does not have any supervision
other plain text. Multilingual NMT uses the English translation as a means of
tying the representations together. I would thus expect that the common
training signal can make the representations more cross-lingual. It does not
happen and the paper does not discuss why.
