---
layout: post
title: "Machine Translation Weekly 59: Notes from EMNLP 2020"
tags: [mt-weekly, en]
lang: en
---

Another large NLP conference that must have taken place in a virtual
environment, [EMNLP 2020](https://2020.emnlp.org), is over, and here are my
notes from the conference. The ACL in the summer that had most Q&A sessions on
Zoom, which meant most of the authors waiting forever if someone takes the
courage to enter the room. EMNLP sort of simulated the standard conference
format that hopefully reduced the communication barrier. There were public Q&A
sessions with short presentations and poster sessions in a tool called
[Gather.town](https://gather.town) – a virtual environment with the look and
feel of a 90's video game. As an avatar, you can have walked from a poster to
poster and talk to people. It seemed quite weird at the beginning, but looking
back, I must admit I almost have false memories of talking to people at a real
poster session, so it probably worked quite well.

## Brief comments on presentations I found most interesting

### ① [Digital Voicing of Silent Speech](https://www.aclweb.org/anthology/2020.emnlp-main.445) 🥇

This paper was awarded with the best paper award and it totally deserves it.
The task in the paper is: put 8 electrodes on a persons' face, the persons move
their face as if they spoke, and a system is supposed to reconstruct what they
say. The paper presents a large dataset of the records from the electrodes
collected in the two setups: vocalized (the people really speak) and silent
(just move their face). By aligning the vocalized and silent electrode signals,
they can generate a synthetic vocalized signal that they use to generate the
speech. To my surprise, the intelligibility of such sentences is only slightly
above 30%. However, it is still 3 times better than previous work.

### ② [MAD-X: An Adapter-Based Framework for Multi-Task Cross-Lingual Transfer](https://www.aclweb.org/anthology/2020.emnlp-main.617) 👍

The task in this paper is transferring a model (for any NLP task) from a high
resource language to a low resource language for which we do not even have a
pre-trained representation model. The main idea is stacking adapter layers and
exchanging already train adapter layers. The adapter is an added feed-forward
sub-layer into the Transformer architecture that is trained while keeping the
the parameters of the rest of the model fixed. Because of the fixed parameters
around, it is forced not to diverge from the representation space of the
original model, which makes the adapter exchangeable. The trick they do: (1)
train language-specific adapters for all languages they need to work with and
(2) train task-specific adapters when the language one is frozen. Then, they
can do the transfer by changing the language adapter and keeping the task
adapter.

### ③ [Best-First Beam Search](https://arxiv.org/abs/2007.03909) 👍

Standard beam search approximates the breath-first search by only keeping _k_
best options in each step. The proposed algorithm is sort of closer to the
depth-first search. At each step, it keeps _k_ best candidates, but only
expands the globally best one (stored in a priority queue). With a monotonic
scoring function, this leads to the same result as the standard beam search in
a much smaller time, especially for large beams. It works also with length
normalization (which makes the scoring function non-monotonic), but I did not
really get why.

### ④ [Incorporating a Local Translation Mechanism into Non-autoregressive Translation](https://www.aclweb.org/anthology/2020.emnlp-main.79/) 👍

In this paper, the authors make the non-autoregressive translation (MT that
generates all output words in parallel) locally autoregressive. Every hidden
state initializes a small RNN that generates several tokens, but still, all the
mini-decoder can run in parallel. Then they run a clever dynamic programming
algorithm to merge the generated segments. The proposed approach reaches much
better translation quality at a similar speed as other non-autoregressive
methods.

### ⑤ [Experience Grounds Language](https://www.aclweb.org/anthology/2020.emnlp-main.703)

The paper is a manifesto asking to rethink NLP tasks (and AI tasks in general)
having the following question in mind: Is knowledge about _X_ most richly
encoded (A) in existing texts or (B) in the physical or social world? If B is
the case, we are unlikely to learn the task _X_ satisfactory from text alone
without allowing the model to interact with the physical or social environment.
I would paraphrase their argument as: The ability to interact with the physical
and the social world is natural to us (and everything seems self-evident before
we start to philosophize), so we do not need to write long texts about it
(unlike for instance about physics, biology or politics). Therefore, there is
no text, our models can learn this from. (And even when there is, it uses
philosophical or scientific jargon that is too distant from everyday
experience, so that it is useless anyway.)

### ⑥ [Identifying Elements Essential for BERT's Multilinguality](https://www.aclweb.org/anthology/2020.emnlp-main.358)

The paper explores multilinguality in a clever small-scale bilingual setup with
English and Fake English (that only has all IDs shifted). They find out that:
(1) Sharing position embeddings and special symbols is crucial; (2) Reverting
the order of one language breaks everything (it perhaps suggests that
positional embeddings learn some information about the sentence structure); (3)
Too many parameters prevent the model from generalizing and it learns each
language separately. Further, they add another trick in the training: instead
of simply masking the inputs, they use the nearest neighbor from unsupervised
word embeddings and get much better language neutrality. They apply all these
findings also in a large-scale English-German-Hindi model and come to the same
conclusions.

### ⑦ [Improving Multilingual Models with Language-Clustered Vocabularies](https://www.aclweb.org/anthology/2020.emnlp-main.367)

Current pre-trained multilingual models use vocabulary that is shared among all
(i.e., around 100) languages. Vocabulary sharing is desirable because it helps
the models to learn similarities across languages, but it discriminates against
languages with unique scripts such as Korean or Japanese. The paper presents a
work-around: train shared vocabularies for clusters of similar languages. The
similarity is based on the monolingual SentencePiece overlap, so it is
beautifully language-agnostic. On the other hand, it requires knowing the
language in advance. However, the resulting model is much more language-neutral
than without using this trick.

### ⑧ [The Multilingual Amazon Reviews Corpus](https://www.aclweb.org/anthology/2020.emnlp-main.369)

A dataset of Amazon reviews in multiple languages, primarily designed for
experiments with the zero-shot transfer of classifiers trained on one language.
Beyond what the authors say, it can be used for evaluation of how
sentiment-preserving MT is or whether we also transfer culture when we transfer
across language.

### ⑨ [BLEU might be Guilty but References are not Innocent](https://www.aclweb.org/anthology/2020.emnlp-main.5)

Because of the way of how we get references, they argue that maximizing BLEU
means aiming for the most average human translation, i.e., the most
translationeese ones. They created more natural paraphrases and the automatic
metric correlates much better using those. The paper raises a provocative
question: if all results in the field are based on comparing against suboptimal
references, didn't we dismiss some good ideas?

### ⑩ [Scaling Hidden Markov Language Models](https://www.aclweb.org/anthology/2020.emnlp-main.103)

Research from the world where neural networks were not invented. The paper
takes some tricks from neural networks to make HMM large. They group words into
clusters (Brown clusters, no embeddings, this is a paper from the world without
neural networks) and only allow groups of states to emit words from one
cluster. This turns the transitions to block matrices only. They also use state
dropout during training, so the model needs to learn to recover from being in
the wrong state. This must be quick as hell, however, the paper does not show a
comprehensive speed comparison.

### ⑪ [Seq2Edits: Sequence Transduction Using Span-level Edit Operations](https://www.aclweb.org/anthology/2020.emnlp-main.418)

They formulate sequence-to-sequence transduction as applying a sequence of edit
operations with a custom representation of the edits. They are triplets of:
edit type, edit span length (start is implicitly computed from previous spans).
Further, they modify the transformer decoder to have sublayers to predict (1)
the operation type that goes as input to the next sublayer, (2) the operation
span using a pointer network, (3) predict what to do with the span. Works
excellent for tasks such as grammatical error correction.

### ⑫ [Detecting Word Sense Disambiguation Biases in Machine Translation for Model-Agnostic Adversarial Attacks](https://www.aclweb.org/anthology/2020.emnlp-main.616)

Method for evaluating word sense disambiguation in machine translation. First,
they identify homographs in the training data: nouns that get translated
differently. Then they identify attractors: words that strongly correlated with
the the distinct translations (hot spring vs. Prague spring) and thus
indicicate the word was used in a different sense. They use this to create a
challenge set: manually modified sentences, such that the sentence contains an
attractor corresponding to a different sense than the one used in the sentence.
The experiments reveal that current NMT uses almost exclusively these shallow
clues to disambiguate word senses.

### ⑬ [How do Decisions Emerge across Layers in Neural Models? Interpretation with Differentiable Masking](https://www.aclweb.org/anthology/2020.emnlp-main.262)

The goal is to find out what activations in the neural network are responsible
for generating the output, ultimately what parts of the input influence the
output the most. The method is a clever mathematical formulation of masking
out some network activations and observing what effect it has. Using
constrained optimization (and Lagrange multiplicators), they want to mask
out as many activations when keeping the KL divergence between the outputs
of the original and the masked as small as possible. On a toy problem where
they know what the model does, they show this method works much better than
previous ones. On real tasks, they show what really matters for existing
models.

### ⑭ [The Grammar of Emergent Languages](https://www.aclweb.org/anthology/2020.emnlp-main.270)

They take an emergent language from a game of two neural agents that need to
communicate using discrete symbols (the game is of course an extremely poor
simulation of communication needs that natural language can satisfy). The paper
tries methods of constituency grammar induction on these languages. They found
out that syntax-like structure emerges only with sufficient length of messages
and a sufficiently large vocabulary, otherwise the code seems unstructured. The
symbols tend to behave more like characters than words, as opposed to what most
people would suspect.

### ⑮  [Spot The Bot: A Robust and Efficient Framework for the Evaluation of Conversational Dialogue Systems](https://www.aclweb.org/anthology/2020.emnlp-main.326)

The paper presents a new methodology for the evaluation of chat-bots, I would
call it a non-binary version of the Turing Test. The annotators are asked to
judge if an answer is an authentic human response or if it was generated by a
chatbot. In the Turing Test, the question is if the systems are distinguishable
at all. Here, they measure how many turns can the chatbot survive before being
busted as a non-human. It appears to be a fast, cheap, and reliable way of
human evaluation.
