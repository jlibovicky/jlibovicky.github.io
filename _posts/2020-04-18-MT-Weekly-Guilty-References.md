---
layout: post
title: "Machine Translation Weekly 38: Taking Care about Reference Sentences"
tags: [mt-weekly, en]
lang: en
---

In the recent week, there were quite a lot of papers on machine translation on
arXiv, at least a few of them every day. Let me have a look at one that tackles
an important topic – machine translation evaluation – from a quite unusual
perspective. When people talk about machine translation evaluation they usually
point out the drawbacks of existing automatic evaluation methods and try to
suggest better ones. The paper I am going to talk about thinks differently:
what if the metrics are not that bad, what if there is something wrong with the
evaluation data. The title of the paper is [BLEU might be Guilty but References
are not Innocent](https://arxiv.org/pdf/2004.06063.pdf) and comes from Google
Research.

In general, it is hard to say what makes a good translation. To avoid thinking
too much about this difficult problem, machine translation adopted an approach
of behaviorist simulation. Some humans can translate between languages. They
can also recognize what is a good translation and what is not. Great! This
everything that we need to know to collect data and train a model that
simulates human behavior when translating. Under these conditions it seems
obvious how we should evaluate the models: we should measure, to what extent
the system succeeded in generating a human-like translation, i.e., measure
similarity with human translations. And a good measurement is a measurement
that well correlates with human judgment, it is a simulation of how much humans
like their own simulation.

The paper mentions findings of translation studies that translated sentences
are different from sentences that are naturally written. The translated
sentences tend to follow the word order and word choice of the source language,
perhaps because it poses a smaller cognitive load for the translator. They call
the language (or a dialect) of the translation
[_translationese_](https://en.wiktionary.org/wiki/translationese). Reference
translation used for evaluation is exactly this kind of translationese. Having
this in mind can surprisingly help with the evaluation.

The most frequently used evaluation metric is the [BLEU
score](https://en.wikipedia.org/wiki/BLEU). It was originally designed to work
with a diverse set of reference sentences. BLEU is an average of _n_-gram
precisions weighted by a number called the brevity penalty. An _n_-gram is a
sequence of _n_ consecutive words in a sentence. The _n_-gram precision is a
proportion of _n_-grams from the translation hypothesis that appear in the
reference sentences, i.e., an _n_-gram is considered correct if it appears in
at least one of the reference translations. The [original study from
2002](https://www.aclweb.org/anthology/P02-1040.pdf) clearly showed that the
more references, the better the metric correlates with what humans think about
the translation.

This is why the guys in Google decided to create additional, presumably, better
quality reference translation to an existing evaluation set. After all, more
translations are supposed to lead to more reliable evaluation. Further, they
asked annotators to create paraphrases of the original and new references and
the goal was to make the sentences sound more natural, less like
translationese. Later they asked another group of people to independently rate
all these translations. The alternative translations were slightly better than
the original ones, the paraphrases were considered to be slightly worse
translations.

They experimented with these different reference sentences and measured how the
results correlate with human judgment. One surprising result: using multiple
references does not help at all. Current machine translation systems are so
much better than in 2002, so with multiple references, all the generated
sentences get really high scores that do not really distinguish between the
systems. Single references are better, but it depends on what reference you
chose. The two equally good options seem to be:

* Create two independent reference translations and then let a third person
  decide which one of them is better.

* Create one reference translation and ask a second person to change as much as
  possible without changing meaning and then let a third person check if it is
  really so. (Even though the paraphrases themselves are not considered to be
  better translations.)

I am not really sure if it is good or bad news for the field. They clearly
showed that high-quality reference sentences can lead to better evaluation even
with existing evaluation metrics. This is certainly a positive result. However,
the protocols to generate high-quality reference sentences are costly. They
include paying hours and hours of expert work which might not be affordable for
large public evaluation campaigns like WMT.
