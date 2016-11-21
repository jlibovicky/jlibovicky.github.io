---
layout: page
title: Tutorial: Punctuation Filling
---

I have always struggled with how to correctly write punctuation in English. The
rules asre complex and there is always plenty of speical casses. In this
tutorial, I will try to show you how can use deep learning to train an
automatic punctuation filler for English and Czech.

## Main Idea

The is a plenty of text on the Internet. Huge part of it is in English and most
of it is correctly puncutated. We can take for instance the English Wikipedia,
remove all the punctuation and train a model that will read the depuncuated
text and try to estimate, whether there should or should not be a comma or a
semicolon. Recurrent neural networks are very powerful models which are used
for such complicated tasks as machine translation or automatic speech
recognition, they should work for this simple task as well.

This, indeed, can never be done 100% correct - the puncutation very often changes
the meaning of the sentences. Let us at least see how far we can get.

## Prerequisities

In this tutorial, we will se Python
