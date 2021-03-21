---
layout: post
title: "Machine Translation Weekly 72: Self-Training for Zero-Shot MT"
tags: [mt-weekly, en]
lang: en
paperTitle: "Self-Learning for Zero Shot Neural Machine Translation"
paperAuthors: "Surafel M. Lakew, Matteo Negri, Marco Turchi"
issue: 72
---

This week, I will have a look at a pre-print that describes an unconventional
setup for zero-shot machine translation. The title of the pre-print is
[Self-Learning for Zero-Shot Neural Machine
Translation](https://arxiv.org/abs/2103.05951) and was written by authors from
the University of Trento.

First of all, I have some doubt about this being really an instance of
zero-shot learning (but it is just nitpicking, the paper is interesting
regardless of the terminology). In machine learning, zero-shot learning means
that a model trained for task _A_ is capable of doing task _B_ without being
explicitly trained for that. An example can be: a model is trained to perform
sentiment analysis in English, but it can also do it in German because it was
trained on top of multilingual representation. This would supervised learning
for English, and zero-shot learning for German. In machine translation, the
typical zero-shot setup means training a joint model translating from _A_
to _B_ and from _C_ to _D_. it this is done correctly, the system can also
translate from _A_ to _D_ without ever having an _A_-to-*D* training
example.

In this pre-print, they start with an existing MT model, and using
back-translation of monolingual data, they turn it into an MT system for a
different language pair. The setup is therefore slightly different than
classical zero-shot learning, but much more realistic, and more useful in
practice.

The paper shows a method for a sort of unsupervised training of MT given that
you have a model that can translate a related source language _S_ into target
language _T_. The model works well, but you are in fact interested in
translating from _U_ (that is related to _S_) into T and you only have
monolingual data for _U_ (and of course plenty of monolingual data for _T_).

The procedure that they propose works as follows:

* Use the _S_→_T_ system to translate _U_ to _T_, this generates synthetic data
  (T is the synthetic side, U is the authentic side)

* Use the synthetic data to train a T→U system

* Translate monolingual T data to get another synthetic set (now, T is the
  authentic side, U is the synthetic side)

* Train a new S→T system using *both* the dataset and iterate further.

They experiment with several low-resource languages, always paired with a
high-resource one (Azerbaijani+Turkish, Belarussian+Russian,
Galician+Portugeese, Slovak+Czech) and trained translation from and into
English. There was a small amount of training data for each of the languages,
so I would expect that using this small amount and do back-translation would be
similarly good as initializing the system with related language and only use
back-translation. This was, however, not the case. The gains were even higher
when the models were initialized by multilingual models rather than the
bilingual ones, but I tend to speculate that the reason might be that the
bilingual parent models were trained on rather small datasets too. The
multilingual parents might be better just because they just used more data in
total.

At LMU, we are now organizing the next round of the WMT Unsupervised and Very
Low Resource Task (will be announced soon; in addition to [last year's Upper
Sorbian-German
translation](http://www.statmt.org/wmt20/unsup_and_very_low_res/), it will
feature Lower Sorbian-German and Chuvash-Russian translation). Methods like
this one would make an excellent contribution to the challenge.
