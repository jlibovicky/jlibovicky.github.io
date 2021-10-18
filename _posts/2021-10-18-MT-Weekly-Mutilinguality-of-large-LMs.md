---
layout: post
title: "Machine Translation Weekly 90: The Surprising Multinguality of Large Language Models"
tags: [mt-weekly, en]
lang: en
issue: 90
---

This week, I am going to share my amazement and doubts about what could be
called the surprising multilinguality of large language models. By large
language models, I mean the really large ones that I can hardly run myself,
trained on huge, hardly curated data and thus harbouring the worst societal
demons, but also having many fascinating properties. Here, I would like to
feature three papers that make me think about the properties of the models.

-------------------------------------------------------------------------------

<big><b>1.</b></big> __[Finetuning to other
languages](https://aclanthology.org/2021.findings-acl.74).__ This paper from
the University of Groningen published in the Findings of ACL 2021 shows a
simple way how the English GPT-2 model can be finetuned to other languages.
They do it in two steps: first, they create a vocabulary for the new language
and only learn the embeddings (as if they just replaced the lexicon of
otherwise universal grammar), second, they finetune the rest of the model. The
results are much better than training a model from scratch.

-------------------------------------------------------------------------------

<big><b>2.</b></big> __[Unsupervised
translation](https://arxiv.org/abs/2110.05448).__ The GPT-3 model showed some
ability to do zero-shot or few-shot machine translation, but translation
performance was not that great (although it is still fascinating that it
works). In this recent pre-print by OpenAI, they did the quite obvious thing:
They start with GPT-3 zero-shot capabilities and do iterative back-translation
that is commonly done in unsupervised MT. In this way, there were able to beat
state-of-the-art approaches that rely on multilingual pre-training. On the
other hand, they start with a much larger model and use French as the target
language. I am sure the results would be much worse if they decided to
translate a truly low-resource language, where unsupervised MT is of much
higher value.

-------------------------------------------------------------------------------

<big><b>3.</b></big> __[Few-shot crosslingual
learning](https://arxiv.org/abs/2109.07684).__ In this recent pre-print by
Google Brain, they took the T5 model and GPTNeo (which should be similar or
even better than GPT-3) and tried the few-shot learning setup known from the
GPT-3 paper. The model is given a few examples, how it is supposed to perform a
task (e.g., assigning labels to sentences), then it is given an unlabeled
sentence, and the model is supposed to continue by generating the proper label.
The surprise of this paper is that it works even if the examples are in a
different language than English.

-------------------------------------------------------------------------------

All these results make me wonder if it is possible that with this amount of
parameters and training data, the model learns something fundamental about the
language, something all languages have in common. The first thing that would
come to my mind is of course Chomsky's dreamed-of language device capable of
learning any language, but it would mean admitting that syntactic structures
are more real than the real sentences and that compositionality rules the
world, which is very hard to agree with. But still, can the models learn
something fundamental about the human language? The answer is probably not,
there is probably some simple explanation we are just not aware of, but the
question is still very tempting. Rigorous answering this question is very
difficult.  There are at least two hypotheses that need to be disproved:

<b>Data contamination hypothesis.</b> There are other languages in the training
data.  Perhaps, it learns the other languages from the training data. The GPT-3
paper explicitly admits, there are sentences in other languages, so they can
try zero-shot MT.

_Rejoinder_: Still, the large majority of the data is in
English.  If only a handful of examples can make the models work
cross-lingually does it merely confirm that the models learn something very
general if only a weak training signal can help?

<b>Meta-language hypothesis.</b> This is probably a crazy one. But still, LMs
can [work partially as knowledge bases](https://aclanthology.org/D19-1250/).
Perhaps just talking about languages (the entire Wikipedia is in the training
data) makes the model know plenty of stuff about the languages. Sort of like if
a brilliant person would read the entire Wikipedia and remember everything.
However, remembering the knowledge about language and using the knowledge are
two totally different things, which makes this hypothesis very implausible.

_Rejoinder_: If this hypothesis were true, it would mean we basically have
[AGI](https://en.wikipedia.org/wiki/Artificial_general_intelligence) (which is
very unlikely, though). Who cares about universal language structure, if we
have AGI!

Finding an answer would require careful curation of the training data, which is
hardly feasible in the required amounts. (And those who are interested in large
LMs have the money for that have other priorities.) Also, running the
contrastive experiments would probably require its own power plant, and such
experiments might not be the best use of electrical energy most people can
imagine.
