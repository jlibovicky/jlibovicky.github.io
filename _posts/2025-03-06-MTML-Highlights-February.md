---
layout: post
title: "Highlights from Machine Translation and Multilinguality in February 2025"
tags: [mtml-highlights, en]
lang: en
---

### [WMT24++: Expanding the Language Coverage of WMT24 to 55 Languages & Dialects](https://arxiv.org/abs/2502.12404v1)

Folks from Google and Unbable extended the [WMT24 test sets](https://aclanthology.org/2024.wmt-1.1) from 8 to 55 languages by adding more human references. They evaluated LLMs and commercial MT services on them. The winner is OpenAI's o1, followed by Claude and Gemini. The best open-source model is [Unbabel's Tower](https://huggingface.co/collections/Unbabel/tower-659eaedfe36e6dd29eb1805c), which outperforms all standard commercial translation services (Google Translate, DeepL, and Microsoft Translator).


### [SMOL: Professionally translated parallel data for 115 under-represented languages](https://arxiv.org/abs/2502.12301v1)

Speaking of machine translation datasets, Google opened-sourced a parallel dataset for 115 languages with some non-English-centric pairs. The data was not crawled from the Internet but manually translated. They show that the data are useful by fine-tuning Gemini and improving translation quality. Well, nice, but hardly replicable.


### [Blessing of Multilinguality: A Systematic Analysis of Multilingual In-Context Learning](https://arxiv.org/abs/2502.11364v1)

This preprint from the University of Waterloo (with a cool title!) shows experiments with multilingual in-context learning. They use few-shot examples in multiple languages. The performance also improves in languages that are not in the example set, but few-shot examples in the target languages are typically the best.


### [MVL-SIB: A Massively Multilingual Vision-Language Benchmark for Cross-Modal Topical Matching](https://arxiv.org/abs/2502.12852v1)

Folks from Hamburg and Würzburg made an evaluation benchmark for multilingual VL models: The task is to decide what sentences best match the topics of images in a multiple-choice (A-D) setup. The dataset has 205 languages. It is based on the [SIB-200 dataset](https://github.com/dadelani/sib-200), which uses multi-parallel sentences from the [Flores datasets](https://huggingface.co/datasets/facebook/flores), which are labeled with seven topics (based on the Wikipedia article they come from). For the dataset, the authors manually find 70 images that represent the topics (and have a suitable license) for those topics. The baseline experiments (not surprisingly) show that the smaller the languages, the worse the results. (A malicious comment: I never thought one could get that many quantitative results from just 70 images.)


### [What are Foundation Models Cooking in the Post-Soviet World?](https://arxiv.org/abs/2502.18583v1)

Folks from the Georgia Institute of Technology compiled a Multimodal QA dataset that assesses what LLM thinks about typical food from the states of the former Soviet Union. Results from experiments with LLaMA and Qwen show that, especially in the visual question-answering setup, models tend to favor the two biggest post-soviet Russia and Ukraine over other countries.


### [Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs](https://arxiv.org/abs/2502.14830v1)

A preprint from Karlsruhe looks into how the cross-lingual alignment of LLM hidden states affects LLMs' multilingual performance. It introduces an additional training object for the middle layers of LLMs to enforce higher hidden state similarity for semantically matching subwords (middle layers because they show the best alignment anyway, so they are also the most promising ones). With this additional objective. With this additional training objective.
