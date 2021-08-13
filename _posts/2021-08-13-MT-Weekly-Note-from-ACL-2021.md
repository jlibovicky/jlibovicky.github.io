---
layout: post
title: "Machine Translation Weekly 87: Notes from ACL 2021"
tags: [mt-weekly, en]
lang: en
issue: 87
---

The story of the science fiction novel [Roadside
Picnic](https://en.wikipedia.org/wiki/Roadside_Picnic) by Arkady and Boris
Strugatsky (mostly known via Tarkovsky's 1979 film
[Stalker](https://en.wikipedia.org/wiki/Stalker_(1979_film))) takes place after
an extraterrestrial event called the Visitation. Some aliens stopped by, made a
roadside picnic, and left behind plenty of weird and dangerous objects having
features that contemporary science cannot explain. Although the UN tries to
prevent people from entering the visitation zones before everything gets fully
explored and explained, objects from the zone are traded on a black market.
Soon, the semi-legal discoveries from the zone find use in the industry without
anyone having a good understanding of how the mysterious objects and materials
work.

I got a very similar feeling from this year's ACL as from this novel. In my not
so elaborated analogy, the advent of deep learning is the extraterrestrial
event, of course. Now, years after, we try to do now is make sense of what
happened, some try to figure out if it is not dangerous and some try to make
some money out of it. No wonder that the best papers at the conference, both
those that the organizers recognized as the best ones and those that I
personally liked the most, did not push the state-of-the-art by a large margin
but brought some interesting insights and reflected the inventions of previous
years.

## What changed my beliefs

Few papers changed what I previously thought were the solid truths of NLP I
would not hesitate to write in a textbook for the next 5 years.

* Standard word embeddings are not best for lexical semantics anymore, it is
  better to extract them from BERT. (See below.)

* [Reranking of MT model outputs can bring much bigger gains than I
  thought.](https://www.aclanthology.org/2021.acl-long.563)

* Multilingual representations are cool, but there are plenty of potentially
  cross-lingual tasks where current cross-lingual models spectacularly fail.
  (See below.)

## Some interesting papers

[__When Do You Need Billions of Words of Pretraining Data?__](https://www.aclanthology.org/2021.acl-long.90)

They train a dozen of RoBERTas on different data sizes. For syntactic tasks,
~10M words pretraining is enough, for semantic tasks ~100M words, for common
sense (here, Winograd) billions of words are necessary (no matter how we
probe). For SuperGLUE not even 30B is enough…

Figure 1 from the paper:
![Pretraining data vs. task performance](/assets/pretraining_data.png)

[__Determinantal Beam Search__](https//www.aclanthology.org/2021.acl-long.512)

Standard beam search maximizes the probability of the hypothesis set, which is
by chance the determinant of a diagonal matrix with candidate probabilities in
each step (this is no miracle, it is a product of the hypotheses probabilities
and a determinant of a diagonal matrix is the product of the diagonal, but
still what a cool observation!). And what if off-diagonal entries encode the
similarity of the hypothesis? Then the algorithm will also optimize the
diversity of the samples.

[__LexFit: Lexical Fine-Tuning of Pretrained Language Models__](https//www.aclanthology.org/2021.acl-long.410)

Pre-trained LMs already contain more lexical knowledge than static word
embeddings. A small finetuning push from WordNet is enough to expose the
lexical knowledge and they get much better results than FastText. The
provocative conclusion is that we might not need the traditional word
embeddings anymore. If we want to get high-quality static word embeddings, we
can get them from BERT-like models (but how to do it without WordNet)?

[__UnNatural Language Inference__](https//www.aclanthology.org/2021.acl-long.569)

The paper introduces a methodology of measuring the sensitivity of models to
sentence reordering and they found out that NLI is surprisingly permutation
invariant, but the invariance indeed depends on how similar it is to the
original order. This is quite a cool extrinsic measure of how contextualized a
model is, by sort measuring its distance from bag-of-words models.

[__Exposing the limits of Zero-shot Cross-lingual Hate Speech Detection__](https//www.aclanthology.org/2021.acl-short.114)

The success of cross-lingual hate speech detection depends on the types of hate
speech. For instance, hate speech against immigrants is easier to detect
cross-lingually than hate speech against women because the language is less
idiomatic in the first case. But in both cases, the results are pretty poor.

[__X-Fact: A New Benchmark Dataset for Multilingual Fact Checking__](https//www.aclanthology.org/2021.acl-short.86)

Dataset for multilingual fact-checking. mBERT works fine within a language,
metadata help, Google search helps. But once we do it cross-lingually, it does
not work almost at all.
