---
layout: post
title: "Highlights from Machine Translation and Multilinguality 02/2022"
tags: [mtml-highlights, en]
lang: en
---

After 100 MT Weekly posts (which took me 130 weeks to write), I realized that
weekly blogging is impossible while weekly teaching. So I decided to change the
format of the post and write monthly summaries of what I found most interesting
in machine translation and multilinguality. This is the first issue that
summarizes what interesting happened in February.

### Exciting news about WMT

There will be some exciting changes in WMT competitions. WMT is an annual
conference on machine translation that organizes competitions in translation
quality and other tasks related to machine translation. Tom Kocmi, who is now
in charge of the competitions [announced on
Twitter](https://twitter.com/KocmiTom/status/1491835342063812609) that that
main task, previously known as the News Task will contain multiple domains
(news, e-commerce, social, and conversational texts) gets renamed to General
Task.  Also, more low-resource languages are to be expected. The change
reflects the fact that translation of news in high-resource languages is almost
solved (unlike all other MT use cases), but more importantly, these are
typically large computational resources rather than creative ideas that help to
win the competitions.

Another good news is that participants will no longer be required to provide
hours and hours of manual evaluation (this will be done by sponsors), which
makes the competition accessible for more research groups.

### Studying COMET via Minimum Bayes Risk decoding

A [pre-print from the University of
Zurich](https://arxiv.org/pdf/2202.05148.pdf) comes with a creative way of
assessing weaknesses of machine translation evaluation metrics using Minimum
Bayes Risk decoding. MBR decoding does not aim to find the most probable
translation.  Instead, it randomly samples many hypotheses from the models and
then selects the one that is the most similar to other sampled hypotheses. In
the paper, they use COMET (the state-of-the-art metric for MT evaluation) as
the similarity measure and analyze the specific features of the outputs. From
this analysis, it seems that COMET tends to ignore errors in numbers and named
entities, which is not evident from measuring the correlation with human
judgment, simply because current MT models do not make these types of errors.

### BERT can mask up to 40%

While pre-training BERT, 15% of input tokens get masked out and should be
predicted by the model using the context. This rule of thumb sounds so
reasonable that no one questioned it so far. An [empirical study from Princeton
University](https://arxiv.org/pdf/2202.08005.pdf) shows that 40% is optimal.
Good to know.

### Multiliguality and multimodality

There is also interesting news in the area of multilingual multimodal tasks.
After announcing the IGLUE benchmark in January, there is was a shared task
announced that focuses on zero-shot and few-shot visual question answering at
the workshop on [Multilingual Multimodal Learning at ACL
2022](https://mml-workshop.github.io/shared_task.html). The training data are
only provided in English, but the models are tested in several different (and
culturally distant languages).

Related to this, folks from Darmstadt published a
[pre-print](https://arxiv.org/abs/2202.07630) showing tricks on how to the
zero-shot transfer of visual question answering between languages much better
than the IGLUE benchmark shows. First, they use a deeper classifier on top of
the CLS token representation. Second, they do some tricks with freezing and
unfreezing model parts during finetuning.

### Czech-Ukrainian Translation

At Charles University, we are building a [Czech-Ukrainian translation
system](https://ufal.mff.cuni.cz/ufal-ukraine) that could help the Ukrainian
refugees and Czech officials with communication in the upcoming weeks. If you
know or have any parallel data that are not among the best-known ones, please
let me know.
