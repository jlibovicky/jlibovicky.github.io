---
layout: post
title: "Machine Translation Weekly 37: Backtranslation and Domain Adaptation"
tags: [mt-weekly, en]
lang: en
---

It is sometimes fascinating to observe how each step of training neural machine
translation systems gets one by one picked up by the research community,
analyzed to the tiniest detail and turned into a complex recipe.

Data augmentation by back-translation used to be a pretty simple thing. You
trained initial systems in both directions, took monolingual data, made
synthetic source side for the data and used it for training a new system. This
can be repeated several times until the systems stop improving.

Researchers from CMU in their most recent [preprint on
arXiv](https://arxiv.org/abs/2004.03672) show that when we put more care into
this process, we can achieve much better translation quality, especially when
adapting the system to a specific domain. They are selecting the data for
back-translation on the fly and try to select such data that would be the most
useful for the model at the current state of training.

Parallel data are rare and valuable material. The more we have, the better. We
cannot really afford to filter out a large part of them just because they do
not look like the data we are going to use our system for (e.g., legal or
medical texts). On the other hand, the Internet offers an abundance of
monolingual data in various domains and those we can choose from those which
are the most helpful. And this is the question the paper attempts to answer.

The approach in the paper is a gradual shift from preferring the simplicity of
the sentences (here, a simple sentence is a sentence that does not change much
when we translate it back and forth) to representativeness (by representative
sentences, they mean sentences that look like those from the target domain).
Simple sentences are more likely to yield less noisy synthetic training
examples, so they are more valuable at the beginning of the training, later
when the system can deal with more complex sentences, it is the time to
specialize and hope that the noise would not matter much. Surprisingly, the
good old [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) measure seems
to be the best choice for similarity, rather than using
[BERT](https://en.wikipedia.org/wiki/BERT_(language_model)).

I have described how they select what sentences to use for back-translation,
but this not everything they do. They also score the data by expected
importance and try to prefer those whose translation quality improved the most
in the previous iterations, because they seem to be the most informative ones.
They used heuristics based on comparing encoder representations and I do not
really understand the intuition behind that, but it seems to work well.

Both of these tricks seem to make quite a big improvement compared to just
using the data for back-translation in a naive way. For translation between
English and German, it seems to add around 2 BLEU points for legal and medical
texts. Unfortunately, the two methods seem to do pretty much the same thing, so
combining them does not help much. It is nice to see the results, but it is a
little bit sad that with this knowledge back-translation for domain adaptation
is no longer a simple thing.
