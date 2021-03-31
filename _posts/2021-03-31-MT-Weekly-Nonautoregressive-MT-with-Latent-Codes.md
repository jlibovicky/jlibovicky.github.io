---
layout: post
title: "Machine Translation Weekly 73: Non-autoregressive MT with Latent Codes"
tags: [mt-weekly, en]
lang: en
paperTitle: "Self-Learning for Zero Shot Neural Machine Translation"
paperAuthors: "Yu Bao, Shujian Huang, Tong Xiao, Dongqi Wang, Xinyu Dai, Jiajun Chen"
issue: 73
---

Today, I will comment on a paper on non-autoregressive machine translation that
shows a neat trick for increasing output fluency. The title of the paper is
[Non-Autoregressive Translation by Learning Target Categorical
Codes](https://arxiv.org/abs/2103.11405), has authors from several Chinese
private and public institutions and will appear at this year's [NAACL
Conference](https://2021.naacl.org).

Unlike standard, so-called autoregressive encoder-decoder architectures that
decode output sequentially (and in theory in linear time), non-autoregressive
models generate all outputs in parallel (and in theory in constant time,
regardless of the input length). This leads to significant speedups, but
typically at the expense of output fluency and overall translation quality. The
output tokens are modeled as conditionally independent, so the tokens on the
right are not aware of what was previously decoded which can lead to
inconsistencies. A typical mistake that I observed is that one half of a
sentence uses one verb tense and another half another one. This is particularly
unpleasant for languages like German that tend to delay some verbs towards the
end of the sentence.

There have been several attempts to fix this: we tried [light-weight
autoregressive decoding](https://arxiv.org/abs/2004.03227), more mainstream way
is the [iterative improvement of the output by masked language
modeling](https://www.aclweb.org/anthology/D19-1633) (see [MT Weekly
3](2019/05/17/MT-Weekly-Constant-Time-MT.html)). Another trick that has been
used is using [Conditional Random Fields
(CRF)](https://en.wikipedia.org/wiki/Conditional_random_field): a sequence
labeling model that takes into account bigram dependencies and unlike direct
labeling does not suffer from the label-bias problem. This is cool, but
modeling the bigram probabilities requires having a matrix with transition
scores for every output token pair, which means a lot of additional parameters.

This paper starts with the CRF idea and tries to get rid of the large
transition matrix by reducing the number of symbols that the CRF models the
dependencies of. This necessarily means that each of the symbols must
correspond to multiple possible output tokens. To make this work, they cluster
the tokens based on their embeddings and group the tokens into classes which we
can imagine as some sort of latent part-of-speech tags. Then they use a CRF to
predict the sequence of the classes, not the output words. This is step is in
fact sequential, but very fast because the number of classes is small compared
to the vocabulary size (in practice, they use 64). The predicted classes
together with the decoder hidden states are then used to generate the target
tokens.

The remaining question is how they get the latent codes, which is in my opinion
the most elegant part of the paper. They just run the [k-means
clustering](https://en.wikipedia.org/wiki/K-means_clustering) over the learned
embeddings.  The cluster centroids get updated with exponentiated moving
average, which provides stability to the training, so the clustering does not
change drastically between training batches. The classes are naturally
represented by the cluster centroids which keeps them in the representation
space used by the model.

The results seem to be pretty good. The paper reports a better tradeoff between
translation quality and speed than previous work. However, the paper does not
yet take into account the [latest results of Gu and
Kong](https://arxiv.org/abs/2012.15833) (see [MT Weekly
64](/2021/01/08/Nonautoregressive-models-strike-back.html)) which is probably
better. On the other hand, the trick presented in this paper is compatible with
it. It is also nice to see that the latent codes tend to be quite homogeneous
with respect to part of speech.

I like the paper because it seems to me as a nice synthesis of the good old
statistical NLP – this method strongly resembles the [class-based language
model with Brown's classes](https://www.aclweb.org/anthology/J92-4003) – and
current neural approaches, even though the authors do not explicitly admit this
connection (maybe there are not even aware of it).
