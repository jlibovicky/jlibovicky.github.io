---
layout: post
title: Neural Machine Translation and Translation Theory
---

A year ago at [EMNLP in Lisbon](http://www.emnlp2015.org/) I saw a paper called
[On Statistical Machine Translation and Translation
Theory](http://www.emnlp2015.org/proceedings/DiscoMT/pdf/DiscoMT22.pdf) by
Christian Hardmeier. He was standing in front of his poster and almost
apologized to everybody who stood by his poster that the poster does not
present any improvements in statistical machine translation — just reflects how
it works with respect to the translation theory. Sadly, this interesting paper
was published at the moment when the statistical translation started to be
replaced by neural models. The neural translation is a big thing now, Google
recently announced it is [launching neural systems in its famous Google
Translate](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html).

In this post, we will have a look at whether and how did the issues from the
paper changed by introducing the entirely new class of models.

## Equivalence of Meaning & Cultural Turn

Traditionally, the translation was understood in terms of meaning equivalence.
The text in the source language has a meaning in that language and we want to
produce a text in a target language that has the same meaning, whatever the
meaning is. If we add the assumption of meaning compositionality — the meaning
of the text arises by aggregating meaning of smaller parts (word, colloquial
multi-word depressions, idiomatic phrases).

If this was really the case, the phrase-based statistical machine translation
would be a very suitable approach to solve the translation computationally.
Statistical machine translation works with a notion of word alignment. Huge
corpora of parallel texts are processed with a statistical model that finds out
which phrases from a source language are frequently translated to phrases in
target language. This is more less what we call a _translation model_. The role
of the model in the translation system is to ensure _the linguistic
equivalence_ of the text's phrases.

There is also a different kind of model called a _language model_ — which is
capable placing these phrases into a meaningful and most importantly a fluent
sentence. Its role in the system is to do the _compositionality job_.

There is also an alternative point of view on what the translation sometimes
called _the cultural turn_. Every text is a potential act of communication. Its
author is trying to say something to the readers of the text. Text does have a
meaning on its own, it receives its meaning only when somebody reads the text —
and at that very moment, the communication is happening. Unlike the meaning
that is attributed to the words themselves, communication is always contextual
— it happens in the physical, psychological and most importantly social
context. Translation itself is an of communication. The translator communicates
what he found in the source language with a text he writes in a target
language. Obviously, the statistical translation does nothing like this.

Hardmeier claims this turn happened in the translation theory in the 1990's,
however this important shift in thinking about language happened much earlier.
British philosopher [John Austin](https://en.wikipedia.org/wiki/J._L._Austin)
published his _How to do things with words_ where he introduces exactly this
twist — viewing everything all utterances as acts of communication instead of
sentences having their truth values. This way of thinking also gave birth to
[Cultural Studies](https://en.wikipedia.org/wiki/Cultural_studies) in the
1960's which applied thesese idea on mass communication.

## Neural Machine Translation is Different

In the statistical translation, the translator first finds many possible
equivalents of words and multi-word phrases in the source sentences that was
learned from a corpus and subsequently it tries to construct a sentence in the
target language under many constraints. Each word from the source-language
sentence should be translated exactly once, the phrases in the target should be
more less in the same order as in the source sentences, it should look as fluent
as possible given the language model, and we could find many other useful
constraints. This is how machine translation worked from the late 1990's until
now.

Recently, this has been outperformed by so-called neural machine translation. A
source sentence is first encoded into a vector of real numbers which is then
used by another recurrent neural network that generates the sentence in the
target language. You can image it as a machine that consumes the words of the
source sentence and every time it gets a word, it changes its inner state which
is a vector of real numbers. When we are finished, we take this vector and put
it into another machine that outputs words and every time it outputs a word, it
changes its inner state. More advanced models are also capable to look how the
encoder network represented the input words and using so called
_attention-mechanism_ focus only on some parts of the input sentence.

We can totally get rid of the notion of linguistic equivalence and
compositionality. The message of the input sentences is encoded into a
numerical representation which is then used to generate a sentence in target
language.

In the previous section, I said that a meaning of a sentence is not only the
sentence itself, but also the context in which it is received. A neural model
can take it into consideration much easier than the statistical models.

There exist methods that are able to embed a whole text into a real-valued
vector (they are used e.g., for similarity search or sentiment analysis). In
this way, the translator get aware of the linguistic context of the text, from
which it can get very get notion of the social context. Social groups have
their special ways of communication (so called sociolects), different language
is used in different situations. If there is enough training data, the neural
models are certainly able to distinguish the contexts just by observing the
texts which reflect the contexts as a side effect. In statistical machine
translation, it was done so-called domain adaptation, but you need the domain
in advance (e.g., that you are translation sports news or a text for medical
professionals).

## What is next

There is probably a huge room for improvement in the neural machine
translation. Similarly to the previous paradigm, people come with more ad more
tricks, how to train the model better, find new ways how to represent the
input. Researcher in machine translation are very competitive, there is an
annual competition on [Workshop on Machine
Translation](http://www.statmt.org/wmt16/) where the researches introduce their
new cool tricks every year.

Cross-lingual techniques also seem very promising. Google recently published a
paper on cross-lingual language representation that can be used train
translation for language pairs we do not have much training data for with the
help other more resource-rich language pairs. Ultimately, all language data can
be used to benefit any translation direction.

For further improvement, I believe it necessary to acquire the
context-awareness not from the context reflection hidden in the text. The
computer will need to go out to the world and learn the language there —
experiencing both physical and social context of the language use.
