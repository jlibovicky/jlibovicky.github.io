u--
layout: post
title: "Machine Translation Weekly 25: Weaknesses of Reinforcement Learning for NMT"
tags: [mt-weekly, en]
lang: en
---

Back in 2016, one of the trendy topics was [reinforcement
learning](https://en.wikipedia.org/wiki/Reinforcement_learning) and other forms
of optimizing NMT directly towards some more relevant metrics rather than using
cross-entropy of the conditional word distributions. Standard machine
translation models are trained to maximize single-word conditional
distribution, which is not exactly what we are interested in when doing machine
translation. What we really want is good translation quality, which does not
factorize over words (or subwords), and can only be assessed on the sequence
level. This line of thinking led to research on reinforcement learning in
machine translation which claimed some successes but after its popularity peak
it seems to me it kind of died out.

Recently, I came across a paper that critically evaluates these approaches and
explains what might be wrong with reinforcement learning in machine
translation. The paper is called [On the Weaknesses of Reinforcement Learning
for Neural Machine Translation](https://arxiv.org/pdf/1907.01752v3.pdf), it
comes from the Hebrew University of Jerusalem and will be presented at this
year's ICRL.

Normally, machine translation models are trained word by word. We feed the
model with a prefix of a reference target sentence, and the model guesses what
the next word is. Based on how incorrect the guess was, the model gets updated.
Reinforcement learning works differently. It is a type of machine learning that
you would expect in robotics: an agent tries to do something on its own and
based on how much it succeeds, it changes its behavior for the next attempts.
When applied to machine translation, we let the model generate an entire
sentence (without providing the reference sentence prefix), measure how good it
is (i.e., a reward) and based on that update the model. The tricky thing we
need to deal with is that we do not really know what words contributed to the
reward.

The methods include [minimum risk
training](https://www.aclweb.org/anthology/P16-1159.pdf) that estimates the
expected BLEU score, various adaptations of the [REINFORCE
equation](http://www.scholarpedia.org/article/Policy_gradient_methods), and
using a generator-discriminator setup to learn more adequate reward function
than BLEU (or another score). One thing all the papers had in common was that
they always started with an already-trained model and only fine-tuned the model
to get a slightly higher translation quality.

This paper I mentioned earlier is very skeptical about the methods. Although
they are always well theoretically justified, the empirical improvement of the
translation quality is small and might have a different reason. The paper
presents experiments that show that most reinforcement learning approaches do
not teach the model anything new it did not know before. It makes the output
distribution peakier, so if the model was already good enough, it just
reinforces it in its good decisions (which presumably helps in beam search).
However, in the experiments, they never observe that a correct (and thus
reward-worth) word that scored really badly in the model got ranked higher
after the finetuning.

I always thought that the reason why these methods do not generate much
improvement was that sentence-level machine translation evaluation is a hard
problem. Even though there exist few decent methods, most of them are too slow
to be used in a setup when the millions of training sentences need to be
repeatedly evaluated during training. Anyway, this paper suggests that even if
we had such an evaluation metric, it probably would not help much.

Maybe the reason why reinforcement learning does not work as well as we would
expect is the assumption that a trained NMT model describes a good distribution
over target sequences. From [a
paper](https://www.aclweb.org/anthology/D19-1331.pdf) that I discussed in [MT
Weekly 20](/2019/11/21/MT-Weekly-Search-and-Model-Errors.html), we know that
this is not entirely true. I would say that by pure luck, the beam search
algorithm leads to good translations, even though its outputs are not the
sentences that are the most probable given the model. Maybe if we can fix the
probability, reinforcement learning would become much more useful.

```bibtex
@article{choshen2019weaknesses,
  title={On the Weaknesses of Reinforcement Learning for Neural Machine Translation},
  author={Choshen, Leshem and Fox, Lior and Aizenbud, Zohar and Abend, Omri},
  journal={arXiv preprint arXiv:1907.01752},
  year={2019}
}
```
