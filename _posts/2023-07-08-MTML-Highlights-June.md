---
layout: post
title: "Highlights from Machine Translation and Multilinguality in June 2023"
tags: [mtml-highlights, en]
lang: en
---

Here are the preprints that I found the most interesting in June 2023.

### [Exploring the Relationship between Alignment and Cross-lingual Transfer in Multilingual Transformers](https://arxiv.org/abs/2306.02790v1)

Folks from LORIA (a French research institute) and Posos (a French company)
study the relationship between cross-lingual representation alignment and
cross-lingual transfer. Here, alignment means what I would call language
neutrality, i.e., that similar sentences should receive similar representation
across languages. (Not alignment as the new word for finetuning language models
to follow instructions, nor the stuff we need to do to prevent AI apocalypse.)

They measure the transfer quality as a relative performance drop across
languages (i.e., the performance in the target language is X points worse than
the source language on task Y). The alignment quality is evaluated using top-1
nearest neighbor retrieval in parallal data (they call it strong alignment if
it is symmetric and weak alignment if it is in at least one direction).
Generally, the transfer quality and (especially strong) alignment quality are
highly correlated across models and languages. Finetuning the models to be more
aligned helps mostly with smaller models. This is an interesting finding
because previous work mainly evaluated bigger models where the effect is not
that large.

### [T3L: Translate-and-Test Transfer Learning for Cross-Lingual Text Classification](https://arxiv.org/abs/2306.04996v1)

A preprint of a paper accepted to TACL from Monash University and the
University of Technology in Sydney studies how far we can get with the
translate-and-test approach for cross-lingual transfer. Translate-and-test is
usually just a fancy name for a two-step pipeline: We have an NLP system that
works in a source language (typically English) that we want to use in a target
language. The translate-and-test approach means that we machine-translate the
target language into English and use the system that we have. It is typically
put into opposition to zero-shot transfer when we finetune a multilingual model
using English (or another source language) training data and use the target
language at inference time.

This paper tries to do the trainslate-test approach within an end-to-end
pipeline. In other words, they connect the machine translation and the
downstream model into a single model and finetune them jointly. They do greedy
decoding on the MT side of the model. Instead of using the decoded tokens
directly (with some trick, such as the Gumble softmax), they use the
probability distributions predicted by the MT model. So, the input of the
task-specific model is not discrete tokens but the entire output distribution
from the model (although conditioned on discrete decoding decisions). It also
has an unpleasant implication that the MT and downstream model need must have
the same vocabulary.

The results presented in the paper look promising: cross-lingual transfer vs.
pipeline; accuracy on XNLI zero shot 62.96% → 67.43%, 10-shot 63.05% → 67.46%.
However, the numbers are quite low compared to what pretty standard models
already achieve.  According to the XTREME paper, the zero-shot transfer with
the vanilla XLM-R has 79.2% accuracy. A preprint [Revisiting Machine
Translation for Cross-lingual Classification](https://arxiv.org/abs/2305.14240)
(that I [highlighted a month ago](/2023/06/08/MTML-Highlights-May.html))
reports, even 84.3 using a translate-and-test pipeline consisting of Meta's
NLLB MT system and RoBERTa.

### [Tokenization with Factorized Subword Encoding](https://arxiv.org/abs/2306.07764)

A paper from the University of Olso that will appear at the upcoming ACL
introduces a new cool way of tokenization for neural models. Instead of
segmenting the text into discrete subword units, they encode words (or actually
any character sequences) into triplets of discrete latent variables, which can
replace the usual token vocabulary. The method saves plenty of parameters for
the embeddings and gets good multilingual performance on Universal
Dependencies, but they lose the transparency that standard subword tokenization
always had.

They use a character-level auto-encoder model that reconstructs the input
string on the character level. It is a Transformer encoder-decoder architecture
(without cross-attention). The encoder has three special tokens at the
beginning. The hidden states corresponding to them get quantized using a
codebook of only 256 tokens using the nearest neighbor search in a codebook.
These tokens are the latent variables from which it should be possible to
decode the original string and that also serve as a replacement for usual
tokenization. This means they always end up with a vocabulary of 3×256 units.
Embeddings of the codebook tokens/centroids are then fed as the first three
tokens of the decoder. They call it a variational autoencoder, which sounds
very fancy, but it is basically _k_-means clustering running simultaneously
with the network training. They also split words into subwords -- which would
not be necessary because they can get the codes for any string. They select the
strings so that the autoencoder can best reconstruct them (with respect to the
likelihood).
