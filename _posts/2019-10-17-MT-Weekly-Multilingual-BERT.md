---
layout: post
title: "Machine Translation Weekly 15: How Multilingual is Multiligual BERT?"
tags: [mt-weekly, en]
lang: en
---

This week, I will slightly depart from machine translation. I will have a look
at a paper [How Multilingual is Multilingual
BERT](https://www.aclweb.org/anthology/P19-1493/) by Google Research.

[BERT](https://www.aclweb.org/anthology/N19-1423/), the [Sesame Street
muppet](https://en.wikipedia.org/wiki/Bert_(Sesame_Street)) that recently
colonized the whole area of natural language processing is a model trained to
predict missing words in a sentence and decide whether two sentences follow
each other in a sentence. It appears that to do these two tasks, the model
needs to learn a lot about language and store the information in the hidden
states of the model. Because of that, the hidden states of the model can be
used as inputs to different models doing real tasks. The great thing about the
pre-training is that you do not need any special data-only plain text that you
can easily download from the internet.

Multilingual BERT does the same, but the sentences it was trained on come from
104 different (or sometimes not so different) languages. The model is not told
what the language is, it just needs to figure it out on its own.

With such a model, we can do various things. We can use monolingual for
different languages (as for instance in MT evaluation metric
[BERTScore](https://arxiv.org/abs/1904.09675) that I discussed in [one of the
previous posts](/2019/05/01/MT-Weekly-BERTScore.html)) or we can train a single
model capable of doing state-of-the-art morphological and [syntactic analysis
for 75 languages](https://arxiv.org/abs/1904.02099) without telling the model
what language it is processing.

Apparently, multilingual BERT gives is an extremely useful sentence
representation. The question the paper tries to answer is: How is that
happening? Are the languages represented universally, or is every language
represented in its unique way? And disappointingly the answer is that it does
kind of both at the same time.

The paper starts with two sets of experiments. The authors trained models for
named entity recognition (detecting names of people, companies, location, etc.
in a text) and part-of-speech tagging. They always train the model for one
language and test it on the other languages. The results seem pretty good. They
are of course worse than training a language-specific model, but the
performance is reasonable. Or it looks good until you notice that there are
only germanic and romance languages that are all kind of similar to each other
than if we trained on English data and test on Chinese data.

For named entity recognition, a natural objection would that is no wonder it
works, names are spelled almost the same in the languages. The paper explores
also this hypothesis. With no lexical overlap, the F-score is around 40%, with
a high lexical overlap, it goes up to 80%. However, a model trained with
English BERT only gets scores between 0% and 60% depending on the lexical
overlap. It means that to some extent, multilingual BERT only memorizes the
input words, but it also generalizes beyond that.

Now, getting back to the parts of speech. They also conducted experiments with
more dissimilar languages. For instance, a tagger trained for Japanese gets
only 57% accuracy on English data. For comparison: if you remember all
closed-class words where the part of speech is ceratin (pronouns, determines,
prepositions, etc.) and say that remaining words are all nouns, you get 74%
percent accuracy. This raises suspicion, it might be the alphabet that makes
the difference. However, tagger trained for Bulgarian gets 87% on English data
and yet the alphabet is different. Also for Hindi and Urdu, two closely related
languages that use different scripts, the tagger can be easily transferred
without almost any loss in the accuracy.

What actually makes the difference are the typological features of the
languages. It appears that the cross-lingual transfer works much better between
languages having the same subject-verb-object order and the same adjective-noun
order. That actually explains why English and Japanese do not go well together,
rather than the different alphabets.

So in the end, [no alarms and no
surprises](https://www.youtube.com/watch?v=u5CVsCnxyXg). Multilingual BERT does
not represent all languages universally, on the other hand, not entirely
separately because it obviously exploits structural similarities among
languages. Also, it kind of generalizes the input and partially only compresses
what was on the input. It almost seems that whatever dichotomy you can think
of, multilingual BERT does both.
