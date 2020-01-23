---
layout: post
title: "Machine Translation Weekly 26: Unsupervised Machine Translation"
tags: [mt-weekly, en]
lang: en
---

One of the hottest topics in machine translation and one of the topics I
ignored so far is unsupervised machine translation, i.e., machine translation
trained without the use of any parallel data. I will go through a
seven-month-old paper published at this year's ACL titled [An Effective
Approach to Unsupervised Machine
Translation](https://www.aclweb.org/anthology/P19-1019.pdf) authored by the
[NLP group from the University of the Basque
Country](https://www.ehu.eus/ehusfera/ixa/). It is neither the first paper on
this topic, nor the most innovative, but it presents great results nicely
summarizes what does it mean to build an unsupervised machine translation
system. And because this post is about a complex system, it is a little bit
longer than usual.

Unlike standard machine translation models that are trained using pairs of
sentences where one is a translation of the other, the authors of this paper
used monolingual data only. Still, they were able to train machine translation
systems that performed better than the best systems at WMT 2014 which used over
4.5M parallel sentence pairs at that time. To calm down the optimism, let me
note that the translation was tested only between German and English and French
and English. The languages are culturally quite similar (from the same region,
talking about similar things) and there are waste amounts of data available. It
is thus quite unlikely that something like this would work for instance for
translation between Czech and Nepali.

In the end, their model is a standard neural machine translation model. The
magic is hidden in how the model is trained which is quite a long story. There
are three phases that you need to go through when training an unsupervised
machine translation systems. (At least in this paper, there are also some
alternative approaches.) They are:

1. Training bilingual word and _n_-gram representations;

2. Building a statistical MT system (Yes, the years-ago-death-sentenced
   technology strikes back!);

3. Iteratively learn neural machine translation on back-translations.

The training goes from the word-level, through phrase-level to sentence-level
neural models.

## Training bilingual word representations

The famous [word2vec](https://en.wikipedia.org/wiki/Word2vec) that can embed
words into a meaningful vector space where semantically similar words end up
close to each other is known since 2013. Since then, people came up with better
ways of embedding words, but the principle is still the same. A pretty small
neural network predicts what words are likely to appear in the surrounding of a
word. To do it well, it needs to learn an informative representation of the
word. Because it has limited working space, it poses an advantage for the model
to represent similar words (i.e., words that are used in similar contexts)
similarly.

Later, people also noticed that if we have a bilingual dictionary or parallel
data, we can fit a projection between the embedding spaces using just simple
linear regression. After the projection, words with similar meanings in both
languages end up having similar vectors.

This sounds cool but even cooler is that since 2016 there are methods on
learning such a projection even without a prior dictionary. A small (so-called
seed) dictionary is enough for the beginning and we can then continue with
self-learning. With the first methods, the seed dictionary contained Arabic
numerals which are supposed to have the same meaning in most languages. Later
it showed up that at the beginning, a very approximate dictionary created using
statistical heuristics is enough.

When we a bilingual dictionary (even a low quality), we can fit the regression
between the words in the dictionary. In the next step, when we have the
projection, we can build a new bilingual dictionary based on the better
projection that we just learned. And then, when we have a new better
dictionary, we can fit a new even better projection, use it to get a
dictionary, and so on. At some point, this process converges and we end up with
a pretty good dictionary and projection of the word embeddings into a common
vector space. We can obtain a dictionary simply by searching for nearest
neighbors in the other language.

This is fine, but if we want to build a statistical machine translation system,
we need more than single word translations. We need the translations of entire
phrases. This is surprisingly easy to get. Once we get the word vectors
trained, we can merge words into word _n_-grams and continue training in the
same way, we did before. The model just learns to guess what words are in the
surrounding of an _n_-gram.

## Building a statistical MT system

The first unsupervised machine translation systems in 2017 were based on neural
networks, but their performance was rather poor. This got changed in 2018 when
guys from the University of Basque Country and from Facebook AI independently
used the good old statistical machine translation.

Statistical machine translation decomposes the translation into two independent
components:

* Generating translation candidates, i.e., suggestions on how parts of the
  source sentence can be translated (so-called translation model), and

* Ordering these fragments in such a way that they make a coherent sentence in
  the target language (decoding with a language model).

The language model is needed only for the target language and is trained with
monolingual data only. This is fine for unsupervised translation, this is the
data we have.

The translation model is implemented as a look-up table: for an _n_-gram in the
source language, the system looks up an entry with possible translations in the
target language. These candidate translations used to be extracted from
parallel corpora. This is something unsupervised translation needs to avoid,
and here the bilingual word and _n_-gram vectors come into play — the candidate
translations are simply the nearest neighbors of the representation from the
other language.

If we stopped here, it would be exactly how the best unsupervised systems
looked like in 2018. Back at the time, the unsupervised statistical model
combined these models and continued with iterative back-translation with neural
models. However, this paper from 2019 contains some additional tricks
dramatically improving the translation quality.

One trick seems to help the model a lot is adding another score for the
translation table which is simple [edit
distance](https://en.wikipedia.org/wiki/Edit_distance) (number of edit
operations you need to do to turn one string into another). For rare words and
_n_-grams, the embeddings are more likely to be noisy and unreliable. On the
other hand, rare words are usually proper names and those do not differ much
among languages (if the languages use the same writing system).

During the model tuning, there are three components whose importance weights
need to get estimated:

* phrase similarity in terms of their embedding distance,

* phrase similarity in terms of edit distance, and

* the language model score used during decoding.

Now, how do we tune such a system? In the supervised setup, we take the source
sentences, try to translate them and tweak the weights in such a way that
translation is closer to the reference translations. In unsupervised
translation, there is, of course, no reference translation. However, when we
have two such systems translating in opposite directions, we can use both of
them — translating back and forth should get a sentence as similar as possible
to the source. Of course, the easiest trick on how to do this is not changing
the sentence at all during neither of the translations and score 100%. To
prevent the model from doing such a nasty trick, there is another objective,
the generated sentence must be as probable in the target language model as
possible.

## Neural system and iterative back-translation

Remember how [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo) learned how to
play go by iteratively playing with different versions of itself. Iterative
back-translation is basically the same but in machine translation.

At this stage, we have a pretty decent statistical system that we can use for
generating synthetic source-side data (i.e., back-translate the target side).
We can use the synthetic data to train a model that from a pretty noisy text on
the source side tries to generate fluent text in the target language. This
system can now be used the other way round. The source language will become the
target language in the next iteration. We can again generate noisy translations
of authentic sentences and use them to train another system in the opposite
direction. By iterating this, we can get better and better translation systems
until it converges at some point.

This is it (plus a few tricks I did not mention, plus tricks that might be
missing in the paper), this is how the guys at the University of the Basque
country managed to develop a pretty decent machine translation system that can
translate better than 2014 systems without the use of parallel data.

## What is next

Although this sounds really cool, the method has some problems that cannot be
easily solved. The first one is that such an approach requires a waste amount
of data. If you can obtain billions of sentences in both languages, you can
certainly obtain millions of sentences which are in both languages which are
already enough to train a good supervised system.

There are even more serious issues that cannot be dealt with by some
incremental innovations. The entire method heavily depends on having bilingual
word embeddings. Training the embeddings, however, assumes that people talk
about similar things that are similarly frequently mentioned. This is certainly
true for languages spoken by nations that live next to each other or even in a
single political unit like the European Union. However, it is certainly not
true for linguistically and geographically distant language. So, unsupervised
machine translation between culturally distant languages is a new challenge for
the field.
