---
layout: post
title: "Machine Translation Weekly 60: Notes about WMT 2020 Shared Tasks"
tags: [mt-weekly, en]
lang: en
---

This week, I will follow up the last week's post and comment on the news from
this year's WMT that was collocated with EMNLP. As every year, there were many
shared tasks on various types of translation and evaluation of machine
translation.

### News translation task

The news translation task is the oldest task at WMT and sort of a flagship task
providing benchmarks for MT research in the long term. Test sets are created by
manually translating recent news stories and new test sets are released every
year. Originally, this task was targeted on sentence-level translation of high
resource language pairs, but recently some language pairs are evaluated on the
document level, and also a few low-resource language pairs were added.

This year, there were 168 entries from 37 institutions. When I superficially
skimmed over the submissions, my impression was that most of the well-scoring
teams did not anything really innovative (although the devil is in the details
and the winners certainly paid a lot of attention to details). Most of the
teams used the Transformer big architecture, used back-translation at scale,
filtered data in a clever way, and did some sort of model ensembling, so
nothing fundamentally different from the last year.

Human evaluation typically led to a few clusters of indistinguishable systems.
Often human translation is in the same cluster (i.e., mutually
indistinguishable) as human translation, especially when translating into
English. Commercial systems are typically worse than the competing systems.

Another interesting observation was that in translation from English to German,
different sets of human references scored differently. They were translated by
different professional agencies with the same quality standard and with the
same instructions, but it seems the translations are of different quality. What
does it say then about the differences among the translation systems? This is
sort of disturbing, isn't it?

### Robustness

Here, the task is translation of noisy user-generated input that contains
typos, smileys, and non-standard language (including slang, profanities or very
toxic language). Similar to the news task, the techniques used by the competing
teams were nothing groundbreakingly new or clever. Multiple teams used adapter
layers to adapt the model trained for standard translation for the noisy data.
Other teams focused more on data pre-processing.

I liked the way this task was evaluated. In addition to directly assessing the
translation quality, the raters were asked to indicate if the sentence contains
a catastrophic error, i.e., something that dramatically changes the meaning, so
it is no longer a good translation. Data from the evaluation campaign might be
a good complement to standard data for metrics evaluation. Using the data about
the "catastrophic errors," we might start to ask if the metrics separate the
good and "catastrophically bad" translations in addition to ranking the
translations in the same order as humans.

A sort of surprise was that there is no correlation of BLEU with the human
scores which did not score that bad in this year's metrics task. However,
evaluation of this task includes several difficult questions: Should the
translation keep the noise? Is it an error when the translation removes
toxicity?

### Post-editing

In the postediting task, the goal is to modify the output of a black box MT
system, in the same way as a professional translator would do. Recently many
interesting architectures were introduced ([Laser
Tager](https://www.aclweb.org/anthology/D19-1510.pdf), [Levenshtein
Transformer](https://papers.nips.cc/paper/2019/hash/675f9820626f5bc0afb47b57890b466e-Abstract.html),
[Seq2Edits](https://www.aclweb.org/anthology/2020.emnlp-main.4180)) that might
be well-suited for this task. Alas, all the submissions were just large
sequence-to-sequence Transformers.

### Low-resourced languages

On the second day of WMT, there was a breath-taking keynote about the
[Masakhane](https://www.masakhane.io) project, a pan-African initiative to make
machine translation NLP in general available for many low-resourced languages
in Africa. It s a bottom-up initiative without any institutional funding or
systematic support from the institutions in the developed world. They did an
amazing job, the people do it for social good, strongly motivate to improve the
life of their own communities.

A question that came to my mind during the keynote and the following discussion
was whether having a high-quality machine translation cannot, in the end, harm
the language communities. Will it bring more opportunities for local
businesses? Or will it on the other hand allow western companies to colonize
other parts of developing economies?  Will it help people to be better
informed? Or will it help governments with authoritative tendencies to collect
more detailed information about the population?

During the session, this question seemed to me to be too cynical to ask, facing
the people that are so passionate about their work and being convinced that
they do the right thing (which they probably do, and these my thought are only
unwanted cynical back-seat driver advice). Anyway, I hope some people ask the
questions that I do, take them seriously, and do something more about it than I
do.
