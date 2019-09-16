---
layout: post
title: "Machine Translation Weekly 11: Gender and Machine Translation"
tags: [mt-weekly, en]
lang: en
---

It's time to talk about gender.  First of all, let's explain what is wrong
about gender in machine translation. Some languages have gendered nouns
(German) or almost everything (Czech, French) and some do not (English). If you
want to translate a sentence like: "My doctor told me to stay at home." the MT
system is very like to translate the sentence as a male doctor because male
doctors are just more frequently present in the training data. Machine
translation usually works on the sentence level, so even if the gender clear
from a broader textual context, the system has no chance to use that context.
Before we will have MT systems that aware of a broader context, the system just
needs to guess. That wouldn't be so bad.

It can get much worse. Let's have a look at what Google Translate does with the
following sentence:

__The doctor asked the nurse to help her in the procedure.__

![Lékař požádal zdravotní sestru, aby jí pomohla v tomto
postupu.](/assets/MT-Weekly-11/encs.png)

![Der Arzt bat die Krankenschwester, ihr bei dem Eingriff zu
helfen.](/assets/MT-Weekly-11/ende.png)

![Le médecin a demandé a l'infirmiere de l'aider dans la
procedédure.](/assets/MT-Weekly-11/enfr.png)

The word "doctor" is heavily associated with male gender that even in a
sentence where the pronoun "her" clearly indicates that we are talking about a
female doctor, the automatic translation is still "Der Arzt" and "Le médecin".

Machine translation model learns from authentic data that our society generates
for different purposes thatn training machine translation. The training
procedure attempts to maximize the probability of the training data given the
model. When looking at the model outputs, it seems that maximizing the
probability of the data involves also making highly stereotypical associations.
This is in fact very said message about our society.

By the way, if the doctor is pretty, it's suddenly a different story:

![La jollie médecin a demandé a l'infirmiere de l'aider dans la
procedédure.](/assets/MT-Weekly-11/enfr.png)

A paper from this year's ACL called [Evaluating Gender Bias in Machine
Translation](https://www.aclweb.org/anthology/P19-1164) shows plenty of such
examples (the one I showed here is actually borrowed from the paper) of this
and introduces an evaluation methodology to tackle gender bias in machine
translation. They have data for 8 language pairs and tested them 6 commercial
machine translation systems. All of them appear to be extremely biased.

Given how strongly the gender stereotypes are present in texts that people
produce, it makes de-biasing of the models quite a challenging problem. One
attempt to fix this issue is presented in a paper that appeared on arXiv last
week and will be published at EMNLP later this year. The title of the paper is
[Getting Gender Right in Neural Machine
Translation](https://arxiv.org/pdf/1909.05088.pdf). It works with the Europarl
corpus which consists of the European Parliament proceedings. Because we can
very well find out who said what in the parliament, we can also tell what was
the gender of the speaker. If the MT model is trained with this additional
information as the encoder's input, it allows the models to correctly resolve
gendered nouns and pronouns related to the speaker. The obvious drawback of
this method is that it only works for the domain of EU parliamentary addresses,
but with little effort, it is surely applicable for online interpreting as
well.
