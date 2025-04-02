---
layout: post
title: "Highlights from Machine Translation and Multilinguality in March 2025"
tags: [mtml-highlights, en]
lang: en
---

### [EuroBERT: Scaling Multilingual Encoders for European Languages](https://arxiv.org/abs/2503.05500v1)

A large group of authors, mostly from CentraleSupélec in Paris and Instituto Técnico in Lisbon, released [EuroBERT](https://huggingface.co/EuroBERT), a multilingual BERT model for European and major global languages. There is also a 2.1 B version, unusually large for encoder models.

### [High-Dimensional Interlingual Representations of Large Language Models](https://arxiv.org/abs/2503.11280v1)

A print from the Hong Kong University of Science and Technology evaluates the sentence-level similarity of LLM hidden states across languages. It shows that the idea that langauge models trained multilingually represent everything in a shared semantic space (perhaps structured by English) is not the whole truth. In the paper, they devise several metrics for comparing the spaces and show that the representations are split into fragmented subspaces. This is, for me, the most important finding of the paper. However, it goes further: Based on the observations, they derived a training scheme with selective freezing so that they don't break the alignment of hidden layers and perform better than when they do not.

### [SuperBPE: Space Travel for Language Models](https://arxiv.org/abs/2503.13423v1)

Folks from the University of Washington, NVIDIA, and AI2 experiment with BPE tokenization that crosses word boundaries. It is not only subword tokenization but also super-word tokenization in some sense. Doing byte-pair encoding regardless of the word boundary from scratch is inefficient, so they start with BPEs trained within word boundaries. At some point, they begin considering merges that cross word boundaries. It is (1) more computationally efficient, (2) leads to better compression ratios, and (3) works better for language modeling. They evaluate their models by training English LMs at 8B from scratch, following the OLMo setup (a set of experiments that are hardly doable for me), and reaching significant gains on MLLU.

### [MMTEB: Massive Multilingual Text Embedding Benchmark](https://arxiv.org/abs/2502.13595)

MMTEB is a new multilingual benchmark for text embeddings covering several tasks and 250 languages, reflecting the newly gained importance of text embeddings for RAG methods. By the way, the current best multilingual text embedding in the benchmark is [multilingual-e5-large-instruct](https://huggingface.co/intfloat/multilingual-e5-large-instruct), with "only" 560 million parameters.

### [Negation: A Pink Elephant in the Large Language Models' Room?]( https://arxiv.org/pdf/2503.22395v1)

Negation has caused problems since I started doing NLP. This pre-print from Brno shows that even with current LLMs, negation can confuse the models when doing a simple task of natural langauge inference. They try English, Czech, German, and Ukrainian; as expected, it gets worse in non-English languages. Also, bigger models are better.
