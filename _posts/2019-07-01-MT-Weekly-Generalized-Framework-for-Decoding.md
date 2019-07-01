---
layout: post
title: "Machine Translation Weekly 8: A Generalized Framework of Sequence Generation"
tags: [mt-weekly, en]
lang: en
---

This week's post contains much more math than other posts. I will talk about a
paper that is based on cool math tricks, so it cannot really be avoided. The
paper is called [A Generalized Framework of Sequence Generation with
Application to Unidirected Sequence
Models](https://arxiv.org/pdf/1905.12790.pdf) from New York University and
appeared on arXiv a month ago.

We speak linearly in time, we write left-to-right, and it seems to me that
researchers in natural language processing get kind of bored from it and try to
come up with models that generate sentences in any order, just not
left-to-right. We already talked about bidirectional decoding, there are
insertion-based models, models generating all words in parallel. A brand new
pre-trained representation [XLNet](https://arxiv.org/pdf/1906.08237.pdf)
considers all possible orders in which a sentence can be generated. It this
thus wonder that the authors of this paper wanted to organize this mess a
little bit and wrote down a simple equation that can describe almost all
existing ways how sequences can be generated.

Let's start with some notation

* _X_ is an input sentence in the source language.

* _L_ is the length of the target sentence.

* _T_ is a number of steps in which the decoder operates. If we generated the
sentence left-to-right, it would be _T_=_L_. If the sentence is generated
non-autoregressively, _T_=1. Non-autoregressive models with iterative refinement
(as the one I wrote about a few weeks ago) use a small constant number steps,
e.g., _T_=10.

In the formalism, generating a sequence can be described using edit operation
(_z_, _y_) which mean insert/rewrite symbol _y_ on position _z_. This means
that "(0, `A`), (1, `B`), (2, `C`), (3, `D`)" will generate sequence `ABCD`. In
each step (_t_) of the decoding, multiple operations can be made.

And here is the magical equation:

![Masked cross-lingual LM](/assets/MT-Weekly-8/equation.svg)

_G_ is the sequence of edit operation, _Y<sup>≤t</sup>_ are symbols used until
step _t_, _Z<sup>t</sup>_ is a set of positions that were edited in step t.

Let's start with the first term:

![Masked cross-lingual LM: length](/assets/MT-Weekly-8/equation_length.svg)

This just a prediction of how long the target sentence will be. It assigns a
probability to all integers from 1 to some large enough value. The reason of
having it before the products in the equation is that it just makes the rest of
the equation much simpler when we know the length.

Now have a look at the products:

![Masked cross-lingual LM: length](/assets/MT-Weekly-8/equation_products.svg)

This means that in each decoding step _t_+1, we have a look at each word in the
target sentence from _i_ to _L_.

First, we have a look at the probability that we will do something with
position i.

![Masked cross-lingual LM: length](/assets/MT-Weekly-8/equation_position.svg)

Interestingly, using this probability function, we can easily
simulate left-ot-right decoding - just assign a probability of to word on
(t+1)-th position and that is it. When we actually decode from the model, we
need to decide based on the probability of whether z should be set to 0 or 1
because we eventually need to make an edit operation or do nothing (because we
just don't have quantum sentences). We can always choose one position and
decode the sentence one by one, or multiple ones and decode in parallel.

The last term is a probability distribution over the target language
vocabulary:

![Masked cross-lingual LM: length](/assets/MT-Weekly-8/equation_word.svg)

Assume I already know I want to edit at position _i_ (i.e.,
_z_<sub>i</sub><sup>t+1</sup> = 1), this distribution tells me scores of
symbols that can be used at the particular position. The decoding algorithm can
take only the best-scoring, or alternatively, it can keep multiple best-scoring
options and used them in a beam search.

And finally, we have the exponent in the equation. If the algorithm decides no
to edit at position i, z_i^t+1 gets the value of zero, this will make the
product equal to 1 and it will not influence the result of the large products.

So, we already know. That that many decoding techniques are special cases of
this equation. But what will happen if it remains as general as it is?

![Masked cross-lingual LM: length](/assets/MT-Weekly-8/equation_exponent.svg)

First of all, we need to find a model architecture that would allow such
decoding. And for this, the authors used an excellent work by Facebook AI from
this January called Cross-lingual Language Model Pretraining. The paper
describes several ways of training cross-lingual language representation that
can be reused for cross-lingual tasks including machine translation.

The basic idea is quite straightforward and can be seen from this image:

![Masked cross-lingual LM](/assets/MT-Weekly-8/lample.png)

(image is taken from Figure 1, page 4, Lample and Conneau: Cross-lingual
Language Model Pretraining)

They just concatenate matching sentences in two languages, mask some words,
apply a stack of Transformer layers and predict what the masked-out words were.
(They basically do the same thing and BERT but on two parallel sentences).

Now, when we have such a trained model and equation that can describe the
decoding in general terms, we can start discussing the decoding. Probabilities
p(y|...) are already trained with the model, the remaining thing to play with
is probability p(z|...) which is not trained from the data, but set manually
for the experiments and define the probability based on properties of
distributions p(y). We can sample position uniformly, prefer positions which
are easy to estimate (distribution p(y|...) has a low entropy), replace tokens
which has the lowest probability,  left-to-right, ... whatever you want.

Anyway, the most magical property here is that you can use the same model and
the strategies both linear-time and constant-time (non-autoregressive)
decoding.

And what are the results? For linear time decoding (word by word), the
translation quality of basically the same as the current best autoregressive
model. The constant time decoding only 2 BLEU points worse.
