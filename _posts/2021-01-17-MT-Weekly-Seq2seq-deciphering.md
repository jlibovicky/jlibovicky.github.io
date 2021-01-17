---
layout: post
title: "Machine Translation Weekly 65: Sequence-to-sequence models and substitution ciphers"
tags: [mt-weekly, en]
lang: en
---

Today, I am going to talk about a recent pre-print on sequence-to-sequence
models for deciphering substitution ciphers. Doing such a thing was somewhere
at the bottom of my todo list for a few years, I suggested it as a thesis topic
to several master students and no one wanted to do it, so I am glad that
someone finally did the experiments. The title of the preprint is [Can
Sequence-to-Sequence Models Crack Substitution
Ciphers?](https://arxiv.org/abs/2012.15229) and the authors are from the
University of Southern California.

They work with [1:1 substitution
ciphers](https://en.wikipedia.org/wiki/Substitution_cipher). This means that
every character in the text gets systematically replaced by another one, but
always the same one. Such ciphers are easy to crack based on the frequency of
the characters. If you would do that manually, you would probably sort the
characters by frequency and do the first substitution. Then, by swapping some
characters, you would probably quickly find the correct substitution key. The
longer the text, the more reliable the frequency statistics, and the easier
cracking of the cipher is. This only true if you know what the target language
is.

The experiments in the paper are actually quite simple too. In the paper, they
sample synthetic data and train a Transformer model on it. One interesting
result is that they did not manage to train the model with arbitrary
substitution without pre-processing. The sequence-to-sequence model is only
capable of learning something useful if they order the characters by frequency.
Although this is just leisurely mentioned in the paper, I think this says an
important thing about the Transformer architecture. It might show that the
architecture itself cannot do much if there is no meaningful information that
could be stored in the symbol embeddings. In this case, it is the information
about the symbol frequency which is already a strong indicator of what the
target characters might be.

The main result of the paper is that it is possible to train a model that is
capable of deciphering in multiple languages without knowing the language in
advance. Unfortunately, with the increasing number of languages, the error rate
increases quite quickly. The model also seems to be rather sensitive to
source-side noise. An important motivation for such models would be the
deciphering of old (medieval or older) manuscripts written in unknown
languages. Noise sensitivity and degradation with more languages included are
very undesirable for such applications.

It might seem that what is presented in the paper are only nice toy
experiments, but I believe, this can a good start for many follow-up
experiments. First, it might be useful for studying inductive biases of the
Transformer architecture: by observing what sentences could be and what
sentences could not be deciphered, we might judge what language features the
model relies on when deciphering, which are likely to be features that are
easier for the Transformer architecture to learn. Second, I wonder if this
could a good way of pre-training character-level machine translation.
