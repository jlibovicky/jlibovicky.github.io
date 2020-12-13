---
layout: post
title: "Machine Translation Weekly 62: The EDITOR"
tags: [mt-weekly, en]
lang: en
---

Papers about new models for sequence-to-sequence modeling have always been my
favorite genre. This week I will talk about a model called
[EDITOR](https://arxiv.org/abs/2011.06868) that was introduced in a pre-print
of a paper that will appear in the [TACL
journal](https://transacl.org/index.php/tacl) with authors from the University
of Maryland.

The model is based on the [Levenshtein
Transformer](https://arxiv.org/abs/1905.11006), a partially non-autoregressive
model for sequence-to-sequence learning. Autoregressive models generate the
output left-to-right (or right-to-left), conditioning each step on the
previously generated token. On the other hand, non-autoregressive models assume
the probability of all target tokens is conditionally independent. The
generation can be thus heavily parallelized, which makes it very fast, but the
speed is typically reached at the expense of the translation quality. Getting
reasonable translation quality requires further tricks such as iterative
refinement. So in the end, it is not clear if the performance gains really pay
off when compared to speed-optimized autoregressive models. (But still,
non-autoregressive models are conceptually very interesting and I believe that
ideas from non-autoregressive modeling will play an important role for
document-level translations.)

The Levenshtein Transformer can be viewed as a mixture of both approaches.
Output tokens are generated sort of in parallel—but at the same time, they are
conditioned on the previously generated tokens. When generating a target
sequence, the Levenshtein Transformer starts with an empty sequence `<s> </s>`,
and using insert and delete operations, it improves the output. It is trained
using imitation learning with an oracle policy defined by the optimal sequence
of edit operations in Levenshtein distance (given that substitution is not
allowed). It means that the first step is basically the standard
non-autoregressive machine translation. In the next iteration, deletion and
insertion operations are applied to improve the first translation that
sufferers mostly with fluency problems, and more iterations are possible.
Levenshtein Transformer matches the translation quality of autoregressive
models while still offering some speed-up.

EDITOR is very similar to Levenshtein Transformer. The main difference is that
the EDITOR uses a different set of edit operations. Instead of deletion, EDITOR
uses a rather unintuitive operation of  _reposition_. Here, reposition means
that we take a token and move it to a different place, and rewrite the original
one. In other words, the only way of deleting a token is to replace it with
another one that already exists in the output. The reason for introducing such
an operation is that it can be well used for inducing lexical constraints in
the translation. For instance, based on a domain-specific glossary, we would
like some terms to appear in the target sentence. Instead of starting with an
empty sequence, we can start with the words that we would like to have in the
target sentence and let the model do the rest. As with the more standard
deletion and insertion operations, the optimal sequence of operations can be
computed using the dynamic-programming [Wagner-Fisher
algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm).

In general, the translation quality and speed are approximately the same as
with the Levenstein Transformer. However, because deleting tokens is not as
simple in the EDITOR, it works better for translation with lexical constraints
with faster decoding than with standard autoregressive models. The translation
quality with the lexical constraints is still better than with a method called
[Dynamic Beam Allocation](https://www.aclweb.org/anthology/N18-1119), which is
on the other hand rather slow at the inference time.

![Decoding with lexical constraints](/assets/editor.png)

How the model works can be best seen in Figure 7 of the paper. The model was
asked to use the words “_faith_”, “_Stephen_”, and “_think_” in a sentence. In
the first step, the Levenshtein Transformer decides not to delete anything,
EDITOR mutually repositions “_faith_” and “_think_”, so nothing gets deleted
and the words are swapped. In the next step, both models generate placeholders
where new tokes can be inserted. In the third step, tokens are inserted at the
places of the placeholders.

I like the model non only because I have a soft spot for the dynamic
programming algorithm incorporated in neural models. I believe this model will
find use in several applications beyond machine translation, such as natural
language generation in dialog systems or automatic paraphrasing.
