---
layout: post
title: "Machine Translation Weekly 96: On Evaluation of Non-Autoregressive MT Systems"
tags: [mt-weekly, en]
lang: en
issue: 96
---

I often review papers on non-autoregressive machine translation a tend the
repeat the same things in my reviews. The papers often compare non-comparable
things to show the non-autoregressive models in a better light. Apart from the
usual flaws in MT evaluation, non-autoregressive papers often (with honorable
exceptions) get lost in the knowledge distillation setup.

In general, papers tend to motivate non-autoregressive MT by potential speedup.
Although it is an important motivation, it is not the main motivation for me.
By attempting to generate sentences non-autoregressively, we acutally ask the
following question: Can we capture the complete target sentence structure
without explicitly modeling it sequentially? Autoregressive decoding seems
quite counter-intuitive to me: like as if I needed to think about what the next
word/syllable/character is after producing the previous one. Generating
utterance in larger "parallel" blocks sounds a little more plausible to me.

Autoregressive decoding is connected with the information-theoretical view of
language. The information theory connects the amount of transmitted information
with the surprisal of the recipient. Communication always happens in time, and
the surprisal, of course, evolves over time too – language is inevitably
temporal. The question is if modeling surprisal over time is something
essential for language modeling or just accidental. In Chomskian linguistics
(that I usually tend to disagree with), the structure is primary and the actual
utterances are only a secondary linearization of something that is in fact a 2D
structure. The possibility of non-autoregressive generation (and its high
quality) might suggest that the surprisal over time fundamental for language as
the Chomskians would prefer. But enough philosophizing...

In practice, non-autoregressive machine translation needs knowledge
distillation to work well. This means that there is an autoregressive teacher
model which is used to translate the training data (the same training data it
was trained on) and the non-autoregressive model is trained on the synthetic
data only. The most frequent speculation why this works so well is that the MT
outputs are more consistent in their choice of vocabulary and structural means.
If there are more options for how to translate something, the MT system just
consistently sticks with one. However, this teacher-student setup is the source
of problems for the evaluation.

In the oldest papers on non-autoregressive MT (including [our 2018
paper](https://aclanthology.org/D18-1336)), the authors used the same data for
training the AR baselines and their NAR counterparts.

![Training without knowledge distilation.](/assets/MT-Weekly-96/no_distil.svg)

This led to comparable models. The non-autoregressive ones were faster, but the
translation quality was tragically bad.

Then the knowledge distillation came to the rescue. Non-autoregressive models
trained on synthetic data are much better. This, however, brought an additional
level of complexity to the evaluation. The papers tend to compare the
autoregressive teacher with the non-autoregressive student model, claiming that
it is almost as good in terms of translation quality, but typically much
faster. This evaluation is not fair.

![Training with knowledge distilation.](/assets/MT-Weekly-96/distil.svg)

The main reason is that the two models are not trained on the same data.  The
only fair comparison would be with an autoregressive model trained on the same
synthetic data. There is a huge speedup potential for the autoregressive models
too if they used the synthetic data, and this cannot be ignored. A fair
comparison would be such a comparison that reaches parity with the
non-autoregressive model: either in translation quality or in decoding time.

The recipe I suggest is training smaller autoregressive student models (perhaps
with deep encoder and shallow encoder, cf. [MT Weekly
45](/2020-06-26-Deep-Encoder-Shallow-Decoder); or use a simple RNN decoder as
[systems in the efficiency
task](http://www.statmt.org/wmt21/pdf/2021.wmt-1.74.pdf) do), trying to reach
either the same translation quality or the same decoding time as the
non-autoregressive model. Once they reach the same translation quality, times
can be compared. Once they reach the same speed, the translation quality can be
compared.
