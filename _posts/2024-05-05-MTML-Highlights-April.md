---
layout: post
title: "Highlights from Machine Translation and Multilinguality in April 2024"
tags: [mtml-highlights, en]
lang: en
---

### [Meta4XNLI: A Crosslingual Parallel Corpus for Metaphor Detection and Interpretation](https://arxiv.org/abs/2404.07053v1)

Folks from the University of the Basque Country prepared an English-Spanish dataset for natural langauge inference (i.e., deciding if sentences follow from each other, are in contradiction, or have nothing to do with each other) with metaphorical expressions. Unlike the standard version of this task (XNLI), which does not use figurative language, there is a large gap between in-language training and language transfer. (Transfer means that we finetune a multilingual model in one language, but then we apply the model in another language). Also, there is a gap between metaphorical and non-metaphorical sentences. I would not necessarily expect this because a pre-trained LM is trained on real-world texts full of metaphors; some are frozen, and some are made up ad-hoc, so LMs need to learn to deal with them. Unlike formal systems, nothing tells an LM to interpret texts like logical formulas, but those results suggest sometimes they might.

### [Does Mapo Tofu Contain Coffee? Probing LLMs for Food-related Cultural Knowledge](https://arxiv.org/abs/2404.06833v1)

People from Universities in Denmark, Israel, and China collected a dataset called FmLAMA about what local food consists of (in Italy, USA, Turkey, Japan, France, UK, Mexico, India, Germany, China, Iran, Greece, Spain, and Russia). They build prompts in different languages and measure if LMs get it right. The main observation is that the models are biased toward the US culture when prompted in English. This is, however, not the case in other languages. Explicit cultural clues (like saying food is from Japan) surprisingly help the model recall that they know the facts.

### [Language Imbalance Can Boost Cross-lingual Generalisation](https://arxiv.org/abs/2404.07982)

A preprint from ETH Zurich and Bar-Ilan University challenges the assumptions that balanced data across languages (and ideally parallel data, too) are needed for a good cross-lingual language model. On the contrary, having one dominant language as an anchor in the model is better than having more balanced data. In the paper, they train several GPT-2-style models. They start with an artificial setup where the other language is an exact clone of the first one, but they use different token IDs. They primarily measure the model's perplexity. The results are evident in the artificial data setup: imbalanced data (90:10 ratio) leads to the best results. The same trend exists with a natural pair of languages but is not that prominent. Another sort of surprising result was that they got better perplexity with disjoined vocabularies rather than sharing the vocabulary the usual way (they call it anchored).

### [Generalization Measures for Zero-Shot Cross-Lingual Transfer](https://arxiv.org/abs/2404.15928v1)

A preprint from NYU comes up with quality metrics of zero-shot cross-lingual transfer without actually doing the cross-lingual transfer. Unlike many existing work that tries to interpret cross-lingual transfer via langauge similarity or vocabulary overlap, this paper only views it from the machine-learning perspective. The classification margin in English (the good old margin you know from SVMs) is a good predictor of the transfer performance. The second measure they use is the sharpness of the loss function. The idea is that if the optimum lies in a flat area, it is more likely to be good in other languages. This seems difficult to compute and does not correlate as well as the margin does.
