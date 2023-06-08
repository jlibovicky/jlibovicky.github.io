---
layout: post
title: "Highlights from Machine Translation and Multilinguality in May 2023"
tags: [mtml-highlights, en]
lang: en
---

Here are a few papers I found most interesting in the flood of new pre-prints
on arXiv. There was ACL's camera-ready deadline and the start of the EMNLP
anonymity period, so there were many more papers than usual.

### [What is the best recipe for character-level encoder-only modeling?](https://arxiv.org/abs/2305.05461v1)

A paper from DeepMind accepted to ACL 2023 systematically (and empirically)
studies how to train a BERT-like model that works directly with character-level
inputs using existing architectural building blocks. Transformers work well
with word-like units, so the main trick with character-level models is that the
long character-level input needs to be downsampled first to get latent
word-like units. In the end, the hidden states need to be upsampled again to
produce characters. According to this paper, the best option is combining two
existing architectures: CANINE and Charformer. But the main message from the
paper is that it does not work well without using proper tokenization for
masked language modeling during training. It remains a mystery to me why such
powerful models as Transformers cannot learn such a simple task as tokenization
end-to-end with the rest. (I also discuss character-level modeling in [a post
about our paper](/2023/01/19/Why-Dont-People-Use-Character-level-MT.html) from
last year's [Findings of ACL](https://aclanthology.org/2022.findings-acl.194).)

### [Taxi1500: A Multilingual Dataset for Text Classification in 1500 Languages](https://arxiv.org/abs/2305.08487)

Folks from LMU Munich did interesting stuff with the multi-parallel Bible
corpus. They built a highly multilingual classification benchmark called
Texi1500. The task is Bible verse classification in 1500 languages into (IMO
rather funny) classes: Recommendation, Faith, Description, Sin, Grace, and
Violence. They compare mBERT, XLM-R, XLM-L, and
[Glot500](https://arxiv.org/abs/2305.12182) (XLM-R finetuned to cover more
languages), for head languages (= high resource); everything except mBERT is
comparable in zero-shot transfer and in-language training setup. Glot500 is
better for tail (= low-resource) languages covered by the model but similar to
other models (which means quite bad) for the languages not covered by any
models.

### [Subword Segmental Machine Translation: Unifying Segmentation and Target Sentence Generation](https://arxiv.org/abs/2305.07005)

A pre-print from the University of Cape Town presents a novel way of jointly
learning machine translation and target language segmentation. It is based on
[Dynamic Programming Encoding](https://arxiv.org/abs/2005.06606) (DPE, see also
[MT Weekly 43](/2020/06/12/MT-Weekly-Dynamic-Programming-Encoding.html)). In
DPE, the decoder has character-level input and subword output. Similarly to
CTC, at training time, it sums all possible target sequence segmentation using
a dynamic programming algorithm. At inference time, it can select the most
probable segmentation. In the original paper, they got good segmentations, but
the translation results were not that great.

This paper introduces an extension of this. They generate the target sentence
character by character (using a small LSTM decoder) and dynamically resegment
(and thus re-rank) the generated output. They test their approach on a few
morphologically complex languages from the Flores 101 test set. The results are
rather mixed (which is a pity because the algorithm is really cool).

### [PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v1)

Google released PaLM 2, including a technical report. At first glance, it seems
to have the best multilingual properties from the current large language
models. The reason might be that they also used parallel data for training.

### [Revisiting Machine Translation for Cross-lingual Classification](https://arxiv.org/abs/2305.14240)

Folks from Meta released a pre-print where they revisit often-repeated claims
about the cross-lingual model transfer, namely that zero-shot cross-lingual
transfer is better than machine-translating the model input at inference time.
The paper argues that the translate-test baseline (i.e., we train the model in
English and machine-translation everything into English at inference time) is
much stronger than previously thought. The reason is surprisingly simple: Weak
machine translation systems were used in the papers that originally made such
claims. When using the Meta's NLLB (No Language Left Behind) MT system, the
results are better than zero-shot transfer and the translate-train setup.

### [mmT5: Modular Multilingual Pre-Training Solves Source Language Hallucinations](https://arxiv.org/abs/2305.14224)

A pre-print from Deepmind presents the mmT5 model, a modification of the mT5
model that uses language-specific adapters. Principally, it is similar to
[X-MOD](https://aclanthology.org/2022.naacl-main.255), a multilingual encoder,
which is basically XLM-R with language-specific adapters, but instead of doing
this in the encoder-only setup, mmT5 is an encoder-decoder model.

The new model is better than mT5 in most evaluation tasks. The main strength
seems to be reducing the number of answers in incorrect language. I found
cross-lingual summarization particularly interesting, perhaps because I did not
read much about the task before.
