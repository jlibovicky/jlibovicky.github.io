#!/usr/bin/python

import re
import sys
import nltk

# patterns to detect stop and start of a document
DOC_START = re.compile(r"^<doc .*>")
DOC_END = re.compile(r"^</doc>$")

def main():
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
            sentences = sentence_splitter.tokenize(collected_text)
            # the last sentence may be unfinished, we leave it for the
            # the next sentence splitting
            for sent in sentences[:-1]:
                print(sent)
            collected_text = sentences[-1]
            lines_added = 0

    for sent in sentence_splitter.tokenize(collected_text):
        print(sent)

if __name__ == "__main__":
    main()
