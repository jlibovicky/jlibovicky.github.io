---
layout: post
title: "Machine Translation Weekly 76: Zero-shot MT with pre-trained encoder"
tags: [mt-weekly, en]
lang: en
paperTitle: "Zero-shot Cross-lingual Transfer of Neural Machine Translation with Multilingual Pretrained Encoders"
paperAuthors: "Guanhua Chen, Shuming Ma, Yun Chen, Li Dong, Dongdong Zhang, Jia Pan, Wenping Wang, Furu Wei"
issue: 76
---

Using pre-trained multilingual representation as a universal encoder for
machine translation might seem like an obvious thing to try: train a decoder
into one target language using one or several source languages and you get a
translation from 100 languages into the target language. This sounds great, but
this is not how it works. (Or it works somehow, but not really well, I tried it
myself.) Recently, I came across a pre-print where the authors figured out how
to do it. The title of the pre-print is ["Zero-shot Cross-lingual Transfer of
Neural Machine Translation with Multilingual Pretrained
Encoders"](https://arxiv.org/abs/2104.08757) and has authors mostly from the
University of Hong Kong and Microsoft Research.

The trick how to do it is a clever training schedule (figuring it that out
probable requires a very strong intuition on how the training dynamics of such
models). They train the models in two stages:

1. Train the decoder only that uses the embeddings from the encoder which are
   kept frozen.

2. In the second stage, train everything except for the encoder embeddings,
   which are kept frozen. Besides, drop some residual connections in the
   encoder.

The entire second stage sounds counterintuitive to me. However, an ablation on
the Europarl data (a rather small dataset) shows that it improves the
translation by 2.5 BLEU points on average. One thing that surprised me was that
they do not keep the embeddings in the encoder and the decoder tied. They use
XLM-R that uses a 250k dictionary this is a huge number of parameters.

There is also very interesting reasoning behind dropping the residual
connections. The residual connections enforce the locality of the information.
No matter how self-attention shuffles the output it gets always summed up with
the input, so from one half the positions never change. In a language-agnostic
encoder, we might want to give the encoder more freedom in reordering, so the
decoder can what it needs always in the same order.

The results seem pretty good. On the large-scale WMT datasets, it seems that
the zero-shot generalization works really well only within the language
families. The method has the biggest potential for low-resource languages.
Unfortunately, most of the languages they use are high-resource, but in the
case of Indo-Aryan languages, we can see that a model trained on Hindi
generalizes very well for Nepali and Gujarati which are low-resource. The
results also confirm what is well-known about the multilingual representations
that they very strongly encode language identity and language similarities
(e.g., as we showed last year) and are not language-neutral beyond groups of
similar languages.
