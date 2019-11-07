---
layout: post
title: "Machine Translation Weekly 18: BPE Dropout"
tags: [mt-weekly, en]
lang: en
---

Everyone who followed natural language processing on Twitter last week must
have noticed a paper called [BPE-Dropout: Simple and effective Subword
Regularizations](https://arxiv.org/pdf/1910.13267.pdf) that introduces a simple
way of adding stochastic noise into text segmentation to increase model
robustness. It sounds complicated, but it is fairly easy.

As we already discussed [here, two weeks
ago](/post/2019/10/23/MT-Weekly-Character-Word-Level-MT), neural machine
translation systems can only work with limited vocabulary which can have at
most tens of thousands of entries. The standard way of dealing with this
problem is using a vocabulary consisting of so-called sub-word units rather
than words. Before training a system, we say in advance that we want a
vocabulary of for instance 30,000 units and use a statistical heuristic that
produces a vocabulary of the desired size.

The most commonly used algorithm is called
[byte-pair-encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding) (BPE;
invented in 1994 originally for data compressing, [discovered for machine
translation in 2016](https://www.aclweb.org/anthology/P16-1162)) that
iteratively creates new symbols by merging the most frequent pairs of existing
symbols until it reaches the desired number of symbols. In practice, it means
that we start with isolated characters and gradually add the most frequent
groups of characters into our vocabulary. BPE vocabulary of 30,000 symbols
contains the most frequent words intact. Less frequent words get split into
smaller units that at least partially reflect the language morphology. The
least frequent words got split into characters.

A drawback of the approach is that the model learns how smaller units compose
into words only using the relatively infrequent words and thus does not have
much material to learn from. This observation motivates the main idea of the
paper: if we from time to time forget that we can merge some groups of
characters, the model will have a better chance to learn something about
morphology and also something about transliteration. This is often the case
with proper names that they are not really translated, but they are differently
inflected in different languages. It thus makes perfect sense to learn the
declination patterns on frequent words (which the model memorizes anyway) and
at the inference time, apply it to the rare words.

The idea is not entirely new. A similar trick is also possible with the
[SentencePiece segmentation](https://www.aclweb.org/anthology/D18-2012/) by
Google from 2018. However, it is a rather complicated thing and to be honest I
never found time to fully understand it.

Anyway, back to the BPE-Dropout. Try it yourself! The demo shows how the text
gets segmented when using up to 32k merges trained WMT14 English-German
parallel data and how the segmentation changes when the dropout is applied.

<iframe src="/assets/bpe_js/index.html" width="100%" height="500">The demo is in an iframe.</iframe>

The results in terms of translation quality are quite good when the BPE-dropout
is applied. It gives around 1 BLEU points improvement for most language pairs.
But most importantly, models trained with BPE-dropout seem to be very robust
towards misspellings. Normally, if you misspell a frequent word, it gets
segmented in a way that was totally alien to the model. With BPE-dropout, it
gets split into something similar to what the model had to deal with many times
during training.

It is very simple to experiment with (the [subword-nmt
package](https://github.com/rsennrich/subword-nmt) included this option
immediately when the paper appeared on arXiv). I tried WMT14 English-to-German
translation with 16k vocabulary and the dropout rate of 0.1 which they used in
the paper and the training did not converge. The reason presumably is that even
with dropout rate 0.1 which seems rather small, the text gets segmented in very
small units. In terms of average segment length vocabulary of 32k merges is
equivalent to a vocabulary of 2k merges, dropout of 0.1 with a vocabulary of
16k merges splits the similarly as a vocabulary of only 1k merges when even
many function words get split. However, it was just my first random experiment,
so don't take it too seriously.
