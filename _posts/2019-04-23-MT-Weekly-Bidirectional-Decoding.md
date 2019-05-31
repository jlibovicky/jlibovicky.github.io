---
layout: post
title: "Machine Translation Weekly 1: Bidirectional Decoding"
tags: [mt-weekly, en]
lang: en
---

This is the first post from a series in which I will try to come up with
summaries of some of the latest papers and other news on machine translation.
The main goal of this exercise is to force myself to read new papers regularly
and more importantly not to forget what they were about.

I will start with a paper called [_Synchronous Bidirectional Neural Machine
Translation_](https://www.mitpressjournals.org/doi/full/10.1162/tacl_a_00256)
that appeared this week in the [TAACL
journal](https://www.transacl.org/ojs/index.php/tacl).

In the last few years, we almost got used to that there is an
innovation that improves machine translation by quite a large margin every
year. It was the [attention model](https://arxiv.org/abs/1409.0473) in 2015,
training data processing innovations like [subword
units](https://www.aclweb.org/anthology/P16-1162) and
[back-translation](https://www.aclweb.org/anthology/P16-1009) in 2016, the
game-changing [Transformer
architecture](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)
in 2017. The year 2018 brought some [practical
tips](https://arxiv.org/abs/1804.00247) on how to train the Transformer model
properly, some work on speeding-up the translation, and of course amazing work
on unsupervised MT – but pretty much nothing changed in the good old supervised
MT. This new paper seems to me to be a hot candidate to be an idea that might
survive the year 2019 and became a part of MT best practices. The idea of the
paper is very simple: don't generate the target sentence left-to-right only, do
it from both sides simultaneously.

Alternative ways of decoding the target sentence are among the most popular
topic in MT research these days. Last year, there were several papers on
methods for generating all target words in parallel and thus save some decoding
time. Earlier this year, there were several groups that independently came with
the idea to generate the target sentence in a random order, so they can
generate the easier parts first and thus be more informed when generating the
more difficult parts.

_Synchronous Bidirectional Neural Machine Translation_ returns back to
sequential text generation but does it from left and right at parallel. It is a
well-known fact that beginnings of the sentences tend to end up better than
what follows. Researchers from the University of Edinburgh used this
observation already in their [winning submission at WMT in
2016](https://www.aclweb.org/anthology/W16-2323) when they generated a list of
candidate translations using a left-to-right and re-scored them using a
right-to-left model.

This model presented in this week's paper follows a similar line of thinking.
During the standard left-to-right decoding, a newly generated word is
conditioned on the already generated left context (and of course on the source
sentence). The proposed model uses two decoders working synchronously. The
first decoder is conditioned not only on what it previously decoded but also on
the output of the second decoder.

The decoding is shown in the following animation. Circles correspond to words,
arrows denote conditioning.

<div align="center">
<img src="/assets/MT-Weekly-1/step0.svg" width="60%" align="center" id="slide" />
</div>

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

Although this idea seems very simple, it requires non-trivial tricks to be
trained properly. If ground truth words were used as simulated outputs of the
other-side decoder, the only thing the model would learn would be copying from
the other decoder as much as possible and do nothing on its own. Instead, the
authors first train two teacher models, one left-to-right and one
right-to-left, and use them while training the bidirectional model to simulate
the decoder running from the other side.

Also, the decoding takes of course twice as long, which makes is kind of
unsuitable in use cases when the latency is a critical issue. However, the
improvement in the translation quality looks very promising. On the WMT14 data,
they report 2 BLEU points improvement over the state-of-the-art Transformer
model (which is quite a lot). Since last year, it is obvious that the
translation quality of the standard Transformer model can improve a lot when
trained properly (and for an incredibly long time). The main question for this
cool new model is, how it will work when combined with the training tricks.
