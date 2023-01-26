---
layout: post
title: "Notes from EMNLP 2022"
tags: [en]
lang: en
---

Last week I was at EMNLP in Abu Dhabi. Besides losing my passport and figuring
out what to do on such an occasion (many thanks to the personnel of the Czech
embassy in Abu Dhabi), I had plenty of interesting conversations and saw many
interesting posters. When I was at my first NLP conference 8 years ago, I was
amazed by the papers presented at the conference and returned with a long list
of ideas of what I should try in my research. The older I get, the less excited
I am about the papers (or was everything already on arXiv?), and the more I
enjoy talking with people at the conference. So, even though nothing was
particularly breathtaking, there were undoubtedly many papers that deserved
attention. Here is my random and incomplete list of what I found noteworthy.

### [WMT Metrics Task](https://www.statmt.org/wmt22/pdf/2022.wmt-1.2.pdf)

The best machine translation evaluation metrics are still the best choice. This
year's winners are Google's MetricX XXL (finetuned mT5, but they did not
publish any details) and a new version of COMET (with better multi-task
learning). The good news is that the metrics are much better on the segment
level. The bad news is that they still have problems with numbers and named
entities (which was the biggest problem of our Czech-Ukrainian MT).
Reference-free metrics are better than the BLEU score.

### [WMT Sign language translation task](https://www.statmt.org/wmt22/pdf/2022.wmt-1.71.pdf)

WMT this year hosted the sign language translation task. It is a great
initiative, but I was quite surprised by how poor the automatic systems are.
The best systems translating from video to written language got around 2 points
out of 100 in human evaluation (compared to 88 points of human baseline), and
0.6 BLEU points in automatic evaluation. (_Edit: Originally, I had these
numbers wrong. Thanks, Leftheris Avramidis for point it out._)

### [Subword-Delimited Downsampling for Better Character-Level Translation](https://arxiv.org/abs/2212.01304)

A paper from the University of Groningen extends [our work on character-level
machine translation](https://aclanthology.org/2022.findings-acl.194). In the
architecture that we proposed, we reused a [2017 idea of processing characters
with a CNN](https://aclanthology.org/Q17-1026) and downsample the state
sequence to latent states that roughly correspond to words. This gets tricky on
the decoder side because the hidden state sequence needs to be upsampled to
characters again. We originally used a fixed downsampling step, but here they
downsample the states by subwords. In this way, they manage to match the
quality of the subword-based models.

### [Chunk-based Nearest Neighbor Machine Translation](https://arxiv.org/abs/2205.12230)

Nearest neighbor machine translation is a non-parametric extension of neural MT
models. Instead of making the usual output projection, it searches a database
of pairs of decoder hidden states and matching output words. Then, it decides
the output word based on the nearest neighbors in the database. It works
particularly well for domain adaptation. However, the nearest neighbor search
is much slower than the usual output projection. This paper has a solution: we
do not have to retrieve single words matching the decoder states, but we can
retrieve longer chunks. It sounds easy; however, it requires clever tricks
to decide what the chunks should be.

### [The (Undesired) Attenuation of Human Biases by Multilinguality](https://preview.aclanthology.org/emnlp-22-ingestion/2022.emnlp-main.133)

Folks from Saarbrücken and Bologna played around with word embedding
association tests and multilingual representation models. They study how
non-moral cultural values are encoded in the embeddings (e.g., if some insect
species are considered disgusting or flower species considered beautiful). They
created a multilingual version of a word assiation that datasets that is unlike
related work not a translation of the US-English one and performed the
experiments on that. The paper concludes that static embeddings exhibit more
cultural biases than contextual ones, and multilingual models also exhibit
fewer biases than monolingual ones. However, in this particular case, we cannot
say if the biases are good or bad; I would even argue that it is a good thing
if models could grasp cultures associated with particular languages.

### [Calibrating Zero-shot Cross-lingual (Un-)structured Predictions](https://preview.aclanthology.org/emnlp-22-ingestion/2022.emnlp-main.170)

A paper from Johns Hopkins University studies model calibration during
cross-lingual transfer. A model is well calibrated when if it predicts
something with _X_% probability, it will be approximately in _X_% cases
correct.  This is, however, not often the case because neural models tend to be
overconfident. During zero-shot language transfer (we train the model in one
language and use it in another one), this gets even worse. The good news is
that calibrating the model in the source language (using temperature scaling or
Gaussian process calibration) helps in the target language too.

### [Don't Stop Fine-Tuning: On Training Regimes for Few-Shot Cross-Lingual Transfer with Multilingual Language Models](https://preview.aclanthology.org/emnlp-22-ingestion/2022.emnlp-main.736)

A paper from Würzburg and Cambridge introduces a recipe for few-shot
cross-lingual transfer. In this specific setup, you have a reasonably large
task-specific dataset for one language but only a very small one (in this case,
100 instances) for a language in which you want to apply the model. The
protocol the paper sees as the most promising one is 1) finetune on source
language only, 2) mix source and target language and keep validating in the
source language. The big advantage of this approach is that we do not need a
validation set in the target language (which would be a weird assumption, if we
had it, we could use it for finetuning).

### [Bloom Library: Multimodal Datasets in 300+ Languages for a Variety of Downstream Tasks](https://arxiv.org/abs/2210.14712)

It has nothing in common with the multilingual Bloom model. This Bloom is a
multilingual dataset with book translation in more than 300 languages, with
various source languages, and with all books translated only to some languages.
The dataset is also accompanied by images. They suggest some tasks like
multilingual visual storytelling or image captioning. When I briefly looked at
the dataset, my impression was that a large part of the stories is actually
religions, which makes the dataset a little domain-specific.

### [Why is Winoground Hard? Investigating Failures in Visuolinguistic Compositionality](https://arxiv.org/abs/2211.00768)

A group from the University of Texas in Austin tries to debunk why current
models tend to fail on the Winoground challenge.
[Winoground](https://arxiv.org/abs/2204.03162) is a challenge set for
language-vision models: for two images and two captions, the model is supposed
to tell which caption belongs to which image. It is tricky because the captions
are composed of the same words in a different order. Thus, the models need not
only to match objects with words but also to understand the structure of both
the sentence and the image. The general opinion is that the models often fail
because they do not capture the structure well. In this paper, they partially
argue against this. They carefully labeled the test dataset and spotted several
problematic phenomena: idioms (non-compositional phrases), unusual (=weird)
texts, unusual (=weird images), visually difficult (even for humans), requiring
complex reasoning.  Using these labels, they show that problem is not that the
models do not understand word order in general; they mostly fail in tricky
situations.
