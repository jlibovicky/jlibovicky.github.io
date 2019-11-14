---
layout: post
title: "Machine Translation Weekly 19: Domain Robustness"
tags: [mt-weekly, en]
lang: en
---

This week, I will briefly have a look at a paper that discusses another major
problem of current machine translation which is domain robustness. The problem
is very well analyzed in a paper from the University of Zurich called [Domain
Robustness in Neural Machine Translation](https://arxiv.org/pdf/1911.03109.pdf)
that appeared on arXiv earlier this week.

Given that MT is approached using machine learning, domain robustness is just
another fancy word for preventing overfitting to training data—although in this
case a special kind of overfitting. It is not surprising that a system trained
on EU legislation, movie subtitles and crawled web pages (which is what most
parallel corpora consist of) will underperform on text for medical
professionals full of expressions that are hardly understandable for the
public. What is really stunning is how exactly the systems usually fail. They
tend to hallucinate fluent text that has nothing in common what was in the
source sentence. The paper shows an excellent example of that.

![Hallucinated translation](/assets/hallucinate.png)

Statistical machine translation that was the state of the art before 2016
provided worse translation quality in general, but it would never produce such
spectacular nonsense.

In the paper, they play around with several methods that should help with this
problem of hallucinating nonsense sentences.

1. __Subword regularization.__ They use a very similar method to what I
   [discussed last week](/2019/11/07/MT-Weekly-BPE-dropout.html). During
   training, they generate various segmentation of the text and thus make more
   robust.

2. __Reconstruction regularization.__ During training, they add another decoder
   that uses hidden states of the standard decoder to generate back the source
   sentence (they kind of pretend that the first decoder is actually an
   encoder). To make it work, they need to do plenty of quite complex tricks,
   but the idea is simple: the decoder should only produce stuff from which the
   original sentence can be reconstructed. In other words: if you cannot
   translate back at all, you probably did not make a good translation.

3. __Noisy channel rescoring.__ The core idea the same as in the previous
   method, but it is applied at the inference time. First, they generate a long
   _n_-best list of translation candidates and then rescore this list using a
   system that was trained to translate in the opposite direction. This again
   should eliminate "translations" that have nothing in common with the source
   sentence. However, the problem of this method is that there is almost no
   variability in the _n_-best lists and requires more computation at inference
   time.

And... Yay, it works! The combination of the reconstruction regularization and
sub-word regularization gets the best results on both in-domain and
out-of-domain data and outperforms the good old statistical systems probably in
the last discipline for which it worked better than neural networks.

Another technique they tried and got quite results was _knowledge
distillation_. It is a technique where they first train one model, translate
plenty of data with the model and train another model on this generated
synthetic data as training data. My intuition would be that the model does not
have any chance to learn anything new that was not already in the first model.
On the in-domain data, the translation quality indeed does not change, but it
significantly improves on the out-of-domain test data. And I have no idea why.
I would understand if they would try to distill what they could get from the
relatively complex noisy channel pipeline into a simpler model, but if I
understood the paper correctly, they only use a vanilla model for the
distillation. If the teacher model hallucinates nonsense sentences, why does
not the student model learn it as well?
