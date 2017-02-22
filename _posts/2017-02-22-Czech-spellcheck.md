---
layout: post
title: Spell checking of y and in Czech using deep learning
---

In the recent years, deep learning (machine learning with neural networks)
became a frequently used buzzword in the technological word. We can find plenty
of articles on how machine intelligence (a new, probably sexier term for
artificial intelligence) can solve machine translation, speech recognition or
enable smart assistants as Google Home or Amazon Echo.

It this post we will have a closer look on how we use deep learning for spell
checking of a particular phenomenon in the Czech language – choosing whether to
write 'i' or 'y'. I have chosen this phenomenon because even native speaker
sometimes tend to  make errors in this. I will try show how we can attempt to
solve it using deep learning and demonstrate how a computer scientist (or a
computational linguist) would think about developing a solution for this
problem. If you are not scared of reading source code, it can also serve as a
programming tutorial.

# How do the Czechs spell it

You probably ask why is it so hard problem that I am even thinking about
developing a deep learning solution for it. The problem is that both 'i' and
'y' are pronounced in the exactly same way (although it wasn't always the case
in long time ago). Even if you are a native speaker, you don't have to know
which one of them you're actually saying. At the elementary school, children
are thought many complicated rules of how we choose whether to write 'y' or
'i'.  Southern Slavic languages as Slovene has reflected that in their spelling
and use 'i' wherever possible. Although it might seem tempting to simplify the
spelling in this way (school kids would be definitely happy about it), it can
also have some unexpected consequences. It brought a lot of ambiguity in the
language and actually slowed down the reading.

The rules Czech children need to acquire are:

* After some consonants, only 'y' or only 'i' can be written. However,
  sometimes placing 'i' changes the pronunciation of the previous consonant, so
  you need to know in advance how the word is pronounced.

* For some words you just need to remember the stem of the word.

* For nouns and adjectives, you need to know to which declination paradigm they
  belong to and memorize the endings for different grammatical cases in all the
  paradigms.

* The verbs should be with grammatical agreement with nouns (for that it is
  necessary to acquire at least basics [dependency
  syntax](https://en.wikipedia.org/wiki/Dependency_grammar)).

* Know what to do when the rules collide and remember countless exceptions.

To be able to program these rules into a programming language, we would need to
be able to do be many things before could even start. We would need to be to
detect the word stems, find in what cases the words are, their gender, number.
We would need to be able do to the dependency parsing to check the agreement.
(If you are curious how automatic syntactic analysis looks like, you have a
look at
[Treex](https://lindat.mff.cuni.cz/services/treex-web/result/2HfygMLDnvZm63ZX4EF)).

Unfortunately, the automatic syntax analyzer usually rely on the sentences to
be spelled correctly (this is how they get the information about gender, number
etc.) and if they are not, the analyzers make mistakes. When we want to
actually correct the sentences, it is a bit unpleasant property. We will leave
this vicious circle using deep learning such that we will be able to cope
without all of these rules.

# Train and test data

Success of all machine learning application always stands and falls with having
enough data to train the models on.  In this case, the data can be obtained
very easily. The only thing we need is a big amount of text in Czech language
which is in most cases grammatically correct. For instance, we can download
complete [Wikipedia dump](https://dumps.wikimedia.org/cswiki/latest/) in XML
format.

Before we start to work with the text, we need clean and preprocess a bit. We
will split it into sentences ([NLTK](http://www.nltk.org) library contains
Czech models). For simplicity, we will keep only characters of Czech alphabet,
numbers and punctuation and replace all the other characters with a special
symbol, e.g., `_`. Wikipedia contains many snippets of text in various
languages in various alphabet and these string wouldn't be useful for our
models anyway. To make the task even simpler, we will lowercase the text.

Now, our data are almost ready. The last thing missing is changing all
occurrences of 'y' to 'i' and remembering their original position. We may
encode it e.g., like this:


*Input:*

```txt
aristotelés dále určil poloměr země, kterí ale odhadl na dvojnásobek...
v aristotelovském modelu země stojí a měsíc se sluncem a hvězdami krouží...
mišlenki aristotelovi rozvinul ve 2. století našeho letopočtu klaudios...
```

*Desired output:*

```txt
00001000000000000000000000000000001000000100000000000000000000001000000100000...
02000002000100000000200000100000000000000001000000000000000000000001000000000...
00000000000000000010000000000001000002000000000000000000020000000000000000000...
```

In this encoding `1` means 'i', `2` means 'y' and other characters are denoted
by `0`. You can preview both the code for [sentence
splitting](/assets/code/yi/sentence_split.py) and the [data
encoding](/assets/code/yi/format_data.py). By the time I downloaded the Czech
Wikipedia, there were more than 5 million sentences.

When we solve any problem using machine learning, no matter whether it is deep
leaning or other machine learning methods, we need to strictly separate train
and test data. As the term suggests, train data are used to train the model and
therefore it is no surprise that the model usually works very well on the data.
What we are really interested in, is how the model will work on data that are
yet to come. We can simulate it by leaving a part of our data aside and use
them only to compare models with each other. For our experiments, we will leave
1,000 sentences for testing and the rest for training.

# Simple Solutions

A trivial solution would be leaving 'i' everywhere. In this trivial manner, we
will get solid performance of __76.4 %__. In computational linguistics, and
artificial intelligence in general, we call this _setting a baseline_. Any
meaningful solution to any problem needs to show that it's significantly better
than a simple base solution. In this section, we will try to come up with
multiple simple solutions to see, how far we can get.

We can for instance may observe that in words with originally Czech stem, there
is always 'y' after 'h', 'k' and 'r'. A similar observation is that many words
starts with the 'vy-' prefix and that it may be a good strategy to put 'y' in
all words beginning like this (my apologies Vikings and
[vicugnas](https://upload.wikimedia.org/wikipedia/commons/e/eb/Vicunacrop.jpg)).

The following table summarizes results of these simple approaches:

|                     |  accuracy |
|:--------------------|----------:|
|'i' everywhere       |    76.4 % |
| + 'h', 'k','r'      |    77.5 % |
| + '_vy_-' prefix    |    80.0 % |

Very simple heuristics (that can be written using a single line regular
expression) brought us to 80.0 % accuracy. If we try harder, we might be able
to come up with some other rules that would increase the accuracy even few
percentage points higher.

Instead of that, will we try a different simple solution which be considered to
be a trivial machine learning solution. Because we have the whole Wikipedia as
our training data, we can simply remember what is the most frequent spelling
for each word. Whenever a word is encountered, we can simply use its most
frequent spelling. The following table shows what was the accuracy after
processing different amounts of training sentences.


| number of seen sentences  |  accuracy |
|--------------------------:|----------:|
|                       500 |    77.9 % |
|                     5,000 |    85.3 % |
|                    50,000 |    88.6 % |
|                   500,000 |    90.4 % |
|                 5,000,000 |    90.8 % |

We can see that with the increasing amount of processed data, the accuracy
increases. It should not surprise us — the more text we see, the smaller
chance, that we will encounter a previously unseen word. On other hand, after
processing 500,000 words, there is only little chance we will see anything new.
The [source code](/assets/code/yi/statistical.py) is very simple.

Now we know what we may expect from our model. Anything over 91 % will be a
success, anything worse would mean that the network was not able to remember
the most frequent spelling of every word. From the preliminary baseline
experiments we also know that to pass this accuracy, the model will have to
learn some grammar to keep nouns and verbs in agreement.

# Model

We will use a recurrent network for our experiments. Every time, such network
gets an input, it updates its inner state (based on the state in was previously
in) and emits some output. The following scheme shows a recurrent network
rolled in time.

![sequence-labeling](/assets/rnn.svg)

The network reads the text letter by letter. In every step, it updates its
stored inner state and emits some output – actually, it makes the same
operation with each letter. It may seem strange at the first sight, but it is
exactly what we want our network to do. Every letter has its own learned
representation and when the network receives it, it decides what to do next.
The inner state of the network is in fact a memory where the network stores
relevant information from what it has already seen and what does it mean for
what is yet to come.

The network is thus forced to learn a suitable representation of the input
letters and the previously seen text. Representation learning is often stressed
as one of the most important properties of deep learning (after all, one of the
most prestigious conference in the field is called International Conference on
Representation Learning). The data does not contain markups for any concepts
that allows humans to conceptualize the spelling rules. We do not even treat
spaces between words in any special way. The data is just a stream of
characters and it is up to the  network to deal with it.

We will use one more trick to improve the networks' performance. We will use
two recurrent networks – one reading the text from the front and the second one
in the backward direction. In this way, we can use information about what is
both left and right from a letter to estimate the spelling.

If you are interested in the details of the network (number of neurons etc.),
you can check out [the model's source code](/assets/code/yi/build_network.py).

# Training

The recurrent network gets an output for every input letter. In fact, we are
interested only in 'i's. We can ignore all other outputs and thus make our work
easier.

At the beginning of the training, the weights of the neurons' connection are
random. During the learning, we always compare the network's estimate is the
desired output and if it makes an error, we shift the weights slightly in such
a way, that it makes a smaller error.

This very simple feedback is sufficient to gradually learn inner data
representation that may be entirely different from human conceptualization.
During the training, there is never the notion of word, or consonants and
vowels. No one tells the network: “This is subject because it is in the
nominative case, you can see it from its ending.” There are no genders, numbers
or persons annotated in the data. Everything the network needs comes just from
the simple feedback of being right or wrong on the outputs.

Training our network on 5 million sentences took 5 hours on an old
low-performance GPU and achieved the accuracy of __98 %__. Although still quite
far from perfection, it is much better than all the other methods as you
can see in the table below.

|method                 |  accuracy |
|:----------------------|----------:|
|'i' everywhere         |    70.4 % |
|simple rules           |    80.0 % |
|most frequent spelling |    90.8 % |
|neural network         |    98.3 % |

If you are interested in the code, have a look at [the training
script](/assets/code/yi/train.py).

# What did the network learn

A disadvantage of neural networks is that we cannot easily find out what the
network have learned by looking at the network itself. We can get at least some
insight by looking at the learning curves. A learning curve is a graph having
amount of data using during training on _x_ axis and the accuracy on the _y_.
It basically tells how fast the learning was.

![sequence-labeling](/assets/rnn_learning_curve.svg)

We can see from the graph that neural network needed quite a lot of data to
learn something better than just putting 'i' everywhere possible. It needed
more than 13,000 sentences. By that time, the network probably starts get the
notion of individual characters.

Whereas the algorithm remembering the most frequent spelling of each word
needed almost 1,500 sentences to beat the simple rules, the network needed
33,000 training sentences. It is 2,200 norm pages of text, it is more that
three times longer Dostoevsky's 'Crime and Punishment'. By that time, the
network can probably tell that under some circumstances, 'y' usually follows
some consonants.

At the beginning, the most frequent spelling algorithms has a big advantage
over the network because it operates with the notion of words from the very
beginning (for simplicity I considered words to be separated by spaces and
ignored hyphens, apostrophes, etc.). The network first needs to find out that
the spaces plays special roles. Therefore, it overcame the most frequent
spelling algorithms only after using 300,000 training sentences. With the
average speed of reading of 200 words per minute, would take 17 days of
non-stop reading (29 times 'Crime and Punishment').

This by the shows the strengths of human abstraction and that the so called
artificial intelligence is something completely different from the human
intelligence. You can probably explain the spelling much faster than by reading
30 voluminous books, but as stated in the introduction, there is no easy way to
tell this rules to a computer. On the other hand, trying to infer spelling
rules from a pile of books would a painstaking intellectual adventure for any
human.

If you are interested in linguistic analysis of the network performance, you
probably speak Czech and can have a look at the [Czech version of the
post](2017/02/22/Pravopis.html).

And that's it. We were able learn a decent spell checker for a particularly
difficult phenomenon in Czech grammar. There are of course ways to improve on
top of this state (use a multi-layer network, regularize with other training
objective, acquire more training data), but more on this maybe later.
