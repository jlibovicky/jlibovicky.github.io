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

Already in 2016, Google announced reaching human parity in machine translation
in a sort of Turing test: the annotators were presented with examples of
authentic and machine-generated sentences and were not able to distinguish
between them. However, the test sentences were rather simple and even the
previous phrase-based systems would do a good job on them.  A slightly bigger
surprise was that in WMT18, the annual competition in machine translation
quality, the Czech-English system from Charles University scored better than
human translations made by a professional translation agency. The paper from
Nature Communication starts with this highly suspicious results and tries to
figure out what is going on.

The first hypothesis of what might be wrong was that the evaluators at WMT were
only presented with isolated sentences without the document context. With the
context, the machine-generated sentences. Unlike WMT, the evaluators in the new
study were presented with the sentences in the context. The result was that
machine translation creates overall better, more adequate, but slightly less
fluent translation than professional translators.

Another experiment was a machine translation version of the already mentioned
Turing test. The participants were presented with a sentence and its
translation and were asked to judge if it is an output of a machine translation
system or a translation made by a human translator. In 60% of cases, the
participants were not able to distinguish between the Charles University system
and human translation. However, in the case of Google Translate the
participants correctly distinguished machine translation in 94% of cases. This
is a very interesting result because the systems are in principle very similar
and according to other criteria they perform similarly as well. It thus seems
that current machine translation quality is in a narrow zone between trashy and
super-human quality and to make it even worse, it is hardly noticeable by
common metrics.

The system used in the paper was trained in a slightly different way than MT
systems are normally trained. The usual way is that we mix authentic parallel
data with synthetic data where the target side is authentic text in the target
language and the source side is the output of a machine translation system.
Often, it also helps to finetune the model on the authentic data only. This
system was trained on alternating blocks of authentic and synthetic data, which
makes the translation quality quite oscillate during the training but
ultimately via seemingly random oscillations, it reaches significantly better
results than data mixing. Unfortunately, I do not have any intuition about why
it might be so and the paper does not provide an answer either.

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
