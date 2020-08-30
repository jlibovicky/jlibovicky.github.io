---
layout: post
title: "Machine Translation Weekly 50: Language-Agnostic Multilingual Representations"
tags: [mt-weekly, en]
lang: en
---

Pre-trained multilingual representations promise to make the current best NLP
model available even for low-resource languages. With a truly language-neutral
pre-trained multilingual representation, we could train a task-specific model
for English (or another language with available training data) and such a model
would work for all languages the representation model can work with.
(Except that by doing so, the models might transfer Western values into
low-resource language applications.)

There are several multilingual contextual embeddings models (such as
[multilingual
BERT](https://github.com/google-research/bert/blob/master/multilingual.md) or
[XLM-R](https://arxiv.org/abs/1911.02116)) covering over one hundred languages
that claim to be capable of being language-neutral enough to work in this
so-called zero-shot learning setup (i.e., a model is trained on one language,
applied on another one). The models are very good indeed, but they are still
quite far from being language neutral. A recent pre-print from the Technical
University Darmstadt and the University of Copenhagen offers several remedies
for that. The title of the paper is [Inducing language-agnostic multilingual
representations](https://arxiv.org/pdf/2008.09112.pdf).

The paper offers three options on how to do that:

* Fine-tune the model on parallel data with an added constraint that matching
  word across languages should receive similar representations. (This requires
  some parallel data for training.)

* Normalize the resulting vectors, in this case using batch-normalization.

* Normalize the input text. (This requires knowing the language identity and
  creating language-specific rules for the text normalization. I am not really
  sure what the takeaways from the experiments should be, so I do not discuss
  it further.)

Both multilingual BERT and XLM-R are trained on monolingual data only. The
pre-training model gets a noisy input with some of the words masked out and it
is supposed to reconstruct what were the words that were masked. There is
actually nothing telling the model that something is the equivalent (or
similar) across languages. When training the models, we silently assume that
given the limited capacity of the model, it is efficient to find patterns with
that repeat and apply across languages and therefore arrive at some common
representation. This, however, only leads to limited language neutrality and
this is what this paper tries to fix by model finetuning.

In the paper, they select two tasks to test out the suggested approaches:
reference-free machine translation evaluation and cross-lingual natural
language inference.

The _reference-free MT evaluation_ is a task of estimating how good machine
translation is without having access to the reference translations. This sounds
similar to MT quality estimation, but surprisingly, it is a different task. All
quality estimation and reference-free evaluation systems can be used for both.
The difference between the tasks is in how these two are evaluated (and what
they are trained for if they are trained). Machine translation evaluation is
evaluated by computing correlation between human judgment about the translation
quality (when the evaluators can check the reference translation), quality
estimation is evaluated by computing a correlation with how many edit
operations are required to post-edit the output sentence to make it correct.

The other task this paper uses to evaluate the language neutrality of the
multilingual representations is _cross-lingual natural language inference_. To
be honest, I do not like this task much. The natural language inference itself
is quite an artificial task. The goal of the task is to say for a pair of
sentences if the second one entails from the first one in a sort of predicate
logic view. For instance a sentence "Three dogs are running on a beach."
entails "There are two dogs on the beach." Technically, it is true, but it is
not how language is usually used, a normal person would react: "No, look, there
are three of them." Therefore, I would worry that representation evaluation
using such a task would prefer representations that do not capture how language
is naturally used. The cross-lingual version of the task is even less natural:
the two sentences are in different languages.

Anyway, back to the paper: it seems that the finetuning on parallel data that
enforces representation similarity of aligned words together with batch
normalization of the output improves the representation language neutrality by
a great deal for both of the tasks. Moreover, the batch normalization and the
finetuning using word alignment seems to be complementary. The use of batch
normalization is quite clever: previous work showed that centered (towards a
language-specific zero mean) representations are more language-neutral.
Finetuning with the batch normalization layer has the same effect, but it no
longer requires knowing the language identity in advance.

One important question that the paper leaves unanswered is how the finetuning
affects the languages that are not in the parallel data for finetuning. Do they
get also represented in a more language-agnostic way? If yes, it would be great
news. Also, it would be interesting to see how much the effect depends on the
size of the parallel data.

Anyway, it is great to see multilingual contextual embeddings getting more
language-neutral. I am really looking forward to seeing the language-neutral
representation applied in zero-shot machine translation (such as any of 100
mBERT languages into English) and unsupervised machine translation.
