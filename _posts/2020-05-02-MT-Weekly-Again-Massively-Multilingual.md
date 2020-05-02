---
layout: post
title: "Machine Translation Weekly 40: Getting Massively Multilingual Again"
tags: [mt-weekly, en]
lang: en
---

More than half a year ago (in [MT Weekly
10](/2019/09/11/MT-Weekly-Massively-Multilingual-NMT.html)), I discussed
massively multilingual models by Google. They managed to train two large
models: one translating from 102 languages into English, the other one from
English into 102 languages. This approach seemed to help a lot for
low-resourced languages that probably can benefit from the presence of related
languages in the training data.

In a new preprint of their ACL 2020 paper, guys from the University of
Edinburgh show several tricks that not only improve the multilingual
translation but also make the models reasonably large. The title of the paper
is [Improving Massively Multilingual Neural Machine Translation and Zero-Shot
Translation](https://arxiv.org/pdf/1903.00089.pdf). What I personally value the
most about the paper are the strong intuitions about what is going on inside
the models.

The tricks are based on introducing language-specific components in the model.
Ultimately, all model parameters can be language-specific, but this would that
model is not really multilingual and cannot benefit from synergies between
related languages. The opposite extreme is what Google did in its original
[multilingual approach](https://arxiv.org/pdf/1903.00089.pdf): brute force with
data and computation power without modifying the Transformer architecture. The
new Edinburgh paper succeeds in setting a middle course between those two
extremes and introduces language-specific layer normalization and encoder state
projection.

Especially the trick with [layer
normalization](https://mlexplained.com/2018/01/13/weight-normalization-and-layer-normalization-explained-normalization-in-deep-learning-part-2/)
is quite a surprise for me. I always viewed layer normalization as a purely
technical trick to force the neuron activation to stay in a reasonable range,
so we can connect layers with residual connections (and thus avoid [the
vanishing gradient
problem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem)). After
normalizing the activations to have a zero mean and unit variance, layer
normalization adds a learned bias vector. Here, this serves as a kind of
language embedding, constantly reminding the following layers, how they should
treat the input. The encoder is followed by a linear projection.

My interpretation is: let the encoder do some language-specific things, but not
too much, just give the layers a small hint, what they should do with the
input. After the encoding finishes, just get rid of the language-specific stuff
and project it to a language-neutral form, just as the decoder likes it.

Unlike Google, these experiments were done on publicly available data. I
believe this is an important signal to researchers that these stunningly
interesting experiments can be done everywhere, not only with Google-scale
equipment. It is tempting to say that what was considered sci-fi a few years
ago, can now run even on your desktop machine.

The multilingual model is better than bilingual models on average, but for the
high-resource languages, the translation quality is much worse than the quality
of the specialized bilingual models. To match the performance of the bilingual
models in the multilingual setup, they need a 4 times bigger model, but still
with approximately half of the parameters of Google's model.
