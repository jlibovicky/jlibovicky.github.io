---
layout: page
title: Punctuation Filling (tutorial)
---

I have always struggled with how to correctly write punctuation in English. The
rules are complex and there is always plenty of special cases. In this
tutorial, I will try to show you how can use deep learning to train an
automatic punctuation filler for English and Czech.

## Main Idea

The is a plenty of text on the Internet. Huge part of it is in English and most
of it is correctly punctuated. We can take for instance the English Wikipedia,
remove all the punctuation and train a model that will read the de-punctuated
text and try to estimate, whether there should or should not be a comma or a
semicolon. Recurrent neural networks are very powerful models which are used
for such complicated tasks as machine translation or automatic speech
recognition, they should work for this simple task as well.

This, indeed, can never be done 100% correctly - the punctuation very often
changes the meaning of the sentences. A computer cannot know whether you wanted
to write a defining or non-defining clause. Let us at least see how far we can
get.

## Prerequisites

In this tutorial, is held in Python (it don't matter whether 2 or 3, I am
using 3) and you will need also Google's Machine learning library
[TensorFlow](https://www.tensorflow.org) and an open-source NLP toolkit
[NLTK](http://www.nltk.org/).

Installation of TensorFlow depends on the platform you are using and on the
platform you are working on, and on whether you can train the model on a GPU.
You can find the detailed information on the [TensorFlow
webpage](https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html).

You can install NLTK easily using PyPi:

```bash
pip install nltk
```

After that, you need to download the pre-trained NLTK tokenizers. You can do it
by opening the Python console and typing:

```python
import nltk
nltk.download()
```

In addition we will use scripts from `wikiextractor` to get the plain text data
from the Wikipedia dump. You can clone its GitHub repository:

```bash
git clone https://github.com/attardi/wikiextractor
```

If you are not familiar with `git`, you can download a [zip
archive](https://github.com/attardi/wikiextractor/archive/master.zip).

## Preparing the data

First, we need to download the data we will work with. Wikipedia allows to
download its complete database in XML format. If you wish (and have enough disk
space), you can even download it with its complete history.

We will download the bzipped database dump, extract it and use the
`wikiextractor` script to obtain raw plain text. In bash, you can do it in the
following way:

```bash
wget http://download.wikimedia.org/en/latest/enwiki-latest-pages-articles.xml.bz2
bzcat enwiki-latest-pages-articles.xml.bz2 | \
     python wikipedia-extractor/WikiExtractor.py -cb 250K -o enwiki-extracted
```

The output will end up in a `enwiki-extracted-text.xml` file.

In a next step, we will write a simple Python script that will reformat the
Wikipedia text in such way that there will be one sentence per line.

```python
#!/usr/bin/python

import re
import sys

# patterns to detect stop and start of a document
DOC_START = re.compile(r"^<doc .*>")
DOC_END = re.compile(r"^</doc>$")

if __name__ == "__main__":
    # initialize the sentence splitter
    sentence_splitter = nltk.data.load("tokenizers/punkt/english.pickle")

    # used for collecting plain text
    collected_text = ""
    lines_added = 0

    for line in sys.stdin:
        line = line.rstrip() # remove \n from the end
        if not DOC_START.match(line) and not DOC_END.match(line):
            collected_text += u" " + line
            lines_added += 1

        if lines_added >= 1000:
            sentences = sentence_splitter.tokenize(tmp_text)
            # the last sentence may be unfinished, we leave it for the
            # the next sentence splitting
            for sent in sentences[:-1]:
                print(sent)
            collected_text = sentences[-1]
            lines_added = 0

    for sent in sentence_splitter.tokenize(current_text):
        print(sent)

```

In order to prevent consuming too much memory, we do the sentence splitting
after every 1000 lines in case of very long documents.
