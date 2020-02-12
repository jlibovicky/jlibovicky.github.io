---
layout: post
title: "Machine Translation Weekly 29: Encode, Tag, Realize - sequence transformation by learned edit operations"
tags: [mt-weekly, en]
lang: en
---

This week I will have a look at a paper from last year's EMNLP that introduces
a relatively simple architecture for sequence generation under the condition
when the target sequence is very similar to the source sequence. The title of
the paper is "[Encode, Tag, Realize: High-Precisions Text
Editing](https://www.aclweb.org/anthology/D19-1510.pdf)" and was written by
authors from Google Research (and was recently also present at [Google AI
Blog](https://ai.googleblog.com/2020/01/encode-tag-and-realize-controllable-and.html)).

There are several natural language processing tasks where you are supposed to
generate some text which is not entirely different from the input. In this
paper, the tasks are text simplification, document summarization (tow tasks
which are obviously interesting for Google's assistant) and grammatical error
correction. For these tasks, we usually use the same models as for machine
translation: encoder-decoder models where the encoder encodes the source
sentence and the decoder generates the target sentence.

The obvious con of these models is that they require large training data
because the decoder basically needs to learn the entire grammar of the language
to generate fluent sentences. Also, these architectures (especially if they are
undertrained) suffer from the hallucination problem when the decoder prefers
fluency of the output at the expense of adequacy.

The approach in this paper is different: they represent the process of sequence
generation as applying edit operation on the source sentence. The basic edit
operations are `KEEP` and `DELETE` and they can be accompanied with n-grams from
vocabulary telling what words should be prepended. This means an extreme
reduction of the vocabulary, the vocabulary does not have to contain words like
_arachnophobia_, it can just say `KEEP` and take care of the rest of the summary
which would be typically playing around pronouns and function words.

How the model works is illustrated in Figure 1 of the paper:

![Model overview](/assets/MT-Weekly-29/overview.png)

An immediate objection when you see the diagram is that it cannot work under
all circumstances and this is indeed a relevent one. With a limited vocabulary,
no all sentence pairs can be encoded like this. In an extreme case, you would
need to delete the whole source sentence and have the entire target sentence in
the vocabulary which is indeed nonsense.

Ideally, we would like to have a small vocabulary that covers all
transformations in training data. It is an optimization problem: for a
vocabulary of 1,000 _n_-grams, find the set of _n_-grams that best covers the
training data. The problem has a name: it is the [Minimum k-union
problem](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.57.9172&rep=rep1&type=pdf)
and it is NP-hard.

Instead of solving the NP-hard problem, the paper proposes a simple heuristic.
For each sentence-pair, they find the longest common subsequence and everything
that is outside the common subsequence into a candidate vocabulary. Then, they
take just the most frequent ones as the model vocabulary. Training examples
that cannot be encoded with the vocabulary are just discarded.

If you are interested in the algorithm that encodes the sentences pairs, into
the tags, have a look at the slideshow:

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ5P0BwfdXKtrk-3oXHWFqzNk4wkueMupD93w4Td_N_SapvDoLY4NOZ-SjNlDBt8Sei3U0Fp7x9gtdF/embed?start=false&loop=true&delayms=1000" frameborder="0" width="700" height="415" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

Now, when we have the sentences encoded, we can start training the tagger. As
an encoder, they use the large version of BERT. The decoder is either one
additional self-attentive layer or a single-layer autoregressive decoder.

The model reaches state-of-the-art results almost all tasks they tried
(sentence fusion, sentence splitting, abstractive summarization) except
grammatical error correction where the best approach includes synthetic data
generation. The results are not dramatically different from training a large
sequence-to-sequence model, the biggest advantage is that that the model works
remarkably well even with relatively small training data. This is well
illustrated in Figure 5 of the paper:

![Model overview](/assets/MT-Weekly-29/curves.png)

Also, it is much faster at inference time because it got rid of the big fat
autoregressive decoder that has many layers and computes an output distribution
over a large vocabulary.

I was quite surprised by the results saying that the non-autoregressive tagger
is much worse than the autoregressive one. The autoregressive decoder
conditions the output on the previously generated outputs. This is indeed a
great advantage when you generate a real sentence. In this case, there is no
really informative grammar in the target symbols. The decoder needs to decipher
what the meaning of the tag is to be able to condition the following tag on the
previous one. This seems to me like a difficult task, but still, this works
even with quite small training data.

The reason why I think the paper is cool is that it presents an approach that
is very affordable because it works with a small amount of training data and
modest resources at inference time. I would very much like to see something
this working for translation of related languages, however, this would require
a better tagging algorithm than relying on the longest common subsequence for
training data preparation.

```bibtex
@inproceedings{malmi-etal-2019-encode,
    title = "Encode, Tag, Realize: High-Precision Text Editing",
    author = "Malmi, Eric  and Krause, Sebastian  and Rothe, Sascha  and Mirylenka, Daniil  and Severyn, Aliaksei",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1510",
    doi = "10.18653/v1/D19-1510",
    pages = "5054--5065",
}
```
