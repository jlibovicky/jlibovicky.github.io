---
layout: post
title: Fake news on artificial intelligence
---

__[Česká verze příspěvku](/2017/05/29/Fake-news-o-AI.html)__

While reading news stories on research or products involving deep learning, I
get often surprised how inaccurate and misleading the news stories are. It is
probably a problem of almost all expert fields which happen to appear in media,
luckily they do not bother me as much as AI.

News stories compete the get our attention in a world with so many things to
do. They need to win the never-ending fight for our attention with our work,
Facebook posts, friends, family, books you want to read—and that is not an easy
task at all. Media scientists claim the news must satisfy some criteria to even
get a chance to attract the readers' attention, these are called the [news
values](https://en.wikipedia.org/wiki/News_values). In case of AI news, these
are most importantly cultural proximity (technologies have a stable place in
our culture), unambiguity (everyone knows what technological progress is and
what it is good for) and possibility to personalize the news stories (both
through stories of its developers and stories of the technology users) what
makes the news attractive enough.

Obviously, the news must be simplified and put in a shape that fits the news
values. Media indeed need to avoid complicated technical terminology and
replace it with something that is more familiar to the readers—in this case,
the terminology and metaphors often come from science fiction literature.

Unspoken connections between emerging technologies and sci-fi genre of course
make the news stories more attractive and help to make the technologies more
popular among the public. On the other hand, it raises false expectations both
in terms of possible use and misuse of the technologies. Public discussion is
misdirected towards hypothetical problems and overlooks the real ones. Books
and movies about AI often re-narrate a myth about the mankind getting into
existential trouble by not reflecting the potential of a recent technology,
always showing the same conceit, self-admiration and arrogance as in old
stories about [Golem](https://en.wikipedia.org/wiki/Golem), [doctor
Faust](https://en.wikipedia.org/wiki/Faust) or [doctor
Frankenstein](https://en.wikipedia.org/wiki/Frankenstein) (have you ever notice
how often the bad guys have academic degrees?).

In this posts, I try to illustrate this on two examples from this year.

# Google's Machine Translation Developed its Own Language

At the end of 2016, Google published a study showing how their neural machine
translation models can be modified in such a way that a single model is capable
of translation between multiple language pairs at the same time. Moreover, it
is supposed to work not only for the language pairs it was trained for, but
also language pairs that were never seen during the training, as illustrated on
a scheme from [Google Research
Blog](https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html).

![Google's Zero-Shot Translation](/assets/google_zero_shot.gif)

Nowadays, we need a separate model for every single language pair, and for some
of them there is only little bilingual texts that can be use for the model
training. If this worked properly, it would be a major advance in machine
translation. However, this did not happen. The results are interesting from the
theoretical perspective, but the performance of presented models is by large
margin worse than what are users of Google Translate used to. In fact, they
more resemble machine translation attempts from the early days of its research.

Many news servers called the input representation the models had to learn as
_interlingua_ which is a hypothetical common meaning representation that should
be the same for all the languages, an ultimate analysis of a sentence (which I
doubt is even theoretically possible). This news has been reported even by the
most read technology news servers:

* [Wired.com, 23.11. 2017: Google's AI just created its own universal
  'language'](http://www.wired.co.uk/article/google-ai-language-create)

* [TechCruch.com, 22.11. 2017: Google’s AI translation tool seems to have
  invented its own secret internal
  language](https://techcrunch.com/2016/11/22/googles-ai-translation-tool-seems-to-have-invented-its-own-secret-internal-language/)

The articles not only do not mention that the translation was useless for any
practical purposes, but they also make a false impression that the intermediate
representation that the system uses is something that can be used a language.
News stories like this in fact tell the readers that current neural networks
are so intelligent that they can not only use human language, but they are
capable of inventing a new, presumably better language. This may sound a little
worrying because, this is an ability that we would normally attribute only to
an autistic genius. In fact, the representations the system uses are tables
with thousands of real numbers for which we have no direct interpretation. It
also has none of the properties people usually attribute to languages.

# Facebook's AI Grew out of Control, so they Had To Stop It

Most of the current models for natural language processing model only _how the
language looks like_ under different circumstances, not _how to use it_. When
we speak, we probably do not have in our mind how language looks like in the
given circumstance. Instead, we might have in our minds that we want to do
using language: entertain someone, find out what time it is, make people vote
for the Green party, pray, or buy a postage stamp. For instance, machine
translation models do not bother with that all. So far it seems, it might be
enough to teach the model how does a sentence in a target usually look like for
the given source sentence, in order to translate it (almost) correctly.

Nevertheless, if we wanted to create a program that e.g., negotiates with
someone about something, a program that intentionally follows the goal you want
it to achieve, trying to simulate what people do in similar situation does not
seem like a good strategy. Obviously, you need to know what you want to achieve
in order to achieve it. You cannot do it just by mimicking of what people
usually do when they negotiate.

During the last summer, a research team at Facebook did an experiment whose
goal was exactly this. In the experiment, they trained chatbots which were
supposed to negotiate with each other about exchanging hats, balls and books.
They used the same principle as was used for instance while training the
AlphaGo, the first system that beat humans in the game of Go. It was trained by
playing millions of games against different version of itself and improved
through trials and errors. In case of Facebook's experiments, the systems were
given some prior knowledge how users chat with each other. Their starting point
was in fact knowing how the language look like. Then, the model were improving
their negotiation skills by constantly communicating with each other. As a
result, the systems learned to negotiate efficiently with each other while
totally diverging from what they knew at the beginning. The code they have
developed for that did not resemble English at all.

The experiment got surprisingly high media coverage. Most of the news stories
were telling that Facebook had conducted an experiment with artificial
intelligence that had got out of control and therefore they had to stop it.

* [Forbes.com, 31.7. 2017: Facebook AI creates its own language in creepy preview of our potential future](https://www.forbes.com/sites/tonybradley/2017/07/31/facebook-ai-creates-its-own-language-in-creepy-preview-of-our-potential-future)

* [Independent.co.uk, 31.7. 2017: Facebook's artificial intelligence robots shut down after they start talking to each other in their own language](http://www.independent.co.uk/life-style/gadgets-and-tech/news/facebook-artificial-intelligence-ai-chatbot-new-language-research-openai-google-a7869706.html)

* [Mirror.co.uk, 1.8. 2017: Robot intelligence is dangerous: Expert's warning after Facebook AI develop their own language](http://www.mirror.co.uk/tech/robot-intelligence-dangerous-experts-warning-10908711)

* [Business Insider 21.7. 2017: Facebooks's AI accidentally created its own language](http://uk.businessinsider.com/facebook-chat-bots-created-their-own-language-2017-6?r=US&IR=T)

This time, it were the technology news servers that tried to calm down and
explain the exaggerated news from other media:

* [Wired.com, 1.8. 2017: No, Facebook’s chatbots will not take over the world](https://www.wired.com/story/facebooks-chatbots-will-not-take-over-the-world/)

* [Gizmodo, 31.7. 2017: No, Facebook Did Not Panic and Shut Down an AI Program That Was Getting Dangerously Smart](https://gizmodo.com/no-facebook-did-not-panic-and-shut-down-an-ai-program-1797414922)

If we think of it more deeply, it is actually no surprise that the code which
the systems had developed was totally different from any human language. Human
language is not probably the most efficient code for negotiating about hats,
balls and books. It has many other fascinating properties, thogh: we can write
poems in it, tell jokes, etc. We can also interpret the result of the
experiment as an argument, that talking business is not the constituting
function of language, which is at least for me good news. Facebook stopped the
experiment not because it was dangerous, but because it already delivered
results they wanted and it was useless for any practical use.

# What are the takeaways?

The way media talk about AI technologies (including using term AI) often
resembles the way in which AI is depicted in the sci-fi literature and movies
where the term means something entirely different. The problem is that while
talking about the potential risks of AI, the sci-fi conceptualization tends to
make us think about sci-fi risks. As we saw in the examples, media do it
whenever there is a story that fits into this framework in order to come up
with an attractive new story. What comes to our minds are technology getting
out of control eventually exterminating humanity or a supervillain using the
emerging technology to conquer the world.

Don't worry, none of it is in preparation, neither in Facebook nor Google labs,
neither anywhere else. After all, how could a model that estimates a
conditional probability of words in an English sentence given a sentence in a
different language conquer the world. Indeed, the technologies are going to
have a big effect on society. And should be publicly discussed, not some kind
of crazy sci-fi scenarios.
