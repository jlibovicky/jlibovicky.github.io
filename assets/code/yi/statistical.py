#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
import string
import sys

SPLITS = set(string.punctuation + string.whitespace)

def main():
    f_text = open(sys.argv[1], encoding='utf-8')
    f_yi = open(sys.argv[2])

    val_text = list(itertools.islice(f_text, 400))
    val_yis = list(itertools.islice(f_yi, 400))

    count_table = {}

    def apply_model(sentence):
        word_buf = []
        estimated = []
        for char in sentence:
            if char in SPLITS:
                word = "".join(word_buf)
                if word in count_table:
                    entries = count_table[word]
                    most_frequent = max(entries, key=lambda x: entries[x])
                    estimated += most_frequent
                else:
                    estimated += "".join("1" if c in list('íi') else "0" for c in word)
                word_buf = []
                estimated += "0"
            else:
                word_buf.append(char)
        return estimated

    def evaluation():
        correct = 0
        total = 0

        for sent, solutions in zip(val_text, val_yis):
            estimated = apply_model(sent)
            for real, estimated in zip(solutions, estimated):
                if real != "0":
                    total += 1
                    correct += int(real == estimated)

        return correct / total

    word_buf = []
    solution_buf = []
    for i, (sent, solutions) in enumerate(zip(f_text, f_yi)):
        for char, clazz in zip(sent, solutions):
            if char in SPLITS:
                if sum(solution_buf):
                    word = "".join(word_buf)
                    solution = "".join(str(x) for x in solution_buf)
                    if word not in count_table:
                        count_table[word] = {}
                    if solution not in count_table[word]:
                        count_table[word][solution] = 1
                    else:
                        count_table[word][solution] += 1
                word_buf = []
                solution_buf = []
            else:
                word_buf.append(char)
                solution_buf.append(int(clazz))

        if i % 500 == 0:
            acc = evaluation()
            print("{}\t{}".format(i, acc))

    for line in sys.stdin:
        print(line.rstrip())
        estimated = apply_model(line.rstrip())
        for c, e in zip(line, estimated):
            if e == "0" or e == "1":
                sys.stdout.write(c)
            elif c == "i":
                sys.stdout.write('y')
            else:
                sys.stdout.write('ý')
        print("\n")

if __name__ == "__main__":
    main()
