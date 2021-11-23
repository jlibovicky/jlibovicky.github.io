---
layout: post
title: "Machine Translation Weekly 94: Notes from WMT 2021"
tags: [mt-weekly, en]
lang: en
issue: 94
---

After the notes from EMNLP 2021, here is also an unsorted list of some
observations from the Conference on Machine Translation.

* Facebook AI won in many translation directions (not at all in all of them) in
  the news task with a [multilingual
  system](http://www.statmt.org/wmt21/pdf/2021.wmt-1.19.pdf).

* At the panel discussion about MT evaluation, Herman Nay expressed a
  controversial opinion: it does not matter what metric we use, the history of
  MT would be the same with any metric (that at least slightly correlates with
  what humans think).

    * Probably partially true: The major breakthroughs brought such large
      improvements that would be obvious in any metric. But saying that would
      mean saying that most of the research is irrelevant and only the major
      breakthroughs matter and most of the papers (like those I write) do not
      have much value. Maybe it is true afterall.

* Another provocative stance: Kenneth Heafield says that significance testing
  using bootstrap resampling is misleading, it only captures the variance of
  the test set, not the variance that comes from the randomness of the method.
  With a sufficiently large test set, every difference would be significant,
  regardless of the randomness of the training process.

    * Tom Kocmi replied that they have empirical evidence that significance testing
      with automatic metrics helps to decide if human annotators would consider one
      system better than another.

    * Rejoinder: considering any difference significant is a particularly weak
      baseline. Maybe simple common-sense-based thresholding would do the same
      job.

* There was also a call for a central repository of translated test sets. With
  model-based metrics, there will be a need to reevaluate existing results,
  with better pre-trained models, there will be naturally also better metrics.
  But such a repository sounds too much like a leaderboard and leaderboards
  make people crazy… The community does not seem to be in favor of this.

* All good evaluation metrics and QE metrics seem to use XLM-R as the
  underlying model.

* Out-of-domain sentences seem to be problematic for model-based metrics. Bad
  news, but an unavoidable drawback of using machine-learning methods.

* Findings paper of the efficiency tasks claims that they know a recipe for how
  to translate 10k times cheaper than cloud services (assuming model training
  and labor of developers is for free). None of the submissions to the task was
  non-autoregressive.
