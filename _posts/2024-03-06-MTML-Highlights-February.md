---
layout: post
title: "Highlights from Machine Translation and Multilinguality in February 2024"
tags: [mtml-highlights, en]
lang: en
---

With a new month, here are a few papers that I noticed on arXiv in February.

### [Linear-time Minimum Bayes Risk Decoding with Reference Aggregation](https://arxiv.org/abs/2402.04251v1)

A preprint from the University of Zurich proposes a linear time version of
Minimum Bayes Risk (MBR) decoding in machine translation. This decoding
algorithm does not aim to generate the most probable sequence given the model
but the most typical one. This is typically done by sampling dozens of
candidate output sentences, from which we select the one that is most similar
to other sentences. This requires quadratically many comparisons. Moreover, the
best results are achieved with trained similarity metrics (such as COMET),
which are slow to compute. The preprint suggests a linear-time version of the
algorithm: instead of comparing all pairs of output candidates, they create an
average representation and compare everything to the average. With chrF, they
represent the average output with their respective character n-gram states.
With COMET, they take average hypothesis embeddings.

### [What is 'Typological Diversity' in NLP? ](https://arxiv.org/abs/2402.04222v2)

Folks from Alborg Univeristy and KU Leuven study (and mostly criticize) how the
notion of typological diversity is used in papers in the ACL anthology. Many
papers say that they do their evaluation on a set of typologically diverse
languages without saying what it means or without quantifying it. The preprint
shows a nice table that splits multilingual benchmarks by inflection type. It
shows that most multilingual benchmarks contain languages with strong suffixing
and little languages with weak prefixing, for which the models typically work
worse. My main takeaway is that I should occasionally check the GramBank for
linguistic features and not only think about languages in terms of langauge
families, geography, and the available resources.

### [Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models](https://arxiv.org/abs/2402.14714v1)

A preprint from Yanolja, a Korean company, shows a recipe for recycling an LM
to be used in another language; in this case, they finetuned LLaMA 2 for
Korean. They extend the vocabulary so Korean does not get over-segmented and
initialize new embedding by the average of the subwords they would consist of
in the original tokenizer. They train on Korean data in stages, starting with
the new embeddings and gradually unfreezing the rest. They made a big
improvement in Korean without losing their English performance. The vocabulary
LLaMA 2 is heavily skewed towards English, so adding more Korean tokens
probably made a large part of the difference.

### [Tower: An Open Multilingual Large Language Model for Translation-Related Tasks](https://arxiv.org/abs/2402.17733v1)

Folks from several Portuguese institutions tried to turn LLaMA 2 into a
multilingual model for 10 languages. They finetune it with both monolingual and
parallel data. Additionally, they did instruction tuning for NER and various
translation-related tasks, such as post-editing, translation ranking, or
conversation translation. They tested the model for machine translation using
the FLORES-200 dataset and WMT23 tests (measure quality with COMET-22), and
they matched the translation quality of GPT-4, which was the WMT23 winner.
