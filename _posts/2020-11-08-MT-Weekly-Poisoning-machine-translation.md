---
layout: post
title: "Machine Translation Weekly 58: Poisoning machine translation"
tags: [mt-weekly, en]
lang: en
---

Today, I am going to talk about a topic that is rather unknown to me: the
safety and vulnerability of machine translation. I will comment on a paper
[Targeted Poisoning Attacks on Black-Box Neural Machine
Translation](https://arxiv.org/pdf/2011.00675.pdf) by authors from the
University of Melbourne and Facebook AI.

The main issue making machine-translation users vulnerable is that they
typically do not understand the target language and do not have any other
choice than trusting the system that target-language output is adequate. Most
machine translation systems are provided as web services, so it seems that the
only one that can manipulate what the system produces is the one who runs the
web service. This is to a large extent true but in this case, the Achilles heel
of the system is the training data and how the training data are collected.

The common way of collecting training data for machine translation is crawling
bilingual web sites. Some tools can identify documents that are mutual
translations of each other and extract so-called parallel sentences. When we
are aware of that, we can try to poison the training data and try to influence
the machine translation. Let's say I do not like Czech prime minister Andrej
Babiš and I would like to cause that translation system would add "incompetent"
in front of his name whenever it appears. One thing I can to create a website
about Czech politics with all articles both in Czech and English—of course with
Andrej Babiš being called incompetent in all the English translations. Now, the
question is: is it possible to influence the translation systems in this way?
This exactly what the paper tries to find out.

In the paper, the translation system is treated as a black box. The authors mix
the artificially created poisoned data into data crawled from the web, then
they run the standard tools for extracting parallel data, and finally, train
the translation system on the data. Then, they evaluate if the data poisoning
has the desired effect on the system outputs.

Long story short: the paper shows, such data poisoning is possible (and for
instance, managed to change German "Flüchtlinge" that should be translated as
"refugees" into "illegal immigrants"). In their experiments, over half of the
poisoned sentences survive standard methods for data filtering and 0.006% of
poisoned data is capable of influencing the translation system to do what the
attacker wants.

Most of the experiments in the paper were done with relatively small training
data. In a large-scale experiment with the winning WMT19 English-to-German
translation system, 4–8k poisoned sentences were enough for a successful
attack. This is indeed only a tiny fraction of the data. The system was trained
on 27.7M authentic parallel sentence pairs and 521M synthetic back-translated
German sentences, but in fact, this quite a lot of text—approximately the
length of the New Testament. Hiding the New Testament inconspicuously between a
much larger amount of standard sentences does not really sound feasible for
high-resource languages. On the other hand, they experiment with phrases that
are fairly frequent in newspaper texts. My guess is that with really infrequent
phrases, the number of poisoned training examples making a difference would be
somewhat smaller.

After reading the paper, I do not think data poisoning is a big danger for
machine translation quality, but especially in low-resource languages, it is
something developers of production systems should keep in mind. A simple remedy
would be only using trusted sources of data, which is however often difficult
without the knowledge of the cultural and political environment of the language
community. This might be perhaps another chance for massively multilingual
models for low-resource languages. Having been trained on much larger data,
they might also be immune to data poisoning.
