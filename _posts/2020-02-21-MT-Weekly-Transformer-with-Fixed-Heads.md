---
layout: post
title: "Machine Translation Weekly 31: Fixing Transformer's Heads"
tags: [mt-weekly, en]
lang: en
---

This week, I am going to comment on a paper that appeared on arXiv on Tuesday
(Feb 25) and raised quite a lot of interest on Twitter. The title of the paper
is [Fixed Encoder Self-Attention Patterns in Transformer-Based Machine
Translation](https://arxiv.org/pdf/2002.10260.pdf) and it describes work that
has been done at the University of Helsinki.

Long story short: they removed almost everything why we though the Transformer
architecture is so powerful, replaced it with simple rules and showed that
nothing really changed. It seems to me that this paper nicely points out the
methodological problems that the current natural language processing research
has, but before I comment on that, let us have a look at what the paper really
does.

The encoder of the Transformer architecture consists of two types of layers
that alternate: self-attentive layers and feed-forward layers. The feed-forward
layers do a non-linear transformation of the input which is nothing special,
neural networks always did that. The self-attentive layers are what makes the
Transformer so special and powerful. If we simplify that, we can say that every
word uses several little search engines (= attention heads) via which it
collects relevant pieces of information from other words (by computing a
probabilistic distribution over them and taking the weighted average of
projections of their representations). This is repeated on every layer of the
network. Words share their little search engines (= attention heads) within
layers, but use different ones on different layers. At the end, we have a
information-rich representation of every input word that is further use in the
decoder.

The Transformer was published in 2017 and pushed forward the state-of-the-art
in machine translation by a large margin. Pretrained sentence representations
based on the Transformer ([BERT](https://arxiv.org/abs/1810.04805) and his
pre-trained friends) made similar progress in other natural language processing
tasks one year later. When the first Transformer paper was published, it came
out with optimistic claims about what the attention heads are capable of. The
appendix of the paper showed what phenomena the attention heads learn to
capture (without being explicitly taught to) such as [dependency
syntax](https://en.wikipedia.org/wiki/Dependency_grammar) or [coreference
chains](https://en.wikipedia.org/wiki/Coreference). Afterward, several papers
confirmed this optimism by showing what interesting phenomena the
self-attention heads learn to capture.

There was also another line of research focusing mostly on efficiency that
showed that most of the attention heads can be pruned out with almost no harm
to the performance of the models. The heads that survive this pruning are not
those that do the fancy linguistic stuff, they mostly do quite trivial things.

This observation led the guys from Helsinki to a simple experiment. They used 7
hardcoded attention heads:

* one attending to the word itself,

* two attending to neighboring words to the left and to the right,

* two attending to a slightly larger left and right contexts,

* one looking at the beginning of the sentence and one at the end,

and one attention head that is learned like in a standard Transformer. This
kind of breaks the search engine metaphor. If no matter what you ask, the
answer is the previous word, we can hardly call it searching. In the decoder,
everything is learned as before.

The translation quality does not seem to be affected by this drastic
simplification and it even improves for low-resource languages. It kind of
suggest that large proportion of the training data is used to learn that
neighboring words matter the most. In an ablation study where they remove the
heads one by one, they show that the head attending to the previous word is the
most important one, more important than the trainable one.

And now I get to my concerns about what this story says about the current
research in natural language processing. We developed (by we I mean the
research community, but it was actually Google who did it) a monstrous
black-box model that works stunningly well. Then I guess people were thinking
something like this:

* Because it works so well, it must know about complex linguistic phenomena the
  previous models were not able to grasp.

* Because self-attention is the thing that is new about the model, the secret
  ingredient must be in the attention distributions.

At this moment, many researchers (including me) threw away their [Occam's
razors](https://en.wikipedia.org/wiki/Occam's_razor) and started to search for
an empirical justification that it is really so. They found it, so it was
possible to jump to a confusion: attention head allows capturing complex
linguistic phenomena, this is why the Transformer works so well, not noticing
this is a circular reasoning.

In the best tradition of western scientific skepticism, one would expect the
opposite: nitpicking into all the details of the model, until we really find
out why it works. If I wanted to sound theatrical, I would say that the
community traded scientific quality for the illusion of taking part in an
overwhelmingly fast technological progress.

Meanwhile, the large black-box Transformer model finds use in industry and I
wonder if this would be possible in other fields of engineering, for instance
in car manufacturing. Imagine your car has a device that reduces fuel
consumption. It is a pretty large complicated thing with many gears. It works
well, but nobody really knows why. After two years, a serviceperson would tell
you that they would disassemble half of gears because people tried it and it
worked just as well, still without knowing why exactly the device works. I can
hardly imagine anyone would be happy to have something like this.

I am tempted to say one of the reasons this is tolerable in natural language
processing is the overuse of the term artificial intelligence. There has always
been something mysterious about intelligence. Developing an artificial one must
be something more than pure engineering like car manufacturing. Maybe this
subconscious feeling of a mystery is what makes people tolerate the opaqueness
of the models.
