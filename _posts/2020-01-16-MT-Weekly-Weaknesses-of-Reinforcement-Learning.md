---
layout: post
title: "Machine Translation Weekly 25: Weaknesses of Reinforcement Learning for NMT"
tags: [mt-weekly, en]
lang: en
---

Back in 2016, one of the trendy topics was reinforcement learning and other
forms of optimizing NMT directly towards some relevant metric rather than using
cross-entropy of the conditional word distributions. Good single word
distributions are not exactly what you are interested in when doing machine
translation. What you really want is good translation quality, which does not
factorize over words (or subwords). This line of thinking led to research on
reinforcement learning in machine translation which claimed some successes but
after its popularity peak in 2016 it kind of died out.

Recently, I came across a paper that critically evaluates these approaches and
explains what might be wrong with reinforcement learning in machine
translation. The paper is called [On the Weaknesses of Reinforcement Learning
for Neural Machine Translation](https://arxiv.org/pdf/1907.01752v3.pdf), it
comes from the Hebrew University of Jerusalem and will be published at this
year's ICRL.

Most of the papers on reinforcement learning started from an already trained
model and were finetuned to get a (typically negligible) higher BLEU score. The
methods include minimum risk training estimating expected BLEU score, various
adaptations of the REINFORCE equation, and using a generator-discriminator
setup to learn more adequate reward function than a BLEU (or another score).
One thing all the papers had in common was that they always started with an
already-trained model and only fine-tuned the model to get a slightly higher
translation quality.

This paper very skeptical about the results. Although the papers are well
theoretically justified, the empirical improvement of the translation quality
might have another reason. The paper presents experiments that show that most
reinforcement learning approaches do not teach the model anything they did not
know before. It makes the output distribution peakier, so if the model was
already good enough, it just reinforces it in its good decisions (which
presumably helps in beam search). However, they never observe in the
experiments that a (correct, reward-worth) word that scored really bad in the
model ranked higher after the finetuning. The funny thing is that the effect
appears also if the reward is constant, so it actually does not matter so much
what the reward function is.

One thing the paper does not mention at all and what I always thought was the
case is that these methods do not work well, after all, sentence-level machine
translation evaluation is a very hard problem and even though there exist few
decent methods, most of them are too slow to be used in a setup when the
millions of training sentences need to be repeatedly evaluated during training.
Anyway, this paper suggests that even if we had such a metric, it probably
would not help.

Maybe the reason why reinforcement learning does not work as well we would
expect is the assumption that a trained NMT model describes a good distribution
over target sequences. From a paper that I discussed in MT Weekly 20, we know
that this is not entirely true and by pure luck, the beam search algorithm
leads to good translations, even though its outputs are not the sentences which
are the most probable given the model. Maybe if we can fix the probability,
reinforcement learning would become much more useful.

```bibtex
@article{choshen2019weaknesses,
  title={On the Weaknesses of Reinforcement Learning for Neural Machine Translation},
  author={Choshen, Leshem and Fox, Lior and Aizenbud, Zohar and Abend, Omri},
  journal={arXiv preprint arXiv:1907.01752},
  year={2019}
}
```
