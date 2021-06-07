---
layout: post
title: "Machine Translation Weekly 82: Multimodal Translation and the Visual Context"
tags: [mt-weekly, en]
lang: en
paperTitle: "Good for Misconceived Reasons: An Empirical Revisiting on the Need for Visual Context in Multimodal Machine Translation"
paperAuthors: "Zhiyong Wu, Lingpeng Kong, Wei Bi, Xiang Li, Ben Kao"
issue: 82
---

This week I am going to discuss (and criticize) a paper on multimodal machine
translation that attempts to once again evaluate if and how the visual
information could be useful in machine translation. The title of the paper is
[Good for Misconceived Reasons: An Empirical Revisiting on the Need for Visual
Context in Multimodal Machine Translation](https://arxiv.org/abs/2105.14462),
it has authors from several institutions in China and Hong Kong and will appear
at this year's ACL.

Multimodal machine translation (also, a topic of my dissertation) is defined as
translation of image captions when both the caption text and the image itself
are the input of the translation system. There is a specialized dataset for
that called Multi30k with 30k simple sentences accompanied with images. Over
time, the dataset became too easy from the translation perspective and people
started to suspect that the visual information might be useless for such an
easy translation. After all, there are relatively few cases when the visual
information can really help (mostly gender in the target language and rarely
some ambiguities). Models that claimed to improve translation quality fell
under suspicion of being only regularizers.  The first paper that tried to
resolve this was an [EMNLP 2018 paper by Desmond
Elliott](https://www.aclweb.org/anthology/D18-1329) that introduced adversarial
evaluation: he tried providing the models with incompatible caption-image pairs
and observed if the translation quality drops.  For some models it does (they
indeed use the image), for some it does not. A [paper that got the best-paper
award at NAACL 2019](https://www.aclweb.org/anthology/N19-1422) tested the
models' multimodal capabilities differently: they masked out some input
sentence words and showed that the models were able to get the relevant
information from the image. This shows that the models are in principle
multimodal, but in most cases, it just does not pay off to check the image.

The newest ACL paper claims to develop an interpretable model with a gate
explicitly letting the visual information to the model. The model reaches a
similar improvement in the translation quality as other multimodal models, but
the gate learns to be closed all the time. The adversarial evaluation shows
that the results are only negligibly affected by feeding a different input.
From this, they conclude their models and neither other models (which just
happened not to be that interpretable) do not use the visual information.

Well, I do not think so. The conclusions of the paper are true only for the
particular model it works with – and the model is a particularly bad choice.
This model uses quite a weak image representation. They use a single vector
from pre-trained ResNet. Models that pass the adversarial evaluation use more
informative image features: either image region features from ResNet or
features from object detection models such as Faster R-CNN or YOLO. The history
of multimodal translation is about finding ways how to better represent the
image and how to make the training signal from the image more concentrated
(e.g., by [using deliberating
networks](https://www.aclweb.org/anthology/P19-1653)) to make use of the visual
information. This goes in the opposite direction and indeed the result is that
the visual is that the visual information is not used.

Moreover, the gating model the paper introduces is not the only model that
offers this sort of interpretability. Our [hierarchical attention from
2017](https://www.aclweb.org/anthology/P17-2031) offers the same
interpretability, but unlike the model from this paper, it can work with image
region features and computes the gate specifically for each output word. This
is a screenshot from [my
dissertation](http://ufal.mff.cuni.cz/biblio/attachments/2019-libovicky-p2525377668575645580.pdf)
(Figure 5.3; the first line in the heatmaps is attention to the source
sentences, the second line is the attention to the image):

![Hierarchical attention](/assets/multimodal.png)

It shows that although most of the time, the decoder only attends to the source
sentence, it partially attends to the image when generating nouns. I
believe the reason is that the hierarchical attention uses a more detailed
image representation and a stronger mechanism to obtain information from the
image. If we averaged everything, indeed the weight of the image would be
almost zero. After all, the problem with multimodal translation is to some
extent similar to document-level machine translation. The document-level
context changes the translation in very few places. On average, it is almost
useless, so the model easily learns to ignore it. For me, this paper only shows
that the encoder-decoder model cannot make use of a weak training signal when a
much stronger training signal is present – which is in fact nothing new.
