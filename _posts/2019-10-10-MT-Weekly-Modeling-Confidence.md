---
layout: post
title: "Machine Translation Weekly 14: Modeling Confidence in Sequence-to-Sequence Models"
tags: [mt-weekly, en]
lang: en
---

Neural machine translation is based on machine learning - we collect training
data, pairs of parallel sentences which we hope represent how language is used
in the two languages. The more model input resembles the sentence the model was
trained on, the better we can expect the translation to be. If we were able to
compute this similarity, we might be able to guess, how well the model can
translate the sentence. Current best systems are trained on tens or even
hundreds of millions of sentence pairs. Obviously, comparing a sentence you
want to translate to so many sentences is not computationally feasible. This
problem (and an elegant solution) is a topic of a recent paper from the
Karlsruhe Institute of Technology called [Modeling Confidence in
Sequence-to-Sequence Models](https://arxiv.org/pdf/1910.01859.pdf).

The paper is based on a  nice, simple and clever trick. If the input sentence
is similar to sentences that were in the training data, the representations in
the encoder and in the decoder should also be similar. This itself is not
really helpful: computing the similarity still requires to go though the
millions of training sentences which is computationally expensive. The authors
actually did that, burned a lot electric power and proved that this really
gives a good estimate how well the translation will be. The question is now how
to do it efficiently, i.e., how to compute the similarity with the training
sentences without  actually using them?

And indeed, there is a clever trick to do that. In the paper, they train an
autoencoder for the hidden states—a neural network that projects inputs into a
vector of smaller dimension and tries to reconstruct the input from this
representation. The bottleneck representation simply does not have enough
capacity to memorize the input, so the network needs to learn how to compress
the input. Because the network is trained to work well on average, frequent
inputs get reconstructed better than inputs that appear only rarely. And voila,
this is exactly what we want: the reconstruction error gives us an estimate how
similar are the encoder and decoder states for the input sentence and for the
training data.

The paper goes even furhter with this. When we have the hopefully reconstructed
decoder states, we can use them instead of the real ones. We thus do not have
to measure the similarity of the hidden states for which we do not have a
straighforward interpretation anyway. We can try how the model output would
change if we used the reconstructed states instead of the real ones. If the
acutal model output gets a low probability, it means the original prediction
was based on a hidden state that was not typical for training data and the
translation is not likely to be of good quality.

Moreover, if we do word alignment (which they did in a quite clever way in the
paper) between the source sentence and the model output, we can say what source
words cause the model not be uncertain which can find use both in user
interfaces and analysis what the models do.

Isn't it amazing? Instead of complaining that the hidden states of neural
machine translation models are totally uinterpretable and that we cannot say
anything about the expected translation quality, this paper shows that with a
little wit and simple statistics, this can be nearly turned into advantage.
