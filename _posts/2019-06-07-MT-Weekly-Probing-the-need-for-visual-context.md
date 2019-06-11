---
layout: post
title: "Machine Translation Weekly 6: Probing the Need for Visual Context in Multimodal Machine Translation"
tags: [mt-weekly, en]
lang: en
---

This week, we will have a look at a paper that won [the best short paper award
at NAACL 2019](https://naacl2019.org/blog/best-papers). The name of the paper
is [_Probing the Need for Visual Context in Multimodal Machine
Translation_](https://www.aclweb.org/anthology/N19-1422) and it was written by
friends of mine from Le Mans University and Imperial College of London.

The paper is concerned with multimodal machine translation. It is a task of
translating image captions when having access both to the sentence in the
source language and the image itself. Multimodal translation first appeared as
a shared task at WMT 2016 and was repeated in 2017 and 2018. (Our—Charles
University team participated in all three rounds and multimodal translation
became the topic of my Ph.D. thesis.) During the three years of the
competition, many interesting techniques for multimodal representation fusion
were developed. However, the gains in translation quality were always modest
and it was never completely clear if the translation quality difference is
caused by the multimodal capabilities of the models or by some random
artifacts. Whereas in 2017, the manual evaluation at WMT suggested that
multimodal models are better than their text-only counterparts, in 2018 when
the translation quality was higher in general (thanks to the Transformer
models), there was basically no difference between the text-only and multimodal
models.

The translation quality, however, is not the only thing that people solving the
task are interested in. The main research question behind the task is how to
design deep learning models to be able to consider textual and visual
information simultaneously. It was never evident from the translation quality
whether it happens or not, but the introspection of the attention in the models
suggested that the models indeed take advantage of both modalities.

This paper finally brings a clear quantitative answer to this question. It
introduces a method that fully shows the capabilities of the models for
multimodal translation using a simple but clever idea. The authors conducted
experiments with artificial noise in the source sentences and measured how well
the missing information from the source sentences can be recovered when
different model architectures are used. In particular, they were masking out
(think of BERT, masking out words is obviously popular these days) following
words:

* color adjectives;

* nouns denoting entities in the image; and

* words from the end of the sentence.

In all the experiments, multimodal models (with only small differences among
the multimodal architectures) were able to recover the missing information
using the image, in contrast to the text-only models that do not any other
option that guessing what missing word can be from the textual context.

The most interesting result of the paper is that masking the words during
training also makes the attention over the image much more aware of the objects
in the picture as can be seen in the following visualization.

![attention visualization](/assets/probing_mmt.png)

Isn't it fascinating? Anyway, congratulations to the authors for the fully
deserved best paper award!
