---
layout: post
title: "Highlights from Machine Translation and Multilinguality in December 2023 and January 2024"
tags: [mtml-highlights, en]
lang: en
---

Many things happened in the field in December: EMNLP, Google released Gemini,
and Mixtral appeared. January was seemingly not that packed with new events,
but plenty of new interesting work popped up on arXiv.

### [Predicting Human Translation Difficulty with Neural Machine Translation](https://arxiv.org/abs/2312.11852)

Folks from the University of Melbourne found out that features from NMT, most
notably the target sentence perplexity and something they call flow features,
are a good predictor of human translation time.

### [Turning English-centric LLMs Into Polyglots: How Much Multilinguality Is Needed?](https://arxiv.org/abs/2312.12683v1)

A preprint from Zurich and Edinburgh experiments with instruction tuning of
English LLM in multiple languages and found it helps the cross-lingual
performance of LMs a lot. They use (authentic, i.e., not machine-translated)
data from the [OpenAssistant
dataset](https://huggingface.co/datasets/OpenAssistant/oasst1) and try
finetuning on an increasing number of languages, which on average (but not
always) improves performance in various cross-lingual setups of question
answering (clearly better), commonsense reasoning, and XNLI (almost no
difference). They also evaluate the chat performance, but they use ChatGPT as a
judge, i.e., they ask it to assess the conversation on the Likert scale.  They
experimented with [LLaMA 2](https://llama.meta.com) 7B and LLaMA 2 70B, and not
surprisingly, bigger is better.

### [Multilingual Instruction Tuning With Just a Pinch of Multilinguality](https://arxiv.org/abs/2401.01854v1)

There was also a preprint on a very similar topic by Google. They do
instruction finetuning of [PaLM 2](https://ai.google/discover/palm2) in
multiple languages. They use more data than the previous papers, including the
OpenAssistant dataset, but augment their data using machine translation. It
seems they have plenty of multilingual data, but they show that as few as 40
non-English examples are enough for solid multilingual performance. However,
this result might be specific for PaLM 2, which was trained with an emphasis on
multilinguality (the training data mix also included parallel data). It is
probably not transferable to LLaMA 2. Again, they use another LLM as a judge of
the conversation capabilities, which I still think is weird.

### [Word Boundary Information Isn't Useful for Encoder Language Models](https://arxiv.org/abs/2401.07923v1)

A preprint from the University of Sheffield and the University of Bath
empirically studies if we need markers for white spaces in subword tokenizers.
Tokenizer use special symbols to indicate either that there should be a
whitespace (SentencePiece uses special UTF-8 underscores as prefixes) or that
it should not be a whitespace (BPE traditionally used @@). In practice, it
often means that many tokens are twice in the vocabulary: with and without the
markup. They finetuned BERT to only use the no-markup tokens and observed
virtually no change in the GLUE and NER performance while saving a large part
of the vocabulary. It would be keen to see results with multilingual models
because it could save even a larger part of the embedding matrix, which is
typically by far the biggest parameter of the model.

### [MaLA-500: Massive Language Adaptation of Large Language Models](https://arxiv.org/abs/2401.13303v1)

Folks from LMU Munich, Helsinki University and Instituto Superior Tecnico in
Lisbon finetune LLaMA 2 7B for 500 langauges.  They extended the vocabulary to
250k using a similar strategy as they did with
[Glot-500](https://aclanthology.org/2023.acl-long.61): They trained unigram LM
(a.k.a. SentencePiece) vocabularies independently and interpolated them.  Then,
they used LoRA to finetune 500 languages. They evaluate the
[SIB-200](https://arxiv.org/abs/2309.07445) (topic classification in 200
languages) and NLU datasets in 200 languages. The preprint has a nice graphic
with 3-shot in-context learning. LLaMA 2-7B is, to my surprise, not that bad;
XGLM is the second best, and MALA is the best.

### [LangBridge: Multilingual Reasoning Without Multilingual Supervision](https://arxiv.org/abs/2401.10695)

Folks from KAIST, the University of Washington, and NAVER AI Lab experiment
with something that I would call hidden state transplantation. They take the
mT5 encoder and train it to have the same hidden states as
[Orca](https://arxiv.org/abs/2311.11045) (which is LLaMA 2 finetuned for some
reasoning tasks). At inference time, they take those transformed hidden states
and let the Orca continue. They evaluate using chain-of-thought reasoning using
some math tasks and get something that looks like good results (but I am not
familar with the datasets at all).
