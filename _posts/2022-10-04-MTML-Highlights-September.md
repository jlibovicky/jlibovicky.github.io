---
layout: post
title: "Highlights from Machine Translation and Multilinguality in September 2022"
tags: [mtml-highlights, en]
lang: en
---

Here are my monthly highlights from paper machine translation and
multilinguality.

A [preprint](https://arxiv.org/abs/2209.04138) from the Nara Institute of
Science and Technology shows that target-language-specific fully connected
layers in the Transformer decoder improve multilingual and zero-shot MT
compared to the current practice of using a special token to indicate what the
target language is. A very similar idea is also in a [preprint from Tianjin
University](https://arxiv.org/abs/2209.01530), but in this case, they add
language-specific parameters for the other part of the Transformer decoder –
the self-attention sublayers. Of course, the improvement is reached at the
expense of a higher number of parameters and as it very often happens, the
pre-prints do not include baselines with the same numbers of parameters as
their improved models. It makes it hard to assess, what the contribution of the
methods really is, but in this case, I tend to believe, it is probably better.

A [preprint from the Tokyo Institute of
Technology](https://arxiv.org/abs/2209.04126) extends the possibility of
subword regularization to yet another segmentation algorithm, WordPiece (it is
not used much nowadays, but .e.g, the original BERT uses it). The idea is the
same as for [BPE Dropout](https://aclanthology.org/2020.acl-main.170/) (see
also [MT Weekly 18](/2019/11/07/MT-Weekly-BPE-dropout.html): stochastically
decide to forbid some subwords and thus produce more, smaller units. With MT,
it works comparably well to BPE Dropout. The paper also shows experiments with
finetuning BERT and using the dropout is better than using the tokenizer as is.
(I fine-tuned RoBERTa and especially XLM-RoBERTa many times and it never
occurred to me that I should use the subword regularization from SentencePiece,
I definitely should consider it the next time.)

Folks from the University of Pennsylvania and Microsoft did a follow-up of the
SiXT model. https://arxiv.org/abs/2209.02821 The original [SiXT
model](https://aclanthology.org/2021.emnlp-main.2) (see also [MT Weekly
91](/2021/10/25/MT-Weekly-Zero-Shot-MT-with-Pretrained-Representations.html))
is a many-to-English translator using XLM-R as a universal encoder. Here, they
use the zero-shot translation capabilities of the model, use additional
monolingual data, and create an English-to-many translator. They test it on 25
relatively high-resource train languages and 8 low-resource test languages and
quite good results.

Folks from Darmstadt, Sheffield, and Bielefeld (which [does not
exist](https://en.wikipedia.org/wiki/Bielefeld_conspiracy), if you did not
know) [elaborated on BERTScore](https://arxiv.org/abs/2209.02317).
[BERTScore](https://arxiv.org/abs/1904.09675) (see also [MT Weekly
2](/2019/05/01/MT-Weekly-BERTScore.html) is a text generation and machine
translation evaluation metric based on comparing BERT embeddings and computing
something as F-Score from it. This pre-print shows that it works much better
when it uses [byT5](https://aclanthology.org/2022.tacl-1.17) as the underlying
model instead of BERT (so it is byte-level instead of token-level), also
earlier layers work better than later ones. Unfortunately, the paper does not
directly compare with COMET, which is currently considered to be the best MT
evaluation metric. (Hey, and what about byT5-based COMET!)

Speaking about evaluation metrics, there was also a [pre-print from
Amazon](https://arxiv.org/abs/2209.02317) that presented a very simple
("embarrassingly easy" as they say in the paper title) way of adding document
context to existing neural-network-based MT evaluation metric. Long story
short: just add as much context as the underlying pre-trained models can handle
and it will work fine.

Google created (and hopefully will also release) a [test set for multilingual
visual question answering in 13 languages](https://arxiv.org/abs/2209.05401)
and presented a model with decent results using an mT5-based model. For those,
that think just applying mT5 is too easy, folks from the Univerity of Zurich
have a [bunch of tricks](https://arxiv.org/abs/2209.02982) based on a very
nuanced understanding and intuitions of how the language-and-vision encoders
work, most of them too complex for me to give them time to really understand
them.
