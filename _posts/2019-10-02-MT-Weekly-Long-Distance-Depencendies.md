---
layout: post
title: "Machine Translation Weekly 12: Long Distance Dependencies"
tags: [mt-weekly, en]
lang: en
---

Let us follow up on the gender paper and have a look at other cases where
machine translation does not work as well as we would like it to work. This
time, we will have a look at a paper that talks about grammatically complex
sentences that contain (as we say in the linguistic lingo) long-distance
dependencies. The impact of these dependencies on machine translation is
studied in a paper from The Hebrew University of Jerusalem called
[Automatically Extracting Challenge Sets for Non-local Phenomena in Neural
Machine Translation](https://arxiv.org/abs/1909.06814v4) that will appear at
this year's CoNLL (if the situation in Hong Kong will allow organizing the
conference).

One case when we talk about relations occurs when the grammar of one of the
languages forces words that are next to each other in one language to be
further apart in the other language.

<table align="left" width="100%">
<tr><th>en</th><td>I <b>have to go</b> home by bus at 5 p.m.</td></tr>
<tr><th>de</th><td>Ich <b>muss</b> um 17 Uhr mit dem Bus nach Hause <b>fahren</b>.</td></tr>
</table>

Here, “go” and “fahren” are the same verbs, but German grammar forces it to be
at the of the sentence.

The other type of long-distance dependencies is monolingual. Grammar rules
often require agreement in gender, number or whatever category of words might
be far from each other.

<table align="left">

<tr><th>en</th><td>Quagga <b>differed</b> from other zebras mainly in color –
it <b>had</b> the typical stripes on the head and neck only.</td></tr>

<tr><th>cs</th><td>Kvaga se od ostatních zeber <b>lišila</b> především
zbarvením – typické pruhy <b>měla</b> jen na hlavě a krku.</td></tr>

</table>

![Quagga](/assets/quagga.jpg)

Here, the predicate in the second clause “had” = “měla” depends on the subject
of the first clause which is in the feminine gender. This is not reflected in
the English pronoun “it”, so the decoder needs to somehow remember the gender
of the subject from the first clause.

Long-distance dependencies were always problematic for machine translation.
Statistical models operated phrase by phrase and employed a specialized
reordering model that allowed the phrases in the target language to be in a
different order than in the source language. It also poses a problem for
recurrent neural networks. They process the input in a linear order. Resolving
a long-distance dependency requires that in every step, the network must
remember (and copy to the next step) that is still has something from the past
to resolve, which appears to be hard for the networks to learn.

It may seem that the Transformer model must have solved this issue. It allows
arbitrary reordering of the information between each of its layers, so it has
even better theoretical prerequisites to work well in these situations.
So-called non-autoregressive models for MT demonstrate that it really has
strong reordering capabilities. However, the paper mentioned earlier shows that
even though the models have the capacity to easily deal with long-distance
dependencies, it just does not learn to do so.

The authors prepared small test sets extracted from existing parallel corpora
using an automatic syntactic analysis and word alignment. Using a set of simple
rules, there extracted hundreds of examples similar to what I showed here.

Although the Transformer is a much better MT model in general compared to
recurrent neural networks, it appears to be more sensitive to long-distance
dependencies. Nevertheless, both of them do a terrible job. The higher is the
distance between the words that depend on each other, the worse translation you
can expect.

The authors conclude that it means that the models do not learn “the structure
underlying the phenomena” – but what they indeed learn remains a mystery. For
the authors, it means encouragement for “explicit modeling of linguistic
biases” in the NMT models by explicitly using dependency syntax while training
the models. I am however skeptical, this can really help. If dependency syntax
was the best way of representing a sentence, we would certainly already
know it. Researches in NLP try to push it everywhere one way or another.
State-of-the-art parsers rely on Transformers, so we know that they are capable
of learning dependency syntax if they are forced to. On the other hand, it is
evident that the same neural architectures do not internally use the dependency
structure if they do not have to (this is after all the main findings of the
paper that we discuss here). This, in my opinion, suggests that the correct
(i.e., most useful for machine translation) structure must be something else.

In the end, the reason why long-distance dependencies pose a problem for
current models might be in some sense similar to the problems of correctly
resolving gender. To resolve the long-distance dependencies (which are of
course everywhere in the data), you only rarely need to resolve what is going
on as you do when you analyze the syntax and draw a dependency tree. Most of
the cases can be probably resolved with simpler patterns.
