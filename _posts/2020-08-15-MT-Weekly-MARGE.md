---
layout: post
title: "Machine Translation Weekly 48: MARGE"
tags: [mt-weekly, en]
lang: en
---

This week, I will comment on a recent pre-print by Facebook AI titled
[Pre-training via Paraphrasing](https://arxiv.org/pdf/2006.15020.pdf). The
paper introduces a model called MARGE (indeed, they want to say it belongs to
the same family as BART by Facebook) that uses a clever way of denoising as a
training objective for the representation.

Most of the currently used pre-trained models are based on some de-noising. We
sample some noise in the input and want the model to get rid of it in the
output. The implicit assumption behind this process is that we believe that the
model needs to learn something about the language to be able to clean out the
noise. In models like BERT or BART, the noise is sort of trivial: we just hide
some parts of the input and want the model to guess what was the part that was
hidden.

MARGE does much more sophisticated stuff. It is a document-level
sequence-to-sequence model. For a document (they say documents, but might more
appropriate to say paragraphs), it uses the representation learned by the
encoder to retrieve similar documents. The retrieved documents are used as an
input to the encoder of the sequence-to-sequence and the decoder is supposed to
predict what was the document used as a retrieval query. As they note in the
paper: it is a chicken-egg problem. You need a reasonable retrieval system to
learn the paraphrasing and you need a good paraphrasing model to learn a
suitable representation for the retrieval.

To my great surprise, the authors did not need to do anything special (at least
how it seems from the paper, in reality, they probably spent days making this
work): even a randomly initialized encoder assigns similar representations to
documents with the same words–and this is enough to start with and the model
gradually in chicken-egg steps converges.

There is a lot of clever engineering to make this beast learning. Doing the
retrieval over a large dataset would be prohibitively expensive. Therefore they
use pre-made clusters of texts (news stories from the same day, sections of the
same Wikipedia articles across languages). They also need to prepare training
data batches in the background based on the current (or only slightly outdated)
encoder weights.

Without further fine-tuning, the model does quite a good job in document
summarization, cross-lingual sentence retrieval, and document-level machine
translation. The paper says it is unsupervised, but I would rather call it
weakly supervised because the training took advantage of prior knowledge about
the texts. When used as an initialization for supervised machine translation,
it seems to perform similarly to BART.

One interesting observation from the training was that the model does not seem
to like multilinguality. (It reminds me when I want to read German Wikipedia to
practice German and end up reading an English or Czech article.) Therefore they
had to artificially boost documents in other languages, but still, the model
seems to prefer to retrieve within a single language. For some reason, this was
especially true for Indo-Iranian languages that got sort of isolated from all
of the others.

### A sidenote on making NLP affordable again

This paper seems to follow the trend that was set up by ELMo and BERT a few
years ago. We need a lot of data, we need strong and expensive hardware and we
need a clever way of getting the knowledge into the model. Models like
[T5](https://arxiv.org/abs/1910.10683) or
[GPT-3](https://arxiv.org/abs/2005.14165) reach improvements by extending the
data and computational power. MARGE chooses to improve the way, the models can
learn from the data and this is certainly a step in a good direction.

[Donald Knuth](https://en.wikiquote.org/wiki/Donald_Knuth) says that understand
something means being able to explain it to the computer. In this sense, we can
say that linguistic fails to fully understand language because when we put our
linguistic knowledge into computer programs, they are never as good as current
deep models.

Strong and appropriate inductive biases (such as space invariance in CNNs in
computer vision, time invariance in speech recognition) are what allow deep
learning models to learn efficiently–but we do not seem to have those in NLP.
So far, every time, we got rid of some assumptions, we achieved better
performance (does not seem to hold for character-level models, though, word and
sub-words might a good inductive bias). This paper is one of the few that adds
assumptions and improve something.

If we want to make NLP affordable again (for small businesses, developing
countries, low-resource languages), we need to explain to the computer how the
language looks like, so we can do the same things with fewer resources. Where
to get those inductive biases if linguistics does not seem to have them? I
don't have a clue.
