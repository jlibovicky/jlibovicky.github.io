---
layout: post
title: "Machine Translation Weekly 19: Domain Robustness"
tags: [mt-weekly, en]
lang: en
---

This week, I will have a look at a paper that discusses another major problem
of current machine translation which is domain robustness. The problem is very
well analyzed in a paper from the University of Zurich called [Domain Robustness
in Neural Machine Translation](https://arxiv.org/pdf/1911.03109.pdf) that
appeared on arXiv earlier this week.

Domain robustness is just another word for preventing overfitting to training
data although in this case very special kind of overfitting. It is not
surprising that a system train on EU legislation movie subtitles (which is what
most parallel corpora consist of) will underperform on text for medical
professionals full of expressions that are hardly understandable for the
public. What is really stunning is how the systems usually fail. They often
hallucinate fluent text that has nothing in common what was in the source
sentence. The paper shows an excellent example.

![Hallucinated translation](/assets/hallucinate.png)

Statistical machine translation that was the state of the art before 2016
provided worse translation quality in general, but it would never do such
embarrassing spectacular nonsense.

In the paper, they play around with several methods that should help with this
problem of hallucinating nonsense sentences.

1. __Subword regularization.__ They use a very similar method to what I
[discussed last week](/2019/11/07/MT-Weekly-BPE-dropout.html). During training,
they generate various segmentation of the text and thus make more robust.

2. __Reconstruction regularization.__ During training, they add another decoder
that uses states of the normal decoder to generate back the source sentence
(they pretend the first decoder is actually an encoder). To make it work, they
need to do plenty of quite complex tricks, but the idea is simple: the decoder
should only produce such stuff from which the original sentence can be
reconstructed. If you cannot translate back, you probably did not do a good
translation.

3. __Noisy channel rescoring.__ The core idea the same as in the previous
method, but it happens at the inference time. First, they generate a long
n-best list and then rescore this n-best list by a system trained in the
opposite direction. This again should eliminate sentences that have nothing in
common with the source. However, the problem of this method is that there is
almost no variability in the n-best lists and requires more computation at
inference time.

And... Yay, it works! The combination of the reconstruction regularization and
subword regularization gets the best results on both in-domain and
out-of-domain data and outperforms the good old statistical system in the last
discipline for which it worked better than neural networks.

Another technique they tried and performed quite well was knowledge
distillation. It is a technique where they first train one model, translate
plenty of data with the model and train another model on the synthetic data. My
intuition is that the model does not have any chance to learn something new
that was not in the first model. On the in-domain data, the translation quality
indeed does not change, but it significantly improves on the out-of-domain test
data. I have no idea why. If the teacher model hallucinates nonsense sentences,
why does not the student model learn it as well?
