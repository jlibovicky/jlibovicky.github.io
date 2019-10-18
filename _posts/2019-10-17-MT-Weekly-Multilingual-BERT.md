---
layout: post
title: "Machine Translation Weekly 15: How Multilingual is Multiligual BERT?"
tags: [mt-weekly, en]
lang: en
---

This week, I will slightly depart from machine translation and have a look at a
paper [How Multilingual is Multilingual
BERT](https://www.aclweb.org/anthology/P19-1493/) by Google Research.

[BERT](https://www.aclweb.org/anthology/N19-1423/), the [Sesame Street
muppet](https://en.wikipedia.org/wiki/Bert_(Sesame_Street)) that recently
colonized the whole area of natural language processing is a model trained to
predict missing words in a sentence and decide whether two sentences follow
each other in a sentence. It appears that to do these two tasks, the model
needs to learn a lot about language and store the information in its hidden
states. Because of that, the hidden states of the model can be used as inputs
to different models doing real tasks. The great thing about the pre-training is
that you do not need any special data—it only needs plain text that you can
easily download from the Internet in huge amounts.

![Training BERT](/assets/bert.svg)

Multilingual BERT does the same, but the sentences it was trained on come from
104 different (or sometimes not so different) languages. The model is not told
what the language is, it just needs to figure it out on its own.

With such a model, people do various things. You can use it monolingually for
different languages (as for instance in MT evaluation metric
[BERTScore](https://arxiv.org/abs/1904.09675) that I discussed in [one of the
previous posts](/2019/05/01/MT-Weekly-BERTScore.html)) or you can train a
single model capable of doing state-of-the-art morphological and [syntactic
analysis for 75 languages](https://arxiv.org/abs/1904.02099) without telling
the model what language it is processing. Sadly, as far as I know, there is no
successful attempt of using multilingual BERT for machine translation.

Apparently, multilingual BERT yields an extremely useful sentence
representation, but actually, we do not know much about it. This paper tries to
shed some light on it and searches for an answer to the following question:
Are the languages represented universally, or is every language represented in
its unique way? (Spoiler: disappointingly, the answer is that it does kind of
both at the same time.)

The paper starts with two sets of experiments. The authors trained models for
named entity recognition (detecting names of people, companies, location, etc.
in a text) and part-of-speech tagging. They always train on model for one
language but test it on the other languages. The results seem pretty good. They
are of course worse than training a language-specific model, but the
performance is reasonable.

You can say it is no wonder that the named-entity recognition works well: names
are spelled almost the same in the languages they experiment with, the model
can only remember how names look like, it does not have to bother at all with
the meaning of the words. In the paper, they try to find out if it is really
the case. They sort the sentences based on the lexical overlap of their
entities with entities in the English sentences. With no lexical overlap, the
recognition F-score is around 40%, with high lexical overlap, it goes up to
80%. However, a model trained with English BERT only gets scores between 0% and
60% depending on the lexical overlap. It means that to some extent,
multilingual BERT only memorizes the input words, but it also very much
generalizes beyond that.

Now, getting back to the parts of speech. The results only look good until you
notice that there are only Germanic and Romance languages that are all kind of
similar to each other. In the paper, they also conducted experiments with more
dissimilar languages. For instance, a tagger trained for Japanese gets only 57%
accuracy on the English data. For comparison: if you enumerate all closed-class
words where the part of speech is certain (pronouns, determines, prepositions,
etc.) and say that remaining words are all nouns, you get 74% percent accuracy
in English. In the case of English and Japanese, the first suspicion you have
is that it might be the alphabet that makes the difference. However, a tagger
trained for Bulgarian gets 87% on English data and yet the alphabet is
different. Also for Hindi and Urdu, two closely related languages that use
different scripts, the tagger can be easily transferred without almost any loss
in the accuracy.

In the end, it seems these are the typological features of the languages that
make the difference. In further experiments, they showed that that the
cross-lingual transfer works much better between languages having the same
subject-verb-object order and the same adjective-noun order. That actually
explains why English and Japanese do not go well together.

So, what is the takeaway from the paper? Multilingual BERT does not represent
all languages universally, on the other hand, not entirely separately because
it obviously exploits structural similarities among languages. Also, it kind of
generalizes the input (in some cross-lingual semantic sense) and partially only
compresses what was on the input. It almost seems that whatever dichotomy you
can think of, multilingual BERT does a little of both. (But isn't that the
reason why it works so well?)

It also might be the answer to why multilingual BERT is not really used for
low-resource or unsupervised machine translation. For that, we would probably
need a representation that is much more cross-lingual and that does not make
differences between languages based on their typological features. You know,
something that is not judging languages just because they have
object-subject-verb word order.

__BibTeX Reference__
```bibtex
@inproceedings{pires2019multilingual,
    title = "How Multilingual is Multilingual {BERT}?",
    author = "Pires, Telmo and Schlinger, Eva and Garrette, Dan",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P19-1493",
    doi = "10.18653/v1/P19-1493",
    pages = "4996--5001"
}
```
