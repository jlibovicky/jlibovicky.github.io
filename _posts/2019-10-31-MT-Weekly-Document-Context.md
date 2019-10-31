---
layout: post
title: "Machine Translation Weekly 17: When is Document-Level Context Useful?"
tags: [mt-weekly, en]
lang: en
---

One of the biggest limitations of current machine translation systems is they
only work with isolated sentences. The systems need to guess when it comes to
phenomena that cross the (often rather arbitrary) sentence boundaries. The
typical example that is mentioned everywhere is the translation of English
pronoun _“it”_ into languages grammatical gender. The gender might be clear from
a broader context, but not within a single English sentence.

Let's make a short sad story about a turtle:

|:--------------------------|-------------------------------------|
|__Document context__      | When I was a kid, I had __a turtle__.  One afternoon, I took __it__ for a walk. |
|__Sentence to translate__ |  __It__ ran away and I never saw __it__ again. |

In Czech, a turtle is _želva_ which is feminine (die Schildkröte, la tortue, la
tartague, черепа́ха—they are also feminine gender). Therefore, _“it”_ needs to
be translated as _“she_“ or _“her_“, but the information is only in the first
sentence.

In the last two years, quite a few papers showed how the document-level context
can be added into an MT system and to slightly improve the translation quality.
Earlier this month a paper from the Aachen University named [When and Why is
Document-level Context Useful in Neural Machine
Translation?](https://arxiv.org/pdf/1910.00294.pdf) critically evaluated almost
all the existing approaches and came to the conclusion that the document-level
models might not be as document-level as their authors claim.

The guys in Aachen took the trouble to re-implemented virtually all approaches
how was document-level MT done so far. In all the approaches, they generate
only one target sentence, however, the input is the entire document.  There are
basically two ways how to do it:

* Simply concatenate sentences in the source document and feed them into
  a single encoder and only translate the final sentence;

* Have a separate encoder for the context and for the sentence that should be
  translated and combine the states of the encoders later when decoding. There
  are of course different how to do it.

The context encoder does not have to be as complicated as the encoder for the
sentence that is actually being translated. As their results show, even plain
word embeddings might be enough.

(My conceited and self-centered comment here is also that they try exactly the
same ways of combining multiple inputs in a Transformer decoder as we did in
[our paper on multi-source MT](https://www.aclweb.org/anthology/W18-6326/) at
WMT18 and they are not citing us.)

They basically confirmed the quantitative results of the previous work and
achieved around 1 BLUE point improvement compared to using sentence-level
input. However, they observed that with the length of the context they provide
to the model, the translation quality drops—which is the exact opposite of what
you would expect: having more context should lead to better translation. And
they found a surprisingly simple remedy for that: remove stop words and only
keep content words in the context. It does not affect the overall translation
and makes the translation quality independent of the provided context length.

Our sad story about the turtle will turn into something like this:

|--------------------------|---------------------------------------|
|__Document context__      | kid turtle afternoon walk             |
|__Sentence to translate__ | It ran away and I never saw it again. |

Already this result suggests that the models do not use the document context in
the way one would expect. After all, how would the system recognize that the
_“it”_ refers to the _“turtle”_ and not, for instance, to the _“afternoon”_? If
just a bag-of-word representation of a document is equivalent to full
sentences, it raises a strong suspicion that it only uses the overall topic of
the document.

Later in the paper, they conducted a manual analysis of the improvements the
document-context brought when compared to the sentence-level baseline.
According to their results, only slightly over 5% of the improvements could be
attributed either to better resolving what pronouns refer to or to a more
adequate lexical choice given the overall topic of the document. The other
changes did not have interpretable causes according to the authors.

The conclusion the authors draw from their experiments is that the improvements
in the translation quality do not come from utilizing the document context, but
rather from simple regularization effect. In other words, the document context
is a noise that helps to make the model more robust. This is a very similar
conclusion to what researchers in Prague claim about the [explicit use of
syntax in the encoder](https://arxiv.org/abs/1910.11218) in a multi-task
learning setup. It seemed to improve the translation quality, but when they
tried a linear chain instead of a real syntax tree, the improvements were the
same.

Nevertheless, I have strong doubts about the methodology that was used to asses
the improvements from the document context. They computed TER between the
outputs of the sentence-level and the document-level models and the reference
sentences. TER (Translation Error Rate) is a word-level edit distance between
the sentence, i.e., the minimum number of operations of types: _insert_,
_delete_ and _substitute a word_ that would transform one sentence into the
other. They looked only on those edit operations that differed in the document-
and sentence-level model outputs and improved the TER score at the same time.
Those are the word-level edits that presumably improve the translation quality.
But what if the document-level model learns to change the structure of the
sentences to better fit the overall topic of the document? I suspect that it
would look exactly the same way what the authors of the paper observed—most of
the word-level changes would not make any sense when taken out of context in
this way.

Anyway, no matter if trust the exact number that only 5% of changes are
context-related, still the paper carries an important message that
document-level systems are not as document-level as we might thing when only
looking at the BLEU scores.

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
