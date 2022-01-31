---
layout: post
title: "Machine Translation Weekly 100: IGLUE as cool as igloo, multilingual and multimodal benchmark"
tags: [mt-weekly, en]
lang: en
issue: 99
---

This week I would like to feature a new [multimodal-multilingual benchmark
called IGLUE](https://iglue-benchmark.github.io/), presented in a
[pre-print](https://arxiv.org/abs/2201.11732) that went out last Friday.  The
authors are from many place around the world: University of Copenhagen, Mila –
Quebec Artificial Intelligence Institute, University of Cambridge, TU
Darmstadt, New York University, and McGill University.

Following the best practices from established multilingual benchmarks, the new
multimodal and multilingual benchmark evaluates zero-shot cross-lingual
transfer with the multimodal tasks. Zero-shot cross-lingual transfer means a
task-specific model (in this case, e.g., for visual question answering) is
trained in English. However, because the sentence representation is
(presumably) multilingual, the model should work in other languages as well.

The benchmark collects multilingual test sets for the following tasks:

* _Visual natural language inference_: Decide what is the logical relation
  between two sentences given an image (one is a consequence of the other, they
  contradict each other or there is no relation at all).

* _Visual question answering_: Answer a question about an image with a single
  word.

* _Visual reasoning_: For two images, decide if a (tricky) statement is true
  for both images.

* _Image retrieval_: Based on a textual description an appropriate image should
  be retrieved from a database.

The training sets for the tasks are English only, the test sets are
multilingual. The authors paid a lot of attention to the choice of languages
that is diverse and covers various languages families and various text sizes
available for the languages.

The authors tested the existing multilingual and English-only models on the
benchmark. The main takeaway from the baseline experiments is that existing
multilingual multimodal models are very poor both zero-shot and few-shot
learners. From what I am used to from text-only tasks, I would say it almost
does not work at all. Machine-translating the test sets into English and using
English-language multimodal models is far better than anything the multilingual
models can do (even though there is no guarantee that the translation will
still correspond to the respective images). Also, unlike purely textual models,
few-shot learning makes actually no difference compared to zero-shot (unlike
text-only models, where a dozen of training examples can make a huge
difference).

I tend to believe that combining multimodality and multilinguality can help
push forward artificial intelligence in general. The recent (and already
famous) [thought experiment with a deep-sea
octopus](https://aclanthology.org/2020.acl-main.463) argues that language
modeling cannot be a path towards more general intelligence. Reporting bias
prevents the models from learning about the reality (whatever it means) that
drives the language behavior, particularly a common-sense grasp of the world
and intentionality of utterances. I believe that multilinguality and
multimodality can help to overcome this problem.

Concepts in different languages are not exact translations of each other.
Modeling concepts multilingually thus requires having a more fine-grained
representation of the underlying reality (whatever it means). Multimodality can
help ground the concepts in something (at least partially) language-agnostic.
Also, multimodality shows the models that there are important obvious facts
people do not talk about. Perhaps, if the octopus not only listened but
followed WhatsApp chats in many languages and with images, it could learn
everything to pass the deep sea Turing test.
