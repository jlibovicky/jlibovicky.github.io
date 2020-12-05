---
layout: post
title: "Machine Translation Weekly 61: Decoding and diversity"
tags: [mt-weekly, en]
lang: en
---

This week I will comment on a short paper from Carnegie Mellon University and
Amazon that shows a simple analysis of the diversity of machine translation
outputs. The title of the paper is [Decoding and Diversity in Machine
Translation](https://arxiv.org/abs/2011.13477) and it will be presented at the
[Resistance AI
Workshop](https://sites.google.com/view/resistance-ai-neurips-20/home) at
NeuRIPS 2020 (what a name for a workshop).

The main thing that the paper shows that is the translation quality measured in
terms of BLEU score strongly negatively correlates with some desirable
properties of machine translation that can be described with an umbrella term
output diversity. This is even more disturbing when we take into account that
the systems with high BLEU scores typically end up as indistinguishable from
human translation in the WMT evaluation campaigns, even though the translations
apparently lack properties that are crucial in human translation.

In the first part of the paper, they compare decoding by sampling from the
model with beam search decoding. By sampling, they mean that at every decoding
step, they do not take one best or several best tokens, but rather sample a
random word from the distribution predicted by the model. Because the sampling
leads to worse translation quality, they built another undertrained system that
gets the same BLEU score with beam search as the state-of-the-art system gets
when sampling from the better model. This experiment shows that beam search is
biased towards more frequent personal pronouns and that it performs generally
worse for shorter sentences. I am not sure though, how reliable these results
are because I consider the undertraining as a rather suspicious move.

I liked the second part of the paper much more. They compare different beam
sizes and variants of sampling from the next word distribution with different
hyperparameters and compare the BLEU scores against various other measures:
distributional _n_-gram similarity with authentic human translations, the
proportion of feminine gender pronouns, and success rate of classifiers
guessing if a sentence is machine-generated. The results show that the higher
the BLUE score, the smaller the distributional similarity with authentic
translations. The success rate of the classifier detecting machine-generated
and authentic sentences first decreases and then increases again as the
translations get presumably better. As in the first experiment, a very
unpleasant finding is also that with the increasing BLEU score, the models tend
to be more biased towards more frequent gendered pronouns (which is feminine
pronoun _sie_ in German because the pronoun is used also for the third person
in the plural, and unlike English, gendered pronouns refer not only to persons
but also to general nouns).

In my view, this paper confirms the trend that we can read multiple recent
papers that training the model (and thus obtaining reasonable conditional
distributions for individual tokens) is one problem, and decoding the best
possible sentence using the probabilities if another problem, and apparently a
tough one.
