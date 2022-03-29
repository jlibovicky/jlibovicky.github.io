---
layout: post
title: "Machine Translation Weekly 69: One-Shot learning in MT"
tags: [mt-weekly, en]
lang: en
---

This week I will discuss a paper about the one-shot vocabulary learning
abilities of machine translation. The title of the paper is [Continuous
Learning in Neural Machine Translation using Bilingual
Dictionaries](https://arxiv.org/abs/2102.06558) and will be presented at EACL
in May this year. A very similar idea is also presented in a paper
[Facilitating Terminology Translation with Target Lemma
Annotations](https://arxiv.org/abs/2101.10035) that will be presented at the
same conference.

One-shot learning is the ability to learn from a single example. In the context
of translation, it means the ability to translate a word or an expression once
you are told what the correct translation is or you just look it up in the
dictionary. Because I am a human and not a machine translation system, I was
able to phone my car mechanic that I broke the _Stoßstange_ (the bumper) on my
car because I looked it up in a dictionary without training myself on hundreds
of uses of the word in context. It sounds trivial, but this is something that
current MT models cannot do.

The paper presents a simple and surprisingly efficient solution to this problem
based on data preprocessing. In the training data, less frequent words are
annotated with glosses telling how they should get translated in the target
sentence. (So, the first step of the preprocessing is doing the word alignment
between the source and the target sentences in the training data.) The
low-frequency words are annotated with the aligned words from the target side
(given that they are also in a bilingual dictionary), but not in the form it is
in the target sentence, but with its lemma (= base form). This makes it more
difficult for the system that needs to learn to correctly decline or conjugate
the words to fit the target sentence. On the other, hand it makes the setup
more realistic. (The second pre-processing step is therefore lemmatization of
the entire training data.) And this is basically it, as illustrated in Table 1
of the paper.

![Example of data pre-processing.](/assets/oneshot.png)

A large part of the paper is dedicated to details on how to properly construct
the train and test sets that would show how well the method works. I will not
go into detail here, but it is a sort of surprise to me that proper evaluation
that convincingly shows if the method works or not is actually more complex
than the trick that gives the MT models the new ability. The most tricky part
is showing that the mechanism generalizes for words that were not encountered
in the training data.

One more thing that I would like to comment on in the paper is how the glosses
are segmented. After experimenting with subword and character-level models, the
best solution was to use subwords for everything except for the words that were
subject of the dictionary glossing. These results might give some hints about
the disturbing problem of low generalization of MT systems for morphology.
Although the state-of-the-art models must be aware of morphology to some
extent, they do not generate forms that were not seen in the training data. On
the other hand, the same sequence-to-sequence architectures can be successfully
used for automatic declination of words, so the architecture should not be a
problem. In this clever setup, the models apparently can generate forms that
never appeared in the training data. Maybe it is the subword segmentation that
prevents the generalization and a proper mix of words and character would be
better.

Anyway, to summarize why I think this paper is noteworthy: Enabling using
translation from domain-specific glossaries extends the practical usability of
MT. In my opinion, it makes them 100% more user-friendly for translation
agencies that often use domain/customer-specific glossaries for various
terminologies.
