---
layout: post
title: "Machine Translation Weekly 67: Where the language neurality of mBERT reside?"
tags: [mt-weekly, en]
lang: en
---

If someone told me ten years ago when I was a freshly graduated bachelor of
computer science that there would models that would produce multilingual
sentence representation allowing zero-shot model transfer, I would have hardly
believed such a prediction. If they added that the models would be total black
boxes and we would not know why it worked, I would think they were insane.
After all, one of the goals of the mathematization of stuff in science is to
make things clear and predictable, often at the expense of some inevitable
reduction. Why would anyone use math and computer science for creating black
box models?  Yet, here we are.

The paper I am going to comment on tries to partially uncover this
black-boxness. The title of the paper is [First Align, then Predict:
Understanding the Cross-Lingual Ability of Multilingual
BERT](https://arxiv.org/abs/2101.11109) with authors mostly from Inria in Paris
(French National Institute for Research in Digital Science and Technology) that
will appear at this year's EACL.

The paper tries to uncover what parts of multilingual BERT are responsible for
the multilingual properties. It skips the question (according to me, the more
interesting one) how did it happen that it has some multilingual properties. It
takes the model as it is, and tries to identify what layers of the already
trained model create language-neutrality.

Multilingual BERT is trained in the same way as the English BERT (and other
monolingual pre-trained models). The input of the model are sentences where
some words are masked out and the model is supposed to guess what words were
missing. The model is thus forced to learn a representation that allows such
guessing. The resulting representation is usually so information-rich that it
almost seems that the model learned to understand the sentences to some extent.

The multilingual model gets the training sentences in different languages at
the same time. It learns a representation that is somewhat similar across the
languages. We can say it is to some extent, although not entirely,
language-neutral. It is not really clear where language neutrality comes from,
although try to figure it out. E.g., [Philipp Dufter and Hinrich
Schütze](https://www.aclweb.org/anthology/2020.emnlp-main.358) recently came
with several very insightful observations (e.g., when the model has too many
parameters, it just fails to be language-neutral) that show what are necessary
conditions to train a multilingual Transformer. However, what actually happens
when these conditions are met remains a riddle.

One consequence of the partial language neutrality is that the multilingual
models can be used for the zero-shot transfer from one language into another.
This means that we train a task-specific model (e.g., for detecting named
entities in English), using the multilingual representation. At the inference
time, this model will also work for other languages that the multilingual
representation can handle, but of course, not that well as in English. Usually,
the less similar the train and test languages are, the worse performance we can
expect. It is called zero-shot because the model was never presented training
examples in the target language and yet it is able to get some predictions.

The paper invents an interesting evaluation technique of what parts of the
model are necessary for the zero-shot transfer. They do the zero-shot transfer
on various tasks.  Before the training, they randomize (in other words break)
weights in one layer of the underlying representation model. During the
task-specific learning (which is monolingual only), the representation model
learns to fix the randomized weights, but just for the one language that is in
the training data. If the layer significantly contributes to language
neutrality, this will break the zero-short transfer. If the layer is
language-agnostic and does some operation independent of the language, it can
even improve the zero-shot transfer because it can help the model adapt to the
new task.

The results of the (beautifully designed controlled) experiments show that the
first few layers of multilingual BERT are responsible for language neutrality,
whereas the later layers are more task-specific. These results get confirmed in
the second set of experiments that compares the representation similarity of
different languages in different layers of the model. If the training forces
the model to sort of economizing on the parameters, it seems to me that it sort of
makes sense, first transform everything into a sort of language-neutral form
and then resolve how the parts of the input interact with each other.

To summarize the paper, we now know a little bit more about the multilingual
representation models. However, how where the language-neutrality comes from
remains a mystery.
