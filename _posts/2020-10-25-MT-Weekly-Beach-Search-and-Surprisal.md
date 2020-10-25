---
layout: post
title: "Machine Translation Weekly 56: Beam Search and Models' Surprisal"
tags: [mt-weekly, en]
lang: en
---

Last year an EMNLP paper ["On NMT Search Errors and Model Errors: Cat Got Your
Tongue?"](https://www.aclweb.org/anthology/D19-1331)  ([that I discussed in MT
Weekly 20](/2019/11/21/MT-Weekly-Search-and-Model-Errors.html)) showed a
mindblowing property of neural machine translation models that the most
probable target sentence is not necessarily the best target sentence.

In NMT, we model the target sentence probably that is factorized using the
chain rule into conditional token probabilities. We can imagine the target
sentence generation like this: The model estimates the probability of the first
word given the source sentence. From this distribution, we pick one word. The
model then estimates the probability of the second word given the first word
and the source sentence. We select the second word from this distribution, and
so on...

Previously, we thought that exact inference under this factorization is
intractable, but we can approximate the inference using the beam search
algorithm. The exact inference would mean that we would keep all possibilities
in each step instead of picking one word (that I suggested in the previous
paragraph). The problem is that the number of possible target sequences grows
exponentially with the length and the number of possible 20-word target
sequences is comparable to the number of atoms in the known universe.
Therefore, in practice, we use an algorithm called beam search. In this
algorithm, we only keep a small number of "surviving" hypotheses after every
time step.

The last year's paper presented a clever way of doing the exact inference (that
is still too slow for any practical use, but fast enough for experimenting) and
found out that often, the most probable target sentence is an empty string. In
other words, the beam search does not approximate the exact search. In fact,
search errors are necessary to find a good translation using a well-trained
model. An additional trick that we use in the beam search is we add length
normalization, i.e., boost the probability of longer sequences, so
high-probability too short sentences fell out of the beam during decoding. This
heuristics (that does not have a theoretical justification) helps also with the
exact inference, but beam search still gets better translation quality.

A paper that will be published at his year's EMNLP ([If Beam Search is the
Answer, What was the Question?](https://arxiv.org/abs/2010.02650)) suggests an
alternative decoding objective that says that the target sentence should be
both highly probable and at the same minimally surprising in terms of
information theory.

The paper provides three types of arguments that should support this objective:

* mathematical,

* cognitive motivation, and

* experimental.

To be honest, I do not entirely buy any of these arguments, but together, they
suggest that this might be a way to go.

The _mathematical_ argument is that optimizing the surprisal of the target
sentence given the model is equivalent to doing beam search. They show formal
proof of this; however, there are, in fact, infinitely many alternative
formulations (e.g., not using the surprisal, but directly the probabilities)
that would have the same theoretical property.

The second argument is that it corresponds to the [uniform information density
theory](http://www.coli.uni-saarland.de/~vera/InfoTheoryLecture4.pdf). It is a
psycholinguistic theory that says that people prefer such sentences where the
information is uniformly distributed. Minimizing the surprisal during decoding
ensures this uniform information density with respect to the translation model.
The entropies with respect to standard language models are known to highly
correlate with human surprisal. However, machine translation models are
conditional language models, and as far as I know, there is no study that would
say MT models have the same properties as language models in this matter.

Finally, they do experiments with the modified decoding objective: they combine
the probability assigned by the model with regularization terms that ensure the
uniform distribution of information. The translation quality is basically the
same as when using the length normalization. However, in their experiments, the
translation quality of the length-normalized beam search decreases with the
increasing beam size, which according to my experience means that they did not
properly tune the weight of the length normalization and the length
normalization might be in fact better than the proposed regularization.

When I read the paper about the search errors last year, I was not thinking
that the training objective is fine; we only want something else than the most
probable target sequence. I always thought that the ultimate solution is
finding a different formalization of the target sentence probability, so this
paper showed this problem from a perspective that was quite new to me.
