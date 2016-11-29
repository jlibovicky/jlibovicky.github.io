---
layout: post
title: What is Neural Machine Translation Capable of?
---

A year ago at [EMNLP in Lisbon](http://www.emnlp2015.org/) I saw a paper called
[On Statistical Machine Translation and Translation
Theory](http://www.emnlp2015.org/proceedings/DiscoMT/pdf/DiscoMT22.pdf) by
Christian Hardmeier. He was standing in front of his poster and almost
apologized to everybody who passed by his poster that the poster does not
present any improvements in statistical machine translation — just reflects how
it works with respect to the translation theory. Sadly, this interesting paper
was published at the moment when the statistical translation started to be
replaced by neural models based on deep neural networks. The neural translation
is a big thing now, Google recently announced it is [launching neural systems
in its famous Google
Translate](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html).

In this post, we will have a look at whether and how did the issues from the
paper change by introducing an entirely new class of models.

## Dealing with the Meaning

Traditionally, the translation was understood in terms of meaning equivalence.
A text in a source language has a meaning in that language and we want to
produce a text in a target language that has the same meaning, whatever the
meaning is. If we add the assumption of meaning compositionality — the meaning
of the text arises from aggregating meaning of smaller parts (i.e., word,
colloquial multi-word expressions and idiomatic phrases).

If this was really the case, [the phrase-based statistical machine
translation](https://en.wikipedia.org/wiki/Statistical_machine_translation)
(i.e., the way machine translation has been done until now) would be a probably
the best approach to solve the translation computationally.  Statistical
machine translation works with a notion of word alignment. Huge amounts of
parallel texts are processed with a statistical model that finds out which
phrases from the source language are frequently translated to phrases in the
target language. This is more or less what we call a _translation model_.  The
role of the model in the translation system is to ensure _the linguistic
equivalence_ of the text's phrases.

Statistical systems contain also another model called the _language model_. It
is capable of placing these phrases into a grammatically correct and fluent
sentence. Its role in the system is to do the _compositionality job_.

There is also an alternative, sometimes called _a cultural_ view on the meaning
and consequently on how translation should work. It does it the other way
round. Each text is a potential act of communication. An author of a text is
trying to say something to its readers, to affect the readers somehow. The
text, however, does have a meaning on its own (it is a series of funny pictures
we call the alphabet), it gets its meaning only when somebody reads the text —
and at that very moment, communication is happening. Unlike the independently
existing meaning that is attributed to the words themselves, communication is
always contextual — it happens in the physical, psychological and most
importantly social context — we could even say, it is the reader who ultimately
constructs the meaning. Author's intention either fulfills or not.

Translation itself is a form of communication as well. A translator
communicates what she found in the source language (the meaning arises in the
translator's context) with a text she writes in a target language (the meaning
arises in the final reader's context). Obviously, the statistical translation
does nothing like this — but the neural translation could at least simulate it.

This interesting view on meaning comes from a British philosopher [John
Austin](https://en.wikipedia.org/wiki/J._L._Austin). In his _How to do things
with words_ an influential book from 1955, he introduced viewing all utterances
as acts of communication instead of sentences having truth values.  This way of
thinking also gave birth to [Cultural
Studies](https://en.wikipedia.org/wiki/Cultural_studies) in the 1960's, which
applied these ideas on mass communication.

## Neural Machine Translation is Different

In the statistical translation, the system first guesses some translations of
words and multi-word phrases in the source sentence. In the next step, it tries
to construct a sentence in the target language under many constraints: each
word from the source-language sentence should be translated exactly once; the
phrases in the target langugae should be more or less in the same order as in
the source sentences; it should look as fluent as possible given the language
model; and we could find many other useful constraints. This is how machine
translation worked from the late 1990's until now.

Recently, this has been outperformed by so-called [neural machine
translation](https://en.wikipedia.org/wiki/Neural_machine_translation).  A
source sentence is first encoded into a vector of real numbers by a recurrent
neural network, called _encoder_. It is then used by another recurrent neural
network, a _decoder_ that generates the sentence in the target language. You
can imagine it as one machine that consumes the words of the input sentence and
every time it receives a word, it changes its inner state (a vector of real
numbers). When this is finished, we take this vector and put it into another
machine that outputs words and every time it outputs a word, it changes its
inner state. (In practice, it is more complicated, so called beam search is
used, which we can imagine like running several of these machines in parallel
and always keeping few best incomplete hypotheses and compare them at the end.)
More advanced models are also capable to look how the encoder network
represented the input words and using so called _attention-mechanism_ — it can
focus only on some parts of the input sentence.

![Neural translation animation](/assets/nmt.gif)

While thinking about the neural systems, we can get rid of the notion of
linguistic equivalence and compositionality entirely. The message of the input
sentences is encoded into a numerical representation which is then used to
generate a sentence in target language.

In the previous section, I said that the meaning arises from not only the
sentence itself, but also the context in which it is received. A neural model
can take it into consideration much more easily than the statistical models.
There exist methods that are able to embed a whole text into a real-valued
vector (they are used e.g., for similarity search or sentiment analysis). By
adding this vector on the input of the network, the translation system can get
aware of the linguistic context of the text, from which it can get notion of
the social context. Social groups have their special ways of communication (so
called sociolects), different language is used in different situations. If
there is enough training data, the neural models are certainly able to
distinguish the contexts just by observing the texts which reflect the contexts
as a side effect. In statistical machine translation, it was done by so-called
domain adaptation, there must have been a separate system for each of the
domains (e.g., that you are translation sports news or a text for medical
professionals).

## What is next?

The neural machine translation is a very young method and therefore there is
still a huge room for improvement. Similarly to the previous paradigm, people
come with more and more tricks, how to train the model better and find new ways
how to represent the input. Researchers in machine translation are very
competitive, there is a competition on [Workshop on Machine
Translation](http://www.statmt.org/wmt16/) where the researches introduce their
new cool tricks every year.

Cross-lingual techniques also seem very promising. Google recently published a
[paper on cross-lingual language
representation](https://arxiv.org/abs/1611.04558) that can be used to train
translation for language pairs we do not have much training data for, with the
help other more resource-rich language pairs. Ultimately, all language data can
be used to benefit any translation direction.
