---
layout: post
title: Further, faster, stronger, dear AI
---

__[Česká verze příspěvku](/2017/04/14/Shared-tasks.html)__

Since I was a little I was astonished how weird sport biathlon is. I couldn't
imagine How could someone possible invent a combination of cross-country skying
and shooting. I blew my mind when I found out there is even weirder combination
of disciplines called modern pentathlon. With this preparation, it was no
surprise that there exist annual competitions in machine translation and many
other tasks.

# The AI combats

There are many computer science competitions in fields that could be called
artificial intelligence and more and more appear every year. The reason is
simple - more and more computer scientists (and scientists in general) in the
world demand to satisfy their urge to compete with each other. Not every
competition looks like when [Deep
Blue](https://en.wikipedia.org/wiki/Deep_Blue_versus_Garry_Kasparov) or
[AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol) try to beat
the champions of the most difficult board games, which typically ends with
exaltation and jubilation of the engineers in front of journalists' cameras in
room conspicuously similar to NASA mission control center.

The competitions are less spectacular and dramatic. While announcing a
competition, organizer provide the competing teams with the training data
(system inputs and expected outputs), which they can train the system on, and
some test data and evaluation methodology (software) they can used for an
independent test of the system performance.  The data that will be used for the
final evaluation are kept in secret, so that the teams cannot cheat by
tailoring the system to the test data.

In case of the already mentioned machine translation, the training data are
publicly available so called parallel corpora - files of millions or even
billions sentence pairs which are translations of each other. They are either
crawled automatically from the web or they can be proceedings of various
European or international institutions. The test data are newspaper stories
collected and translated for the particular year of the competition.

Machine translation is not the only task computer scientists compete in. Some
of them are very specialized tasks, hardly comprehensible of an non-expert. On
the other hand, there some very practical tasks and some them were able to
achieve quite a lot media attention. In 2009, video streaming service provider
Netflix held [a competition in predicting user rating for
movies](https://en.wikipedia.org/wiki/Netflix_Prize), based on other the user's
history and preferences of other users. Quite popular are also competition in
[robotic football](https://en.wikipedia.org/wiki/RoboCup) or [DARPA Grand
Challenge](https://en.wikipedia.org/wiki/DARPA_Grand_Challenge), a competition
of autonomous car. By the way, in the first round, in 2004, all of the cares
get lost none of the competing cars was able to manage 240 km in Mohave desert.
Today's car are able to orient in urban traffic.

# To compete or not to compete

Holding the competitions have many apparent advantages. Most of the research
papers focus on narrow and isolated aspects of the problems and tend to neglect
the overall view. A typical conclusion of a paper utilizing machine learning
is: we invented a start model which improves performance of a baseline model on
is some aspects. How the individual improvements influence each other is not so
interesting from a research perspective as inventing a new model. There also
thing that "everybody knows", so there is need to write about it. For instance
a combination of more slightly models usually leads to better results because
they have slightly different distribution of errors. Everyone knows it, and
many people may feel there is no need to spend the valuable researchers time on
trying it.

On the other hand, if it is a competition, every trick that improves the
performance comes handy. No one no longer cares about the novelty of the
approach - the only goal is to use the know-how obtained by reading a
publishing research papers to do the engineering job possible.

The competitions have drawbacks as well. If the researchers would accept their
rank in a competition as a main measure of their success, it could happen that
they start their institute would gradually change research for pure
development. Even though they could win the competitions, their scientific
impact would be rather low.

Another problem the competitions suffer with is the fact that no metric is
perfect. You can gain an advantage in the competition by greedily optimize
towards the competition metric, even though it does not correlate with how
people perceive the task. In machine translation it even led to creating
another competition, not in the translation itself, but in measuring the
quality of the translation. The participants try to develop such a metric that
correlates the most with how humans perceive translation quality - which needs
to be measured as well! Luckily, there is no competition in measuring the
quality of measuring the quality of machine translation.

Finding a weakness of the competition metric can lead to success even though it
totally misses the objective of the competition tries to follow. An excellent
example could be so called Turing Test which has been for a long time
considered to be criterion of AI being intelligent. A system passes the Turing
Test if it is able to chat with a human in such a way that the human is not
able to tell whether he or she talks to another human or a computer program.
The first and the only one system that passed this test was a project of the
Russian programmers in 2014. It fooled the judges by pretending, it was [a
thirteen-years-old boy from Ukraine who was not a native speaker of
English](https://www.theguardian.com/technology/2014/jun/08/super-computer-simulates-13-year-old-boy-passes-turing-test).
Obviously, winning the competition in this way does not shows more intelligence
of the authors than intelligence of the program itself.

When a competition gets established in the scientific community with its
standard datasets and standard metrics, researchers may continue to take part
even though, the problem does have to be as relevant as in the time the
competition started. This is in my  point of view case of [Dialog State
Tracking Challenge](http://workshop.colips.org/dstc5/). The goal of the
competing systems is to find out what is a goal of a user of a spoken dialog
system (e.g., find out when the next tram arrives). The design of the task
assumes a decomposition of the dialog system which was invented ten years ago.
This has changed with the advent of deep learning, however new rounds of the
challenge start every year.

# Kaggle

This maybe surprising competitiveness of AI researchers has been used by a
company [Kaggle](https://www.kaggle.com) with a very interesting business
model. This server holds competition in various machine learning problems
accessible for broad public. Kaggle's clients can come up with a machine
learning problem and list a reward for the best solvers. These are problems
like [automatic labeling of YouTube
videos](https://www.kaggle.com/c/youtube8m), [searching satellite pictures for
places where the Amazon rain forest is being
destroyed](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space).
In addition to commercially motivated problems, there are also competitions on
the server to help programmers learn how to work with machine learning, as well
as problems motivated more academically.

Kaggle was founded in 2010 and since the time, it gathered a community of 536
thousand registered users and supposedly [earned 12.5 million
dollars](https://www.crunchbase.com/organization/kaggle#/entity). The company
was recently bought by
[Google](https://techcrunch.com/2017/03/07/google-is-acquiring-data-science-community-kaggle/)
and became a part of the Alphabet holding.

