#!/usr/bin/python

import re
import sys

# standard characters in Englih
ENGLISH_CHARS = re.compile(r"[0-9A-Za-z\"\'?!.% #@$(){}\[\]]")


def main():
    # file with text without punctuation
    f_text = open("text.txt", 'w')
    # file with the correct punctuation
    f_punct = open("punct.txt", 'w')

    for line in sys.stdin:
        line = line.rstrip()

        text = []
        punct = []

        wait = True
        for char in line:
            if wait:  # we need to wait what the next symbol will be
                wait = False
            else:
                if char == ',' or char == ';':
                    punct.append(char)
                else:
                    punct.append('_')

            if ENGLISH_CHARS.match(char):
                text.append(char)
            elif char != ',' and char != ';':
                text.append('_')  # placeholder for non-standard characters
            else:
                wait = True


        punct.append('_')

        assert len(text) == len(punct)

        print("".join(text), file=f_text)
        print("".join(punct), file=f_punct)

    f_text.close()
    f_punct.close()


if __name__ == "__main__":
    main()
