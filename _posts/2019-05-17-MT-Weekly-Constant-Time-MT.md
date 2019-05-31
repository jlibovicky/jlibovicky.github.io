---
layout: post
title: "Machine Translation Weekly 3: Constant-Time Machine Translation with Conditional Masked Language Models"
tags: [mt-weekly, en]
lang: en
---

This week, we will have a look at a brand-new method for non-autoregressive
machine translation published [a few weeks ago on
arXiv](https://arxiv.org/pdf/1904.09324.pdf) by [Facebook AI
Research](https://research.fb.com/category/facebook-ai-research/), two days
before the anonymity period for [the EMNLP
conference](https://www.emnlp-ijcnlp2019.org/).

Most models for neural machine translation work autoregressively. When the
model outputs a word, its decision is always conditioned on what words were
generated previously. One of the pros of this approach is that it ensures the
generated sentences are coherent. On the other hand, it limits to what extent
the computation can be parallelized because each word can be produced only
after the previous ones were generated.

Last year, there were several attempts to come up with non-autoregressive
models which proceed in parallel and generate all target words at once. The
models usually reach 200–300% speedup at the cost of a significant drop in
translation quality. This new paper called [_Constant-Time Machine Translation
with Conditional Masked Language Models_](https://arxiv.org/pdf/1904.09324.pdf)
manages to keep the same speedup, however, it narrows the quality gap from the
autoregressive model to 5–10%.

The model borrows the idea of masked language modeling from [_BERT_, a general
sentence representation model](https://arxiv.org/pdf/1810.04805.pdf). In BERT,
a neural network is taught to guess what words were masked-out in the input.
The network is thus forced “comprehend” (whatever it means) the rest of the
sentence in such a way, it can guess what word is missing. And this is exactly
what this translation model is trained to do as well.

As the first step, the model encodes the source sentence in the same way the
standard MT models do. It also uses the source sentence representation to
estimate the target sentence length. (Like others, they just do classification
and treat all possible lengths as _independent_, which for some weird reason
works better than regression.) This estimate is used to generate a fully masked
target sentence (i.e., only a sequence of blank symbols) which is the input to
the decoder in its first iteration.

As in BERT, the decoder is a stack of Transformer layers that attend to the
masked input. But unlike BERT (and like decoders in MT) it also attends to the
source sentence representation from the encoder. Because everything can be
computed in parallel, the decoder generates a sequence of output words in
asymptotically constant time.

<div align="center">
<img src="/assets/MT-Weekly-3/step00.svg" id="slide" />
</div>

<script>
Number.prototype.pad = function(size) {
    var s = String(this);
    while (s.length < (size || 2)) {s = "0" + s;}
    return s;
}

function slideshow() {
    var slide_src = document.getElementById("slide").src;
	var slide_id_str = slide_src[slide_src.length - 6] + slide_src[slide_src.length - 5];
    var slide_id = parseInt(slide_src[slide_src.length - 6] + slide_src[slide_src.length - 5]);
    var next_id = (slide_id + 1) % 16;
    document.getElementById("slide").src = "/assets/MT-Weekly-3/step" + next_id.pad(2) + ".svg";
    setTimeout(slideshow, 2000);
}
setTimeout(slideshow, 2000);
</script>

Words generated with the lowest probability are masked out and the output is
used as an input to the decoder in the next step. The mask-out words are
replaced by more fine-grained estimates. The paper suggests repeating this 10
times. My guess is that more iterations only slow down the computation and do
not further improve the translation quality.

This is an example (page 3, Figure 1) from the paper (examples in papers always
carefully cherry-picked, but maybe I'm just judging others by my own standards)
which shows how the translation gets gradually improved during the iterations.

![Paper example](/assets/constant_time.png)

The authors used another trick to deal with the target length estimate. A prior
estimate of how long the target sentence will be is quite a difficult task.
(Would you be able to say, how many words you will say in a sentence before you
start to write down any words? Me certainly not.) This is, in fact, the
Achilles heel of all non-autoregressive models. In this paper, they just try
several possible target sentence lengths and simply chose the one yields the
best result. Because all of them can be explored in parallel, it only means a
negligible delay.
