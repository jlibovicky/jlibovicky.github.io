---
layout: post
title: "Machine Translation Weekly 91: Zero-Shot Machine Translation with a Universal Encoder from Pre-trained Representations"
tags: [mt-weekly, en]
lang: en
paperTitle: "Towards Making the Most of Multilingual Pretraining for Zero-Shot Neural Machine Translation"
paperAuthors: "Guanhua Chen, Shuming Ma, Yun Chen, Dongdong Zhang, Jia Pan, Wenping Wang, Furu Wei"
issue: 91
---

How many times have you heard someone saying that multilingual BERT or similar
models could be used as a universal encoder in machine translation? I heard
that (and said that) many times, but never heard about someone who actually did
that, until now. Folks from The University of Hong Kong, Mircosoft Research,
Shanghai University, and Texas A&M University published their preprint on this
topic last Thursday on arXiv. The title of the paper is [Towards Making the
Most of Multilingual Pretraining for Zero-Shot Neural Machine
Translation](https://arxiv.org/abs/2110.08547). They actually published a large
deal in this direction already in April, but at that time I did not notice, and
this time their method works much better.

The idea is simple. Multilingual BERT and XLM-RoBERTa provide sentence
representation for more than 100 languages, which is to some extent
language-neutral (on the other hand it also contains information that makes it
extremely easy to guess the language identity). If we trained a machine
translation model that only relies on the language-neutral traits of the
representation, we would get a machine translation model that translates from
all the remaining languages sort of for free. The challenge of training such a
model is thus: first, to only use the language-neutral traits, and second, not
to break the multilingual model.

The first challenge is addressed in a pretty straightforward way: they use six
different source languages. The solution to the second challenge is simple and
elegant. They first only train the decoder while keeping the encoder (which is
the pre-trained XLM-R model) frozen. This ensures that the decoder is
accustomed to the representation from XLM-R. At this point, the encoder does
not know, it should adapt for machine translation. In the second step, they
finetune the complete model, so also the encoder can adapt for the task, but
the changes in the encoder are small because the decoder got first adapted to
the encoder.

The results look quite good. In the zero-shot fashion, without
language-specific training data, they get better results than the [m2m-100
model by Facebook](https://arxiv.org/abs/2010.11125) that uses parallel data in
all directions. This model, however, does not use any parallel data for the
languages they test on. They also get great results in low-resource translation
into Nepali and Sinhala by starting with their model and iterating
back-translation as people normally in low-resource and unsupervised machine
translation.

I like how this is complementary to other pre-training approaches in machine
translation. The paper ends with having a decent zero-shot system, but I assume
this trick has the potential to change how low-resource machine translation is
done. My general impression from unsupervised and low-resource translation is
that the better you can get before iterating back-translation, the better the
system you get in the end. And this seems like a good way to get a decent
initial system before even using any language-specific data. I can imagine
using this as the first iteration of back-translation used at scale for
finetuning models like [mBART](https://arxiv.org/abs/2001.08210).
