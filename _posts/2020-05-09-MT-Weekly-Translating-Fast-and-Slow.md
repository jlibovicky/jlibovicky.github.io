---
layout: post
title: "Machine Translation Weekly 41: Translating Fast and Slow"
tags: [mt-weekly, en]
lang: en
---

Recently, I came across a paper that announces a dataset release. The dataset
is called _PuzzLing_ and collects translation puzzles from the international
linguistic olympiad. In machine translation jargon, I would say it provides
extremely small training data to learn how to translate unknown languages.  The
title of the paper is [PuzzLing Machines: A Challenge on Learning From Small
Data](https://arxiv.org/pdf/2004.13161.pdf), it has authors from the Technical
University of Darmstadt and the University of Copenhagen and will be published
on this year's (virtual) [ACL](https://acl2020.org/).

The paper is motivated by a dichotomy between two modes of thought discussed in
[Thinking Fast and Slow](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)
by [Daniel Kahneman](https://en.wikipedia.org/wiki/Daniel_Kahneman), a
best-seller popular book on behavioral psychology. It distinguishes between
System 1 thinking which is fast, instinctive, emotional, based on associations;
and System 2 thinking which is slower, more deliberative, and more rational.
System 2 is more expensive to use and therefore we use it only when necessary.

Current neural networks might do something similar to what the book attributes
to System 1 thinking. We often interpret hidden layer activations as a result
of measuring the similarity of the input with some “prototypes” learned from
the data. This looks pretty much like associative thinking. After dozens of
layers of measuring similarities of similarities (associations of
associations), the networks can do quite complex decisions.

Kahneman's book shows plenty of experiments that supposed to show people often
do not make rational decisions (and by rational, he means that they do not
maximize some utility). Most of the examples were word problems that
included gambling and probabilities. I tend to interpret many of the
examples linguistically as not resolving compositionality in the sentences:
as if the experiment subjects only did some local keyword spotting instead
of proper reading (whatever it is). My private conclusion from this was
that most language understanding can be managed by fast associative
thinking and only occasionally, it requires deeper thinking, and sometimes
people do not really notice they should think slow.

The paper introducing the dataset argues that with the current NLP tasks and
test sets, we cannot say whether our models only simulate capabilities of the
System 1 thinking or if they can things we attribute to System 2 thinking as
well (assuming System 2 thinking is necessary for NLP). To show this, they used
translation puzzles from the International Linguistic Olympiad. In the
Olympiad, the contestants are given a small set of translation examples between
English and some not widely spoken language from the other side of the globe.
They should use the examples to infer regularities in the languages and
translate several other sentences. The examples are chosen such that there are
no obvious analogies (no System 1 thinking), but they should be enough to
uncover some complex underlying rules. We can say they are System-2-only
puzzles.

The authors hope that people will share their assumptions and consider this
task attractive. The other hope is that when solving this toy task, they can
come up with something of general use. I am quite skeptical about this because
I am not really sure if solving this task requires something that is
conceptually necessary for solving some not-so-toy tasks. I cannot think of any
real-world task that would be System-2-only (even AI for solving [Sherlock
Holmes
gamebook](https://en.wikipedia.org/wiki/Sherlock_Holmes:_Consulting_Detective_(gamebook))
is probably not the case).

Do we really need to explicitly simulate System 2 thinking to learn to
translate well? If yes, is there really no workaround? Behavioral psychology
tries to describe how human beings think (or at least how they do some
cognitive tasks). Is there any reason to believe that the findings of
behavioral psychology should provide guidelines on how should computers proceed
when performing similar tasks? After all, airplanes do not fly like birds, why
should computers think fast and slow.

Anyway, I am glad that the dataset was created and I am glad to see the
powerful NLP models to fail on this dataset. It gives the community an
excellent material for discussion whether the System 2 thinking capability is
necessary for NLP models. (And I say probably not.) By the way, what would it
mean if a pre-trained Transformer worked well on this task? Such a discussion
is after all much more interesting than competing who will get more BLEU points
on WMT test sets.
