---
layout: post
title: "Machine Translation Weekly 53: Code Swithing Pre-training for NMT"
tags: [mt-weekly, en]
lang: en
---

After a short break, MT weekly is again here, and today I will talk about a
paper ["CSP: Code-Switching Pre-training for Neural Machine
Translation"](https://arxiv.org/pdf/2009.08088.pdf) that will appear at [this
year's virtual EMNLP](https://2020.emnlp.org). The paper proposes a new and
surprisingly elegant way of monolingual pre-training for both supervised and
unsupervised neural machine translation.

The idea is quite simple. The model they use is the standard Transformer; all
the magic is how the model is trained. First, it is pre-trained on synthetic
"half-translations" created from monolingual data. It is then trained either on
parallel data in a supervised way or by iterative back-translation on
monolingual data in the unsupervised setup. What I just called the
"half-translations" are sentences where some of the words were replaced by
their dictionary translations. They call the preparation of the synthetic data
self-confidently code switching (therefore the paper title), but in real code
switching, the foreign words would be used more cleverly. The good thing is
that the bilingual dictionary can be generated from bilingual word embeddings
that can be trained without bilingual supervision.

In the unsupervised setup, the pipeline is the following:

* Train word embeddings for both the source and the target language.

* Do an unsupervised mapping of the embeddings, and create a probabilistic
  dictionary of between the languages. For those who are not familiar with
  this: unsupervised bilingual embeddings assume that similar things are said
  similarly often across languages, so the word embedding spaces should also be
  similar. We only need to find how to rotate and scale the vector spaces so
  they match each other.

* Use this dictionary to generate synthetic half-translated data: randomly
  replace a half of the words with their translation counterparts from the
  estimated dictionary.

* Train a Transformer that translates from the synthetic half-translated data
  into the original sentences. This can be viewed as a sort of bilingual
  denoising. After this step, there is already a first-iteration translator
  that already can somehow translate between the languages.

* Start iterative back-translation: Use the current translator to translate the
  monolingual data into the target language. In the next iteration, they will
  be used as training data in the opposite direction.

This procedure gets the state-of-the-art results in unsupervised machine
translation. It is, in fact, quite similar to the previous best approach called
[MASS (Masked Sequence to Sequence Pre-training for Language
Generation)](https://arxiv.org/abs/1905.02450). MASS did the monolingual
pre-training as a pure denoising autoencoder with some tokens from the input
sentence replaces by `[MASK]` tokens. In MASS, the decoder learns well the
target language.  Simultaneously, the encoder is forced to represent both
languages similarly because the encoder state poses an information bottleneck
of the architecture. The bilingual supervision comes later only in the
iterative back-translation phase. CSP is better (at least in my opinion)
because the bilingual supervision comes from the bilingual embeddings and the
model gets the supervision already during the pre-training state.

Similarly to MASS, CSP can also bring some supervised translation improvements,
especially when only little training data is available. But I think the
unsupervised use case is much more important in this paper.
