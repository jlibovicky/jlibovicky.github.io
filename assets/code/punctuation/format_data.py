#!/usr/bin/python

import re
import sys
import unicodedata

def remove_accents(input_str):
    """Convert text to pure ASCII."""
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode('ASCII')

def main():
    # file with text without capitaluation
    f_text = open("text.txt", 'w')
    # file with the correct capitaluation
    f_capital = open("capital.txt", 'w')

    for line in sys.stdin:
        line = remove_accents(line.strip())

        text = []
        capital = []

        wait = True
        for char in line:
            text.append(char.lower())
            capital.append(str(int(char.isupper())))

        print("".join(text), file=f_text)
        print("".join(capital), file=f_capital)

    f_text.close()
    f_capital.close()


if __name__ == "__main__":
    main()
