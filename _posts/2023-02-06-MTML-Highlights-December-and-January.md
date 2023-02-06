---
layout: post
title: "Highlights from Machine Translation and Multilinguality in December 2022 and January 2023"
tags: [mtml-highlights, en]
lang: en
---

Here is what I found interesting on arXiv in December 2022 and January 2023. At
the beginning of January, there a relatively few new pre-prints in general.
But now it is catching momentum again, with more papers appearing every
day.

### [BLOOM+1: Adding Language Support to BLOOM for Zero-Shot Prompting](http://arxiv.org/abs/2212.09535)

In this paper, folks from the Big Science Workshop elaborate on how to add
language support to the already trained BLOOM model. They tried two approaches:
[MAD-X](https://aclanthology.org/2020.emnlp-main.617) (clever stuff with
adapters, which adds parameters) and [IA^3](https://arxiv.org/abs/2205.05638)
(some clever finetuning, which does not add parameters). They did nothing with
tokenization (a slight disappointment for me) and just said BLOOM uses
byte-based BPE, so there are never out-of-vocabulary tokens. Technically, this
is true, but new alphabets split down to bytes, so the tokens are hardly
commensurable across languages.

Their main finding is that 100M tokens are needed to add language to the model.
They say they matched the performance of mGPT (which has 60 languages) but did
not match mT0, which already contained all the languages from the very
beginning.

### [Cross-Lingual Retrieval Augmented Prompt for Low-Resource Languages](http://arxiv.org/abs/2212.09651)

This preprint from LMU Munich introduces an alternative to standard zero-shot
cross-lingual model transfer from high-resource to low-resource languages. For
a test example in a low-resource language, they retrieve a few similar training
instances in the high-resource language, turn this into a prompt, and continue
in the low-resource language. This trick works better than finetuning the model
using the retrieved examples and, of course, better than not finetuning at all.
I missed a comparison with finetuning the model with all available data, which
is the most standard way of doing the zero-shot model transfer. On the other
hand, the results show that the finetuning performance no longer increases with
the number of retrieved examples, so it may not help much. Also, everything is
done with mBERT and XLM-R, so no huge pre-trained languages model are necessary
to make this work.

### [Cross-lingual Similarity of Multilingual Representations Revisited](http://arxiv.org/abs/2212.01924)

Folks from Tartu notice that measuring cross-lingual similarity with CCA and
similar methods is not suitable when interested in cross-lingual performance.
Those methods determine if there is a projection between the representations so
that they are correlated. However, during zero-shot transfer, there is no
additional projection in a shared representation space, and the spaces must be
correlated already as they are. Therefore, they suggest measuring the average
correlation of neuron values as they are.

### [Optimal Transport for Unsupervised Hallucination Detection in Neural Machine Translation](http://arxiv.org/abs/2212.09631)

The preprint studies hallucination in neural machine translation, a weird model
behavior when it generates a coherent sentence with nothing in common with the
source sentence. It starts with an observation that cross-attention looks
strange for hallucinated sentences. The authors suggest an unsupervised method
based on measuring the Wasserstein distance between the actual attention matrix
and what they assume it should look like.

The method works pretty well. I was also surprised by how the other techniques
work: [COMET-QE](https://aclanthology.org/2021.wmt-1.111), a state-of-the-art
learned quality estimation metric is much worse than this unsupervised method,
however, comparing [LaBSE
embeddings](https://aclanthology.org/2022.acl-long.62), initially meant for
parallel sentence mining.

### [Prompting Large Language Model for Machine Translation: A Case Study](https://arxiv.org/abs/2301.07069)

Folks from the University of Edinburgh explored the machine translation
capabilities of large language models. They use
[GLM-130B](https://arxiv.org/abs/2210.02414), a large bilingual language model
from Tsinghua University.

With quantization and some other tricks, the model can be run on reasonable
GPUs: on 4 24GB-memory (or 8 11GB-memory) GPUs. Not surprisingly, they show
that prompting is better than zero-shot translation. The prompt matters,
pseudo-parallel data for prompting works well.

It is good to know that you do not need PaLM to do this sort of experiment and
that such experiments are doable on relatively reasonable hardware.

### [XLM-V: Overcoming the Vocabulary Bottleneck in Multilingual Masked Language Models](https://arxiv.org/abs/2301.10472v1)

XLM-V is a new multilingual representation model by Meta, a sort of new
generation of the frequently used
[XLM-R](https://aclanthology.org/2020.acl-main.747) model. The only difference
from XLM-R is that it uses a 4-times larger vocabulary; they even use the very
same dataset. The main contribution is in a more clever design of the
tokenizer, so it does not overrepresent large languages because just scaling
the vocabulary to 1M would not help.

They start with training a SentnecePiece (Unigram LM) subwords for each
language, and then they cluster languages according to vocabulary overlap.
Then, they train a new SentnecePiece model for each cluster, so there is a
vocabulary overlap due to language relatedness rather than random
co-occurrence. Finally, they merge everything into a single vocabulary.

The resulting model is better than XLM-R in basically everything (including a
1M-vocabulary version XLM-R).
