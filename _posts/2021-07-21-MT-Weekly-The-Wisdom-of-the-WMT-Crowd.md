---
layout: post
title: "Machine Translation Weekly 86: The Wisdom of the WMT Crowd"
tags: [mt-weekly, en]
lang: en
issue: 85
---

Most of the papers that I comment on and review here present novel and cool
ideas on how to improve something in machine translation or multilingual NLP.
On the other hand, the WMT submissions are different. People want to get the
best translation quality and value efficiency, and simplicity. Novelty and
prettiness of the ideas are secondary. [WMT](http://www.statmt.org/wmt21)
organizes annual competitions in machine translation quality (and other tasks
related to machine translation) where dozens of companies and universities
participate. Each submission is accompanied by a system description paper that
summarizes what the teams did for the competition.

For a project I am working on, I annotated the system description paper from
WMT18-20 and here I bring some statistics on what people do in their
submissions. Here are some basic statistics on what people when they want to
compete in WMT.

### Models

Most people use the Transformer BIG model or more recently even bigger
transformers. Smaller Transformers and RNNs are out of fashion. If you want to
compete, you should just use a Transformer, and the bigger the better.

![Model types](/assets/MT-Weekly-86/model_types.svg)


### Toolkits

In 2019, [Marian](https://marian-nmt.github.io/) was the most popular Toolkit.
In 2020, it was [Fairseq](https://github.com/pytorch/fairseq). It is hard to
say why. Surely, it is easier to make architecture changes in the Python code
of Fairseq than in Marian, especially for a newcomer. However, this is what
only a minority of contestants do. In 2018,
[Sockey](https://github.com/awslabs/sockeye) and
[Tensor2Tensor](https://github.com/tensorflow/tensor2tensor) were used a lot. I
guess they lost popularity because of the underlying frameworks (MXNet and
TensorFlow 1.x). Maybe their users prefer Fairseq now.  Also, the number of
teams using their own implementation tends to decrease.

![Model types](/assets/MT-Weekly-86/toolkits.svg)

### Other tricks

Here comes a summary of other tricks (proportion of teams that used the listed
techniques):

|                            | 2018| 2019| 2020|
|:---------------------------|----:|----:|----:|
| Architecture changes       |  4% | 22% | 16% |
| Pre-training               |  4% | 16% | 22% |
| Backtranslation            | 85% | 82% | 94% |
| ↳ Tagged backtranslation   |  0% |  0% | 19% |
| ↳ Iterated backtranslation | 11% | 20% | 16% |
| Knowledge distilation      |  0% |  7% | 25% |
| Domain tags                |  4% |  2% |  9% |
| Handling named entities    |  7% |  7% |  0% |
| Multilingual training      |  4% |  7% |  9% |
| Ensembles                  | 67% | 67% | 75% |
| Reranking                  | 41% | 29% | 44% |

Only a minority of teams does some form of pre-training, mostly for
low-resource setups. This is also when the teams hope for multilingual training
to help. (Maybe this changes this year, last year's deadlines were only several
weeks after releasing [mBART](https://arxiv.org/abs/2001.08210).)
Back-translation looks a total must for a submission: it appeared in 94% of the
2020 submission, quite often it was iterated several times. In 2020, people
also started to use tagged back-translation (a neat way how to the model to
distinguish between the synthetic and authentic data).

An interesting trend is that the average vocabulary size decreases. I believe
this is also due to the bigger popularity of low-resource languages where
smaller vocabulary size seems to have some benefits.

![Model types](/assets/MT-Weekly-86/vocab_size.svg)
