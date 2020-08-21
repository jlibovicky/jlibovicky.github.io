---
layout: post
title: "Machine Translation Weekly 49: Paraphrasing using multilingual MT"
tags: [mt-weekly, en]
lang: en
---

It is a well-known fact that when you have a hammer, everything looks like a
nail. It is a less-known fact that when you have a sequence-to-sequence model,
everything looks like machine translation.  One example of this thinking is the
paper [Paraphrase Generation as Zero-Shot Multilingual Translation:
Disentangling Semantic Similarity from Lexical and Syntactic
Diversity](https://arxiv.org/pdf/2008.04935.pdf) recently uploaded to arXiv by
researchers from Johns Hopkins University.

The paper approaches the task of paraphrase generation, i.e., for a source
sentence, they want to generate a target sentence in the same language, with
the meaning as similar as possible to the source sentence, but worded as
differently as possible. Their approach does not need any training examples of
paraphrased sentence pairs. It only needs a multilingual machine translation
system (which is indeed a complex system that not everyone just has on their
hard drives for case). The training requires plenty of parallel sentences
(i.e., sentences which are a translation of each other) in several languages.
It is hard to say what sort of data is easier to obtain: whether mutual
paraphrases or mutual translations, but I would probably vote in favor of the
translation.

The paper creatively reiterates the idea of zero-shot machine translation. In
such a setup, we only have parallel data for some language pairs and we train a
single model to translate between all of them. To do so, the model needs to be
told what is the source language and what is the target language and it uses
special symbols appended to the input for that. When this is trained properly,
we can tell the model to translate between two languages it was never presented
together at the training time, but only within different language pairs.
Something like what is shown in the following scheme (from [MT Weekly 7 about
zero-shot translation](2019/06/24/MT-Weekly-Improved-Zero-shot-NMT.html)):

![Zero-shot translation](/assets/MT-Weekly-7/scheme.svg)

This is basically the model they train in this paper. However, in the end, they
tell the model to translate from English into English, and this is how they get
the paraphrases.

This is cool, but there is nothing telling the model that output should be
worded differently than the input. It appears to have a simple solution which
is the second innovation of the paper. They introduce a simple modification of
the beam search algorithm such that it penalizes using word _n_-grams that are
in the source sentence. We can thus view the beam search as optimization of two
opposing objectives: the probability given the model, and dissimilarity from
the source. And this is it! This how the best current paraphrasing system works
(although it is hard to say what the best means because the evaluation of
paraphrases is quite tricky).

I like the paper because it shows a creative way of using existing models. The
models are trained to solve some specific tasks, but to so, they must be aware
of plenty of other things. Being able to hack the models and get what is hidden
inside is just cool. It shows that neural models are no longer total
black-boxes, so we can bend them such that they do what we want.

Dual-use disclaimer: Dear plagiarists, academic pirates, and lazy students,
this is a tool for you! But don't overdo it, machine-generated text can be
easily automatically recognized.
