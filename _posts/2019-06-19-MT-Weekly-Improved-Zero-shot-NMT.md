---
layout: post
title: "Machine Translation Weekly 7: Improved Zero-shot Neural Machine Translation via Ignoring Spurious Correlations"
tags: [mt-weekly, en]
lang: en
---

Remember two years ago when all tech-related servers enthusiastically reported
that a translator by Google created its own language? These were based on a
[paper that was at the end published in
TAACL](https://www.aclweb.org/anthology/Q17-1024) in summer 2017 after its
pre-print was available on arXiv since November 2016.

The paper was about what we call _zero-shot machine translation_. In such a
setup, a single model is trained to be able to translate between many language
pairs. This forces the model to learn to represent the inputs in a
language-agnostic way and allows the model to work for language pairs that were
never seen during training but both the source and the target language are
already well-known to the model. Let's say you have a single model that you
train to translate in both directions between German and English, and between
French and English. If everything goes well, such a model might also be able to
translate between French and German. (Yes, it's fascinating to see something
like this working.)

Back at that time (in 2016), soon after it became clear that neural machine
translation works better than statistical models, I believe most of the
researches thought some kind of zero-shot translation was possible and knew how
they would design their experiments if they had the resources (and nothing else
to do). However, there were only a few places with sufficient resources to
conduct the experiments. If I recall correctly, at that time our department
only had two GPUs (compared to over one hundred right now). Result of the
experiments in the 2016 paper were thus no real surprise for the community. The
translation quality of the zero-shot systems was never better than using
English as a pivot language and was too low for any practical use.  They showed
it was somehow possible but not a breakthrough. Nevertheless, Google did a very
good PR job and newspapers wrote that artificial intelligence created its own
language.

Now, two and half years later, outside the media spotlight, researches from
Facebook AI, New York University and The University of Hong Kong, published a
paper that shows a surprisingly simple way how to make the zero-shot
translation work better than pivoting through English. The paper is called
[Improved Zero-shot Neural Machine Translation via Ignoring Spurious
Correlations](https://arxiv.org/pdf/1906.01181.pdf) and was accepted to this
year's [ACL](http://www.acl2019.org/).

The original Google paper used a special symbol added to the source sentence
that says to which language the sentence should be translated.

```
<2es> How are you? → ¿Cómo estás?
<2fr> How are you? → Comment ça va?
```

Authors of the new paper argue (if I simplify that) that this is not a
particularly good idea because, in the zero-shot setup, the encoder never sees
the combination of the language tag and the source language. The information
about the source language is thus passed as a separate input to the decoder.

Most of the improvement comes from using back-translation. Back-translation is
a technique for training data augmentation by generating synthetic source-side
data using another MT system. It is important that the target data always
consist of authentic sentences, so the decoder does learn to imitate another
decoder, but to imitate real sentences. Back-translation was the key ingredient
in all well-scoring systems at last-year WMT competition. It is also the main
technique allowing low-resource and unsupervised translation when an initially
not really well-performing system is iteratively improved by back-translation
of monolingual text with better and better systems. (It is kind of similar to
how AlphaGo learned to play by playing countless games against itself.)

This paper shows that this technique also fits nicely to the zero-shot
translation. In the first stage, the model is trained only using for the
available language pairs. As in the original Google paper, the model gets a
(surprising and cool) emergent feature that it is able to translate even
between language pairs it never encountered during training. This model is used
to generate synthetic data for unseen language pairs. Finally, the training
continues with a mix of authentic and synthetic data.

The obvious drawback compared to the original Google approach is that for _n_
languages, you need to generate _n_<sup>2</sup> sets of parallel data. However,
it would be also the case when training _n_<sup>2</sup> translation models,
whereas here a single model can be used for multiple language pairs.

