---
layout: post
title: "Machine Translation Weekly 4: Analyzing Multi-Head Self-Attention"
tags: [MT Weekly]
lang: en
---

With the ACL camera-ready deadline slowly approaching, future ACL papers start
to pop up on arXiv. One of these which went public just a few days ago is paper
called [_Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy
Lifting, the Rest Can Be Pruned_](https://arxiv.org/pdf/1905.09418.pdf) and was
done by quite a diverse group of researchers from University of Amsterdam,
University of Edinburgh, Moscow Institute of Physics and Technology and Russian
company Yandex.

The paper analyzes the encoder of the Transformer models for machine
translation and tries to get to the bottom of what the self-attention heads in
the encoder do. The self-attention is known to capture some linguistic
phenomena, but most of the attention heads learn to do mysterious operations
that no one understands. It is indeed tempting to think that this is what makes
the Transformer such a powerful model. However, this paper shows that exactly
these heads the most superfluous ones and if you (cleverly) remove them from an
already trained model nothing happens.

<details>

<summary>First, let me remind you how the self-attention heads in the <a
href="https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf">Transformer
model</a> look like. (Click to unroll if your interested in a clumsy
summary.)</summary>

<p>The inputs of the encoder are word embedding vectors. A word vector in the
next sublayer is a combination of the vectors on the previous layers, more
precisely a linear combination of so-called heads. Each head computes a
distribution over all vectors in the layer and uses it to compute a weighted
sum learned projections of the vectors. The distribution can be interpreted as
information: “to which words a word attends on a particular layer.” (And this
interpretation is what this paper is concerned about.) When visualized, it can
look like this (taken from <a
href="https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html">Google
AI Blog</a> announcing the Transformer paper).</p>

<img src="/assets/MT-Weekly-4/google.png" />

<p>The self-attentive layers are interleaved with non-linear layers. There are
also residual connections between all sublayers which kind of make sure that
the information about the words stays locally and does travel arbitrarily among
the states. (This also what the discussed here assumes.) The encoder usually
has 8 attention heads in each of its 6 layers, it means 48 heads in total.</p>

<p>If you need even more details about the Transformer model, you can have a
look at nice illustrations by <a
href="http://jalammar.github.io/illustrated-transformer/">Jay Alammar</a></p>

<hr />

</details>

<p></p>

The paper classifies the attention heads into several categories. In the first
category, there are _position heads_, systematically attending to words
surrounding words (the Transformer is by design not aware of word order and
needs to learn it). The second category consists of _syntactic heads_. The
authors came up with a clever technique (which might be enough for a separate
paper) and detected heads that reach the maximum values when attending from one
syntactic category to another one. There are heads identifying object-verb
relation, a verb with an adverbial modifier, etc. In the third and last
category, there are heads attending to _rare words_. It is hard to say why they
are there, perhaps because rare tend say a lot about the topic of the sentence.

Then, they used [Layer-wise Relevance
Propagation](https://pdfs.semanticscholar.org/17a2/73bbd4448083b01b5a9389b3c37f5425aac0.pdf),
a technique that estimates the importance of particular neurons for the network
output (I had no idea it existed until now) and also measure how sharp the
attention distributions are. And, amazingly, the most important heads according
to relevance propagation and those with the sharpest distributions, are exactly
those from the three categories as is shown on a picture in the paper (the
picture is taken from the paper, page 3, figure 1).

![head categories](/assets/MT-Weekly-4/head_categories.png)

This might be enough for a good paper, but it does not end yet. The paper
continues with a clever technique for learnable switching off the attention
heads. There is a gate added to every attention head (something similar to the
[Gumbel-softmax](https://arxiv.org/pdf/1611.01144.pdf)) which makes a hard 0/1
decision whether the head is used, but the decision is still differentiable and
the gradient can get through during training. It is used for model finetuning
which has two objectives: switch off as many heads as possible, and minimize
cross-entropy of reference sentences (i.e., the standard way of training MT).
The more weight is given to the first objective, the more heads get switched
off. The experiments again show that “mysterious” heads are the first ones that
get removed and it barely influences the translation quality. This is shown on
a diagram with the number of remaining headson the horizontal axis and head
categories on the vertical axis (the picture takem from the paper, page 7,
figure 8).

![head pruning](/assets/MT-Weekly-4/head_pruning.png)

At first glance, the method seems a bit over-engineered, but my guess is that
just removing one of the heads without finetuning would just break the model
immediately. Even if the “mysterious” head would only generate noise, the rest
of the network is tuned to the particular activations. So, if I think about it
in more detail, this is truly an elegant way of learning to remove something
from a neural network without doing much harm.
