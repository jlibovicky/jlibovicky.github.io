---
layout: post
title: "Machine Translation Weekly 99: Multilingual models can also be evil"
tags: [mt-weekly, en]
lang: en
issue: 99
---

In a [report published in December on arXiv](https://arxiv.org/abs/2112.04359),
Google Deepmind tries to categorize major ethical and societal issues connected
to large language models. The report probably does not say anything that was
not known before, but I like the way they categorize the issues they talk
about. Because the report mostly talks about monolingual language models, in
this post, I will go over some of the issues they discuss and speculate how
they in the paper are relevant for machine translation and multilingual models.

1. The classification the paper uses is:
2. Discrimination, exclusions, and toxicity
3. Information hazards
4. Misinformation harms
5. Malicious uses

  And two areas that I am not going to discuss here in detail because they
  are not particularly interesting from the multilingual view:

6. Human-computer interaction harms
7. Automation, access, and environmental harms

## Discrimination, Exclusion, Toxicity

Language models learn to mimic the data they are trained on, which is a reason
for many problems. Language models capture (often harmful) stereotypes present
in the training data. In addition, some groups are underrepresented in the
training data, people with extreme or unusual opinions tend to promote them
more than mainstream and thus are overrepresented. So, the first problem is
that the models replicate what is in the training data and there are many
evil things inside.

The second problem in this area is the homogenizing effect due to the
statistical nature of the training. The most frequent patterns in the training
data become the only ones that the model outputs. The example in the survey
puts an example that a family = a man and a woman who get married and have
children. Although this might be most frequently the case, it would be very
harmful to interpret this normatively.

These two problems might get even more serious in the case of multilingual
language models. The uneven size of available training data can cause
stereotypes or general opinions from one culture can be imposed on languages of
other cultures. E.g., an answer to a question: "Is it OK to eat
horses/pork/beef/whales?" will very likely differ around the globe. A
multilingual model trained mostly on western languages can impose the western
viewpoint into other languages as well. Biases learned from data (especially
gender bias) in machine translation are [quite well
studied](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00401/106991/Gender-Bias-in-Machine-Translation)
in machine translation.

The previous two problems are closely related to the danger of generating toxic
language. This also can get worse when multilinguality comes in. What is
appropriate to say can differ a lot across cultures and importing norms from
one language into another one can be problematic here as well.

Even though, machine translation should be less problematic here - after all,
it only should transfer meaning from one language into another one - I am
pretty sure that machine-translating texts about sex education could often lead
to profanities. (Or perhaps not, I played for a while with text from WikiHow
translating it into Czech and everything seemed appropriate to me.)

Lower performance for some languages and social groups is explicitly assessed
in the survey. Even though I would say, this is what multilingual research is
mostly about, I can still imagine that people would use unreliable models
transferred into languages where they do not work well without considering it.

## Information hazards

One of the information hazards is leaking or inferring private information from
the training data. The same holds for multilingual models. There is a similar
risk (although probably much smaller) for machine translation too. A [2020
paper from JHU](https://aclanthology.org/2020.tacl-1.4/) shows that it might be
possible to detect if a sentence was part of the training data, even though it
is very hard.

## Misinformation harms

The next part of the report is dedicated to the risk that the language models
would provide false or misleading information. The models can disseminate false
or misleading information from the training data, cause harm by incorrect
answers (e.g., in law or medical domain), or lead users to perform unethical or
illegal actions. Plenty of misinformation, superstitions, and urban legends are
repeated so often that language models will happily repeat them.

As in the previous case, multilingual language models have the same problems
plus many more. Again, we need to deal with the issue that many social,
cultural, and legal norms differ across cultures. The correct answer to the
question: "Is it OK when a two-year-old kid is naked on a public beach?" is "It
depends on in what country." However, my guess is that the model will be more
prone to answer yes or no. In short: what is true for speakers of one language
(being part of one culture) might not be true for speakers of another language
(being part of another culture).

In machine translation, there is always a risk of inaccurate translation that
can potentially deceive the reader (e.g., by dropping a negation). In
particularly fluent translations might make the reader think that everything is
alright even though it is not.

## Malicious uses

Language models can make the spread of disinformation cheaper and more
effective and frauds and scams easier. Obviously, being able to do this in
multiple languages simultaneously will can increase the reach of disinformation
and scams.

Another malicious use case discussed by the DeepMind report is illegitimate
surveillance and censorship. The few-shot learning ability of current language
models makes it easier than ever to do things such as detect text that talk
negatively about a particular event. One of the most important capabilities of
multilingual models is enabling tasks that we can do in high-resource languages
in low-resource languages too. Good multilingual models could be a valuable
tool for authoritarian regimes targeting ethnic minorities and good
low-resource machine translation too.

## Summary

Basically, everything that the report mentions holds also for multilingual
models and partially also for machine translation. The dominance of western
languages in the training data and different representations of different
cultures in the training data can be a reason for many other problems compared
to monolingual models.
