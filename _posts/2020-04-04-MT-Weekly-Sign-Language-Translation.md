---
layout: post
title: "Machine Translation Weekly 36: Sign Language Translation"
tags: [mt-weekly, en]
lang: en
---

This week, I am going to have a look at a topic that I was not thinking about
much before: sign language translation. I will comment on [a bachelor thesis
from Ecole Polytechnique in Paris](https://arxiv.org/pdf/2004.00588.pdf) that
was uploaded to arXiv earlier this week.

It was a very educative reading for me and the first surprise for me was that
sign languages are very different from their local spoken counterparts. For
illustration, they say that American sign language has a more similar grammar
to Japanese than to English. My first idea that monotonic word-by-word
translation with some local changes would work well is indeed naive.

One thing that makes automatic sign language translation difficult is that
there is no standard formal way of transcribing sign languages. The language is
multidimensional and body posture and facial expressions are as important as
hand gesture signs. One can argue, that we can say similar things about spoken
language as well, prosody or facial expression can entirely change the meaning.
We can see this in misunderstandings in written communication or in the need to
use emoticons to clarify how we meant what we wrote. However, centuries-long
history of writing down spoken languages resulted in a standard way of writing
down what we say. This is missing for sign languages.

Still, people need to write down the sign language somehow, for example in
textbooks for training new interpreters. Such transcriptions are called glosses
and follow some semi-formal conventions of writing down, what the interpreter
should do. Unlike for instance Latin alphabet which can be with some effort
used for plenty of languages, the glosses are strongly language-dependent.

Examples of glosses for American sign look like this (taken from [ASL
University](https://www.lifeprint.com/asl101/topics/gloss.htm), an online
American Sign Language curriculum resource center):

**ASL:** ASK-him STUDENT WHERE IX-he LIVE <br />
**English:** Ask the student where he lives.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rkL2XbD6EyM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<p></p>


**ASL:**     two-WEEK-future SATURDAY IX-you # BUSY? <br />
**English:** Are you busy two weeks from now?

<iframe width="560" height="315" src="https://www.youtube.com/embed/pV4E42Ynlsc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<p></p>


Automatic translation of a sign language is done in two steps:

1. Automatic glossing of a video record.

2. Translation of the glosses into target languages.

They experiment with a dataset that was created from news and weather forecast
on a German TV station. The dataset contains video recordings of people talking
in the German sign language, segmentation into sentence-like segments, and
translations into standard written German. Although the authors must have made
a large effort to collect the dataset, from the machine translation
perspective, the dataset is rather small, it only contains 7k training
segments.

The bachelor thesis says that it presents state-of-the-art results and still
the BLEU scores for German are in the twenties for a relatively simple domain.
The German scores in WMT News Task are usually much higher for much more
complex texts. On the other hand, the training data is really small, so I am
not sure what I should think about the numbers. But they probably say that it
is rather a difficult problem than an easy one. No examples are provided and if
they were, I would not understand them anyway.

Sign language translation is also an inherently low-resource problem. There are
only small datasets available, the community of speakers is also small and
there is no easy way to get synthetic data as we do for low-resourced
translation with iterative back-translation, there is no monolingual data out
there that can be just crawled from somewhere and used, painstaking manual data
annotation seems to be inevitable. One iteration of back-translation would be
possible here too: using native German sentences as targets with synthetic
sources. Unfortunately, such an experiment is missing in the thesis, but
perhaps the author will decide to turn the thesis into a proper research paper
and we will see these experiments later.
