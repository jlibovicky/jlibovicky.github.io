---
layout: post
title: "Machine Translation Weekly 33: Document-level translation via self-fine-tuning"
tags: [mt-weekly, en]
lang: en
---

This week, I will have a look at a recent pre-print that presents an
interesting method for document-level machine translation that is quite
different from all previous ones. The title of the paper [Capturing document
context inside sentence-level neural machine translation models with
self-training](https://arxiv.org/pdf/2003.05259.pdf) and has authors from New
York University and Google DeepMind.

The method that they present is an off-line method: you need to provide the
entire document to the model, then something is happening for quite a long time
and then you get the whole translation at once. First, they translate the
entire document with a model that was trained on sentence-level. The translated
document is then used as training data for fine-tuning the model. This is
iterated several times. At the end of the process, they take the translation of
the document and discard the fine-tuned model. They thus create a
document-specific model but still translate on the sentence level.

They call the method self-training, but I think more accurate would be calling
the trick domain self-adaptation. They report some small BLEU score
improvements, which is what people usually observe when they try to improve
translation using the document-level context. But here, they also present a
thorough user study that shows that the fine-tuned models work better with the
study participants consistently preferring the translations from the
document-specific models.

The interesting question is how does it happen. The information about the topic
of the documents probably gets propagated into the model from the sentences
where it is clear what the document is about. This probably allows
domain-specific translation even in cases when a domain-specific translation is
required, but it is not clear from the source sentence. Here, the necessary
information gets somehow imprinted in the model during the refinement.

I believe that what the current models are missing to achieve good
document-level translation quality is first, being aware of the overall message
of the document (some kind of author's master plan) and second, being able to
track sparse long-distance relations between entities in the document.

Now, the question is: is this approach capable of reaching these goals? Models
that explicitly use the context (like [Doc
Transformer](https://arxiv.org/pdf/1810.03581.pdf)) seem to be in theory
capable of doing both, however, [the
paper](https://arxiv.org/pdf/1910.00294.pdf) that I discussed in [MT Weekly
17](/2019/10/31/MT-Weekly-Document-Context.html) shows that if they only keep
nouns from the context and discard their order, they get the same improvement
as when considering the entire documents. No matter, how complex the
document-context information on the input is, it only considers the nouns.

It thus seems that usual document-level models only do domain adaptation and
help to improve vocabulary consistency. Now, the question is: is this approach
capable of something more than domain adaptation based on the content words
that appear in the text? I would worry that no, that this is only a
computationally more demanding way of doing what document-level translation
always did. With the notable exception that this paper approach does not
require document-level training data.
