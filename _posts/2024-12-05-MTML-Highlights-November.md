---
layout: post
title: "Highlights from Machine Translation and Multilinguality in November 2024"
tags: [mtml-highlights, en]
lang: en
---

### [Mitigating Metric Bias in Minimum Bayes Risk Decoding](https://arxiv.org/abs/2411.03524v1)

Minimum Bayes Risk Decoding tries to get the most typical output from a language or machine translation model rather than the most probable one. The main idea is that the probability scores do not consider how semantically similar sentences are. Therefore, the most probable sequence might not be the most typical from a meaning perspective. The weak point is that we have to decide what metric to use to estimate the similarity, which typically leads to overfitting towards the metric of choice. Those metrics are typically COMET, BLEURT, or MetriX (which are slow to compute) for machine translation. This paper from Google shows that if they use an ensemble of metrics (so, we make the slow decoding even slower), this problem of overfitting can be largely fixed.

### [Tomato, Tomahto, Tomate: Measuring the Role of Shared Semantics among Subwords in Multilingual Language Models](https://arxiv.org/abs/2411.04530v1)

Folks from the University of Waterloo and Google DeepMind play around with shrinking the vocabulary of massively multilingual pre-trained encoders. They cluster embeddings of pre-trained multilingual encoders (mBERT, XLM-R, XLM-V) using k-means to see what happens. They get only a slight decrease in performance when the vocabulary size is significantly decreased. It indirectly shows the importance of having alignable vocabulary items across languages: this would work better for better-aligned tokens.

### [Watching the Watchers: Exposing Gender Disparities in Machine Translation Quality Estimation](https://arxiv.org/abs/2410.10995v2)

Folks from Lisbon looked at gender bias in MT quality estimation. Most SoTA QA metrics tend to prefer stereotypical sentences.

### [Why do language models perform worse for morphologically complex languages?](https://arxiv.org/pdf/2411.14198v1)

A preprint from the University of California San Diego assesses the reason why morphologically rich languages seem to perform worse in large language models, which means that they measure the properties of the tokenization and evaluate its effect on the perplexity of the languages covered by the models. They consider morphological plausibility, compression ratio, and training data size. The results show that the most predictive factor is the training data size, but only if they compensate for what they call byte-premium: a number saying by what factor a text in the language is longer in number of bytes.
For the morphological plausibility, they introduce MorphScore, something like recall of morpheme boundaries: A word scores 1 if all morpheme boundaries are in the tokenization. This is opposite to what we measured in [our paper on lexically grounded tokenization](https://aclanthology.org/2024.emnlp-main.421): We measured precision at a given vocabulary size, where we argue that we do not know if frequent morphemes are joint, but when the tokenizer decides to split the tokens, it should be correctly. Character tokenization would be a total winner of this MorphScore.

### [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://arxiv.org/pdf/2411.19799v1)

Cohere and people from a few Swiss institutions prepared a dataset for regional QA dataset with 197k multiple-choice questions in 44 languages. The dataset is based on some standardized school tests, so the distribution of topics is slightly different for each country, ranging from really regional topics to general science stuff. For better consistency, it was filtered and post-edited by native speakers. They evaluated many (both open-source and closed models). All models suck except for GPT-4o (which is not great either). As expected, there was worse performance for less-resourced languages.