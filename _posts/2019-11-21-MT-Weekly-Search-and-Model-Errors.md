---
layout: post
title: "Machine Translation Weekly 20: Search and Model Errors in Neural Machine translation"
tags: [mt-weekly, en]
lang: en
---

This week, I will have a look at a paper from this year's EMNLP that got a lot
of attention on Twitter this week. If there was an award for the most
disturbing machine translation paper, this would be a good candidate. The title
of the paper is [On NMT Search Errors and Model Errors: Cat Got Your
Tongue?](https://www.aclweb.org/anthology/D19-1331.pdf) and comes from the
University of Cambridge.

Even though the authors do not put it this way, the paper critically revisits
how neural machine translation is mathematically formulated and shows that the
current formulation leads to absurd consequences.

The current mathematical formulation of NMT models can be summarized like this:
Let's factorize the sentence probability by tokens using the chain rule. This
allows us to formulate the loss as a sum of negative log-likelihoods and we end
up with a model that can estimate conditional probabilities of individual
words. This is nice, but what we really want is to get an entire sequence of
words that maximizes the probability estimate given the equation. This is not
computationally tractable, so we have to approximate the inference using the
beam search algorithm.

In more detail, the decoder in NMT models is a conditional language model: it
estimates a probability distribution of a target sentence word given the source
sentence and the previous words in the target sentence. Formally for target
sentence $\mathbf{y}$ and source sentence $\mathbf{x}$:

$$ P(y_n | y_0, \ldots y_{n-1}, \mathbf{x}). $$

When we factorize the equation word by words using the chain rule, we get:

$$ P(\mathbf{y} | \mathbf{x}) = P(y_0, \ldots, y_n | \mathbf{x}) = P(y_0 | \mathbf{x}) \cdot P(y_1 | y_0, \mathbf{x}) \cdot \ldots \cdot P(y_n | y_{n-1}, \ldots, y_0, \mathbf{x}) $$

This equation is just an application of rules from a high school probability
class. It must work, one would say. The problem now is how to get a good
sentence out of this model. As they notice in the paper, the number of possible
sentences of length 20 is bigger than the number of atoms in the known universe
and until this paper was published we believed the exact inference is not
tractable. Therefore, we use approximations like greedy search or beam search.

The paper presents a feasible algorithm for doing the exact inference, i.e.,
finding the best scoring sequence given the equation above (without checking
all atoms in the known universe). In the log domain, probabilities are negative
numbers, multiplying probabilities then means adding negative numbers. When you
expand a hypothesis during the search, its score only decreases, so you can
always discard partial hypotheses that have a lower score than the best-scoring
completed hypothesis and efficiently prune the search. Unfortunately, they did
not report how long this inference took, but apparently it was a reasonable
finite time, otherwise, they would not be able to report it in the paper.

Their surprising conclusion is that often, the globally best-scoring hypothesis
is an empty string and the optimal translation given the trained model gets
around 2 BLEU points (compared to 30 BLUE points of the beam search). Both
greedy and beam search do most of the search decisions “incorrectly”, meaning
that they select a different symbol than would otherwise maximize the sentence
probability given the model. Still, the translation is good. But why? The exact
search works much worse than what was believed to be its poor approximation.
And this is weird.

Do you remember the paper on the [Generalized Framework for
Decoding](https://arxiv.org/abs/1905.12790) that I [discussed here in
July](/2019/07/04/MT-Weekly-Generalized-Framework-for-Decoding.html)? They
wanted to have one single equation covering all ways of decoding:
left-to-right, non-autoregressive, insertion-based… The equation contains a
special term for length probability.

![Generalized framework: length](/assets/MT-Weekly-8/equation_length.svg)

In the “optimal” decoding, we assume target sentence lengths are equally
probable. It is hardly a realistic assumption, especially given that the number
of possible hypotheses grows exponentially with the hypothesis length. So, even
though they are equally probable, this uniform probability gets distributed
into more and more hypotheses with the growing length, which poses a great
advantage for the short hypotheses—even the empty ones.

This is, of course, a well-known problem that we need to address even when
doing the standard beam search. The heuristic that we use is called _length
normalization_ and is basically computing the geometric average of the
probabilities (with slight modifications now and then) instead of multiplying
the probabilities. This works well in practice, but the problem is that the
scores are no longer probabilities, i.e., they are not what the model was
trained for. In the paper, they also did the exact inference under the length
normalization condition, and they still got a result that was 10 BLEU points
worse than the beam search.

My takeaway from the paper is that modeling sentences using a chain rule
probably just wrong. But we are extremely lucky that:

1. The wrong equation leads to reasonably good loss function that allows the
   model to train;

2. The decoding heuristics (that do suboptimal decisions all the time)
   compensate for the flaws of the chain rule formulation so that no one really
   noticed it might be wrong.

For me, the message of the paper is clear: The probabilistic assumptions of NMT
models are wrong and we have no idea why the models work so well. It is kind of
disturbing, isn't it?

__BibTeX Reference__
```bibtex
@inproceedings{stahlberg-byrne-2019-nmt,
    title = "On {NMT} Search Errors and Model Errors: Cat Got Your Tongue?",
    author = "Stahlberg, Felix  and
      Byrne, Bill",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1331",
    doi = "10.18653/v1/D19-1331",
    pages = "3354--3360",
}
```
