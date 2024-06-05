---
layout: post
title: "Highlights from Machine Translation and Multilinguality in May 2024"
tags: [mtml-highlights, en]
lang: en
---

Here are short summaries of three pre-prints that I enjoyed reading in May.

### [Zero-Shot Tokenizer Transfer](https://arxiv.org/abs/2405.07883v1)
Folks from the University of Cambridge and the Univerisity of Edinburgh propose a nice trick for changing the vocabulary of an already trained language model. They train a hyper-network (a neural network that predicts parameters of a different neural network) that predicts what embeddings a token would have if it were trained with the rest of the model. For each training batch, they build an ad-hoc vocabulary using a simplified and randomized version of the SentencePiece Unigram tokenizer (they just count the substring frequencies and add some random noise). They run the hypernetwork to generate the embeddings for this new tokenizer and compute the language modeling cross-entropy as if they were training the language model. However, instead of updating the model weights, they update the hyper-network to produce embeddings that lead to better cross-entropy. This way, they get a network ready for basically any reasonable tokenizer. The paper claims to make a contribution to efficiency by allowing shorter segmentations. However, for me, the main thing is that it opens up a possibility to experiment with different tokenizers without the need for expensive retraining of large language models.

### [TransMI: A Framework to Create Strong Baselines from Multilingual Pretrained Language Models for Transliterated Data](https://arxiv.org/abs/2405.09913v1)

A preprint from LMU Munich experiments with transliteration into the Latin script in multilingual encoder models. Instead of using large vocabulary that sometimes needs to accommodate pretty inefficient UTF-8 codepoints, they transliterate all languages into Latin script and finetune the encoders. The experiment with XLM-R, Glot500, and FURINA (a post-aligned version of GLOT500). They retrain the vocabulary on the transliterated data and experiment with merging the vocabularies. They made reasonable improvements across the tasks (including NER, POS tagging, topic classification, and sentence retrieval).

### [The Echoes of Multilinguality: Tracing Cultural Value Shifts during LM Finetuning](https://arxiv.org/abs/2405.12744v1)

A preprint from the University of Amsterdam and the University of Hamburg studies how finetuning on different data in various languages influences the answers to the value question of multilingual encoder-decoder models. They build up on [previous work](https://aclanthology.org/2023.c3nlp-1.12) that turned a part of the [World Value Survey](https://www.worldvaluessurvey.org/wvs.jsp) into cloze-style questions that get easily scored by a language model. First, they measure how often the models agree with the survey (the average agreement is slightly over 80%). Then, they finetune the model on data they assume carries some value, like Partisan News or the Bible in different languages. Overall, the effect was quite small, but there are some trends. News has almost no effect; the Bible and the Tanzil Corpus (that contains Wikipedia, the Bible, and the Quran) have a slightly bigger effect (the strongest effect is in Vietnamese). The paper looks very much like a work in progress, but these results are already pretty interesting. One thing I miss is that they do not measure the direction in which the results were shifted, especially if they shift towards the finetuning language.
