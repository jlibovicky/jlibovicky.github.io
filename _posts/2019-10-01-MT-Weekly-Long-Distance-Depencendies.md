---
layout: post
title: "Machine Translation Weekly 12: Long Distance Dependencies"
tags: [mt-weekly, en]
lang: en
---

Let us follow up on the gender paper and have a look at other cases where
machine translation does not work as well as we would like it to work. This
time, we will have a look at a paper that talks about grammatically complex
sentences that are hindered with (as we say in the linguistic lingo)
long-distance dependencies. The impact of these dependencies on machine
translation is studied in a paper from The Hebrew University of Jerusalem
called [Automatically Extracting Challenge Sets for Non-local Phenomena in
Neural Machine Translation](https://arxiv.org/abs/1909.06814v4) that will
appear at this year's CoNLL (if the situation in Hong Kong will allow
organizing the conference).

One case in which we talk about relations occurs when the grammar of one of the
languages forces words that are next to each other in one language to be
further apart in the other language.

<table align="left" width="100%">
<tr><th>en</th><td>I have to go home by bus at 5 p.m.</td></tr>
<tr><th>de</th><td>Ich muss um 17 Uhr mit dem Bus nach Hause fahren.</td></tr>
</table>

Here, “go” and “fahren” are the same verbs, both in the infinitive, both with a
model verb, but German grammar forces it to be at the of the sentence.

The other type of long-distance dependencies might be only within one language.
Rules of agreement in gender, number or whatever category might be far from
each other. For instance, in Czech, the subject and the predicate might be
quite far from each other, but they still have to agree in number.

<table align="left">

<tr><th>en</th><td>Quagga <b>differed</b> from other zebras mainly in color –
it <b>had</b> the typical stripes on the head and neck only.</td></tr>

<tr><th>cs</th><td>Kvaga se od ostatních zeber <b>lišila</b> především
zbarvením – typické pruhy <b>měla</b> jen na hlavě a krku.</td></tr>

</table>

![Quagga](/assets/quagga.jpg)

Here, in the predicate in the second clause “had” = “měla” depends on the
subject of the first clause which is in the feminine gender. It is not
reflected in the English pronoun “it”, so the decoder needs to somehow remember
the gender of the subject from the first clause.

Long-distance relationships were always a problem for machine translation.
Statistical models operated phrase by phrase and employed a specialized
reordering model that allowed the phrases in the target language to be in a
different order than in the source language. But of course not much – too much
freedom in phrase reordering would lead into a fluent sentence made of
approximately correct words, but with a totally different meaning. It also
posed a problem for recurrent neural networks. They process the input in a
linear order. Resolving a long-distance relationship requires that in every
step network must remember (and copy to the next step) that is still has
something from the past to resolve. Of course, it is not impossible, but it
appears to be hard for the networks to learn.

It may seem that the Transformer model that in principle allows arbitrary
reordering of the information between each layer, so it has even better
theoretical prerequisites to work well in these situations. (So-called
non-autoregressive models show that it really has strong reordering
capabilities.) However, the paper mentioned earlier shows that it does not
learn to do so.

The authors prepared small test sets extracted from existing corpora using an
automatic syntactic analysis and word alignment. Using a set of simple rules,
there extracted hundreds of examples similar to what I showed here.

Although the Transformer is a much better MT model in general, it appears to be
more sensitive to these phenomena that the recurrent models. Nevertheless, both
of them do a terrible job. The higher is the distance between the words that
depend on each other, the worse translation you can expect.

The authors conclude that it means that the models do not learn “structure
underlying the phenomena” – but what they indeed learn it indeed remains a
mystery. For the authors, it means encouragement for “explicit modeling of
linguistic biases” in the NMT models, I am however skeptical, this can really
help. If dependency syntax would be the best way of representing a sentence, we
would certainly already know it. Researches in NLP try to push it everywhere
one way or another. We know that the current architectures are capable of
learning dependency syntax if they are forced to, on the other hand, we also
suspect that the same neural architectures do not internally use the dependency
structure if they do not have to (this is after all the main finding of the
paper that we discuss here). This in my opinions suggest that the correct
(i.e., most useful) structure must be something else.

In the end, the reason why long-distance dependencies pose a problem might be
in some sense similar to the problems of correctly resolving gender in MT. To
resolve the long-distance dependency (which are of course everywhere in the
data), you only rarely need to resolve what is going on as you do when you
analyze the syntax. Most of the cases can be probably resolved with simpler
patterns which the neural networks learns, happily ignoring the rest.
