---
layout: post
title: "Machine Translation Weekly 1: Bidirectional Decoding"
categories: [MT Weekly]
lang: en
---

This is the first post from a series in which I will try to come up with a
summary some of the latest papers on machine translation or anything new and
interesting in machine translation. The main goal of this exercise is to force
myself to read new papers regularly and not to forget what they were about.

I will start with paper called [_Synchronous Bidirectional Neural Machine
Translation_](https://www.mitpressjournals.org/doi/full/10.1162/tacl_a_00256)
that appeared this week in the [TAACL
journal](https://www.transacl.org/ojs/index.php/tacl).

In the last years, we almost got used to innovations that there is an
innovation that improves machine translation by quite a large margin every
year. After the [attention model](https://arxiv.org/abs/1409.0473) in 2015,
training innovations like [subword
units](https://www.aclweb.org/anthology/P16-1162) and
[back-translation](https://www.aclweb.org/anthology/P16-1009) in 2016, the
[Transformer
model](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf) in
2017, it seemed will be nothing principally new. 2018 brought some [practical
trips](https://arxiv.org/abs/1804.00247) how to train the Transformer model
properly.  It seems to me that is a hot candidate to be the thing that might
survive 2019 and became a part of MT is done. The idea of the paper is very
simple: don't generate the target sentence left-to-right only, do it from both
sides simultaneously.

Alternative ways of decoding the target sentence became relatively frequent.
Last year, there were several papers trying to generate all target words in
parallel and save some decoding time. Earlier this year, there were several
groups that independently came with the idea generate the target sentence in a
random order, so we can generate the easier parts first and thus be more sure
when generating the more difficult parts.

_Synchronous Bidirectional Neural Machine Translation_ returns back to
sequential text generation, but does it from both sides at parallel. It is a
well-known fact for most people working on machine translation that beginnings
of the sentences tend to end up better than what follows. People from the
University of Edinburgh used this observation in their winning submission at
WMT in 2016 when they generated a list of candidate translations using a
left-to-right and re-scored them using a right-to-left model.

This model goes further in this direction. During the standard decoding, a
newly generated word is conditioned on the already generated left context (and
the source sentence). The proposed model uses two decoders working
synchronously. The first decoder conditioned not only on what it previously
decoded but also on the output of the second decoder.

The decoding is shown in the following animation. Circles correspond to words,
arrows capture conditioning.

<img src="/assets/MT-Weekly-1/step0.svg" width="60%" align="center" id="slide" />

<script>
function slideshow() {
    var slide_src = document.getElementById("slide").src;
    var slide_id = parseInt(slide_src[slide_src.length - 5]);
    var next_id = (slide_id + 1) % 10;
    document.getElementById("slide").src = "/assets/MT-Weekly-1/step" + next_id + ".svg";
    setTimeout(slideshow, 2000);
}
setTimeout(slideshow, 2000);
</script>

Although this idea seems very simple, it requires some additional tricks to be
trained properly. If they used ground truth words as simulated outputs of the
other decoder, the only thing the model learned was copying from the other
decoder as much as possible. Instead, they first train two teacher models, one
left-to-right and one right-to-left, and use them while training the
bidirectional model to simulate the decoder running from the other side.

In this way, the decoding takes of course twice as long, which makes is kind of
unsuitable in use cases when the latency is a critical issue. However, the
results look very promising. On the WMT14 data, they report 2 BLEU points
improvement over the state-of-the-art Transformer model (which is quite a lot).
The translation quality of the Transformer model can improve a lot when trained
properly, Martin Popel https://www.aclweb.org/anthology/W18-6424 got another 2
BLEU points with his training technique with iterative back-translation. So,
the main question for this cool new model is, how it will work when combined
with this back-translation tricks.
