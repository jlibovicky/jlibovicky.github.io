---
layout: post
title: "Machine Translation Weekly 75: Outbound Translation"
tags: [mt-weekly, en]
lang: en
paperTitle: "Backtranslation Feedback Improves User Confidence in MT, Not Quality"
paperAuthors: "Vilém Zouhar, Michal Novák, Matúš Žilinec, Ondřej Bojar, Mateo Obregón, Robin L. Hill, Frédéric Blain, Marina Fomicheva, Lucia Specia, Lisa Yankovskaya"
issue: 75
---

This week, I will comment on a paper by my good old friends from Charles
University in collaboration with the University of Edinburgh, the University of
Sheffield, and the University of Tartu within the [Bergamot
project](https://browser.mt/). The main goal of the project is to develop a
high-quality machine translation that runs locally in an internet browser and
unlike services such as Google Translate or Microsoft Translator does not send
any (potentially sensitive) data to any server. This is a very cool project,
that totally matches my view on what technology deserves public support.
Lowering the technological dependency on big companies and strengthening user
privacy is certainly is totally wort of investing public money.

The paper that I am going to discuss is, however, on a slightly different
topic. Its title is [Backtranslation Feedback Improves User Confidence in MT,
Not Quality](https://arxiv.org/abs/2104.05688) and will be published at this
year's [NAACL](https://2021.naacl.org/). It explores the use case of so-called
outbound translation (a term a never heard before).

The paper distinguishes two use cases for machine translation: one is _inbound_
– into a language the users understand; the other one is _outbound_ –
translation into a language the user does not understand, but their
conversation partner does. In the case of inbound translation, the users are
fully aware that what they see is machine-generated and take what see with a
grain of salt. The outbound setup demands much higher user trust because the
communication partner might misunderstand the message. Image a situation when
you want to discuss details of your holiday accommodation, but you do not speak
the local language. Such a communication situation requires that the users are
totally certain that they wrote they would come on Saturday evening and that
the translator did not confuse it for instance with Sunday afternoon.

The paper presents a user study that evaluates three tools that are supposed to
improve the user trust in the output and the quality of the output. These were:

* Word-level quality estimation;

* Back-translation into the source language;

* Automatic paraphrasing of the input, so the users see some suggestions on how
  the input can be changed.

The paraphrasing tool seems to be rather useless, which is probably no wonder:
the paraphrasing suggestions have nothing to do with translation and I guess
people are smart enough to try several modifications of the input on their own.
The automatic quality estimation was quite useless as well. This is quite
surprising to me. But maybe a better system would help more. However, the
option to try back-translation into the source language increased the
confidence of the users quite a lot. The translation quality on the receiver
side was not affected at all.

The results sound paradoxical a bit. The users do not trust the machine
translation even though, in this sort of everyday communication situation it is
quite reliable. No wonder, everyone has seen machine translation failing
spectacularly many times. A person without large experience with MT has no
reason to believe that in a particular case, it will work fine.
Back-translation might be a good way to show when MT should or should not be
trusted.

The main takeaway of the probably is that think separately about inbound and
outbound use of machine translation and about user trust in these setups. My
personal takeaway is that in many years when traveling will be normal again, I
probably should worry to use MT when planning my next vacation (but maybe at
the time the Corona restriction are gone, MT will be already perfect).
