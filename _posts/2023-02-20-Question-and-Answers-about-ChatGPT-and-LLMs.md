---
layout: post
title: "Questions and answers about ChatGPT and large language models"
tags: [popularization, en]
lang: en
---

__[Česká verze příspěvku](/2023/02/07/Otazky-a-odpovedi-o-ChatGPT-a-jazykovych-modelech.html)__

There's been a lot of media coverage of ChatGPT and language models lately, and
I feel like not everything is being said quite right. That's why I have
prepared some questions and answers that hopefully help clarify what they are
talking about.

Questions:

1. [What is a (large) language model?](#what-is-lm)
2. [What is ChatGPT?](#what-is-chatgpt)
3. [Are GPT-3.5 and ChatGPT the best things out there?](#is-gpt-best)
4. [Are there any available alternatives, ideally open source?](#open-source)
5. [How can ChatGPT speak multiple languages? Does it use machine translation?](#is-it-mt)
6. [Where does the knowledge ChatGPT has come from? Does he use a search engine?](#knowdlege)
7. [What to do about pupils and students using it in schools?](#schools)
8. [Language models have opponents who consider them dangerous technology. What's the danger?](#dange)

## What is a (large) language model? {#what-is-lm}

Mathematically speaking, a language model is a function or algorithm that, for
some text (completed or incomplete), estimates the probability of what word
will follow in the text. It is a basic tool that has been used in natural
language processing since the 1990s, originally mainly to select variants in
speech recognition and automatic translation that are more fluent and make
better sense in a given context.

Language models learn from data: from plain text, today, most often on texts
mined from the Internet. Since the 1990s, the way language models are trained
fundamentally changed several times. The available computing power and the
amount of available training data have increased dramatically. Current language
models are neural networks based on the [Transformer
architecture](https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf).
The architecture represents input words as sequences of continuous number
vectors. It alternates between classical feed-forward layers and something
called an _attention mechanism_. In these layers, the model seems to “pick”
relevant information from the input text (there is no disturbing between the
input and the generated text) to predict the next word.

The actual learning or training is done by presenting real human-written texts
to the model. The model receives training data in batches of tens of thousands
of words. With each batch, the model adjusts its parameters so that the model
considers the last batch of data a little more probable than before.  Training
can take anywhere from hours to months, depending on the size of the data and
the size of the model.

Recently, there has been a lot of talk about large language models showing
remarkable abilities that could be described as intelligent behavior. In
addition to the ability to creatively and interestingly continue texts, they
can pick up complex patterns from a few examples. This is sometimes called
_few-shot learning_. In this case, a user formulates a task (e.g. deciding if
it is a hateful post, shortening a sentence, correcting spelling mistakes,
etc.) in natural language and adds several examples of inputs and outputs. The
model then continues the pattern it picked up from the input.  Surprisingly,
language models are able to solve tasks that usually require considerable
intellectual effort.

The best-known examples are the large GPT language models from OpenAI. For an
idea of what big means: For the [training of
GPT-3](https://papers.nips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf)
published in May 2020) 45TB of text was used, which corresponds, for example,
to 37 million copies of Dostoevsky's Crime and Punishment (if spread on a
football field, they would reach a height of 4.5 meters). GPT-3 has 175 billion
trainable parameters. Each parameter is a real number whose storage requires 4
bytes. So 561 GiB of memory is needed just to store the model. Additional
memory is then needed for the calculations themselves.

## What is ChatGPT? {#what-is-chatgpt}

ChatGPT is a chatbot – a program that communicates with humans in natural
language. OpenAI launched a free [public demo](https://openai.com/blog/chatgpt)
in December 2022. There are plans to [charge
it](https://www.nytimes.com/2023/02/01/technology/openai-chatgpt-plus-subscription.html).

Technically, ChatGPT is finetuned GPT 3.5 model (an improved version of GPT 3,
for which OpenAI has not published many details) so it does not need to
get examples of how to perform tasks, but can solve them based on instructions
from the user. OpenAI used a similar principle in its InstuctGPT model, for
which a [preprint](https://arxiv.org/abs/2203.02155) was published in April
2022, which has not yet been published in any peer-reviewed proceedings.

ChatGPT training takes place in two phases: in the first phase, annotators
(workers who prepare training data for machine learning) used the GPT model to
create sample dialogues, showcasing how the chatbot should behave. By the
second stage, the system no longer directly received samples of dialogues, but
only learns through simple feedback: annotators marked answers as good or bad.
Based on this, the system improved without direct examples of correct answers.
To reduce the need for human annotations, the system's authors trained
additional neural networks to simulate the human feedback. The entire system
can then be further trained using simulated feedback without the need for human
input. Experts estimate that hundreds of thousands to millions of annotations
were needed to develop ChatGPT. According to [Time
magazine](https://time.com/6247678/openai-chatgpt-kenya-workers), OpenAI hired
agencies in English-speaking developing countries. In Nairobi, Kenya, for
example, annotators were paid between $1.32 and $2 an hour.

ChatGPT can answer questions and generate text according to user instructions
in natural language. It exhibits extensive encyclopedic knowledge, and since a
lot of source code and computer science texts were part of the training data,
it seems to be quite good at programming. This is probably the first time in
the history of computer science that a computer system has largely met popular
ideas about what artificial intelligence could or should look like. The biggest
problem with the system is that all information it provides sounds plausible,
but it does not mention any sources and is often factually wrong. When working
with ChatGPT, it is necessary to check all the facts against reliable sources.

## Are GPT-3.5 and ChatGPT the best things out there? {#is-gpt-best}

GPT 3.5 and ChatGPT are probably the best models readily available to the
broader public. But they are not the biggest and best models that exist.
Google has its PaLM model (a [preprint](https://arxiv.org/abs/2204.02311)
describing it was published in April 2022, no peer-reviewed article has been
published yet) that reportedly shows interesting capabilities that GPT-3 does
not. What resonated most on social media was the alleged [ability to
explain](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html)
jokes. Essentially the same models as the GPT-3 called Open Pretrained
Transformer (OPT) were [completely published including technical
details](https://ai.facebook.com/blog/democratizing-access-to-large-scale-language-models-with-opt-175b)
by Meta (operator of Facebook, Instagram, and WhatsApp) two years after the GPT
3 in May 2022.

Google also has the LaMDA chatbot ([January 2022
preprint](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html),
peer-reviewed article not yet published), which was trained slightly
differently from ChatGPT. It is a pure language model trained on conversations
only, i.e., without training on feedback. The LaMDA chatbot caused a stir in
the first half of 2022 when one of its developers [claimed that LaMDA was a
feeling
being](https://www.washingtonpost.com/technology/2022/06/11/google-ai-lamda-blake-lemoine)
and should be treated accordingly. In January 2023, more than half a year after
the scandal, Google announced [public testing
of](https://blog.google/technology/ai/join-us-in-the-ai-test-kitchen) the
chatbot.

## Are there any available alternatives, ideally open source? {#open-source}

OpenAI is quite secretive. It did not even make the GPT 3 available to the
expert community, explaining that it feared abuse. However, the model is
available through a web interface, and OpenAI [charges considerable
fees](https://openai.com/api/pricing).

There are open-source alternatives. Meta has prepared OPT models that are very
similar to GPT-3 and made them freely available for download. The [Big Science
Workshop](https://bigscience.huggingface.co) initiative, backed by New
York-based startup [HuggingFace](https://huggingface.co) and a consortium of
European and American universities, has developed a [multilingual BLOOM
model](https://bigscience.huggingface.co/blog/bloom) that was trained for
around 40 languages. The European Union is also supporting the development of
large language models for Europeans through several projects – one of them
([HPTLP](https://cordis.europa.eu/project/id/101070350)) includes the Institute
of Formal and Applied Linguistics at Charles University.

There is an open-source
[Open-Assistant](https://github.com/LAION-AI/Open-Assistant) initiative led by
the German non-profit organization [LAION](https://laion.ai). Its goal is to
create a model with similar capabilities to ChatGPT but is open source and can
be used on commonly available hardware. While it is an ambitious goal, if the
project is successful in a large university, it has a reasonable chance of
success.

In a commercial setting, it offers a similar tool to ChatGPT [search engine
You.com](https://you.com/search?q=who+are+you&tbm=youchat&cfr=chat) from a
California-based AI startup that originates in Salesforce and Stanford
University. Subjectively, it seems to work worse than ChatGPT. Unlike it,
however, it works with a search engine and generates answers from search
results. This allows the user to verify which sources the answer comes from.

## How can ChatGPT speak multiple languages? Does it use machine translation? {#is-it-mt}

ChatGPT learned Czech and other languages almost as a by-product of using
training data that contained more languages besides English. It is not the case
that the chatbot would be connected to a translator.

The larger the digital footprint of a language, the better ChatGPT can handle
it. We can estimate how well a language is covered based on how well ChatGPT
can translate the language. A recent [preprint from Chinese company
Tencent](https://arxiv.org/abs/2301.08745) shows that it works quite well for
languages with a big digital footprint, comparable to state-of-the-art machine
translation about five years ago. On the other hand, languages with a small
digital footprint work much worse than today's automatic translators.

We can guess that there is no explicit translator involved from the fact that
the generated text gradually appears. In English, whole words usually appear.
However, Czech is generated in much smaller pieces, in pairs or triples of
letters. The reason is that language models can only work with a limited number
of language units, on the order of tens of thousands, at most hundreds of
thousands. The frequent words remain intact – in this case, the most common
words are English. The less frequent a word is in the training data, the more
units it consists of. If it were an automatic translation, there would be
longer units on the Czech side too. In addition, ChatGPT would have a longer
response time in Czech: it would generate the text first and then translate it.

## Where does the knowledge of ChatGPT come from? Does he use a search engine? {#knowledge}

Everything ChatGPT and all language models know about the world is encoded in
the learned parameters of the model. No search engine is used. It is
problematic in many ways. One problem is that we do not know the source of
information. Another problem is that it is not entirely easy to edit knowledge
in the model and thus selectively remove disinformation, for example. Yet
another problem is that the whole system has been trained at some point, and
there is no straightforward way to update it. ChatGPT thus has no knowledge of
what happened after 2020.

In general, neural networks are difficult to interpret, and people try to come
up with explanations of the inner workings of neural networks only after they
are trained. Recent [experiments with language models at MIT have
shown](https://rome.baulab.info) that factual knowledge is stored distributed
in the feed-forward layers. Some facts can be localized and edited, others not.
How to apply this method on a larger scale and whether it works for really
large language models is unclear.

Some systems combine [search with response
generation](https://aclanthology.org/2021.findings-acl.374). They can tell what
the generated answer is based on. Still, there is no guarantee that the sources
are credible and that the language model can extract truthful information from
credible sources.

## What to do about pupils and students using it in schools? {#schools}

A 2020 [study with older language
models](https://aclanthology.org/2020.acl-main.164) from Google and the
University of Pennsylvania, as well as a very recent [preprint from
Stanford](https://arxiv.org/abs/2301.11305), shows that it is relatively easy
to machine-detect generated text, while humans have great difficulty doing so.
For easier recognition of generated text, a technique called _watermarking_ can
be used, where _a virtual watermark_ is added to the generated text. This method
is summarized very well by a recent [preprint from
the University of Maryland](https://arxiv.org/abs/2301.10226). In practice, this
means adjusting the probabilities in the model so that some words or sequences
of words occur significantly more often than in natural text, but this is
imperceptible to humans. It is then relatively easy to test whether the text
contains a watermark or not. OpenAI made [its own generated
text](https://platform.openai.com/ai-text-classifier) detector available at the
end of January.

If auto-generated text detection tools become widespread, it can start a
never-ending arms race. Whoever has a generated text detector and can run it
arbitrarily many times can also use it to train another, smaller language model
to paraphrase the original text so that it does not change the content and
tricks the detector.

I believe efforts to restrict the use of language models are doomed to fail.
There is no point in banning anything, but it is necessary to prepare pupils
for an artificial intelligence world. Technologies like ChatGPT will change the
way knowledge is handled in the future, and schools should prepare pupils
and learners for it.

## Language models have opponents who consider them dangerous technology. What is the danger? {#danger}

As with any other technology, there is a risk of abuse of large language
models. The ability to generate authentic-sounding fluent text using examples
or instructions can be misused to generate fake news. The ability to have a
conversation with a purpose can be used to automate fraudulent emails, unfair
business practices, or political propaganda.

In addition to direct abuse, other problematic aspects are much more subtle.
Language models are trained on large amounts of data that contain many
pathologies and toxic behavior (sexism, racism, political extremism). Because
the models learn to imitate training data, it inevitably learns to imitate this
behavior. [Studies](https://aclanthology.org/2021.acl-long.416) examining
smaller language models in the US have found very disturbing results. Because
of another problematic property of all neural networks, namely the opacity of
the models, we cannot know when models are generating some output based on
racist or sexist biases that were in the training data.

Professor Emily Bender of the University of Washington is the most vocal critic
of use the of language models in the expert community. Her arguments are based
on the assumption that linguistic meaning is actually the intention of a person
who says or writes something. The language models have no intention and only
sophisticatedly parrot what was in the training data in different variations.
According to this argument, using language models safely is impossible because
the model cannot know what one _should or should not do_ but only what one
_does or does not_. Moreover, it often acquires knowledge from notoriously
toxic Internet environment. Bender and her coworkers summarize their arguments
in [a 2020 article](https://dl.acm.org/doi/10.1145/3442188.3445922).

A large part of the  expert community (at least partially) disagrees with this
criticism for various reasons. For example, because they disagree with the
definition of meaning. There are also [empirical
studies](https://aclanthology.org/2022.findings-emnlp.423) that show that some
models can partially simulate properties that should be unattainable under this
concept of meaning. Another argument is that ChatGPT is not [just
parroting](https://gist.github.com/yoavg/59d174608e92e845c8994ac2e234c8a9)
texts from the Internet, but through reinforcement learning, it tries to get as
many thumbs up from annotators as possible.

However, this disagreement does not change the fact that language models often
very subtly replicate racial, gender and other biases from training data and
generate very plausible sounding false texts. If no action is taken in this
direction, it can cause considerable social damage.
