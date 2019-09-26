---
layout: post
title: "Machine Translation Weekly 12: Memory-Augmented Networks"
tags: [mt-weekly, en]
lang: en
---

Five years ago when deep learning slowly started to be cool, there was a paper
called [Neural Turing Machines](https://arxiv.org/abs/1410.5401) (which are not
really [Turing machines](https://en.wikipedia.org/wiki/Turing_machine), but at
least they are neural in a narrow technical sense). The paper left me with a
foolishly naive impression that it might be the beginning of the end of
computer science as we know it.  (And also with an impression that everything I
do for my Ph.D. is hopelessly bad compared to such cool papers.)

The paper introduces an architecture that attempts to mimic how the Turing
machine operates. Instead of a potentially infinite memory tape, it has a
constant-sized memory matrix that is addressed using the attention mechanism
(which was not known as the attention mechanism at that time) for read and
write operations. It was showcased on a few simple algorithmic tasks and it
kind of worked. (It can learn to sort numbers, isn't that great?) I secretly
hoped that soon more powerful architectures would be invented and eventually,
we might have models able to pick up what a program should do based on dozens
of examples. Programmers could have been the first ones to lose jobs due to AI.
(Wouldn't that be great?)

The architecture of the Neural Turing Machine was not only the main source of
inspiration for the attention mechanism, one of the most important ideas in
natural language processing of the last couple of years, but it also gave birth
to a research direction exploring neural architectures called Memory-Augmented
Networks. The main feature of these neural networks is that they explicitly
read-and-write memories which sort of mimics how current computer programs work
and also makes the computation of the network a little bit more interpretable.
They are usually tested on theoretically motivated algorithmic tasks, which
always makes me suspect that they might not work on more real-world tasks.

The reason why I am talking about this is that a paper called [Memory-Augmented
Neural Networks for Machine
Translation](https://www.aclweb.org/anthology/W19-6617) from Trinity College
Dublin recently showed how these architectures can work when applied on machine
translation. In the standard encoder-decoder architecture, the encoder
processes the source sentence and the decoder uses the attention mechanism to
collect relevant information from the encoder. From the perspective of the
memory networks, the decoder uses the encoder outputs as a memory from which it
only can read. In the fully memory-network setup presented in the paper, the
encoder has read-write access to the memory and so does the decoder. First, the
model must learn to write the relevant pieces of information in the memory and
then, during the decoding, read what was written in the memory and eventually
delete what is no longer of use. This is illustrated well on a scheme in the
paper:

![Architecture.](/assets/memory_agumented.png)

As mention earlier, the paper shows that it is indeed possible to train a model
like this. The analysis of the read and write gates shows that they do exactly
what was expected. It even outperforms the standard architecture for
English-Vietnamese translation and gets a bit worse for English-Romanian
translation. This (and the fact that the paper does not show any results on
high-resource languages) kind of suggests that the more training data you have,
the more the memory networks lag behind the more standard approaches. Anyway,
it is still cool to see that such a general architecture actually can learn to
translate.

A footnote: Does anyone remember the [Universal
Transformer](https://arxiv.org/pdf/1807.03819.pdf) (the last year's summer
hit)? It applied the same Transformer layer over and over until some criteria
were reached. This was also a kind of memory network—the self-attention reads
the information from the memory and decides how much it should get overwritten.
Maybe we should think more about the notion of memory in machine translation.
