#!/usr/bin/python

"""Prepare text and correct answers."""

import sys
import unicodedata

CZECH_CHARS = set(list("aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž"
                       "AÁBCČDĎEÉĚFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ"))


def remove_accents(input_str):
    """Convert text to pure ASCII."""
    res = ""
    for char in input_str:
        if char in CZECH_CHARS:
            res += char
        else: # if not Czech char, use ASCII equivalent
            nfkd_form = unicodedata.normalize('NFKD', char)
            only_ascii = nfkd_form.encode('ASCII', 'ignore')
            res += only_ascii.decode('ASCII')
    return res


def main():
    """Run the formating."""

    # file with text without capitaluation
    f_text = open("text.txt", 'w')
    # file with the correct capitaluation
    f_capital = open("capital.txt", 'w')

    for line in sys.stdin:
        line = remove_accents(line.strip())

        text = []
        capital = []

        for char in line:
            lower_char = char.lower()
            if lower_char == 'i' or lower_char == "í":
                text.append(lower_char)
                capital.append("1")
            elif lower_char == 'y':
                text.append('i')
                capital.append("2")
            elif lower_char == "ý":
                text.append("í")
                capital.append("2")
            else:
                text.append(lower_char)
                capital.append("0")

        print("".join(text), file=f_text)
        print("".join(capital), file=f_capital)

    f_text.close()
    f_capital.close()


if __name__ == "__main__":
    main()
