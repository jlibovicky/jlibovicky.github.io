---
layout: post
title: "Machine Translation Weekly 1: Bidirectional Decoding"
lang: en
---

This is the first post from a series where I will try to come up with a summary
of some of the latest papers on machine translation.

I will start with paper Synchronous Bidirectional Neural Machine Translation
that appeared this week in the TAACL journal.

In the last years, we almost got used to innovations that there is an
innovation that improves machine translation by quite a large margin every
year. After the attention model in 2015, training innovations like subword
units and back-translation in 2016, the Transformer model in 2017, it seemed
will be nothing principally new. This paper, however, seems to be one of those
that really push the translation quality forward and the most stunning thing is
how simple the idea is.

After ideas as generate all target words in parallel and save some decoding
time or generate the target sentence in a random order, this is another idea of
alternative decoding: generate the target sentence left-to-right and
right-to-left simultaneously.

It is a well-known fact for most people working on machine translation that
beginnings of the sentences tend to end up better than what follows. People
from the University of Edinburgh used this observation in their winning
submission at WMT in 2016 when they generated a list of candidate translations
using a left-to-right and re-scored them using a right-to-left model.

This model goes further in this direction. During the standard decoding, a
newly generated word is conditioned on the already generated left context (and
the source sentence). In the proposed model, there two decoders working
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

In this way, the decoding takes of course twice as long, which makes is kind of
unsuitable in use cases when the latency is a critical issue. However, the
results look very promising. On the WMT14 data, they report 2 BLEU points
improvement over the state-of-the-art Transformer model (which is quite a lot).
The translation quality of the Transformer model can improve a lot when trained
properly, Martin Popel https://www.aclweb.org/anthology/W18-6424 got another 2
BLEU points with his training technique with iterative back-translation. So,
the main question for this cool new model is, how it will work when combined
with this back-translation tricks. If it goes well, this paper is a hot
candidate to become a standard model in cases when the latency is not an issue.
