---
layout: post
title: "Highlights from Machine Translation and Multilinguality in Summer 2024"
tags: [mtml-highlights, en]
lang: en
---

Here are summaries of a few papers that I liked during the (long academic) summer.

### [BertaQA: How Much Do Language Models Know About Local Culture?](https://arxiv.org/pdf/2406.07302)

People from the University of the Basque Country prepared a QA dataset consisting of local knowledge about the Basque Country, hopefully including facts that might now exist on the English-speaking Internet and contrast that with global (but it probably means Western) facts. The questions are in the multiple-choice style. Then, they asked professional translators to translate the questions into English. They experimented with SoTA LLMs at that time (LLaMA2, Gemma, and a few commercial ones) and observed that LLMs are much worse in local knowledge than global knowledge. The most interesting finding is that finetuning the models in Basque improves the local QA performance, even in English, at the cost of decreased global QA performance, which is a nice piece of evidence that cross-lingual actually works with LLMs.

### [Is It Good Data for Multilingual Instruction Tuning or Just Bad Multilingual Evaluation for Large Language Models?](https://arxiv.org/pdf/2406.12822v1)

A paper from Edinburgh, Northeastern University, and Tsinghua University in China, accepted to EMNLP 2024, studies differences between LLM performance with machine-translated data and with authentic data in various languages. It is yet another paper that deepens my scepsis on the scientific credibility of results presented in many LLM papers. The paper experiments with multilingual instruction tuning of LLMs and tests it on various QA benchmarks. Significant differences exist based on whether the dataset is translated or native (keyword translationese) to the extent that it is hardly possible to say what is better.

### [xTower: A Multilingual LLM for Explaining and Correcting Translation Errors](https://arxiv.org/abs/2406.19482)

Portuguese company Unbabel and their university friends from Lisbon and Paris released a language model finetuned for translation-related tasks: a sort of copilot for translation. It complements their previous release, TowerInstruct, which was meant directly for translation.
The model can explain an error provided on the input, either by a human translator or an automatic system (they use a model called xCOMET that emulates human MQM error annotation), and fix the error based on the explanation. The nice thing is that all parts can be either done by the translator (who can mark an error and explain it) or automatically because LMs do not care what was generated and was provided by the user.
Experiments show that even the automatic (and quite computationally expensive) pipeline of MT + xCOMET error annotation + xTower to fix the errors improves the translation quality.

### [How Effective are State Space Models for Machine Translation?](https://arxiv.org/abs/2407.05489v1)

Folks from Munich and Lisbon say, "Yes, they are." The quality looks the same, and they are slightly faster.

### [Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for Low-Resource NLP](https://arxiv.org/abs/2408.04303v1)

A COLM 2024 paper from KU Leuven, Ghent University, and other European institutions looks into transferring language models into languages unseen during training. Their methods start with training a tokenizer for the added languages (otherwise, the added languages will get tokenized into very small units) and continue with clever initialization embeddings corresponding to the newly added tokens. They used word alignment (yes, the good old word alignment from statistical machine translation) on parallel data to find out what words often translate into each other, and they used this information to initialize the embeddings and finetune the model as usual. They evaluate their models using LM perplexity, text summarization, and machine translation for Tatar and Dutch and reach quite a solid improvement compared to not doing the clever initialization.