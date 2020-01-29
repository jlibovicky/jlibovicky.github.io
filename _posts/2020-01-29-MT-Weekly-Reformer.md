---
layout: post
title: "Machine Translation Weekly 27: Explaining the Reformer"
tags: [mt-weekly, en]
lang: en
---

This week I will not review a paper that is not primarily about machine
translation but has the potential to make a big impact on machine translation.
I will talk about Google's Reformer, an architecture that is a more
memory-efficient brother of the widely used Transformer architecture. I will
try to explain what are the two main innovations that allow the model to save
memory. Unlike my previous posts, this one contains a bit more math and
requires a bit more knowledgable audience.

The Transformer is currently the most popular architecture for deep learning in
natural language processing. It first became popular in machine translation in 2017.
In 2018, it was used to train BERT, a pre-trained text representation
that can be used in almost all NLP tasks and in 2019 even better pre-trained
representation models appeared.

The strength of the Transformer models probably comes from the fact that at
each layer, it considers all possible combinations of its input tokens. This
can be done quickly because of intensive GPU parallelization, but the number of
all combinations is still quadratic. Also, the deeper the network is, the
better performance you get, which also increases the memory requirements.

Reformer does two things differently from the standard Transformer Adds a
hashing function into the self-attention similarity computation, so only a
small subset of states is actually used.  Uses a trick with so-called
reversible layers, a brilliant idea using trivial algebra that causes that the
model does not store values of activation function during training.

## Self-Attention Locally Sensitive Hashing

The transformer model is based on self-attention layers (this is the place that
considers all combinations). We can imagine attention as probabilistic
retrieval. For a query, you want to retrieve some information about entries
that you have in a data storage. We have some _queries_ $Q$, we compare them
with some _keys_ $K$ and based on that comparison, we retrieve some values $V$.

In Transformers, each state corresponds to one input token (i.e. a word or a
sub-word). We can imagine the self-attention as collecting information that is
encoded in some other hidden states (carried by other words). In each layer,
each subword collects some information the other subwords have and pass it
further.

Because we might not want all the information from other subwords, but only
some parts, we do something called multi-head attention. Each head gets
specialized for retrieving a specific kind of information. This
"specialization" is achieved linear projections of the states. The projection
cannot add any information to the states, they only can make suppress something
or make something more prominent.

When we have all the projections, the attention is computed as follows:

$$ O = \text{softmax}\left( QK^\top / \sqrt{d} \right) V $$

$Q \in \mathbb{R}^{L \times d} = (q_1, \ldots, q_n)$ are $L$ query vectors,
analogically $K$ and $V$ are keys and values respectively. All of them are
linear projections of the model's hidden states.

Now, let us have a look at this from a perspective of a single query $q_i$ and
re-write the dot-product (the $i$-th subword is looking for what subwords
have).

$$o_i = \text{softmax} \left( \frac{q_i K}{\sqrt{d}}\right) V = \sum_{j=1 \ldots L} \left[ \text{softmax} \left( \frac{q_i K}{\sqrt{d}} \right) \right]_j \cdot v_j$$

If we further re-write the softmax, we get:

$$o_i = \sum_{j=1 \ldots L} \frac{\exp{q_i k_j / \sqrt{d}}} {\sum_{k=1 \ldots L}\exp{q_i k_k / \sqrt{d}}} v_j =  \sum_{j=1 \ldots L} \exp \left( q_i k_j / \sqrt{d} - \log\sum_{k=1 \ldots L}\exp q_i k_k / \sqrt{d} \right )$$

In the paper, they call the log-sum-exp term $z$. If we further call the set of
all indices $1 \ldots L$ as $\mathcal{P}(i)$, we get exactly the formulation
that is in the paper, in Equation 2 on page 3.

$$o_i = \sum_{j \in \mathcal{P}_i} \exp \left( q_i k_j / \sqrt{d} - z(i, \mathcal{P}_i) \right)$$

$$z(i, \mathcal{P}_i) = \log\sum_{j \in \mathcal{P}_i}\exp q_i k_j / \sqrt{d}$$

From analyses of learned Transformer models, we now that the attention
distributions are usually quite sharp and only attend to few keys. Now, if we
were able to iterate over a substantially smaller set $\mathcal{P}(i)$ than $1
\ldots L$, we can save a lot of memory (and maybe some computation time as
well). This is where the hashing comes into play.

The first part of the trick is to unify the projection of keys and queries. If
we do this, for one head it holds that we are looking for few vectors that are
the most similar to the query, vectors that belong to the same cluster (the set
$\mathcal{P}(i)$ from the previous paragraph). The clustering can be
approximated by a fast hashing function. And in the best computer science
tradition, the clusters are called buckets.

For $b$ buckets,  we will sample $b/2$ random vectors and compare every query
and key with those vectors. There are two buckets for each random vector $r \in
\mathbb{R}^d$: one for those which are the most similar to the vector $r$ and
one for those which are the most similar to a negation of the vector. In the
paper, they formally introduce a matrix $R \in \mathbb{R}^{d\times b/2} =
\left( r_1, \ldots, r_{b/2} \right)$ and define the hashing function as:

$$h(x) = \arg\max\left([ xR; -xR ]\right)$$

With such a hash function, you can do the attention only over the vectors that
fall into the same bucket. In Equation 4 at page 4 of the paper, they formally
write:

$$\mathcal{P}_i = \left\{ j: h(q_i) = h(k_j) \right\} $$

A hashing function like this might be useful if computed everything vector by
vector on CPU, but we need a fast GPU implementation. GPUs are good in matrix
multiplications and dealing with sets of indices of different sizes does not
sound like a task for GPU-accelerated computing. Here comes another trick for
rescue.

If we sort the vectors according to their bucket number and split them into
several chunks, vectors with the same hash number are likely to end up in the
same chunk. To lower the chance that we miss something because of chunking, the
attention also considers one chunk back as keys. Yes, if your comrade you want
to attend to is in the next chunk, you have bad luck, they can still attend to
you. In a language model where you attend to previous positions anyway, this
does not matter at all (given the sorting was stable). In a bidirectional
encoder,  it can play a more important role and a different strategy might be
better.

In Figure 2 at the top of page 4, they illustrate the process like this:

![Local Sensitivity Hashing](/assets/MT-Weekly-27/paper_lhs_scheme.png)

Also, a technical detail: you do not want to attend to vectors that ended up in
the same chunk but got a different hash. Those need to be masked out.

To further lower the chance that hashing will miss something, we can do the
hashing multiple times (in parallel) and then just average what you get from
the rounds.

To better illustrate how the local sensitivty hashing works, I made a small
JavaScript demo that hashes 2k most frequent English words into buckets based
on their FastText embeddings. Maybe there is a bug, but it does not really tend
to bucket similar words together.

<iframe src="/assets/lsh_js/index.html" width="100%" height="500">The demo is
in an iframe.</iframe>

## Reversible layers

The other trick they use to improve memory efficiency is using reversible
layers. But before I explain what exactly the reversive layers are, allow me to
remind how back-propagation in neural networks works and how parameter
gradients get computed.

Let us start with  a simple example of logistic regression:

$$o = \sigma \left( \mathbf{W}\mathbf{x} + b \right)$$

The computation can be represented as a graph and computing the loss
derivatives with respect to the parameters as a backward graph, a graph with
reversed edges where the nodes represent derivatives of the operations in the
original graph. $L$ is the loss function, let us say binary cross-entropy, and
$y^\ast$ is the expected output of the network.

![Back-propagation graph](/assets/MT-Weekly-27/backprob.png)

Looking at the graph, we can express the derivative of a loss function with
respect to parameter $b$:

$$ \frac{\partial L}{\partial b} = \frac{\partial L}{\partial o} \cdot \frac{\partial o}{\partial h} \cdot \frac{\partial h}{\partial b} $$

Now, let us have a look at the look at how terms look like:

$$ \frac{\partial L}{\partial o} = \frac{o - y^\ast}{o(1-o)}$$

$$\frac{\partial o}{\partial h} = \sigma(h)\left( 1 - \sigma(h) \right)$$

This example shows us that no matter what the function is when doing the
back-propagation, we need to remember what was the value of the node in the
forward pass. And with Transformers, it means a lot of memory.

The standard Transformer uses residual connections. The purpose of residual
connections is preventing the vanishing gradient problem. The trick is simple,
we just sum the layer output with the layer input. When computing the loss
derivative by back-propagation, there is always a path that leads through only
through the summation operations, which are linear with respect to derivation.
Other functions have derivatives that are often quite small or zero. Without
the residual connections, you would multiply the gradients by this small or
zero derivatives so many times that it would eventually vanish. Such a path
with summations is sometimes called the information highway.

![Standard Transformer Encoder](/assets/MT-Weekly-27/residual.svg)

The trick of the reversible layers is that if we have two information highways
instead of one, so we can manage to compute the gradients without remembering
the activation values. The architecture gets changed like this:

![Reversible Transformer Encoder](/assets/MT-Weekly-27/reversible.svg)

Expressed by formulas:

$$Y_1 = X_1 + \text{Attention}(X_2)$$

$$Y_2 = \text{FeedForward}(Y_1)$$

When doing the back-propagation, and computing gradients for the particular
layer, we need the values of $X_1$ and $X_2$, but instead of remembering them,
we can do:

$$X_2 = Y_2 - \text{FeedForward}(Y_1)$$

$$X_1 = Y_1 - \text{Attention}(X_2)$$

Indeed, we need to call the $\text{FeedForward}$ and $\text{Attention}$
functions again which will cost us some time, but it will save a lot of memory.
We only need to remember the activations on the current layer and we can forget
them as soon as we move in the back-propagation further. The memory
requirements are now independent of the total number of layers.

## What will happen now

And this is it. This is how to save memory when training big Transformer
models. The paper shows only a few experimental results, but they manage to
show that with approximately the same performance as the Transformer, it is
much more memory efficient and thanks to the hashing also faster than standard
Transformers.

The Reformer was released together with code in Google's JAX. The paper was
anonymously available on OpenReview since the end of September and even before
publishing the non-anonymous pre-print on arXiv, there was a PyTorch
re-implementation that gets seems to get better every day.

With Reformer training deeper NLP networks becomes more accessible. It will
certainly allow more research on character-level processing and pre-trained
representation outside big companies. Or maybe Google and Facebook will train
even better and larger BERTs that still will be almost impossible for anyone
else to develop. We will see in 2020.
