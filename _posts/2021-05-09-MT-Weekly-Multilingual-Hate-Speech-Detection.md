---
layout: post
title: "Machine Translation Weekly 78: Multilingual Hate Speech Detection"
tags: [mt-weekly, en]
lang: en
paperTitle: "Cross-lingual hate speech detection based on multilingual domain-specific word embeddings"
paperAuthors: "Aymé Arango, Jorge Pérez, Barbara Poblete"
issue: 78
---

This week I will comment on a preprint [Cross-lingual hate speech detection
based on multilingual domain-specific word
embeddings](https://arxiv.org/pdf/2104.14728.pdf) by authors from the
University of Chile.

The pre-print evaluates the possibility of cross-lingual transfer of models for
hate speech detection, i.e., training a model in one language and testing it in
a different language. Hate speech detection is a particularly tough task for
model transfer because many of the words have a different meaning or at least
different connotations when used in hate speech than in their more standard
use. An example from the paper says that the Italian word "migranti" is usually
translated into English as migrants, but in the hate speech context, it
typically means illegal immigrants – which are in the context of American hate
speech usually called "illegals" and not "migrants".

The cross-lingual representations for zero-shot cross-lingual transfer of hate
speech models should be thus very contextualized because they need to identify
the very special context-dependent meaning. In this case, we want the
embeddings to be not only aware of the syntactic and semantic context, but also
to do some sort of pragmatic inference. In other words, cross-lingual transfer,
in this case, would require to represent the pragmatics regardless of the
culture-specific practices. The authors of the paper are primarily interested
in detecting hate speech, but for me, their experiments are a test of the
cultural neutrality of multilingual contextual representations.

The paper test several input representations as an input to a classifier:

1. Multilingual BERT;

2. Standard aligned static word embeddings; and

3. Word embeddings aligned specifically for the purpose of hate speech.

The later alignment uses a resource called
[Hurtlex](https://github.com/valeriobasile/hurtlex), a lexicon of offensive,
aggressive, and hateful words in over 50 languages with quite a rich annotation
including mutual translation of the items. What an incredible resource!

When trained and tested in the same languages, multilingual BERT is clearly the
best choice. The models benefit from the rich contextualization of the
representation compared to the static embeddings. This is however not true for
the cross-lingual transfer. The cross-lingual transfer is dominated by the word
embeddings that were aligned using the Hurtlex lexicon. This result shows that
multilingual BERT failed to recognize the pragmatics in a language- or
culture-neutral way. The domain contextualization of word embeddings
outperforms sentence contextualization of multilingual BERT despite the clear
disadvantages of static word embeddings. The task that requires even more
contextualization than usual NLP tasks has better results with static
embeddings.

The results (although if I were the reviewer of the paper, I would harshly some
methodological issues) raise many questions. Can we make the multilingual
contextual embeddings culturally neutral? Would training the representations on
less scholarly-looking texts make the models more aware of the pragmatics? Is
there a more direct way of measuring cultural neutrality, so we can optimize
for it during training?
