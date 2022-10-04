---
layout: post
title: "Highlights from Machine Translation and Multilinguality in August 2022"
tags: [mtml-highlights, en]
lang: en
---

There were not many papers I made notes about in August (likely because I was
on vacation most of it). Anyway, here are three papers that I think should not
be forgotten just because they went out in August.

A [paper](https://arxiv.org/abs/2208.06061) by folks from JHU, Microsoft and
UNC Chappel Hill accepted to [AMTA](https://2022.amta.org) experiment with
morphologically rich and rather low-resource languages (Inuktitut and Turkish)
and play around with morphological segmentation and additional inductive biases
in the Transformer architecture. First, they use morphological segmentation
works much better than statistical segmentation. Second, they tried an
architecture improvement originally designed for models doing arithmetics,
hoping that this component will take over morphological regularities that in
some sense remind regularities of arithmetic operations.

Folks from NYU and JHU did a [survey among NLP
researchers](https://arxiv.org/abs/2208.12852). They asked about what people
think about NLP and AI in general and also what they think most of the
community thinks.  Some of the results are quite interesting. People think big
companies have too much influence, two thirds (including me) think that most
NLP research is dubious science (but half of the people thinks other do not
think so). This discrepancy is even bigger by the question of whether scaling
up models will solve virtually all NLP problems, almost no one thinks that, but
they think others think so.

Microsoft published a pre-print for a [language-vision model called
BEIT](https://arxiv.org/abs/2208.10442), which looks like a good model for
vision-language modeling. If I were supposed to work on multimodal translation
once again, I would definitely have a look at this model. There are no
groundbreaking ideas: it is based on masked-language modeling, images are
represented with patches, there are specialized heads for modalities... Anyway,
it seems to work well, which makes it a valuable resource.
