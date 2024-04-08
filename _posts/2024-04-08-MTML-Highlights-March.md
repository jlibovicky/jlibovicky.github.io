---
layout: post
title: "Highlights from Machine Translation and Multilinguality in March 2024"
tags: [mtml-highlights, en]
lang: en
---

### [Did Translation Models Get More Robust Without Anyone Even Noticing?](https://arxiv.org/abs/2403.03923v1)

Folks from Libsbon study how robust the newest MT systems are against source-side noise. Machine translation using large models, including translation-specific NLLB or via LLMs (such as Tower or GPT-3.5), is much more robust both towards synthetic noise (the nice feature of synthetic noise is that you can check the translation quality for different noise levels) and also real-world noisy data from social networks.

### [Tracing the Roots of Facts in Multilingual Language Models: Independent, Shared, and Transferred Knowledge](https://arxiv.org/abs/2403.05189v1)

In a recent EACL paper, folks from the University of Tokyo analyze the consistency of factual knowledge in mBERT and XLM-R. They used the [mLAMA dataset](https://aclanthology.org/2021.eacl-main.284/) ( machine-translate LAMA dataset, which is basically a knowledge graph formulated as simple sentences). The performance correlates with the in-language training data size (which itself suggests that the facts might not always diffuse from language to language). mBERT is not the best model out there, but its nice property is that it was only trained on Wikipedia, so it is possible to identify where the knowledge triplets in LAMA come from. The talks about three patterns of what happens with facts in the training data: some facts are language-specific (the fact is one language, and the model knows in the same language only), some are cross-lingual shared, and some are transferred across languages (the fact is one language only).

### [Can Machine Translation Bridge Multilingual Pretraining and Cross-lingual Transfer Learning?](https://arxiv.org/abs/2403.16777v1)

A negative result LREC paper from the University of Helsinki shows that continued pretraining of mBART and mBERT on machine translation does not improve multilingual performance. Also, contrary to what everyone (at least the paper authors and me) would expect, it does not make the representations more aligned.

### [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://arxiv.org/abs/2403.10258)

A study from several institutions in Singapore attempts to evaluate the multilingual abilities of LLMs while comparing ChatGPT, LLaMA 2, and Mistral. For the established more linguistic NLP tasks such as natural langauge inference or paraphrase detection, the best strategy was to translate the input into English and do the task in English. For prompts from ShareGPT (a web page where users can upload their experience with ChatGPT), the situation was slightly different, and it appears that for prompts that require cultural knowledge, it is better to prompt the model in the language.
