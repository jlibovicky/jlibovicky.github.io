---
layout: post
title: Further, faster, stronger, dear AI
---

__[Česká verze příspěvku](/2017/05/29/Souteze.html)__

Since I was a little boy, I was astonished how weird sport biathlon is. I
couldn't imagine how could someone possible invent a combination of
cross-country skying and shooting. It blew my mind when I found out there is
even weirder combination of disciplines called [modern
pentathlon](https://en.wikipedia.org/wiki/Modern_pentathlon). With this
preparation, it was no surprise that there exist annual competitions in machine
translation and many other even weirder and more specialized tasks in computer
science.

# The AI combats

There are many computer science competitions in fields that could be called
artificial intelligence and more and more appear every year. The (cynical)
reason is simple – more and more computer scientists (and scientists in
general) in the world demand to satisfy their urge to compete with each other.
The more competitions and more specialized, the bigger is your chance to win.
Not every competition looks like when [Deep
Blue](https://en.wikipedia.org/wiki/Deep_Blue_versus_Garry_Kasparov) or
[AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol) try to beat
the champions of the most difficult board games, which typically ends with
exaltation and jubilation of the engineers in front of journalists' cameras in
a room conspicuously similar to NASA mission control center.

The competitions are less spectacular and dramatic. While announcing a
competition, organizer typically provide the competing teams with the training
data (system inputs and expected outputs), which they can train the system on,
and some test data and evaluation methodology (or software) they can be used
for an independent test of the system performance. The data that will be used
for the final evaluation are kept in secret, so the teams cannot cheat by
tailoring the system to the test data (or even memorizing the expected
outputs).

In case of the already mentioned machine translation, the training data are
publicly available bodies of text, so called parallel corpora – files of
millions or even billions sentence pairs which are translations of each other.
They are either crawled automatically from the web or they can be proceedings
of various European or international institutions. The test data are newspaper
stories collected and translated for the particular year of the competition.

Machine translation is not the only task computer scientists compete in. Some
of them are very specialized tasks, hardly comprehensible of a non-expert. On
the other hand, there some practical tasks and some them were able to achieve
quite a lot media attention. In 2009, video streaming service provider Netflix
held [a competition in predicting user rating for
movies](https://en.wikipedia.org/wiki/Netflix_Prize) based on the user's
history and preferences of other users.  Quite popular are also competition in
[robotic football](https://en.wikipedia.org/wiki/RoboCup) or [DARPA Grand
Challenge](https://en.wikipedia.org/wiki/DARPA_Grand_Challenge), a competition
of autonomous car. By the way, in the first round, in 2004, all the cars get
lost or broken and none of them was able to beat the 240 km long route in
Mohave desert. Today's autonomous car already start to be capable of orienting
in urban traffic.

# To compete or not to compete?

Holding the competitions have many apparent advantages. Most of the research
papers focus on narrow and isolated aspects of the problems and tend to neglect
the overall view on the problems. A typical conclusion of a paper utilizing
machine learning is: we invented a smart model which improves performance of a
baseline model in some aspects. A mutual influence of the individual
improvements is not usually considered to be interesting from a research
perspective as inventing a new model, you can just try it and see (pure
engineering, no science in there). There are also things that “everybody
knows”, so there is need to write about it. For instance a combination of more
slightly different models usually leads to better results because they also
have slightly different distribution of errors. It has been proven long time
ago, so there is no need to spend the valuable researchers time on trying it.

On the other hand, if it is a competition, every trick that improves the
performance comes handy. No one no longer cares about the novelty of the
approach – the only goal is to use the know-how obtained by reading and
publishing research papers to do the best engineering job possible.

The competitions have drawbacks as well. If the researchers would accept their
rank in a competition as a main measure of their success, it could happen that
they their institute would gradually exchange research for pure development.
Even though they could win the competitions, the scientific impact of their
work would be rather low.

Another problem the competitions suffer with is the fact that no metric is
perfect and in many cases such as sentiment analysis or word similarity, a good
metric cannot exist in principle, still you need to measure the performance
somehow. You can gain an advantage in the competition by greedily optimizing
towards the competition metric, even though it may not correlate with how
people perceive the task. In machine translation, it even led to creating
another competition, not in the automatic translation itself, but in measuring
the quality of the automatic translation. The participants try to develop such
a metric that correlates the most with how humans perceive translation quality
– which needs to be measured as well and it quite unclear what is the best way!
Luckily, there is no competition in measuring the quality of measuring the
quality of machine translation (yet).

Finding a weakness of the competition evaluation process can lead to success
even though it totally misses the objective the competition tries to follow.
An excellent example could be the [Turing
Test](https://en.wikipedia.org/wiki/Turing_test) which has been for a long time
considered to be criterion of AI being really intelligent. A system passes the
Turing Test if it is able to chat with a human in such a way that the human is
not able to tell whether he or she talks to another human or a computer
program. The first and the only one system that passed this test was a project
of two Russian programmers in 2014. It fooled the judges by pretending, it was
[a thirteen-years-old boy from Ukraine who was not a native speaker of
English](https://www.theguardian.com/technology/2014/jun/08/super-computer-simulates-13-year-old-boy-passes-turing-test).
Obviously, winning the competition in this way shows more intelligence of the
authors than intelligence of the program itself.

When a competition gets established in the scientific community with its
standard datasets and standard metrics, researchers may continue to take part
even though, the problem does have to be as relevant as in the time the
competition started. This is in my point of view the case of [Dialog State
Tracking Challenge](http://workshop.colips.org/dstc5/). The goal of the
competing systems is to find out what is the goal of a user of a spoken dialog
system (e.g., find out when the next tram arrives). The design of the task
assumes a decomposition of the dialog system which was invented ten years ago
and is quite different from what the current smart assistants like [Google
Home](https://madeby.google.com/home/) or [Amazon
Echo](https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-WiFi-Alexa/dp/B00X4WHP5E)
look like. Ideas about the systems design has changed with the advent of deep
learning and with experience from production deployment of such systems,
however new rounds of the challenge start every year.

# Kaggle

This maybe surprising competitiveness of AI researchers and engineers has been
used by company [Kaggle](https://www.kaggle.com) with a very interesting
business model. It runs a server that holds competitions in various machine
learning problems open for broad public. Kaggle's clients are businesses that
can come up with a machine learning problem and list a reward for the best
solvers.

These could be problems like [automatic labeling of YouTube
videos](https://www.kaggle.com/c/youtube8m) or [searching satellite pictures
for places where the Amazon rain forest is being
destroyed](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space).
In addition to commercially motivated problems, there are also competitions on
the server to help programmers learn how to work with machine learning, as well
as problems motivated more academically.

Kaggle was founded in 2010 and since that time, it gathered a community of 536
thousand registered users and supposedly [earned 12.5 million
dollars](https://www.crunchbase.com/organization/kaggle#/entity). The company
was recently [bought by
Google](https://techcrunch.com/2017/03/07/google-is-acquiring-data-science-community-kaggle/)
and became a part of the Alphabet holding.

# An infinite list of competitions

I spent 30 minutes by googling to get an idea how many AI competitions for
scientific community are out there. I was certainly biased towards natural
language processing (moreover other fields do not use the term _shared task_
which makes the search easier), so most of the are language oriented. Here is
what I found. (By the way, in the Olympic Games, there are just 28 sports with
300 disciplines).

* [automated syntactic sentence
  analysis](http://universaldependencies.org/conll17/) in 45 languages

* [surface discourse
  analysis](https://aclweb.org/anthology/K/K16/K16-2001.pdf),
  detection of relations between sentences and paragraphs

* [text recognition from photographs and videos](http://rrc.cvc.uab.es/)

* [recognition of text in historical prints](http://icdar2017hba.litislab.eu/)

* [analysis of medieval
  manuscripts](http://diuf.unifr.ch/main/hisdoc/icdar2017-hisdoc-layout-comp)

* [recognition and detection of object in photographs and
  videos](http://www.image-net.org/challenges/LSVRC/) – the cradle of deep learning

* [visual question answering](http://visualqa.org/challenge.html) – Questions
  like: “What is the man in the picture wearing.” Answer: “Trousers.”

* [automated Chinese language
  processing](http://tcci.ccf.org.cn/conference/2017/cfpt.php) – word
  segmentation, part-of-speech tagging, information search

* [word inflection](http://ryancotterell.github.io/sigmorphon2016/) given the
  base form, case, number etc.

* [resolving language
  coreference](http://corbon.nlp.ipipan.waw.pl/index.php/shared-task/) –
  finding out what pronouns in text refer to

* [detection and automatic correction of spelling and grammar
  mistakes](http://www.comp.nus.edu.sg/~nlp/conll13st.html)

* [native language identification of English speakers from text and
  speech](https://www.aclweb.org/portal/content/2017-shared-task-native-language-identification)
  – This should be a nightmare of everyone taking the TOEFL exam. Everything
  you say or write can be used training data in this competition.

* [fake news detection](http://www.fakenewschallenge.org/)

* [emotional analysis of social network
  post](http://saifmohammad.com/WebPages/EmotionIntensity-SharedTask.html)

* [identification of a speaker on a
  recording](http://www.speech.sri.com/projects/sitw/)

* [semantic similarity of words](http://alt.qcri.org/semeval2017/task2/) both
  within a language and across languages

* [sentiment analysis of Twitter posts](http://alt.qcri.org/semeval2017/task4/)

* [humor detection on Twitter](http://alt.qcri.org/semeval2017/task6/)

* [keyword and key phrase extraction from scientific
  publications](http://alt.qcri.org/semeval2017/task10/)

* [face recognition from
  photographs](http://www.face-recognition-challenge.com/)

* [AI for video games playing](http://www.gvgai.net/)

And by the way, chess-box is an interesting sport as well:
<iframe width="560" height="315" src="https://www.youtube.com/embed/kK5TQSKmS3o" frameborder="0" allowfullscreen></iframe>
