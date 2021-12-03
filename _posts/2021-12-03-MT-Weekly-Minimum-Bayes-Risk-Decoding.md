---
layout: post
title: "Machine Translation Weekly 95: Minimum Bayes Risk Decoding – the Cooler the Metric, the Cooler it gets"
tags: [mt-weekly, en]
lang: en
issue: 94
---

This week I am returning to a topic that I follow with fascination (cf. MT
Weekly [#20](/2019/11/21/MT-Weekly-Search-and-Model-Errors.html),
[#61](/2020/12/05/MT-Weekly-Decoding-and-Diversity.html),
[#63](/2020/12/20/MT-Weekly-MAP-vs-Minimum-Bayes.html), and
[#66](/2021/01/24/MT-Weekly-Empty-Outputs.html)) without actually doing any
research myself – decoding in machine learning models. The preprint I will
discuss today comes from Google Research and has the title [Minimum Bayes Risk
Decoding with Neural Metrics of Translation
Quality](https://arxiv.org/pdf/2111.09388.pdf). It shows that Minimum Bayes
Risk (MBR) decoding can outperform beam search when done properly and that
there might be some serious problems in how encoder-decoder-based MT is
formalized.

In neural machine translation, we think (and tell students and tell each other)
that we model the probability of the target sentence given the source sentence
factorized over target words. With such a model, it makes total sense to
formulate the translation process as searching for a target sentence that is
maximally probable given the source sentence. The exact search is not
tractable, so we approximate it using beam search, which works pretty well.
But... things are not that easy. It actually appears that doing the [exact
search is worse than the beam search](https://aclanthology.org/D19-1331) and
there is no widely accepted explanation why beam search works that well.

[Minimum Bayes Risk (MBR)
decoding](https://aclanthology.org/2020.coling-main.398) seems to offer a
solution to the problem. The most probable sentence could be a random artifact
of the model. On the other hand, a well-behaved model should have some other
properties too: It should assign a similar probability to similar sentences
(whatever similar means). Moreover, if we sample multiple sentences from the
model, we will very likely sample many sentences which are similar to the
sentences with high probability. Based on these two assumptions, we can end
with the idea of sampling many possible translations and choosing the one that
is most similar to all others – and this is it, this is Minimum Bayes Risk
decoding.

So far so good. The really interesting question is choosing the similarity
function, which is called the utility function in the papers. Obviously, the
similarity should reflect the meaning similarity more than the orthographic
similarity. The original paper opted for the METEOR score and got decent
results in terms of BLEU.

In our [recent preprint](https://arxiv.org/abs/2110.08191), we noticed that MBR
that uses chrF as a utility function scores well with respect to chrF and BLEU,
but is not that great when measured by COMET (a state-of-the-art
machine-learned MT quality metric). The same observation also appears in the
preprint from Google Research, but they take this observation much further.
They experiment with MBR with recent high-quality metrics and discover the
following pattern: Using a metric as a utility function always leads to scoring
well in the metric that was used as the utility. But in the end, they also get
much higher translation quality than using beam search.

The paper uses human evaluation to make the ultimate decision about the
translation quality and shows that using [BLEURT
v0.2](https://arxiv.org/abs/2004.04696) as the utility function leads to the
best results. (I wonder why they use BLEURT and not COMET. Is it because BLEURT
is from Google and COMET not?) Surprisingly, the sentence BLEU is not a bad
choice either, although much worse than BLEURT.

The main and the most distressing result of the paper is that what was
considered the best translation in human evaluation is actually the worse both
with respect to BLEU score (with two different sets of reference sentences!)
and also has the highest perplexity given the model. Standard beam search on
the other hand searches for low-perplexity target sentences. This strongly
suggests that there is a conceptual error in how the target sentence
probability is formulated.

Another takeaway from the paper could be that it might be worth doing this
rather time-consuming decoding when generating data for knowledge distillation
and distilling student models that can greedily generate sentences that are
similar to the MBR outputs. It works with beam search, it might work here as
well.
