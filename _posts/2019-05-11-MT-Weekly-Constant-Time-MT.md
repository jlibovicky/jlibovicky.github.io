---
layout: post
title: "Machine Translation Weekly 3: Constant-Time Machine Translation with Conditional Masked Language Models"
tags: [MT Weekly]
lang: en
---

This week, we will have a look at a brand-new method for non-autoregressive
machine translation published [week ago on
arXiv](https://arxiv.org/pdf/1904.09324.pdf) by [Facebook AI
Research](https://research.fb.com/category/facebook-ai-research/).

Most models for neural machine translation work autoregressively. When the
model outputs a word, the decision is always conditioned on what words were
generated in the past. This ensures the coherence of the generated sentences.
On the other hand, it limits to what extent the computation can be parallelized
because each word can be produced only after the previous ones were generated.

Last year, there were several attempts to come up with non-autoregressive
models which proceed in parallel and generate all target words at once. The
models usually reach 200-300% speedup at the cost of a significant drop in
translation quality. This new paper called [_Constant-Time Machine Translation
with Conditional Masked Language Models_](https://arxiv.org/pdf/1904.09324.pdf)
keeps the same speedup, however, narrows the quality gap from the
autoregressive model to 5-10%.

The model borrows the idea of masked language modeling from [_BERT_, a general
sentence representation model](https://arxiv.org/pdf/1810.04805.pdf). In BERT,
the neural network is taught to guess what words were masked-out in the input.
The network is thus forced "comprehend" (whatever it means) the rest of the
sentence in such a way, it can guess what word is missing. And this is exactly
what this translation model does as well.

As the first step, it encodes the source sentence the same way the standard MT
models do. It also uses the source sentence representation to estimate the
target sentence length. This estimate is used to generate a fully masked target
sentence which is the input to the decoder in its first iteration.

As in the BERT model, the decoder is a stack of Transformer layers that attend
the masked input, but also to the source sentence representation from the
encoder. Because everything can be computed in parallel, the decoder generates
a sequence of output words in asymptotically constant time.

Words  generated with the lowest probability are masked out and the output is
used as an input to the decoder in the next step. The mask-out words are
replaced by more fine-grained estimates. The paper suggest to repeat this 10
times, probably more iteration only slow down the computation and do not
further improve the translation quality.

[my animation]

This is an example (page 3, Figure 1) from the paper (examples in papers always
carefully cherry-picked) which shows how translation get gradually improved
during the iterations.

![Example](/assets/constant_time.png)

The authors use another trick to deal with the target length estimate. A prior
estimate of how long the target sentence will be is quite difficult. (Would you
be able to say, how many words you will say in a sentence before you start to
write down the sentence? Me certainly not.) This is in fact the Achilles heel
of all non-autoregressive models. In this paper, they just try several possible
target sentence lengths and simply chose the one yields the best result.
Because all of them can be explored in parallel, it only means a negligible
delay.

A kind of mystery (at least for me) that is common to all non-autoregressive
models is that these model work much better if they are trained on outputs of
standard autoregressive models rather than real-world translated sentences.
This, by the way, means that the non-autoregressive model can never beat the
original one because the best thing it can do is to learn to fully replicate
their behavior. This trick is sometimes called knowledge distillation. To your
disappointment, my dear readers, I cannot really think about what makes the
synthetic (and thus often incorrect) data so special that the
non-autoregressive models like them so much.
