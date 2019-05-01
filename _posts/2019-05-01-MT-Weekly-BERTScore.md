---
layout: post
title: "Machine Translation Weekly 2: BERTScore"
tags: [MT Weekly]
lang: en
---

Last week, there was [a paper on arXiv](https://arxiv.org/pdf/1904.09675.pdf)
that uses BERT sentence representation for machine translation evaluation. The
metric seems to be the new state of the are in MT evaluation. Its name is
BERTScore and was done at Cornell University.

MT evaluation is itself a difficult task. Because we are not (and probably
never will be) able to explicitly algorithmically check if two sentences carry
the same meaning in all relevant aspects. We know (or at least assume) that
people can do it even though they don't know how they do it. So, we ground the
metrics that we use for MT evaluation in human judgment by measuring the
correlation of the metrics with human judgment.

[BERT](https://arxiv.org/pdf/1810.04805.pdf) is a neural-network-based sentence
representation published by Google in October 2018 including the pre-trained
models that are [freely available](https://github.com/google-research/bert)
since November. Since then, it is one of the most discussed topics in natural
language processing.

The model itself is based on the [Transformer
architecture](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf),
originally introduced for machine translation. The model is trained to guess
what words were randomly masked out on the input and to decide whether two
sentences follow each other in a sentence. This relatively simply supervision
causes that the model develops so informative representation of the sentences,
that models based on BERT set the new state of the art in many NLP tasks
including sentiment analysis, paraphrase detection or finding an answer for a
question in a coherent text.

And surprise… MT evaluation is another task where BERT rules. According to
the results in the paper, BERTScore is the best MT evaluation metric we
currently have. The scoring algorithm is relatively straightforward and
proceeds as follows:

1. Get the BERT representation for the translation hypothesis and the reference
sentence.

2. Compute a matrix of cosine similarities of all words from the hypothesis and
from the reference sentence.

3. For each word from the hypothesis find the most similar word from the
reference and compute the average of the maxima over the hypothesis words. This
number tells us: how much on average each word was matched with a word in the
reference. In the paper, they call this precision (which is kind of a
terminological cheat because the averaged number are neither relative
frequencies nor probabilities).

4. Do the same with swapped hypotheses and reference and compute recall (with
the same terminological cheat).

5. Compute the F1 score: the harmonic average of precision and recall.

And that's it, the algorithm is as simple as this. The authors do some
additional tricks with idf score, but it does not seem to influence the score
much.

The results are the most interesting in case evaluation of single sentences.
The correlation with human judgment is around 0.5 with most of currently used
metrics and goes over 0.7 with BERTScore.

The margin is narrow in case of corpus level metrics. Most of the existing
metrics manifest correlation with human judgment between 0.9 and 0.95 which are
already

Recently, many of the new evaluation metrics that achieved a high correlation
with humans were based on supervised learning. This makes them dependent on how
the machine translation outputs look like these days and pose a risk that they
won't work well with newer MT systems. BERTScore is similarly as the good old
BLUE score independent on how the system outputs currently look like which
makes it more robust in the future.
