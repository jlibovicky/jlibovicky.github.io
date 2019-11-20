---
layout: post
title: "Machine Translation Weekly 20: Search and Model Errors in Neural Machine translation"
tags: [mt-weekly, en]
lang: en
---

This week, I will have a look at a paper from this year's EMNLP that got a lot
of attention on Twitter this week. The title of the paper is [On NMT Search
Errors and Model Errors: Cat Got Your
Tongue?](https://www.aclweb.org/anthology/D19-1331.pdf) and comes from the
University of Cambridge.

Even though the authors do not put it this way, the paper critically revisits
how neural machine translation is mathematically formulated and shows that the
current formulation leads to absurd consequences.

The decoder in NMT models is a conditional language model: it estimates a
probability distribution of a target sentence word given the source sentence
and the previous words in the target sentence. Formally for target sentence
__y__ and source sentence __x__:

$$ P(y_n | y_0, \ldots y_{n-1}, \mathbf{x}). $$

When we decode left-to-right, we always want to have a good estimate of what
word can follow. So far, it looks fine. The problem is that we are not
interested in the score of a single word, we would ideally like to score the
whole sentences (e.g., to score them in a beam search). For that, we can easily
use the chain rule:

$$ P(\mathbf{y} | \mathbf{x}) = P(y_0, \ldots, y_n | \mathbf{x}) = P(y_0 | \mathbf{x}) \cdot P(y_1 | y_0, \mathbf{x}) \cdot \ldots \cdot P(y_n | y_{n-1}, \ldots, y_0, \mathbf{x}) $$

This equation is from a high school probability class, it must work, one would
say. The equation starts to get tricky, once we consider target sentences of
different lengths. As they notice in the paper, the number of possible
sentences of length 20 is bigger than the number of atoms in the known
universe. Searching the entire hypothesis space is impossible and in practice,
we use approximations like greedy search or beam search.

The paper presents a feasible algorithm for doing the exact inference, i.e.,
finding the best scoring sequence given the equation above (without checking
all atoms in the known universe). They used a simple observation to make the
search feasible. In the log domain, probabilities are negative numbers and
Multiplying probabilities then means adding negative numbers. When you expand a
hypothesis during the search, its score only decreases, so you can always
discard partial hypotheses that have a lower score than the best-scoring
completed hypothesis and thus efficiently prune the search. Unfortunately, they
did not report how long this inference took, but apparently it was a reasonable
finite time, otherwise they would not be able to report it in the paper.

Their surprising conclusion is that often, the globally best-scoring hypothesis
is an empty string and the optimal translation given the trained model gets
around 2 BLEU points (compared to 30 BLUE points of the beam search). Both
greedy and beam search do most of the search decisions "incorrectly", meaning
that a different symbol selected than one that would otherwise maximize the
sentence probability given the model, and yet they lead to a good translation.

Do you remember the paper on the [Generalized Framework for
Decoding](https://arxiv.org/abs/1905.12790) that I [discussed here in
July](/2019/07/04/MT-Weekly-Generalized-Framework-for-Decoding.html)? They
wanted to have one single equation covering all ways of decoding: left-right,
non-autoregressive, insertion-based… The equation contains a special term for
length probability.

![Generation equation: length](/assets/MT-Weekly-8/equation_products.svg)

In the "optimal" decoding, we assume target sentence lengths are equally
possible. It is hardly a realistic assumption and it suffers from the fact that
the number of possible hypotheses grows exponentially with the hypothesis
length. So, even though they are equally probable, this uniform probability
gets distributed into more and more hypotheses with the growing length, which
poses a great advantage for the short hypotheses—even the empty ones.

This is, of course, a well-known problem that we need to address even when
doing the standard beam search. The heuristic that we use is called length
normalization and is basically the geometric average of the probabilities (with
slight modifications now and then). This works well in practice, but in the
language of the general decoding equation, it means that the length probability
grows exponentially with the length. This is even less realistic than a uniform
distribution over all possible lengths, but at least it works.  However, in the
paper, when they did the exact inference under the length normalization
condition, they still got a  result that was 10 BLEU points worse than the beam
search.

My takeaway from the paper is that modeling sentences using a chain rule
probably just wrong. But we are extremely lucky that

1. The wrong equation leads to reasonably good loss function that allows the
   model to train;

2. The decoding heuristics (that do suboptimal decisions all the time)
   compensate for the flaws of the chain rule formulation so that no one really
   noticed it might be wrong.

For me, the message of the paper is clear: We need a better equation to model
machine translation!
