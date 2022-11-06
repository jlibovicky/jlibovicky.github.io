---
layout: post
title: "Highlights from Machine Translation and Multilinguality in October 2022"
tags: [mtml-highlights, en]
lang: en
---

Here are my monthly highlights from paper machine translation and
multilinguality that appeared on arXiv, many of them preprints from the
upcoming EMNLP conference.

Folks from Amazon [published a pre-print](https://arxiv.org/abs/2210.04782)
that introduces a simple method of how to make pre-trained multilingual
representation more robust towards noisy inputs. It is a very straightforward
approach: they sample typos based on Wikipedia logs and use those during model
training. In addition, they add a contrastive loss that forces the noisy
versions of sentences to get the same representations as the originals.

Aligning word embeddings across languages often fails because the monolingual
word embedding spaces are not isomorphic. In [their EMNLP
paper](https://arxiv.org/abs/2210.05098), folks from Johns Hopkins University
try to get rid of this problem by forcing the monolingual embeddings to be
isomorphic already during the monolingual part of training. They come up with
several measures of how isomorphic the embeddings are (e.g., the Pearson
correlation of distances on a seed dictionary, and eigenvalues in-language
similarity matrices). It is a beautiful idea (I particularly like the
eigenvalues), but it only brings a modest improvement.

Folks from Stanford University [published a
pre-print](https://arxiv.org/abs/2210.05619) showing that multilingual BERT has
grammatical biases toward English. They created a challenge set in Greek and
Spanish with sentences that have two variants: one with a grammatical
phenomenon that does not exist in English and a second one that conforms also
with the English grammar. In Spanish, they drop pronouns that are obvious from
the context. In Greek, they switch the verb and object. Multilingual BERT
prefers the English-conform sentence versions.

All neural NLP models manifest some biases: against gender, race, age, or
socioeconomic status. Automatic evaluation metrics such as BERTScore (they do
not evaluate COMET though!) seem to be no exception, as a [soon-to-be EMNLP
paper](https://arxiv.org/abs/2210.07626) from Fudan University shows. In their
further experiments, they try to base the metrics on the debiased model (with
debiasing adapters) and they got better results on the attributes they were
evaluating. A sidenote: Always when I think about biases, there must be dozens
of attributes we discriminate against and have no idea… those are of course
missing in any study.

Researchers from RTWH Aachen [ask the
question](https://arxiv.org/pdf/2210.11807) if a separate encoder and decoder
are really needed in machine translation. They try replacing encoder-decoder
models with decoder-only models, and there was virtually no difference in the
translation quality. So, there is probably not much benefit from the encoder
being bidirectional. Although, this is a nice theoretical finding, in practice,
models with a deep encoder and a shallow (even simple RNN) decoder seem to be
the most efficient ones from a computational perspective. This is something
that a decoder-only model can hardly reach.

An [EMNLP paper](https://arxiv.org/abs/2210.13134) by folks from Wuhan,
Bucharest, and Copenhagen tries using machine translation for zero-shot
cross-lingual transfer in language-and-visions tasks. Their conclusion is that
including machine translation both in the pre-training and in the finetuning
stage helps (but the effect does not seem to be complementary). This is an
interesting finding: in all language-vision tasks, there is an inherent danger
that the machine-translated sentences do not entirely match the images, but
here, they seem to be very useful. It probably means that we are not yet at the
point where the exact cross-modal correspondence would be important and our
odels still have some more fundamental problems.

A [paper accepted to EMNLP](https://arxiv.org/pdf/2210.12360) from Salesforce
AI Research compares prompt-tuning and standard fine-tuning in zero-shot
cross-lingual transfer. Prompt tuning means learning special token embeddings
that get prepended to model the model input and train the model for a task.
This makes very much sense: task-specific finetuning of a multilingual model is
always a trade-off between forgetting other languages and learning the task in
the training language. When only the continuous prompt is learned and the rest
of the network remains frozen, the danger of unlearning other languages is much
smaller.
