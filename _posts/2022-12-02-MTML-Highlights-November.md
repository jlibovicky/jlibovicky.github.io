---
layout: post
title: "Highlights from Machine Translation and Multilinguality in November 2022"
tags: [mtml-highlights, en]
lang: en
---

Here are my monthly highlights from paper machine translation and
multilinguality that appeared on arXiv in November 2022.

A [preprint with 19 authors from 13
institutions](https://arxiv.org/abs/2211.01786) presents something like the T0
model: but instead of starting with the (more or less) monolingual T5 model,
they use multilingual BLOOM and mT5 and call the resulting model BLOOMZ and
mT0. The main idea is finetuning the underlying model (or the foundation
model?) on as many tasks as possible so that the model learns that it will be
used to solve different sorts of stuff instead of language modeling. It seems
to work well for most tasks.  Machine-translating training data of the
adaptation/first-finetuning/task training worked well.

A [preprint with authors from three Beijing
institutions](https://arxiv.org/abs/2211.06679) shows interesting work on
improving the language abilities of the CLIP model. CLIP is a large
language-vision model from OpenAI that trains both the language and vision
components jointly from scratch. Nowadays, it is probably best known as a
component in the popular diffusion models for image generation. In the
preprint, they replace the CLIP text encoder with pre-trained XLM-R. Or in
other words, they finetune XLM-R to behave like the CLIP encoder regardless of
the languages (but they only consider English and Chinese). Surprisingly, it
improves both image-to-text and text-to-image retrieval in both English and
Chinese. During training, the CLIP text encoder only encountered image
descriptions, which is a rather specific use of language. Perhaps, replacing
this limited encoder with something that generalizes beyond visual descriptions
and anchoring that something on the visual description is the way to have a
generally visually aware text encoder.

A preprint from the Imperial College and the University of Sheffield [studies
hallucinations in machine translation](https://arxiv.org/abs/2211.09878).
Hallucinations are an undesirable property of machine translation models. The
models sometimes generate something that is totally unrelated to the source
sentence but is quite fluent and nicely fits in the target sentence. They
authors find out that the usual triggers of this behavior are out-of-vocabulary
and rare words. Further, they analyzed the model's inner workings and observed
that hallucinations often connect with higher attention entropy and their
integrated gradient entropy. Based on this observation, they add entropy as a
regularization term to the training objective and successfully decrease the
hallucination rate.

Folks from Google studied the [machine translation abilities of the PaLM
model](https://arxiv.org/abs/2211.09102), a mythical language model that can
explain jokes, and only Google can experiment with it. They use a few-shot
setup, present the model with a couple of (= five) translation examples and let
it continue. They construct the prompt on the fly by searching for the
source-sentence nearest neighbors in a parallel corpus. The translation that
they get is, by a large margin, worse than SoTA MT models, but still, the
translation quality is pretty decent (i.e., hardly thinkable a few years ago,
regardless of the method). German, one of the foreign languages tested, is only
3.3% of the training data of PaLM, so I wonder what would happen if we did the
same thing with something that is inherently multilingual. Did someone try
something like this with Bloom or OPT? The authors also deserve kudos for the
exceptional quality of the machine translation evaluation.
