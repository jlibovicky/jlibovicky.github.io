---
layout: post
title: "Machine Translation Weekly 21: Understanding Knowledge Distillation in Non-Autoregressive Machine Translation"
tags: [mt-weekly, en]
lang: en
---

Last week, I discussed a paper claiming that [forward-translation might be a
better data augmentation technique as
back-translation](/2019/11/28/MT-Weekly-Translationese-and-Backtranslation.html).
This week, I will follow with a paper that might touch a similar topic, but in
a slightly different context. The name of the paper is [Understanding Knowledge
Distillation in Non-Autoregressive Machine
Translation](https://arxiv.org/pdf/1911.02727.pdf) and was uploaded to arXiv by
the authors from CMU and Facebook a month ago.

Non-autoregressive models generate the target sentences in a single parallel
step. Standard (i.e., autoregressive) models generate the translation
word-by-word and every word generated is conditioned by the previously
generated ones. In the Transformer architecture, all computations can be
heavily parallelized except for the decoding  (that needs to wait for previous
words) which poses a speed bottleneck. Non-autoregressive models remove this
bottleneck at the expense of the translation quality.

We talk about knowledge distillation when a simpler model (student) is trained
not using real training data, but using outputs of a stronger model (teacher).
Knowledge distillation techniques often use KL-divergence between the teacher
and the student models output distribution as a loss function. In the case of
non-autoregressive machine translation, we use a special case where we want the
student model to generate the same output of the teacher model, regardless of
the probability distribution that was at the output of the model. After all, it
would not make much sense here, because autoregressive models are trained to
model conditional distributions, whereas in the non-autoregressive model
outputs are conditionally independent. In other words, here, knowledge
distillation is the same as data augmentation by forward-translation by Nikolay
Bogoychev and Rico Sennrich that I discussed last week.

The reason why it is discussed in the context of non-autoregressive models is
that knowledge distillation brings large improvements in translation quality.
The paper I am going look into tries to find out why it is the case. So, once
again how does the knowledge distillation work with non-autoregressive models:
first, an autoregressive model is trained and used to translate the source side
of the training data. The training data with the synthetic target side are
then used to train the non-autoregressive model.

The main hypothesis they want to support in the paper is that the knowledge
distillation limits the diversity of the translations and it prevents the
non-autoregressive models from generating inconsistent translation. They call
the diversity multimodality, which seems little misleading to me like there are
modalities other than text (like speech, vision, smell, ...). By that they mean
that the distribution over target sentences has multiple modi (which I believe
should be the correct plural of modus). They hypothesize that autoregressive
models tend to choose one mode consistently. The biggest weakness of the
non-autoregressive models is that often mess up word order and do not cover the
entire source sentence because they chose two mutually inconsistent way of
translation. With [our non-autoregressive models with
CTC](https://www.aclweb.org/anthology/D18-1336.pdf), it often happened that
translation of past sentences into German mixed both German ways of expressing
the past tense (one modifies the verb itself, the other is a combination of an
auxiliary verb and a participle form). If the teacher model is consistent in
this, the student model might not be so confused.

In the paper, they test this hypothesis on an interesting toy experiment. They
train models that translate from English into German, French, and Spanish at
the same time without telling the model what the target language should be -
every English sentence has three different targets in the training data. At
test time, the model picks the target language basically randomly. The result
was that the autoregressive model indeed chose the language randomly, but it
was always very confident about the decisions. The non-autoregressive models
were always very unsure about what target language to chose. They show it on a
cool visualization (distribution over 3 values can be shown as 2D simplex):

![Distributions](/assets/nat_distribution.png)

The first experiment suggests that the outputs of autoregressive models tend to
be structurally consistent. In another experiment, they show that they are also
more lexically consistent. (At least this is my interpretation of the
experiments.) They measure the training data entropy given a word alignment
model fitted on the data. They use a simple probabilistic model that assumes
that every target word was generated from a source word with some probability.
It turns out that the synthetic data have much lower entropy under this model
which again suggest higher consistency

Finally, they do an empirical evaluation that shows that like everything in MT,
neither knowledge distillation has a simple recipe on how to train the best
system. Different teacher models perform differently with different student
models. Nevertheless, the main result is that if we find a correct combination,
a non-autoregressive model might as good an autoregressive one.

Getting back to the last weeks paper, the experiments in this paper might also
be the answer to why forward-translation as a data augmentation technique works
well, given the parent model is good. It might be the bigger consistency
synthetic data that prevents the model from being too distracted by the
variability in the real-world training data.


```bibtex
@article{zhou2019understanding,
  title={Understanding Knowledge Distillation in Non-autoregressive Machine Translation},
  author={Zhou, Chunting and Neubig, Graham and Gu, Jiatao},
  journal={arXiv preprint arXiv:1911.02727},
  year={2019}
}
```
