---
layout: post
title: "Machine Translation Weekly 52: Human Parity in Machine Translation"
tags: [mt-weekly, en]
lang: en
---

This week I am going to have a look at a paper by my former colleagues from
Prague "[Transforming machine translation: a deep learning system reaches news
translation quality comparable to human
professionals](https://www.nature.com/articles/s41467-020-18073-9)" that was
published in Nature Communications. The paper systematically studies machine
translation quality compared to human translation quality with the main
criterion being the human judgment about the translations.

Already in 2016, [Google announced](https://arxiv.org/abs/1609.08144) almost
reaching human parity on their internal test sets. However, these results were
achieved on proprietary tests only and public evaluation campaigns at WMT did
not really confirm the results. A slightly bigger surprise was that in WMT18,
the annual competition in machine translation quality, the Czech-English system
from Charles University scored better than human translations made by a
professional translation agency. This week's paper tries to understand this
highly suspicious results and tell if it is an artifact of how MT is evaluated
or if the MT quality is really so high.

The first hypothesis of what might be wrong was that the evaluators at WMT were
only presented with _isolated sentences without the document context_. With the
context, the machine-generated sentences might look better unlike the human
translator, the MT system does not care about the output coherency. Unlike WMT,
the evaluators in the new study were presented with the sentences in the
document context. The result was that machine translation creates overall
better, more adequate, but slightly less fluent translation than professional
translators.

Another experiment was a machine translation version of the already mentioned
[Turing test](https://en.wikipedia.org/wiki/Turing_test). The participants were
presented with a sentence and its translation and were asked to judge if it is
an output of a machine translation system or a translation made by a human
translator. In 60% of cases, the participants were not able to distinguish
between the Charles University system and human translation. However, in the
case of Google Translate the participants correctly distinguished machine
translation in 94% of cases. This is a very interesting result because the
systems are in principle very similar and according to other criteria they
perform similarly as well. It thus seems that current machine translation
quality is in a narrow zone between trashy and super-human quality and to make
it even worse, it is hardly noticeable by common metrics.

The system used in the paper was trained in a slightly different way than MT
systems are normally trained. The usual way is that we mix authentic parallel
data with synthetic data where the target side is authentic text in the target
language and the source side is the output of a machine translation system.
Often, it also helps to finetune the model on the authentic data only as a last
step. This system was trained on alternating blocks of authentic and synthetic
data, which causes the translation quality quite oscillates during the training
but ultimately via the seemingly random oscillations, it reaches significantly
better results than data mixing. Unfortunately, I do not have any intuition
about why it might be so and the paper does not provide an answer either.

The paper tries to answer the question of how does current best machine
translation compare to human translation. But it seems to me that it rather
raises plenty of difficult questions such as: How does the best possible
translation look like? If the gold standard is not human, is it divine then?
Does that mean that we need really carefully prepared (and expensive) test sets
that the references are always better than MT? And what if they are not? With
such a translation quality, what do the automatic metrics say when they compare
the MT output with a reference translation that is actually worse? And my final
question is: if the paper so rigorously showed that machine translation reached
human parity, how is it possible that we machine translation so often so
spectacularly fail (in other words, what is wrong with most evaluations)?
