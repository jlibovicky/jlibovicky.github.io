---
layout: post
title: "Machine Translation Weekly 45: Deep Encoder, Shallow Decoder, and the Fall of Non-autoregressive models"
tags: [mt-weekly, en]
lang: en
---

Researchers concerned with machine translation speed invented several methods
that are supposed to significantly speed up the translation while maintaining
as much as possible from the translation quality of the state-of-the-art
models. The methods are usually based on generating as many words as possible
in parallel.

State-of-the-art models do not generate in parallel, they are autoregressive:
it means that they generate words one by one and condition the decisions about
the next words on the previously generated words. On the other hand, all
computations in the rest of the Transformer models can be heavily parallelized,
such that they can process sentences almost in constant time with respect to
the sentence length. Normally this applies only to the encoder because the
decoder needs to proceed word by word anyway. This parallelism is of course
very attractive for researchers that tried parallelize the decoding phase as
well and generate all (or at least some) output words at once. These efforts
led the to invention of so-called non-autoregressive models.

A recent preprint [Deep Encoder, Shallow Decoder: Reevaluating the Speed-Quality
Tradeoff in Machine Translation](https://arxiv.org/abs/2006.10369) with authors
mostly from the University of Washington shows that similar speedup and much
better translation quality can be achieved by making the parallelizable encoder
deeper and reducing the size of the decoder that generates the sentence
sequentially. The only thing the authors did is that instead of using a 6-layer
encoder and a 6-layer decoder, they used a 12-layer encoder and a single-layer
decoder. And of course, they analyzed very carefully both the speed and the
translation quality.

The paper rigorously studies the latency of machine translation systems by
distinguishing two use cases:

1. _Online translation_ when we translate sentences one by one and present it
   immediately to the user, and

2. _Batched translation_ when we want to translate a large amount of text at
   once (and it does really make sense present it sentence by sentence).

Non-autoregressive models excel in the first type of latency, but papers about
the models kind of forget to mention that they really suck in the second setup,
sometimes being 10 times slower than the standard autoregressive models. The
model promoted in this paper excels in both of the setups.

After reading the paper, I wonder what the future of the non-autoregressive
models is. If I was supposed to deploy a low latency MT system in a production
setup, I would definitely opt for an autoregressive one with a deep encoder and
a shallow decoder. On the other hand, my humble introspective intuition (but
who cares about introspection, language is a social phenomenon!) tells me that
autoregressive generation is not exactly the most efficient and natural way of
text generation. Usually, when I speak or write I do not feel like I think what
to say next after every single subword unit, but I always know what the next
few words will be. (Maybe psycholinguists or neuroscientists would tell me I do
not.) So, perhaps some sort of semi-non-autoregressive approach would be the
best: when it is clear what will follow generates the words in parallel and
generate autoregressively otherwise. (It sounds like yet another opportunity
for reinforcement learning.)

While reading the paper, I was also asking a question what does this paper say
about how we do research. How did it happen that people started to work on
non-autoregressive methods before trying out deep encoder and shallow encoder
first? I can think of two main reasons:

1. Encoder-decoder models are often explained as conditional language models.
   It implies that the decoder is the most important part. The decoder is the
   language model and only uses the encoder as a sort of external memory.

2. Publication-driven research prefers a certain type of innovation. People
   might be afraid that simple ideas (like this one) can be considered trivial
   and not worth publishing. This is why people started to think about fancy
   solutions before trying a simple one.

Whatever the reason is, it seems our community Occam's razor is not sharp
enough.
