---
layout: post
title: "Machine Translation Weekly 80: Deontological ethics and MT"
tags: [mt-weekly, en]
lang: en
paperTitle: "Case Study: Deontological Ethics in NLP"
paperAuthors: "Shrimai Prabhumoye, Brendon Boldt, Ruslan Salakhutdinov, Alan W Black"
issue: 80
---

At this year's NAACL, there will be a paper that tries to view NLP from the
perspective of deontological ethics and promotes an unusual and very insightful
view on NLP ethics. The title of the paper is [Case Study: Deontological Ethics
in NLP](https://arxiv.org/pdf/2010.04658.pdf), it was written by authors from
CMU and discusses several NLP applications from the perspective of
deontological ethics.

Usually, ethics in NLP is discussed from the [consequentialist
perspective](https://en.wikipedia.org/wiki/Consequentialism). In this view, the
morality of an action is determined by its consequences. Consequentialist
ethics considers an action right if it causes as much happiness to as many
people as possible, or negatively defined, the right action minimizes overall
harm. This sounds beautiful in theory, but the problem is how to exactly weigh
the positive and negative consequences of our actions and who can decide that.
(There are famous dilemmas that show how tricky this conception of ethics is,
e.g., the [ticking bomb
scenario](https://en.wikipedia.org/wiki/Ticking_time_bomb_scenario) or the
[trolley problem](https://en.wikipedia.org/wiki/Trolley_problem)).

Most papers (at least the limited amount that I had a chance to read) on NLP
ethics deal with the desirable and undesirable consequences of technology use.
The benefits of the technology are considered self-evident (this is why we work
in the field, we all must know) and possible and actual harms caused by the
technology are begin discussed, classified, quantified, mitigated... This
endeavor has one more unuttered assumption: that we can keep the benefits and
minimize the harms, in other words, secure better consequences of the
technology use.

Deontological ethics considers an action to be right if it follows some rules
that were previously well justified, regardless of the actual consequences. The
most famous concept of deontological ethics is probably Kant's [Categorical
imperative](https://en.wikipedia.org/wiki/Categorical_imperative): _Act only
according to that maxim whereby you can, at the same time, will that it should
become a universal law._ My (certainly very ignorant and barbaric)
interpretation of its justification is that if all people are born equal, no
one is special, nor I am special, therefore I should only what everyone else
should do. People were given reason (which is according to Kant universal),
therefore all must necessarily deduce the set of universally applicable rules.

The NAACL paper uses this type of ethical reasoning and builds the arguments on
two principles: the _generalization principle_ and _respect for autonomy_. The
generalization principle is (in my probably naive perspective) just a variation
on the categorical imperative. A more interesting principle is respect for
autonomy. People who are rational and equal can make decisions autonomously.
Making such decisions requires having all the necessary information. This leads
to the principle of [informed
consent](https://en.wikipedia.org/wiki/Informed_consent), so important in
medical ethics.

One of the NLP applications the paper discusses is machine translation and the
main problem it identifies is the lack of respect to user's autonomy. A usual
MT system generates gets input and generates output and that is all. This might
be fine for a professional translator who uses MT integrated into a translation
management system, but probably not for most common users. It does not tell the
user: Watch out, I translated the "Mr." like this, but this translation might
be inappropriate or impolite in many communication situations in the target
language. It does not ask: My translation makes you sound like a middle-class
middle-aged male person, are you okay with it? It does not warn you: The target
language has gendered nouns, keep in mind that the gender might be wrong in the
translation. In most cases, it does not even provide a reliable quality
estimation and when it does, it does not provide any justification (something
like your dialect or sociolect was not covered well enough by the training
data, the text seems to be from a narrow expert domain, etc.).

After reading this paper I started to think that by only thinking of minimizing
the harms NLP applications can cause, we might miss something important.
Normally, when we say that the models do harmful things (which is a really big
problem), we silently assume that we as a community should solve the problems
(you know, we are computer scientists, we solve problems for a living).
However, by saying this, we say we do not respect the autonomy of the users and
do not plan to give much autonomy to the user. The problem is that applications
are presented to the users as flawless black boxes, something they should
just trust without having a chance to know when and why the application can
manifest harmful behavior. By mitigating biases, covering more dialects,
increasing robustness, making the model culturally neutral, etc., we
certainly make this much better. But we do not give the user autonomy,
almost as if we would be afraid of losing power over the technology users.
