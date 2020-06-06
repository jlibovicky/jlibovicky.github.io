---
layout: post
title: "Machine Translation Weekly 42: Unsupervised Multimodal Machine Translation"
tags: [mt-weekly, en]
lang: en
---

Several weeks ago, I discussed a paper that showed [how parallel data between
two languages can be used to improve unsupervised translation between one of
the two languages and a third
one](/2020/02/21/MT-Weekly-Multilingual-View-on-Unsupervised-MT.html). This
week, I will have a look at a similar idea applied in a different context. I am
going to talk about multimodal translation: translation of image captions when
you also have access to the original image. Multimodal translation was my Ph.D.
topic, so I love to read any news from this topic.

In the paper I am going to discuess today, the setup is slightly different: we
have monolingual data in two languages, but in addition to that, we have
captioned images in the languages, but no parallel data. The goal is to learn
to translate between the languages. The title of the paper that attempts to
solve this task is [Unsupervised Multimodal Neural Machine Translation with
Pseudo Visual Pivoting](https://arxiv.org/pdf/2005.03119.pdf), it has authors
from CMU and Monash University and will appear at this year's virtual ACL.

The main idea of the paper following: in the described data setup, we can train
image captioning in both languages. Using the image captioning system, they can
generate synthetic source sentences and use them to train a multimodal
translation system using both image and source sentence as its input.

![Pseudo-Pivoting](/assets/MT-Weekly-42/captioning.svg)

And these translation systems can be used to generate another synthetic data
for standard back-translation (in the paper, they call it quite cryptically
Pivoted Captioning for Back-Translation).

![Backtranslation](/assets/MT-Weekly-42/backtranslation.svg)

And besides, they add a third artificial task to keep everything together. They
want captions of the same image to be translations of each other, i.e., get a
high probability in the translation model (this is called Pivoted Captioning
for Paired-Translation).

![Paired Translation](/assets/MT-Weekly-42/paired_translation.svg)

Everything sounds like a very straightforward application of ideas that are
around for quite a while, but it has a secrete ingredient that makes it work
efficiently. It is the way they represent the image that they call
"Visual-Semantic Embedding". They run an object detector for the images and
represent each object by the penultimate layer of the object detection network.
Then, they learn a projection of the object representations such that hidden
states of the text encoder can be expressed as a linear combination of the
projected object representations.

Compared to the standard unsupervised translation that relies on iterative
back-translation, this way of training improves the translation quality quite a
lot. On the other hand, the standard unsupervised methods are designed to work
with much larger datasets and these data come from a quite narrow domain. When
they integrate this training machinery into a supervised learning setup in
addition to standard training examples, they reach the state-of-the-art
results.

We can of course object, that these results only hold for the Multi30k dataset
that consists mostly of simple sentences that use only concepts that do have a
visual counterpart which is indeed a limited use language. Sentences like: "I
am hungry.", "I cannot have your pain." or "All human beings are born free and
equal in dignity and rights." have no direct visual representation (in the
sense that there is no photograph that could be captioned like this).

However, I believe that being able to ground even the simple concepts in vision
has the potential to help to get truly multilingual language representations.
The famous book [Metaphors we live
by](https://en.wikipedia.org/wiki/Metaphors_We_Live_By) promotes the idea that
all concepts are partially understood in terms of other concepts and ultimately
grounded in basic physical experience. Complex and abstract words are
understood in terms of a more familiar concept that we have more direct
experience with. For instance, a _rational argument_ is partially understood as
a war: you can attack your opponent, partially as a journey: it can lead
nowhere, and partially as other concepts. If we succeed in grounding the basic
concepts in the visual modality in a language-agnostic way, this might be the
representation that we might use to build multilingual models covering even
more abstract corners of human languages.
