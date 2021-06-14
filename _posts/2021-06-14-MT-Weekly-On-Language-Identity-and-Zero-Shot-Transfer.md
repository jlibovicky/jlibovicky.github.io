---
layout: post
title: "Machine Translation Weekly 83: On Language Indentity and Zero-Shot Transfer"
tags: [mt-weekly, en]
lang: en
---

This week I will comment on two papers on zero-shot cross-lingual model
transfer which do not focus on the representation quality but on the transfer
itself. The title of the first one is [Language Embeddings for Typology and
Cross-lingual Transfer Learning](https://arxiv.org/abs/2106.02082) and has
authors from UC Davis.  The second is [Syntax-augmented Multilingual BERT for
Cross-lingual Transfer](https://arxiv.org/abs/2106.02134) and has authors from
UC LA and Facebook AI. Both papers will appear at [this year's
ACL](https://2021.aclweb.org).

Just a reminder, zero-shot model transfer means training a model on one
language for which training data exist, but using the model with a different
language at inference time. This magic should be possible thanks to
language-agnostic underlying representation that should capture the sentence
structure and meaning similarly regardless of the language. Limited language
neutrality of the representations is considered one of the major issues that
make the transfer difficult.

The first paper introduces language identity embeddings that later improve the
zero-shot transfer. In the first stage, they train a denoising autoencoder
using the original recurrent sequence-to-sequence architecture. The encoder RNN
reads the input sentence and immediately a decoder RNN follows and generates
the target sequence. The only interface between the encoder and the decoder is
a single vector – the RNN state. In the autoencoder setup in the paper, they
randomly shuffle words of the input sentence and attempt to decode it in the
original order. They use pre-trained word embeddings concatenated with the
language identity embedding. By training this thing, they end up with language
embeddings that should contain something like instruction on how to correctly
order a sentence. The intrinsic evaluation of these vectors shows that the
embeddings contain information quite a lot of information about various
language features (as categorized in the [WALS database](https://wals.info)).

Now, the most interesting thing (or perhaps the weirdest thing): When they
added those embeddings to pre-trained sentence representation and tried
zero-shot transfer on natural language inference and syntactic parsing, the
performance dramatically improved. The language embedding then plays a role of
a reminder of what properties the input language has as if the model forgot
that during finetuning.

The second paper makes an observation that task-specific finetuning of a
pre-trained model ruins interesting spatial properties of pre-trained
representations. A [very cool paper by John Hewitt and Christopher
Manning](https://www.aclweb.org/anthology/N19-1419/) from 2019 showed that it
is possible to find a linear projection of BERT embeddings such that the
distances of the embedding would correspond to distances in a syntax tree. This
property however seems to get broken when finetuning the representation for
downstream tasks, at least in the languages that are not part of the training.
The paper comes with an auxiliary loss function that ensures that the syntactic
properties do not break during finetuning. Again, with this trick added, the
zero-shot transfer improves a lot.

The thing these two papers have in common is that they try to fix the transfer
step by fixing some representation properties which are specific to
multilingual representations. So far, my impression was that the transfer phase
is clear (just train on one language and test on another one) and what we need
to focus on is making the representations more language-neutral. In [our
previous
experiments](https://www.aclweb.org/anthology/2020.findings-emnlp.150), we
found out that it is easy to guess the language identity from the
representations, basically no matter what we do with the models and I assumed
this is something we need to get rid of. Maybe this was wrong thinking. Both of
these papers get improvements by strengthening language-specific properties at
the right place of the model.
