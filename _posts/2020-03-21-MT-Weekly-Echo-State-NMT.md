---
layout: post
title: "Machine Translation Weekly 34: Echo State Neural Machine Translation"
tags: [mt-weekly, en]
lang: en
---

This week I am going to write a few notes on paper [Echo State Neural Machine
Translation](https://arxiv.org/abs/2002.11847) by Google Research from some
weeks ago.

Echo state networks are a rather weird idea: initialize the parameters of a
recurrent neural network randomly, keep them fixed and only train how the
output of the network is generated. I think the intuition behind that can be
something like: a random transition matrix captures to some extent almost all
possible transition dynamics / information flows anyway, so it should be enough
to train the output projection that will choose what is actually meaningful.

The experiments conducted in the paper show that in the case of neural machine
translation it is not exactly like this. When they took the recurrent
sequence-to-sequence architecture and only trained the output layer of the
decoder, the results were a total mess. What appears to be crucial to make this
idea work is training also the input embeddings. It makes sense because
otherwise, the input (i.e., random word vectors) is totally uninformative.
Unfortunately, it also means that they have to backpropagate through the entire
network anyway and do not save much time during training anyway. Training the
input embeddings and output projection gives 69% of the translation quality of
a fully trained system.

If they in addition train the attention between encoder and decoder, they get
80% of the quality of the fully trained model. This also kind of expected
result, that the attention is the second most sensitive component. The decoder
uses the attention to retrieve the context-specific information from the
encoder. For me, it is a surprise that even random attention can work somehow.

I wonder what should the takeaways from this paper be. Does that mean that
recurrent networks are easier to train because they by default capture many
possible information flows in time and the classical training only reinforces
some of them and suppresses the others? The paper mentions using Transformers
as potential future work, but my guess is that they must have tried and it did
not work. Does that mean Transformers are better or stronger because they do
not make any assumptions about the data and can thus learn more than recurrent
networks? On the other hand, Transformers (as we discussed in [MT Weekly
31](/2020/02/28/MT-Weekly-Transformer-with-Fixed-Heads.html)) usually only
learn quite simple rules anyway in the end, what is the strength at the end
good for?
