---
layout: post
title: "Machine Translation Weekly 77: Reference-free Evaluation"
tags: [mt-weekly, en]
lang: en
paperTitle: "Assessing Reference-Free Peer Evaluation for Machine Translation"
paperAuthors: "Sweta Agrawal, George Foster, Markus Freitag, Colin Cherry"
issue: 77
---

This week, I am will comment on a paper by authors from the University of
Maryland and Google Research on reference-free evaluation of machine
translation, which seems quite disturbing to me and suggests there is a lot
about current MT models we still don't quite understand. The title of the paper
is ["Assessing Reference-Free Peer Evaluation for Machine
Translation"](https://arxiv.org/abs/2104.05146) and it will be published at
this year's [NAACL conference](https://2021.naacl.org).

The standard evaluation of machine translation uses reference translations:
translations that were produced by humans and that we believe are of high
quality (although there could be a very long discussion about what high quality
in this context means). Machine translation systems are evaluated by measuring
the similarity of their outputs with these high-quality reference translations.
The adequacy of the similarity measures themselves is validated by measuring
how much the similarity scores correlate with human judgment on the translation
quality.

This paper is a follow-up to [previous
results](https://www.aclweb.org/anthology/2020.emnlp-main.8/) that showed that
probability scores from a multilingual machine translation model are a very
good estimator of the translation quality but in a different and much more
reasonable setup. MT models are trained as conditional language models, which
means that for an input sentence and a prefix of the output sentence, it
computes a probability distribution of what symbol should come next. These
distributions can be used for actual generating of the probable next words, but
also for scoring of how probable a given translation is given the model. The
original paper by [Thompson and
Post](https://www.aclweb.org/anthology/2020.emnlp-main.8/) used multilingual
translation as a zero-shot paraphraser. They trained a single model for
translation between many language pairs at once, but in the end, they asked the
model to translate to the same language as the source language. It caused the
model to paraphrase the input. They used this model to measure how well the
machine translation hypothesis paraphrases the reference translation – and this
appeared to be a very good estimation of the translation quality.

The most recent paper, however, uses the translation models directly, not as
zero-shot paraphrasers: they asked a different translation model (also trained
in the multilingual setup), how probable the MT output would be given the
source sentence in the multilingual model. Surprisingly, these scores correlate
quite well with the human judgment, even though no reference translation was
used. And even though the multilingual model itself would generate a worse
translation.

Such evaluation has one undesirable property: outputs of the multilingual model
get by definition a high probability given the model, although, we know that
other models are better. The authors naturally suspected that such evaluation
will be biased towards sentences that are more similar to the outputs of the
multilingual model. The experiments show that it is not the case. This is cool,
but I have no idea (and probably neither do the authors) how this can happen.

One trick the paper does is sampling different segmentations using
sentence-piece and then ensembling the scores that they get with different
random segmentations. This seems to be too little to explain this weird
behavior.

The authors seem to be very happy about the result. The reference-free
evaluation is almost as good as the standard evaluation but does not need the
high-quality reference translations which are expensive to produce. The
reference-free evaluation can be thus done on a much larger dataset and thus be
in the end more reliable. I am on the other hand more concerned than happy
about the results: they seem to show that there is something that we do not
know about the models.
