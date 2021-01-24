---
layout: post
title: "Machine Translation Weekly 66: Means against ends of sentences"
tags: [mt-weekly, en]
lang: en
---

This week I am going to revisit the mystery of decoding in neural machine
translation for one more time. It has been more than a year ago when Felix
Stahlberg and Bill Byrne discovered the very [disturbing feature of neural
machine translation models](https://www.aclweb.org/anthology/D19-1331) – that
the most probable target sentence is an empty sequence and this it is a sort of
luck that we decode good translations from the models ([MT Weekly
20](/2019/11/21/MT-Weekly-Search-and-Model-Errors.html)). The paper disproved
the narrative of NMT being a relatively accurately trained model that knows
well how the most probable target sentence looks like, but we only have an
approximative algorithm that can get us a highly probable, but not the most
probable target sentence.

Recently, two papers reacted to this finding: [one
suggested](https://www.aclweb.org/anthology/2020.emnlp-main.170) that we do not
get the sentence that is the most probable, but also a sentence with even
distribution of the model surprisal which corresponds to the uniform
information density theory from psycholinguistics ([MT Weekly
56](/2020/10/25/MT-Weekly-Beach-Search-and-Surprisal.html)). The [other
alternative approach](https://www.aclweb.org/anthology/2020.coling-main.398)
says that we might not want the most probable individual sentence, but a
sentence that well represents a cluster of similar highly probable sentences
which together might be much more probable than the most probable individual
sentence ([MT Weekly 63](/2020/12/20/MT-Weekly-MAP-vs-Minimum-Bayes.html)).
Both the papers agree that the models are trained well.

This week, I will comment on a paper that views this problem from a less
theoretical, but very pragmatic engineering point of view and shows how to
train the models slightly differently to get rid of this property. The title of
the pre-print is [Why Neural Machine Translation Prefers Empty
Outputs](https://arxiv.org/abs/2012.13454) and describes work done at [DiDi
Labs](https://en.wikipedia.org/wiki/DiDi_(company)).

The thinking in the paper is as follows: _Why does the decoding lead to short
or even empty sentences?_ Well, because the end-sentence-token gets assigned
probability that is too high. _Why is it too high?_ Because it is a priori
probable, it is every single sentence. When the model is unsure about what the
next token should be, the end of the sentence might appear as a safe choice
because it just has to be there somewhere.

When the problem is put like this, then the solution is relatively
straightforward. In the paper, they propose using multiple different
end-of-sentence tokens, one per target sentence length. And this is it: this
change causes that the prior probability of each of the end-of-sentence symbols
will be much lower and the inclination of the model to generate short sentences
will be much smaller.

The pre-print went out on December 24, so my guess is that the authors wanted
to have something out before the anonymity period of ACL started and hopefully,
the final published version will answer questions that the pre-print leaves
unanswered: Does this change exactly influence the translation quality with
standard beam search decoding with length normalization? Is length
normalization still necessary? Does the model always generate the correct
end-of-sentence symbol with the correct number?
