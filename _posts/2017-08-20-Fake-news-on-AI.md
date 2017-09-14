---
layout: post
title: Fake news on AI
---

__[Česká verze příspěvku](/2017/05/29/Fake-news-o-AI.html)__

While reading news stories about research or products involving deep learning,
I get often astonished how inaccurate and misleading the news stories are.
Very likely, the same feeling must have doctors, flight engineers and other
experts reading articles on their field.

News stories are competing the get our attention in a world where so many
things to do. There the news stories that appear in the news must satisfy some
criteria to even get chance to attract the readers' attention, these are often
call [news values](https://en.wikipedia.org/wiki/News_values).

It is obvious, the news must be simplified and put in a shape that fits the
news values. This why the media tend to avoid complicated technical terminology
with something more familiar to the readers -- in this case the terminology
often comes from science fiction literature. Sci-fi books and movies about AI
often re-narrate a myth about the mankind getting into existential trouble by
not reflecting the potential of a recent technology. These are either machine
getting self-awareness or some kind of villain using the technology to conquer
the world.

These associations of course make the news stories more attractive and make the
technologies more popular among the public, on the other hand it makes false
expectations both in terms of use and possible misuse of the technologies.
Public discussion is misdirected towards hypothetical risks and overlooks the
real ones.

In this post, I would like to discuss some of these misconceptions and highlight
what are the main risks these emerging technologies pose.

# Neural Network Simulates Brain

Terms _artificial intelligence_ and _neural network_ stand at the beginning of
the conceptual misunderstanding. The word _intelligence_ (no matter what
intelligence means in general) makes a false impression that AI is something
comparable to human intelligence. Indeed, AI algorithms perform tasks which
require some cognitive effort like speech recognition or playing Go, however
these algorithms can always do one thing.

The term _neural network_ makes a false impression that the goal the algorithms
simulate human brain. Artificial neural network originated from computational
simulation of what scientists believed could be a simplified model of a
biological neuron. Not only is the model no longer consider biologically
plausible, but it has been abandoned by the computer scientists as well.
Artificial neural networks are no longer conceptualized as networks of
individual neurons, but as network of so called _layers_ with purely algebraic
intuition.

One of the evergreen of popular articles mentioning deep learning is comparison
to human or animal brains.  Marketing of technology companies with brands like
_Google Brain_ or _Google Deepmind_ then only deepen these misconception.

https://www.nytimes.com/2016/12/14/magazine/the-great-ai-awakening.html?mcubz=0

# Google's Machine Translation Developed its Own Language

https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html

# Facebook's AI Grew out of Control, so they Had To Stop It

One weakness of current models natural language processing is that they model
_how does the language look like_. Language is mostly a means of communication.
Almost everything that we say with some intention: entertain someone, make
someone angry, tell the world what is the right thing to do or buy a postage
stamp. Knowing how the language look like may be good enough when you do
machine translation, but when you want a program to negotiate about something,
intentionally following the goal you want to achieve sounds like a better
strategy that simulating what other people usually say in similar situations.

The goal of Facebook's experiment was train models that will be able to achieve
some communication goals. (Machine translation in )

What actually happened was that the machines were able to find a code that may
be efficient for negotiating about the price of apples, but does not resemble
human language at all. If we think of it more deeply, it is actually no
surprise. Human language is not probably the most efficient code for
negotiating the prices of apples, but it has many other fascinating properties:
we can write poems in it, tell jokes, etc.

https://www.forbes.com/sites/tonybradley/2017/07/31/facebook-ai-creates-its-own-language-in-creepy-preview-of-our-potential-future

Recently a similar result has been presented, a similar result has been
presented on experiments with a more controlled language whose goal was

# Why are these News Dangerous

The way media talk about AI technologies (even the usage of the term AI, what
will say when we will have _real_ intelligence?!) intentionally resembles the
way AI is depicted in the sci-fi literature and movies. Illustration photos in
the news stories usually come from the movies.

_TODO: some examples_

This might be what makes the stories more attractive to the users, but it is
highly misleading while talking about the potential risks of AI because the
sci-fi conceptualization tend to make us think about sci-fi risks. What comes
to our minds are technology getting out of control eventually exterminating
humanity or a super villain using the emerging technology to conquer the world.
The risk are in fact earthbound well-known problems that has been here since
ever: criminality, power struggle and careless way of doing business.

Recently, Elon Musk initiated an important discussion on possible misuse of AI
in the weapon industry. However, the more closer risk are different. What I
would worry the most is criminal abuse. I can imagine robots crawling web and
finding opportunities for blackmailing people (matching faces from LinkedIn
images with some or wild parties photos). There are endless opportunities to
make better and more personalized [advance-fee
scams](https://en.wikipedia.org/wiki/Advance-fee_scam).

Compromising peoples privacy is another big issue. Recently, Stanford university
researchers published a method for estimating sexual orientation exclusively
from images.

Deep learning models are always optimized towards an objective that is
necessarily agnostic to everything except the objective. This problem has been
popularized by the though experiment of [paperclip
maximizer](https://wiki.lesswrong.com/wiki/Paperclip_maximizer) in which general
AI is deployed in a factory producing paperclips with the only objective:
producing as many paperclips for as low price as possible, eventually turning
the entire solar system into a paperclip factory.

The risk are not as fatal as in this though experiment and therefore maybe less
interesting for media, but are based on the same principle.
