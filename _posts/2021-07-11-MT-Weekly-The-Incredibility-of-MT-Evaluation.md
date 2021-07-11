---
layout: post
title: "Machine Translation Weekly 85: The Incredibility of MT Evaluation"
tags: [mt-weekly, en]
lang: en
paperTitle: "Scientific Credibility of Machine Translation Research: A Meta-Evaluation of 769 Papers"
paperAuthors: "Benjamin Marie, Atsushi Fujita, Raphael Rubino"
issue: 85
---

This week, I will comment on a paper that quantifies and exactly measures the
dimensions of the elephant in the room of machine translation: the lack of
empirical support of claims in research papers on machine translation. The
title of the paper is [Scientific Credibility of Machine Translation Research:
A Meta-Evaluation of 769 Papers](https://arxiv.org/abs/2106.15195), it has
awill appear at this year's ACL.uthors from NICT in Japan and was awarded as an
oustanding paper ACL 2021.

The authors manually annotated an incredible number of papers and looked for
the methodological mortal sins of machine translation:

* Papers tend to use the BLEU score as the only evaluation metric (although it
  is well known not to correlate well enough with human judgment).

* Statistical significance tests are rarely conducted.

* Outputs of automatic metrics are compared with numbers reported in other
  papers without ensuring the metric was exactly the same.

* Outputs of automatic metrics are compared with systems trained on different
  data (e.g., differently preprocessed).

The papers could get one point for doing each of these things right. Figure 6
of the paper shows how the evaluation thoroughness degrades over time, except
for the last year when the discussion about automatic metrics for MT evaluation
became more prominent again.

![Evaluation points in time.](/assets/evaluation_points.png)

But there also other disturbing things. For instance, the paper shows that tiny
details in model training that are usually omitted in papers can lead to
differences in BLEU scores that were considered significant in many papers that
claim some improvement. On the other hand, the annotation only considered the
papers themselves. Many papers publish also their source code and those details
might often be obtained from the training scripts.

I wonder what the reasons are that the paper authors became so negligent about
the evaluation and the paper reviewers became so indulgent at the same time.

The drop of the evaluation thoroughness coincides with the advent of the deep
learning methods in machine translation. I believe that part of the reason
might be that people tend to imitate what they think are the most influential
papers and what are the foundations of the methods they use. Here, the most
influential papers were those that introduced the architectures, papers by
[Sutskever et al.
(2014)](https://papers.nips.cc/paper/2014/file/a14ac55a4f27472c5d894ec1c3c743d2-Paper.pdf)
and [Bahdanau et al. (2015)](https://arxiv.org/abs/1409.0473), often leaving
out the pioneering work Kalchbrenner and Blunsom (2013). The thing these papers
have in common is that their main message is that the architectures they
introduced do at least something interesting. They did not have the ambition to
show their models were significantly better than the state-of-the-art
statistical MT at that time, they wanted to show their results are comparable
and worth of future research. From that perspective, the evaluation in these
papers was just enough.

Soon after that Rico Sennrich came with two crucial innovations:
[back-translation](https://aclanthology.org/P16-1162/) and [subword
segmentation](https://aclanthology.org/P16-1009/), the preprints appeared on
arXiv in August and November 2015. The gains from using these techniques were
so large that there was no doubt the differences are significant. A similar
situation appeared when the Transformer architecture was introduced. These
papers are those that established the new paradigm in machine translation. None
of them did a very thorough evaluation because none of them needed it. It is
possible that they unintentionally created a model of "good" neural MT paper
that other papers followed.
