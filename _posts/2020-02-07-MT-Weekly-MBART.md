---
layout: post
title: "Machine Translation Weekly 28: mBART – Multilingual Pretraining of Sequence-to-sequence Models"
tags: [mt-weekly, en]
lang: en
---

The trend of model-pretraining and task-specific fine-tuning finally fully hit
machine translation as well. After begin used for some time for unsupervised
machine translation training, at the end of January Facebook published a model,
a pre-trained sequence-to-sequence model for 25 languages at the same time. The
tile of the paper is [Multilingual Denoiseing Pre-training for Neural Machine
Translation](https://arxiv.org/pdf/2001.08210.pdf) and the mode is called
mBART.

![BART](/assets/bart.png)

(This is how I imagine mBART looks like, courtesy of Wikimedia Commons.)

As the paper title suggests, mBART is [a denoising
autoencoder](https://en.wikipedia.org/wiki/Autoencoder#Denoising_autoencoder_(DAE)).
Denoising autoencoders are a rather strange class of models that solve an
artificial task that could be formulated as: imagine someone came, insidiously
messed up your data and you should now reconstruct how they originally looked
like. The reason why someone would do such a strange thing is that this trick
forces the model to learn how the data look and to pick up the regularities in
the data, in other words it is a way of representation learning. In the case of
language, the decoder part needs to know very well how well-formed sentences
look like to reconstruct them from the input noise. The encoder must be capable
of picking up even the weakest clues of what the meaning the noisy input should
be, so it can provide meaningful input to the decoder.

This is exactly what mBART does for 25 languages simultaneously. The model
looks like a standard neural machine translation model with an encoder and a
decoder, just the data is different. It is coherent text in various languages.
The noising procedure is the following:

* Masking out random consecutive segments of the text that form 35% of the
  text.

* Randomly permuting the sentences.

If you want to try out if you can denoise text like mBART, you can <a
href="javascript:noisifyParagraph();">add noise to the next paragraph.</a>

<p id="testParagraph">

<span>From this poor crippled text, the model is supposed to reconstruct the original
text in its full beauty.</span>

<span>As if this task would not be hard enough, mBART needs
to squeeze its knowledge about the languages into a single model (yet with 680M
parameters which is indeed a lot of information) which encourages it to take
into consideration similarities between languages and share as much information
as possible.</span>

<span>The number of sentences spans from 56 million for Gujarati to 55
billion for English.</span>

</p>

<script>

function noisifyParagraph() {
    $("#testParagraph").children().each(function() {
        this.textContent = this.textContent.split(" ").map(
            function (word) {
                if (Math.random() > 0.35) {return word;}
                else {return "[MASK]";}}).join(" ");
    });
    $("#testParagraph").children().sort(function() { return 0.5 - Math.random(); });
}

function noisifySpan(span) {
    console.log(span);
    if (!span.textContent) { return; }
    console.log("I am going to mask.");
}

</script>

Unlike standard neural machine translation models, mBART is explicitly told
what language it should generate by initializing the decoder part with a
language embedding. If you now expect a miracle like giving mBART an English
sentence and telling him to generate in German would give you a good
translation, you will probably be disappointed. You would get a terrible
translation. But even a terrible translation might be a good start.

The paper presents two sets of experiments where they start with mBART and tune
for machine translation. One set of experiments is supervised, the other one is
with unsupervised translation.

The supervised setup is pretty straightforward: take the pre-trained mBART and
continue training on parallel data. The pre-training helped for language pairs
for which there is only a limited amount of parallel data. It seems to help for
language pairs with up to 15 million sentence pairs available.

An immediate objection that should come to your mind is: they just used the
monolingual data at a different stage than usual. If they would have used the
monolingual for generating synthetic data by back-translation (a standard trick
used since 2016), it might be the same. Well, it might, but their experiments
show that it is not. The contribution of pre-training and iterative
back-translation accumulates, so unless you have more than 15 million parallel
sentence pairs, it is totally worth doing both pre-training and
back-translation.

They further tested two setups of fully unsupervised translation. In one setup,
they start with the very poor translation that you get when you feed the model
with a sentence in one language, but tell the model to decode another language.
At first, the translation quality is indeed terrible, but it gets better via
iterative generating synthetic training data with back-translation. The results
are comparable with the state-of-the-art unsupervised MT models. This approach
(although it is not entirely novel, a model called MASS did a very similar
thing already a few months earlier) is more elegant than the pipeline that
starting with bilingual word embeddings, going via statistical MT to neural
models ([see MT Weekly
26](/2020/01/23/MT-Weekly-Unsupervised-Translation.html)) and gets the same or
slightly better results.

Although the fully unsupervised setup is fascinating and theoretically very
interesting, a more practical unsupervised setup is transfer learning when we
have parallel training data for only a related language. The paper shows
experiments with translation into English and the results are very interesting.
For many language pairs, fine-tuning mBART using parallel data only in a
related language can be almost as good using the real parallel data (of course
given that the mBART was pre-trained for all the languages).

The main takeaways of this paper are:

1. The pre-train and fine-tune approach (the new divide and conquer) works can
   also work well in machine translation.

2. The way to go for low-resource languages is probably multi-lingual and
   exploiting related languages.

In other words, even for low-resource languages, high-resource computation
offers a solution—which is good and bad news at the same time. The good news is
that there is a solution for translation of low-resourced languages, the bad
news is that the solution is only available to those who have large
computational resources, which are often unavailable both for universities and
businesses in regions where the low-resource languages are spoken.
