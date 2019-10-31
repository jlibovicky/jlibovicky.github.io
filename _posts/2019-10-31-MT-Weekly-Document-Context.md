---
layout: post
title: "Machine Translation Weekly 17: When is Document-level Context Useful?"
tags: [mt-weekly, en]
lang: en
---

One of the biggest limitations of current machine translation systems is they
only work with isolated sentences. The systems need to guess when it comes to
phenomena that cross the (often rather arbitrary) sentence boundaries. The
typical example that is mentioned everywhere is the translation of English
pronoun _it_ into languages where everything has grammatical gender, which
might be clear from a broader context, but not within a single English
sentence.

In the last two years, quite a few papers were showed how the document-level
context can be added into an MT system and claimed to make improvements in
translation quality. Earlier this month a paper from the Aachen University
called [When and Why is Document-level Context Useful in Neural Machine
Translation?](https://arxiv.org/pdf/1910.00294.pdf) critically evaluates almost
all the existing approaches and comes to a conclusion that the document-level
models might not be as document-level as their authors claim.

The guys in Aachen took the trouble to re-implemented virtually all approaches
how was document-level MT done so far. In all the approaches, they generate
only one target sentence, however, the input document is used differently.
There are basically two ways:

* Simply concatenate sentences in the source document and feed them into a
single encoder;

* Have a separate encoder for context and for the sentence that should be
translated and combine the states of the encoder in the decoder in different
ways.

Also, the context encoder does not have to be as complicated as the encoder for
the sentence that is actually being translated. As their results show, even
plain word embeddings might be enough.

(My conceited and self-centered comment here is also that they try exactly the
same ways of combining multiple inputs in a Transformer decoder as we did in
[our paper on multi-source MT](https://www.aclweb.org/anthology/W18-6326/) at
WMT18 and they are not citing us.)

They basically confirmed quantitative results of the previous work and achieved
around 1 BLUE point improvement compared to using sentence-level input.
However, they observed that with the length of the context they provide to the
model, the translation quality drops-which is the exact opposite of what you
would expect: having more context should lead to better translation. And they
found a surprisingly simple remedy for that: remove stop words and only keep
content words in the context. It does not affect the overall translation and
makes the translation quality independent of the provided context length.

Already this result suggests that the models do not use the document context in
the way one would expect. If just a bag-of-word representation of a document is
equivalent to full sentences, it raises a strong suspicion that it only uses
the overall topic of the document.

Later in the paper, they conducted a thorough manual analysis of the
improvements the document-context brought when compared to the sentence-level
baseline. Only slightly over 5% of the improvements could be attributed either
to better resolving what pronouns refer to or better lexical choice given the
overall topic of the document. The other changes did not have interpretable
causes.

The conclusion the authors draw from their experiments that the improvements in
the translation quality do not come from utilizing the document context, but
rather from simple regularization effect—in other words, the document context
is a noise that helps to make the model more robust. This is a very similar
conclusion to what researchers in Prague claim about the explicit use of syntax
in the encoder (https://arxiv.org/abs/1910.11218) in a multi-task learning
setup. It seemed to improve the translation quality, but when they tried a
linear chain instead of a real syntax tree, the improvements were the same.

However, I have some doubts about the methodology that was used to asses the
improvements from the document context. They computed TER between the outputs
of the sentence-level and the document-level models and the reference
sentences. TER (Translation Error Rate) is a word-level edit distance between
the sentence, the minimum number of operations of types: insert, delete and
substitute that would transform one sentence into the other. They looked only
on those edit operations that differed in the document- and sentence-level
model outputs and improved the TER score at the same time. Those are the
word-level edits that presumably improve the translation quality. But what if
the document-level model learns to change the structure of the sentences to
better fit the overall topic of the document? I suspect that it would look
exactly the same way what the authors of the paper observed—most of the
word-level changes would not make any sense when taken out of context in this
way.

__BibTeX Reference__
```bibtex
@misc{kim2019documentlevel,
    title={When and Why is Document-level Context Useful in Neural Machine Translation?},
    author={Yunsu Kim and Duc Thanh Tran and Hermann Ney},
    year={2019},
    eprint={1910.00294},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
