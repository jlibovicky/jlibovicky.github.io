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
people perceive the task.
To vedlo v oblasti strojového překladu k tomu, že se kromě
samotného překladu soutěží i v tom, jak automaticky měřit kvalitu strojového
překladu tak, aby co nejvíce odpovídala lidskému hodnocení. Kvalitu těchto
metrik je ale potřeba nějak měřit. Soutěž v tom, jak měřit kvalitu měření
kvality strojového překladu se ovšem zatím nekoná.

Ten, kdo najde slabinu hodnocení, může uspět, přestože se mu ve skutečnosti
vůbec nepodaří vyřešit úlohu, o kterou v soutěži primárně jde. Příkladem toho
může být soutěž v tvz. Turingově testu. Turingovým testem, který byl poměrně
dlouho považován za kritérium "inteligentnosti" umělé inteligence, projde
takový systém, se kterým se dá chatovat takovým způsobem, že člověk nerozezná,
zda na druhé straně sedí člověk nebo počítačový program. To se skutečně v roce
2014 podařilo, když porotce dokázal zmást program, který předstíral, že je
[třináctiletý chlapec z Ukrajiny, který není rodilý mluvčí
angličtiny](https://www.theguardian.com/technology/2014/jun/08/super-computer-simulates-13-year-old-boy-passes-turing-test).
Způsob, jakým toho program dosáhl nevypovídá ani tolik o inteligenci programu
samotného jako jeho autorů.

Když se soutěž ve vědecké komunitě etabluje, může se stát se na jejich
standardních datech se standardními metrikami soutěží nadále, přestože samotný
soutěžní úkol pozbyl vědecké i praktické relevance. To je podle mě případ
soutěže ve [sledování stavu mluveného
dialogu](http://workshop.colips.org/dstc5/). V soutěži se měří to, jak dobrou
má systém představu o tom, jaký je cíl uživatele, který telefonu s dialogovým
systémem (člověk si chce třeba koupit lístek do kina, nebo zjistit kdy mu jede
příští tramvaj z Náměstí bratří Synků). Podoba soutěžního úkolu vychází z toho,
jak bylo před deseti lety zvykem dekomponovat architekturu dialogového systému.
To se s nástupem takzvaného hlubokého učení výrazně změnilo, přesto se vypisují
další a další kola této soutěže.

