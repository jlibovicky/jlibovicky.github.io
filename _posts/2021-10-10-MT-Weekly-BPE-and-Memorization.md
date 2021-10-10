---
layout: post
title: "Machine Translation Weekly 89: BPE and Memorization"
tags: [mt-weekly, en]
lang: en
paperTitle: "How BPE affects memorization in Transformers"
paperAuthors: "Eugene Kharitonov, Marco Baroni, Dieuwke Hupkes"
issue: 89
---

Similar to last week, I will discuss a paper about input segmentation. The
paper is not directly about machine translation or multilinguality but brings
interesting insights for Transformer models in general. The title of the paper
is [How BPE affects memorization in
Transformers](https://arxiv.org/abs/2110.02782), it has authors from Facebook
AI and the preprint appeared on Thursday on arXiv.

The paper presents a series of experiments with Transformer models for natural
language inferences and different sizes of BPE-based vocabulary by which they
want to measure to what extent the models memorize the training data (while
ignoring generalization). They came up with three measures for memorization:

1. Being able to memorize data with random labels;

2. Comparing the confidence of the model on training and validation data;

3. Ability to reconstruct the training data.

An obvious question: how can a classifier reconstruct the training data? The
answer is: the classifier can be in fact a language model that predicts the
classification label as the last token after the sentence. Besides this special
setup, they also tried a standard classifier on top of a Transformer encoder
and training with the masked language modeling objective.

All the experiments show that the larger the vocabulary, the more the models
tend to memorize. This sounds like a trivial claim: more parameters mean more
memorization. The authors however hypothesize that this is due to the sequences
being shorter. To support the claim, they conduct further experiments to
disprove that the reason is the number of parameters in the embedding layer or
that the is due to compressing the input information (having in mind that BPE
was originally a compression algorithm).

Their conclusion that it is the sequence length that matters makes intuitive
sense. The Transformer architecture internally compares all input token pairs
many times and the number of token combinations grows quadratically with the
sequence length. When we imagine the classification as searching for particular
relation in the input, it totally makes sense that the fewer possible relations
we have, the easier it is to find something.

I guess this can lead to interesting applications. If we can say in advance or
somehow learn what is worth memorizing (e.g., idioms) and what not (proper
names), it might be possible to design segmentations with desirable properties
leading to better generalization. Or maybe the best thing might be learning the
segmentation jointly with the models, which is obviously a hard task (otherwise
someone would have already done that).
