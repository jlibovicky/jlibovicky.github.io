---
layout: post
title: "Machine Translation Weekly 23: Word Sense Disambiguation in Neural Machine Translation"
tags: [mt-weekly, en]
lang: en
---

This week, I would like to give some thoughts about word senses and
representation contextualization in machine translation.

I will start by explaining why I think the current way of writing about word
senses in NLP is kind of misleading and why I think we should rather talk about
contextualization rather than word sense disambiguation. Then, I will have a
look at a paper that discusses the word-sense disambiguation capabilities of
representations in machine translation and try to interpret it in a slightly
different way than the authors do.

It seems to me that when someone talks about word senses and the need to
disambiguate them, the implicit underlying model of communication is the
following:

* _A_ wants to communicate a precise sense and puts it into a suitable envelope
  and seals the envelope. (The envelope is a word.)

* She does the same with every single word and passes a pile of envelopes (a
  sentence) to _B_.

* _B_ takes the envelopes, which he cannot unseal. He carefully goes over the
  envelopes and based on how all the envelopes look like and how they were
  ordered, he tries to guess what is in the envelopes. For some envelopes, it
  is clear what is inside, for others, an educated guess about the content is
  required.

* _B_ thinks he knows what _A_ wanted to tell him.

The penultimate step is the word sense disambiguation. In the words of this
poor metaphor, my objection is the following: How can _B_ even know something
is in the envelopes? _B_ can know that he puts something in the envelopes, but
how can he know that others do it as well if he cannot unseal the envelopes?
How can he know others put the same things in the envelopes?

The traditional formulation of word-sense disambiguation assumes that sense is
something primary (although not directly observable) and senses are an inherent
property of (or behind) words. Words are then necessarily ambiguous because
multiple senses can be represented by a single word (put in the same envelope).
Unlike words, word senses can never be observed and unlike other theoretical
entities (like elementary particles in physics) you can hardly imagine a
scientific experiment that would prove their existence. Talking about something
that cannot be observed or proved is something researchers should avoid.

Luckily, we can reformulate the thing with word senses in a different way that
eliminates this problem. When words do not have any sense on their own and get
meaning only when _used in context_, it poses no surprise that when used in a
different context, the meaning can be different as well. Word-sense
disambiguation can be reformulated as classifying the (outer) context rather
than a (inner) sense. Classes of (similar and dissimilar) contexts are
something that without doubts exists. Word sense disambiguation is thus giving
interpretable names to distinct classes of contexts in which words can be used.
Disambiguation is contextualization.

This nitpicky theoretical introduction gets me to what I wanted to talk about
today. It is a paper titled [Encoders Help You Disambiguate Word Senses in
Neural Machine Translation](https://www.aclweb.org/anthology/D19-1149.pdf)
published at this year's EMNLP.

It is an exploratory paper that evaluates whether and how hidden states
(internal representations) in neural networks for machine translation are
useful for word-sense disambiguation. Long story short: they are very useful.
Without proper context, the models can guess the sense (= context class) with
accuracy between 63% and 68% when utilizing the internal states, it gets
accuracy between 91% and 97%.

They compared models based on recurrent networks and Transformer architectures
and also two target languages: German and French (with English source because
the word-sense disambiguation data only exist for English). The results show
that translation in German knows more about word senses, perhaps there are more
semantic mismatches between words than between English and French. Also, the
Transformer encoders do a better job than recurrent encoders. If we view the
word sense disambiguation as introducing more context (instead of specifying
the meaning by removing unused sense), this makes perfect sense.

The slightly surprising result of the paper is that representations from the
Transformer decoder perform worse than the encoder. In the paper, they call it
a surprise because they assume word sense must be entirely clear at the end of
the translation process.

I have some doubts about it. First, the experiment seems to be a little
methodologically skewed, because the decoder is provided with the ground-truth
prefix of the target sentence and this target sentence context can clarify what
in what sense the source-sentence word is used (especially when they sum
subword representations), so the accuracy might be overestimated. Second, the
last (the only tested) decoder layer can already live in the world of ambiguous
target language words, so it might be already obfuscated by the target language
ambiguities.

The paper concludes that the hidden states contain information that is useful
for word-sense disambiguation, but I would not be afraid of distilling more
interesting hypotheses from the paper.

If we view word-sense disambiguation as context classification, we can conclude
that the encoder states are better contextualized — managed to gather the
context that is relevant to getting the meaning of the word. The model needs to
do also the reverse process: decontextualize the information to ultimately get
a distribution over (ambiguous if you want) target words. Differences
between the recurrent and Transformer networks only show that the models
learned a different dynamics of contextualizing and decontextualizing the
representation. Since the self-attentive layers consider all possible word
combinations, I believe it is easier for them to do both contextualization
and decontextualization more quickly.

```bibtex
@inproceedings{tang-etal-2019-encoders,
    title = "Encoders Help You Disambiguate Word Senses in Neural Machine Translation",
    author = "Tang, Gongbo and Sennrich, Rico and Nivre, Joakim",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1149",
    doi = "10.18653/v1/D19-1149",
    pages = "1429--1435",
}
```
