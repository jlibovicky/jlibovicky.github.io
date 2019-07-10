---
layout: post
title: "Machine Translation Weekly 9: Shared Task on Machine Translation Robustness"
tags: [mt-weekly, en]
lang: en
---

Machine translation is typically trained on bilingual data that can be found on
the Internet. It mostly comes from international government and non-government
organizations, commercial web presentations, books, movie subtitles, etc.
Therefore, most of the text is quite formal and almost without typos and
certainly without emojis. The more you sound like an EU institution, the better
is the translation you get. Once you start using weird CAPITALIZATION, add
emojis 😃😵😂 and occasionally do a typo, the translation system gets usually
lost.

One of the competition tasks (so-called shared tasks) at this year [WMT
Conference](http://www.statmt.org/wmt19) (Conference on Machine Translation
that gets abbreviated as WMT it used to be a workshop) was [translation of
Reddit posts](http://www.statmt.org/wmt19/robustness.html). The organizers let
professional translators translate several hundreds of Reddit posts between
French and English and between English and Japanese and asked the translators
to preserve all the weird stuff as closely as possible (poor translators doing
this weird job). Some posts were left for possible training or fine-tuning of
the systems, some for testing. Organizers published the data and competing
teams sent their translations. [Findings of the
competition](https://arxiv.org/pdf/1906.11943.pdf) were out almost four weeks
before the actual conference.

Half-a-dozen teams submitted their systems to the competition and the results
are actually pretty good. It almost seems that if you are careful enough, the
translation system can be as good as with standard sentences.

What did the teams do to make their systems work well on the [Reddit
data](https://arxiv.org/pdf/1809.00388.pdf)?

1. _Data augmentation with back-translation._ One thing that makes the Reddit
   posts different from standard text is capitalization and non-standard
   splitting of the words (with hyphens or spaces). At training time, all of
   these can be simulated on the target sentence. For the modified sentences,
   you can generate a synthetic source sentence and use it as additional
   training data.

2. _Placeholders for emojis._ Emojis and ASCII art do not get translated, they
   are just the same in the source sentence and in the target sentence. There
   is plenty of different emojis and for each of them the system needs to learn
   to copy it to the target sentence. If we replace all of them by the same
   placeholder symbols, the system will learn to copy the placeholders. In a
   post-processing step, the placeholders are one-by-one replaced with the
   strings from the source sentence.

3. _Fine-tuning._ If you have a few hundreds of examples of how the actual data
   will look like, you can use it to fine-tune a system that was trained on
   large data. If you are careful, it will not even hurt the performance on the
   standard texts.

It seems to me from the findings of the shared task that making a translation
system robust enough to work on Reddit posts is actually quite easy (maybe
easier than the organizers expected, but certainly than I expected), which is
certainly a pleasant surprise. If there is a competition next year, I hope the
data should be much noisier to keep the task interesting.
