---
layout: post
title: "Machine Translation Weekly 70: Loss Masking instead of Data Filtering"
tags: [mt-weekly, en]
lang: en
---

This week, I will have a closer look at a recent pre-print introducing an
alternative for parallel data filtering for machine translation training. The
title of the pre-print is [Gradient-guided Loss Masking for Neural Machine
Translation](https://arxiv.org/abs/2102.13549) and comes from CMU and Google.

Training data cleanness is a surprisingly important factor for machine
translation quality. A large part of the data that we use for training comes
from crawling the Internet, so there is no quality guarantee. On the other
hand, the tools for crawling parallel data are pretty good, so the sentence
pairs that we get are always at least partial translations of each other. One
would expect that the more data the better and that few bad sentence pairs get
lost in the majority of the good parallel sentence pairs in the training data.
However, this only holds to a certain extent. The problem of data cleanness is
of such interest to the machine translation community that there is a [parallel
data filtering task at the Conference of Machine
Translation](http://statmt.org/wmt20/parallel-corpus-filtering.html). The
results of the task show that filtering can improve the translation quality by
several BLEU points if it is done well.

The pre-print takes a different approach: they want to use all data they have.
After all, there must be some information value in them. Otherwise, they would
not have ended up aligned together as mutual translations. On the other hand,
we know that low-quality sentence pairs can harm the model training. In the
pre-print, they want to detect those sentences automatically and dynamically
mask them out. The advantage is that the sentence can harm the training only at
certain stages of the training.

They do this by having a separate small set of high-quality translations which
can be pretty small (several thousand sentence pairs). In a training step, they
compute the loss function gradient on both the regular training batch and the
high-quality data. The gradient says in what direction and how much the model
parameters should be shifted so that the loss function decreases (and the model
outputs get more similar to the training data batch). They compare the
gradients obtained from every sentence in the regular batch with the gradients
from the high-quality data. If they point in a roughly same direction, they are
used for training, if they point in a totally opposite direction, they get
masked out.

A question that may arise at this point is if it is not better to use the
high-quality data directly for training. I do not think so. It would either
dissolve in the large training data and have no effect on the training, or if
they upsample it to be more prominent in the training data, the model would
overfit and memorize them instead of learning general patterns from it. So, I
think this held-out gradient-validation set is actually a very good use of the
high-quality data if most of the training data is noisy.

Computing the gradients separately for each training sentence in the batch is
computationally quite expensive (although the paper says they have a pretty
efficient way of doing so), so they do not do this clever update for every
batch, but only once in a while. Still, the trick seems to improve the
translation quality.

The paper reports solid translation quality improvements on high-resource
languages and the low-resource scenario is simulated on IWSLT data. However,
because it is an alternative to parallel data filtering, I would appreciate
more the evaluation on real low-resource pairs where data filtering plays a
much more important role and comparison with parallel data filtering
techniques.

The idea of the paper is a sign of a better and better understanding of what is
going inside of the neural networks in NLP. Several years ago, the main problem
(at least for me) was just to make the beast work somehow. I believe that
exploiting the insights about the network for such cool hacks will occur more
and more often has currently the biggest potential to improve MT in the next
few years. (At least, before the next large paradigm shift comes.)
