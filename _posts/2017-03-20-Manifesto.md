---
layout: post
title: Computational Linguistics in the 21st century – a private manifesto of its perpetual student
---

In this essay, I would like to sum up my opinions on what is the role of
computational linguistics, why should people concern with it and I believe are
its current problems, and most importantly why it is a very exciting field of
study.

Computational linguistics is a something between a research and an engineering
field whose goal is to use mathematical models to describe natural languages
(like English or Czech, not e.g., programming languages) and come up with
technological applications of these models. Due to these goals it is necessary
a multidisciplinary field which combines something from classical linguistics,
artificial intelligence, mathematics and software engineering.

The attempts for automatic processing of natural languages are with us from the
early days of artificial intelligence. After all, the famous _Turing test_,
which is sometimes considered to be a criterion of artificial intelligence
being really intelligent, assumes that an intelligent machine must be able to
communicate in natural language. The artificial intelligence took a different
direction in the last 50 years – most importantly it focused on attempts to
model some of the most basic human cognitive abilities and development of
intelligent agents trying to meet some objectives in an environment.
Computational linguistics with its effort to model language without general AI
sitting in the background got established as a standalone research discipline.

In the last thirty years, computational linguistics undergone a fascinating
development when it transformed from an almost obscure research field into to
solving practical engineering problem. At the same time, it somehow diverged
from its parent field – formal linguistics whose goal is to use formal
(algebraic) apparatus to describe language phenomena. It diverged so much that
it seems that the fields can hardly enrich each other anymore, which is
according to me a big shame and pity.

# Linguistics as Almost a Natural Science

Contemporary linguistics stressing descriptive (describes the phenomena as they
are and does not prescribe how they should look like) and synchronous view
(describes the current state of language and disregards the history the
language user don't need to know to use speak) of language is very similar to
natural sciences. This is also a suitable view for technological applications.
When I am building a machine translation system, I don't care so much how
people should spell something and what are the historical reasons for that,
what I need to know is how do the sentences they the users want to translate
look like.

Linguists usually use so called language corpora for their theoretical work.
These are databases of texts collected form various sources. Mostly, they are
newspaper and magazine texts (journalists are generating loads of text every
day) and both fiction and non-fiction books. Linguists try to collect data also
from the other types of language use, including for instance spontaneous speech
or communication on social networks. In addition to that, various phenomena are
either manually or automatically annotated in the texts, such that the
linguists can analyze them both quantitatively and qualitatively. For
acceptance of a scientific hypothesis, it is no longer important to persuade
other linguists with their language intuition, but statistical significance of
explaining the phenomenon in the corpus.

Natural sciences often methodologically rely on some version of Karl Popper's
critical rationalism. What is important for scientific hypotheses is their
openness to future falsification. We consider a scientific theory to be valid
if it has not been empirically (usually experimentally) falsified even though
scientists have tried as hard as they could. The theory is considered valid
until some contradictory observation are made, but in some sense it remains
valid even after they are falsified. Discovery of the theory of relativity of
course didn't make fall all bridges whose stability had been computed using
Newtonian mechanics. It didn't even change the way, the stability of bridges is
nowadays computed (except that [slide
rules](https://en.wikipedia.org/wiki/Slide_rule) was replaced by computers).
To summarize, if a scientific theory is in contradiction with the empirical
observations, scientists need to search a for a new theory that will explain
the observations in a more precise, indisputable and more elegant way.

Linguistics works very similarly to natural sciences in this manner. It tries
to build such theories that could be statistically tested on the collected
observations – language corpora. In addition to that, they collect more and
more data which can potentially show some problems in the current theories.

# Theories considered “real”

Scientific theories often come up with theoretical entities which can seem very
bizarre at the time of their discovery, but after some time start to believe
they are real – not only the scientific community, but also the public.

For acceptance of newly postulated theoretical entities in the scientific
community, it is important that it elegantly solves problems they had in the
previous theoretical framework of the field. Assumption of a new entity allows
explaining previously inexplicable observations, or explaining something more
exactly or more elegantly.

For the public, there needs to be something more for the theory to get
accepted. For instance, the superstring theory explains very well many
experiments in the contemporary physics. In spite of that, the idea of living
in the eleven-dimensional space with seven dimensions tangled up in themselves
is not how public thinks about reality. On the other hand, nobody is surprised
by the fact that the matter around is “in fact” empty space with elementary
particles occasionally flying around. No one cares that this “reality”
contradicts the natural experience with the world in the same way as seven
spacial dimension mysteriously tangled up in themselves.

What I believe is crucial for public acceptance of scientific theoretical
entities is existence of technological application which are based on the
theories. Unlike the theoretical entities, the technological artifacts are part
of our everyday reality. Hardware of the computer I am right now using to write
this text is based on technologies which are unthinkable without assuming
existence of elementary particles. Knowledge of the theory of relativity
allowed us to develop satellite communication and navigation. Without it I
would hardly believe that if would travel with a speed close to the speed of
light, the time will run in different pace for me than for those who stayed
home.

Technology is a visible and concrete part of our everyday experience – because
of that we can't easily ignore the theoretical concepts behind them. Maybe
because of that some people can easily deny the existence of global warming or
Darwinist evolution which can in principle never be an underlying technology of
a technological innovation.

# Linguistics and Technology

Some twenty of twenty-five years ago, it may have seemed that the automatic
natural language processing can provide the same assurance of the truth to the
theories as engineering innovations provide to the theories in physics.
Methods of natural language processing used linguistic theories during the
development and the source code was usually pack with a lot of explicit
linguistic knowledge. At the beginning of the 21st century, it started to
appear that machine-learning based systems learning from the annotated data
worked better than those where the programmers tried to put the linguistic
knowledge explicitly in the source code. With the increasing availability of
the data and computational power, the required amount of linguistic knowledge
was gradually decreasing. At this moment, complicated systems as automatic
speech recognition, machine translation or text summarization are trained from
the data end-to-end with no linguistics inside. The technologies found their
own way, working totally independently of the language understanding provided
by linguistics.

Nowadays, we are in a unique situation where the language technologies live
outside of the conceptual framework provided by classical linguistics which has
some paradox consequences. Results of the experiments in physics can be
predicted using the theory. However, when we do deep learning experiments in
computational linguistics, there is no theory that could in advance say what
the results will be. There is only the researcher's or developer's (usually
strongly mathematically grounded) intuition which is either confirmed or not.
Often, it may seem that the researcher has prepared arguments for both success
and failure of the experiments and only waits for the results of the
experiments.

The almost miraculous success of deep learning methods in natural language
processing is so important to me, that if I were asked how languages are like,
I would certainly answer they are exactly such that they can be efficiently
processed by artificial neural networks. I don't know what exactly it means and
unfortunately, linguistics has no answer for that.

I don't want to claim linguistic theories are useless. They provided a
conceptual framework without which any meaningful discussion about language
would even be possible. Linguistic theories prove their usefulness when we want
talk about some complex language phenomena and provide invaluable service while
learning both mother tongue and foreign languages. Their usefulness, however
seems to vanish when we try to use them for automatic processing. Somehow
similarly, the Newtonian physics is a great tool for engineering. Given strange
circumstances when objects move at very high speeds, the use of the theory
starts to be very limited. It would be great if linguistics could find its
unifying theory that could be used both as a basis for technological
applications and have the same descriptive power as the current linguistic
theories.

# What to Do with Computation Linguistics

While doing computational linguistic, we need to take care of what is becoming
a pure engineering which is usually done more efficiently by private companies
and aim the public support to project trying to answer interesting questions
which are not of primary interest of the enterprises. Computational linguistics
is experiencing something similar to astronautics twenty years ago. The
exclusive government-funded engineering field became a technological business
as any other. Private communication satellites are flying around the globe,
although the outset of space technology wouldn't be possible without generous
public support.

I believe that public support is crucial for development of complex
technologies. The Internet has its origin in an U.S. army project. The success
of deep learning would be possible without long-lasting generous support of
Canadian government. On the other hand, it is important to capture the right
moment when the public support is no longer indispensable for the technology as
for instance in case of the satellite communication.

It is no longer true that machine translation is a basic research, whose public
support can bring groundbreaking results. It is neither automatic syntactic
analysis, nor speech recognition – these are all well-managed engineering tasks
where big technological companies have better results than academic
institutions. Improving the performance of the application doesn't have to be
to main part of computational linguists' work. Working on application have of
course the advantage that you can easily show some quantitative progress.
Reducing error rate in an application is a clear result you can report to grant
agency – which is doable until the grant agency eventually finds out that what
you do is no longer basic research but pure development. (And being a developer
is a great intellectual adventure as well!) This situation is also convenient
for the companies – publicly funded research generates innovation which they
can easily monetize.

It does not mean that computational linguistic as a research field should leave
academia and move to entirely to industry. In fact, academic computational
linguists should be happy that they no longer need to focus on technological
innovations (and if they want, they have where to go). The researchers have now
a unique chance to use and develop the technologies in such a way that would
gather new observation about language that will eventually lead to new
linguistic theories that would play the role of the current linguistic theories
and explain the experience which we get from the automatic natural language
processing.

Moreover, computational linguistics experts are still needed in academia to
train new generations of experts and via they public activity ensure that there
will be always public control over the new technologies and their potential
misuse.
