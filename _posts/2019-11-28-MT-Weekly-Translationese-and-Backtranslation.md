---
layout: post
title: "Machine Translation Weekly 21: On Translationese and Back-Translation"
tags: [mt-weekly, en]
lang: en
---

Does WMT speak translationese? And who else speaks translationese? Is the
success of back-translation fake news? These are the questions that implicitly
ask authors of a paper called [Domain, Translationese and Noise in Synthetic
Data for Neural Machine Translation](https://arxiv.org/pdf/1911.03362.pdf) that
was uploaded on arXiv earlier this month.

Translationese is a term by which we mean the language of translation. (At
least in natural language processing, otherwise it is a rather pejorative term
for unnaturally sounding translation.) When someone translates something from
one language into another, the language of the translation is different from
what would a native speaker say if the same text was not a translation. It is
hard to notice for humans, but surprisingly easy to distinguish automatically.
It seems like an innocent fact, but it has tremendous consequences for machine
translation and its evaluation especially when it uses back-translation.

Machine translation is approached basically as a behaviorist simulation. We do
not care what actually translation is or what makes it good—we just want to
learn a process that simulates how people translate and that is it. When people
translate, they by definition translate into translationese. However, when we
use back-translation for training data augmentation, we teach the model to do
something else: translate from (machine-)translationese into the original
language, and funny enough, the standard evaluation datasets tend to reward the
models for doing so.

Back-translation is a technique of generating synthetic training data for
machine translation. When we train a system for translation from $L_1$ into
$L_2$, we can take additional sentences in $L_2$ and use it to better teach the
decoder how authentic sentences in $L_2$ look like. Because we cannot really
train the decoder without the encoder, we need something to feed the encoder
with. We just use automatic translation from $L_2$ to $L_1$. With the synthetic
data, we get a better system that can be in theory used to train even a better
system in the opposite direction… something similar to what AlphaGo did when it
improved by playing Go repeatedly against different versions of itself.

The paper shows that it is far from being as easy as this. (By the way, one of
the authors of this paper is Rico Sennrich, the same guy that introduced
back-translation into MT four years ago.) The output of machine translation
trained on authentic parallel data has similar statistical properties to
translationese. This is shown in the paper by experiments with language
modeling. Translationese sentences are assigned a higher probability by
language models trained on machine-translated sentences. Given that, the
natural question is: wouldn't it be better to generate synthetic target
sentences and train a new model with them?

With what we already know, the main results of the paper pose no surprise, but
first, let me explain how the standard test sets used for the WMT competitions
look like. Since 2015, every test set has 2 parts:

<table align="center" cellspacing="10">
<tr>
    <th>Language <i>L</i><sub>1</sub></th>
    <th>Language <i>L</i><sub>2</sub></th>
</tr>
<tr>
    <td bgcolor="#e6f2ff">News in language <i>L</i><sub>1</sub></td>
    <td bgcolor="#ffe6f2">Translation into <i>L</i><sub>2</sub></td>
</tr>
<tr>
    <td bgcolor="#ffe6f2">Translation into <i>L</i><sub>1</sub></td>
    <td bgcolor="#e6f2ff">News in L2 <i>L</i><sub>2</sub></td>
</tr>
</table>

So, half of the test set is kind of artificially reversed: instead of
translating native sentences, we take translations in $L2$ and try to reversely
translate them into the original native sentences in $L1$, which is obviously
an artificial task.

Models trained with back-translation excel at translating from translationese
into original languages (the artificial scenario), models trained on synthetic
data-target sides are better for translation into translationese (the natural
scenario). The same results got confirmed even in human evaluation. The gain on
the artificial half of the test set is so big that it prevails in the
aggregated results. This is why the research community believed that
back-translation is so great for such a long time.

As the paper further shows, this is only true for high-resource language pairs
where translation quality is high enough from the very beginning.  If the
output of the model is rubbish, something only vaguely related to the source
sentence, it does not make any sense to reinforce the decoder in generating
such sentences and augmenting training data with back-translation give better
results.

Even though the quantitative results are quite convincing, it is still hard for
me to understand, how can the forward-translated synthetic data help so much.
The newly trained decoder only learns to generate what the previous decoder was
generating, and it is the encoder that might get stronger by encountering more
authentic sentences during training. Is the reason that the encoder is
confronted with more authentic source sentences and fewer translationese
sentences? (Because when collecting parallel training data, we do not care
about what the original language was either.) Is thus translationese the new
key term for machine translation? Or do the forward-translated synthetic data
help for a different reason?

__BibTeX Reference__
```bibtex
@article{bogoychev2019domain,
  title={Domain, Translationese and Noise in Synthetic Data for Neural Machine Translation},
  author={Bogoychev, Nikolay and Sennrich, Rico},
  journal={arXiv preprint arXiv:1911.03362},
  year={2019}
}
```
