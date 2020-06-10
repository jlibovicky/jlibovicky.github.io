---
layout: post
title: "Machine Translation Weekly 43: Dynamic Programming Encoding"
tags: [mt-weekly, en]
lang: en
---

One of the strongest narratives people (including me) love to associate with
neural machine translation is that we got rid of all linguistic assumptions
about the text and let the neural network learn their own way independent of
what people think about language. It sounds cool, it almost gives a
science-fiction feeling. But what I think that we really do is that we move our
assumptions about the language from hard constrains of discrete representation
into soft constraints of inductive biases that we impose on our neural
architecture.

This is also the case of the paper I am going to discuss today. It throws away
the assumption that input should be tokenized into words that get split into
statistically learned subword units. This is replaced by learned segmentation
that should be tailored specifically to the task of machine translation. The
title of the paper is [Dynamic Programming Encoding for Subword Segmentation in
Neural Machine Translation](https://arxiv.org/pdf/2005.06606.pdf), it has
authors from the Monash University and from Google Research and will appear on
this year's ACL conference.

The main idea of the paper is to build a hybrid character-subword decoder. It
is a standard autoregressive decoder that conditions the current output on what
it generated before. The inputs to the decoder are characters, but the outputs
of the decoder are subwords. At inference time, it would like in the following
figure:

![DPE at inference itme](/assets/MT-Weekly-43/dpe.svg)

The more interesting question is, how such a model can be trained. The paper
introduces a simple dynamic programming algorithm that can sum probabilities of
all possible subword segmentation of the input even though there is
exponentially many of them and it would never be possible to enumerate them
explicitly. The reason why they can use the dynamic programming algorithm is
that the state of the decoder does not depend on what subwords were previously
chosen, but only on what characters the subwords consist of.

In some pseudo-Python the algorithm would look like:

```python
prefix_logprobs = [0 for y in input]
for i, y in enumerate(input):
    partial_probs = []
    for j in range(max_subword_len):
        subword = input[i - j - 1:i]
        if subword in vocab:
            partial_probs.append(prefix_logprobs[i - j - 1] + logprob(subword, states[i -j - 1])
    prefix_logprobs[i] = logsumexp(partial_probs)
```

States are hidden states of the decoder, function `logprobs` gets the
probability the subword given the decoder state

The algorithm, unlike the figure above, does not care what the next step will
be, it rather asks what must have happened, so that the decoder ended up in the
$i$-th state. It iterates over all possible subwords that might have moved it
to state, and for all of them, we already computed the probability was assigned
to the state.

![DPE at training time](/assets/MT-Weekly-43/dpe_train.svg)

Although the model is a fully functional machine translation model, the authors
decided for some reason not to use it so and only used it to learn the
segmentation of the target side of parallel data. Similarly to all dynamic
programming algorithms of this kind, we can replace the log-sum-exp operation
with argmax (i.e., instead of summing all possibilities, just take always the
best one) and thus get the most probable sequence of subwords given the model.
This what the authors do and what they use to segment the training data.

So in the end, this interesting model ends up as a very expensive way of
preprocessing the training data. It improves the translation quality, it makes
a small but significant improvement compared both to standard BPE and BPE
dropout. Also, compared to BPE, it leads to segmentation that makes much more
sense. This is a selection from Table 4 from the paper (the first column is
classical byte-pair encoding, the second column is the new method):

![Examples](/assets/MT-Weekly-43/table.png)

Still, I am quite disappointed that they did not show how the model works when
used for translation. Is it that bad? Or the authors did not bother to
implement the decoding?

The drawback of this method is that you still need the classical segmentation
of the source. At inference time, we do not need to care about the target-side
segmentation, we will use whatever the decoder generates, but the source
sentence, of course, needs to get segmented before it is fed into the encoder.
I was thinking if a similar approach could be used also for the target
sentence... and unfortunately probably not. But maybe someone else will figure
it out. Anyway, I still believe that this paper is an important step on the way
of getting rid of any pre-defined text segmentation.
