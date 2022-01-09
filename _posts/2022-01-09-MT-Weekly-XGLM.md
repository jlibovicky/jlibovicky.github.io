---
layout: post
title: "Machine Translation Weekly 98: XGLM: GPT-3 for 30 languages"
tags: [mt-weekly, en]
lang: en
issue: 98
---

By the end of the year, Meta AI (previously Facebook AI) published a pre-print
introducing a multilingual version of GPT-3 called XGLM. As its title –
[Few-shot Learning with Multilingual Language
Models](https://arxiv.org/abs/2112.10668) – suggests, it explores the few-shot
learning capabilities. The main takeaways are:

* _Good news_: It is indeed possible to train such a model and it works somehow.

* _Bad news 1_: Cross-lingual transfer of few-shot learned tasks is not as good
  as I would expect.

* _Bad news 2_: Huge models are needed for reasonable performance.

* _Ambiguous news_: In the few-shot setup, it is better to machine-translate
  everything into English and proceed in English.

The model is in principle simple: It is an autoregressive language model (i.e.,
predicts what the next token in a sequence given the history) trained on a
corpus of 500B tokens in 30 languages. It uses a SentencePiece-based vocabulary
of 250k tokens.

The few-shot learning capabilities are similar to GPT-3. For paraphrase
detection, it matches the supervised zero-shot transfer. In XNLI (cross-lingual
natural language inference), the accuracy is half of the supervised case.
Supervised means training using English and using in other languages (often
denoted zero-shot transfer). Fully zero-shot means using only hand-designed
prompts. In-language few-shot learning means using hand-designed prompts and a
few examples in the same language as is used for testing. For those, who like
me did not know how the prompts look like, an example for natural language
inference is:

```[sentence1], right? [Yes/No/Also], [sentence2].```

`Yes` means implication, `No` means contradiction, `Also` is neutral. The text
with the highest probability is considered to be the correct answer. This
miriad of different setups implies that designing a fair comparison of the
accuracy would be rather hard. Anyway, the paper only wants to show if it works
at all, it is not that important what the exact accuracy is (the paper actually
avoids any comparison with supervised learning, so they do not run into these
issues).

Although the few-short learning works in all languages, translating into
English and doing zero-shot or few-shot learning in English is much better than
anything else, even for Haitian Creol, an extremely low-resource language where
the machine translation is probably of quite low quality.

The most interesting experiments are those with cross-lingual few-shot
learning, i.e., the model is primed with examples in one language, but the
final classification example is in a different language. The success of
zero-shot and in-language few-shot learn can mean that models learn to
represent all languages almost independently. A truly language-neutral model
should be able to work with prompts with any language. Priming the model with
examples in other languages is slightly better than the zero-shot setup in most
languages, but only if we transfer from English and partially also from
Russian.

This result makes me wonder if it is the case that very high resource languages
(English and Russian) form a sort of backbone of the model with other languages
being sort of dependent on how the high-resource ones are represented – English
being the controller language, others being peripheral. Unfortunately, I have
no idea how I would test such a hypothesis more empirically.

And by the way, the performance on few-shot MT is impressive.
