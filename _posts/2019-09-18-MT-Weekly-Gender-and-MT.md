---
layout: post
title: "Machine Translation Weekly 11: Gender and Machine Translation"
tags: [mt-weekly, en]
lang: en
---

It’s time to talk about gender, why things go wrong with gender in machine
translation and what people do about it. Some languages have gendered nouns
(German), some have gendered almost everything (Czech, French) and some only
few words (English). Let's say you want to translate sentence: “My doctor told
me to stay at home.” into a language that has gendered nouns. A machine
translation system is likely to translate the word “doctor” as a male doctor
because male doctors are just more frequently present in the training data than
female doctors. Machine translation usually works on the sentence level, so
even if the gender is clear from a broader textual context, the system has no
chance to use that context. Until MT systems will not be aware of a broader
context, they just need to guess—and the safest guess is always the most
frequent variety.

Things can get much worse. Let's have a look at what Google Translate does with
the following sentence:

__The doctor asked the nurse to help her in the procedure.__

__English → Czech__
![Lékař požádal zdravotní sestru, aby jí pomohla v tomto
postupu.](/assets/MT-Weekly-11/encs.png)


__English → German__
![Der Arzt bat die Krankenschwester, ihr bei dem Eingriff zu
helfen.](/assets/MT-Weekly-11/ende.png)


__English → French__
![Le médecin a demandé a l'infirmiere de l'aider dans la
procedédure.](/assets/MT-Weekly-11/enfr.png)


The word “doctor” is so heavily associated with the male gender that even in a
sentence where the pronoun “her” clearly indicates that we are talking about a
female doctor, the automatic translation is still “Der Arzt” and “Le médecin”.

Machine translation models learn from authentic data that human society
generates for other purposes than training machine translation. The training
procedure attempts to maximize the probability of the training data given the
model. When looking at the model outputs, it seems that maximizing the
probability of the data involves also making highly stereotypical associations.
This tells, in fact, a sad message about our society.

By the way, if the doctor is pretty, it is suddenly a different story, the
gender gets fixed:

![La jollie médecin a demandé a l'infirmiere de l'aider dans la
procedédure.](/assets/MT-Weekly-11/enfr_pretty.png)

A paper from this year's ACL called [Evaluating Gender Bias in Machine
Translation](https://www.aclweb.org/anthology/P19-1164) shows plenty of such
examples (the one I showed here is kind of  borrowed from the paper) of this
and introduces an evaluation methodology to tackle gender bias in machine
translation. They have data for 8 language pairs and tested them 6 commercial
machine translation systems. All of them appear to be extremely biased.

Given how strongly gender stereotypes are present in texts that people produce,
it makes de-biasing of the models quite a challenging problem. One attempt to
fix this issue is presented in a paper that appeared on arXiv last week and
will be presented at EMNLP later this year. The title of the paper is [Getting
Gender Right in Neural Machine
Translation](https://arxiv.org/pdf/1909.05088.pdf). It works with the Europarl
corpus which consists of the European Parliament proceedings. Because we can
well find out who said what in the parliament, we can also tell what was the
gender of the speaker. If the MT model is trained with this additional
information as the encoder's input, it allows the models to correctly resolve
gendered nouns and pronouns related to the speaker. The obvious drawback of
this method is that it only works for the domain of EU parliamentary addresses,
but with little effort, it is surely applicable for simultaneous interpreting
as well.
