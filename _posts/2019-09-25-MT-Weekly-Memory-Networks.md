---
layout: post
title: "Machine Translation Weekly 12: Memomory-Agumented Networks"
tags: [mt-weekly, en]
lang: en
---

Five years ago when deep learning slowly started to be cool, there was a paper
called Neural Turing Machines (https://arxiv.org/abs/1410.5401) (which are not
really [Turing machines](https://en.wikipedia.org/wiki/Turing_machine), but at
least they are neural). When I read the paper, it left me with an impression
that it might be the beginning end of computer science as we know it. (And also
with an impression that everything I do for my Ph.D. is hopelessly bad compared
to such cool papers.)

The paper introduces an architecture that attempts to mimic how the Turing
machine operates. Instead of a potentially infinite memory tape, it has a
constant-sized memory matrix that is addressed using the attention mechanism
(which was not known as the attention mechanism at that time) for read and
write operations. It was showcased on a few simple algorithmic tasks and it
kind of worked. I secretly hoped that soon more powerful architectures would be
invented and eventually, we might have models able to pick up what a program
should do based on dozens of examples. Programmers could have been the first
ones to lose jobs due to AI. Now, it is 2019 and obviously, it is not
happening.

The architecture of the Neural Turing Machine was not only the main source of
inspiration for the attention mechanism, one of the most important ideas in
natural language processing of the last couple of years, it also gave birth to
neural architectures called Memory-Augmented Networks. The main feature of
these neural networks is that they explicitly read-and-write memories which
sort of mimics how current computer programs work and also makes the networks a
little bit more interpretable. They are usually tested on theoretically
motivated algorithmic tasks, which always makes me suspect that they might not
work on real tasks.

The reason why I am talking about this is that a paper called [Memory-Augmented
Neural Networks for Machine
Translation](https://www.aclweb.org/anthology/W19-6617) from Trinity College
Dublin that shows how these architectures can work when applied on machine
translation. In the standard encoder-decoder architecture, the encoder
processes the source sentence and the decoder uses the attention mechanism to
get information from the encoder. From the perspective of the memory networks,
the decoder uses the encoder outputs as a memory from which it only can read.
In the fully memory-network setup presented in the paper, the encoder has
read-write access to the memory and so does the decoder. The model must first
learn to write the relevant pieces of information in the memory and then,
during the decoding, read what was written in the memory and eventually delete
what is no longer of use.

![Architecture.](/assets/memory_agumented.png)

The paper shows that it is indeed possible to train a model like this. It even
outperforms the standard architecture for English-Vietnamese translation and
gets a bit worse for English-Romanian translation. This (and the fact that the
paper does not show any results on high-resource languages) kind of suggests
that the more training data you have, the more the memory network lags behind,
which makes not really useful for production use cases. Anyway, it is cool to
see that such a general architecture actually can learn to translate.

A footnote: Does anyone remember the [Universal
Transformer](https://arxiv.org/pdf/1807.03819.pdf) (the last year's summer
hit)? It applied the same Transformer layer over and over until some criteria
were reached. This was also a kind of memory network—the self-attention reads
the information from the memory and decides how much it should get overwritten.
Maybe we should think more about the notion of memory in machine translation.
