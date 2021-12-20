---
layout: post
title: "Machine Translation Weekly 97: Multilingual and Non-autoregressive MT at the same time"
tags: [mt-weekly, en]
lang: en
issue: 97
---

Multilingual machine translation models look very promising, especially for
low-resource languages that can benefit from similar patterns in similar
languages. A new preprint with authors from the University of Maryland and
Google Research studies how these results transfer to non-autoregressive
machine translation models. The title of the paper is [Can Multilinguality
benefit Non-autoregressive Machine
Translation?](https://arxiv.org/abs/2112.08570). Spoiler: it is not as good as
it might seem.

The paper tries to answer two questions: First, is it better to use a
multilingual teacher model or bilingual teacher models? Second, how does the
positive and negative transfer differ in the case of autoregressive and
non-autoregressive models? The _negative transfer_ happens if unrelated
languages share a model, so the model has a limited capacity. The _positive
transfer_ happens if the languages are related and can benefit from each other.
(I heard the concepts of positive and negative transfer for the first time and
seemed to me like a very good way to conceptualize what is going on. But I
guess it is not a contribution of the paper and it was mentioned somewhere
before.)

Non-autoregressive MT is typically trained on synthetic data: a parallel corpus
translated by an autoregressive teacher model. Because it is the training data
of the teacher model, it is a little overfitted to the data, so the translation
quality is really good. On the other hand, the sentences still look like
machine translation outputs, which among others means that they tend to be
simpler than the original bitext and more consistent in choice of linguistic
structures. This is exactly what the NAR models can benefit from at training
time. This paper makes an observation that outputs of multilingual models are
even simpler and even more consistent, which looks promising. But no, bilingual
teachers are better than multilingual one.

When I opened the paper I secretly hoped that the non-autoregressive model
would be surprisingly good in the multilingual setup. The NAR models are after
all weaker than their autoregressive counterparts, so it might force them to
learn stronger representation and benefit from the positive-transfer setup.
Well... not really. The negative effect of the negative transfer (unrelated
languages) is more negative with NAR models, the positive transfer (related
languages that reinforce each other) is less positive with NAR models.

In the end, I also need to acknowledge that the paper does not make unjustified
claims about translation speed and most importantly compares distilled
autoregressive with distilled non-autoregressive models, the greates sins of
non-autoregressive MT that I [warned about last
week](/2021/12/11/MT-Weekly-Evaluating-Non-autoregressive-MT.html). Good job!
