---
layout: post
title: "Highlights from Machine Translation and Multilinguality 04/2022"
tags: [mtml-highlights, en]
lang: en
---

Another month is over, so here is my overview of what I found most interesting
in machine translation and multilinguality.

### Rotation ciphers as regularizers

A paper [accepted to ACL 2022](https://arxiv.org/abs/2204.00665) from Simon
Fraser University experiments with using rotation ciphers on the source side of
MT as a data augmentation technique. They tested it in low data scenarios and
it seems to work quite well, which actually seems quite strange to me. It's
just systematic replacing characters with different characters – it does not
lead to similar subwords on the source and the target side, it does not make
the tokens better alignable, but it still works.

### Characters vs. subwords: it depends on the task

A [pre-print from Tel Aviv and Bar Ilan
University](https://arxiv.org/abs/2204.04748) they compare character-level and
subword tokenization for BERT-like models for morphologically rich languages.
They find that subwords are better than characters for semantically oriented
tasks (Hebrew, Arabic, Turkish), and for surface level tasks, character-level
segmentation is better.

### Nearest neighbor machine translation becomes reasonable fast

A [paper from Tianjin University and Alibaba DAMO
Academy](https://arxiv.org/abs/2204.06175) that was accepted to ACL 2022
presents a clever way of making nearest neighbor translation faster. Nearest
neighbor MT is a non-parametric extension of an already trained model. Decoder
states and corresponding output tokens from training data are stored in a
database and retrieved at inference time. The database needs to be huge to work
well and with a huge database, retrieval is slow. This paper makes works fast
with dimension reduction and clustering.

### Finetuning multilingual representations on parallel data has non-trivial effects on zero-shot transfer

A [pre-print from several Russian universities and Bosch Center for Artificial
Intelligence](https://arxiv.org/abs/2204.06457) analyzes a common assumption
that multilingual representation can be improved by continued training on
parallel data and that it will presumably also improve zero-shot model
transfer. The pre-print studies transfer to distance languages on three tasks
and observe different results for each of the tasks. Whereas natural language
inference gets improved, the results are mixed for named entity recognition and
there is even some drop for question answering. Almost as if the models lost
some common sense abilities when getting exposed to parallel data.

### Neither language-agnostic nor language-specific

A [paper that will appear at RepL4NLP 2022](https://arxiv.org/abs/2204.09168)
with authors from the University of Washington, Bar Ilan University, and Allen
Institute of AI attempts to find out if pre-trained multilingual models
represent gender (chosen as a random example, it probably holds for other
meaning aspects too) in a language-specific or language-agnostic way. The
surprising result is: it's actually both. Gender classification can be well
transferred across languages, which suggests it must be represented similarly
across languages. On the other hand, the adversarial removal of gender
representation from one language does not prevent getting it right in other
languages.

### A cheap trick for improving beam search

A [preprint](https://arxiv.org/abs/2204.05424) from the University of
Washington, Yale University, and Allen Institute of AI proposes a simple
modification of beam search decoding. The only change in the algorithm is that
they keep a separate list of finished and unfinished hypotheses. The list of
finished hypotheses might be longer than the beam size. The decoding stops when
the number of finished hypotheses (that did not fall out from the beam) reaches
a threshold. It does not help much, but sometimes it does help a bit.
