#!/usr/bin/env python3

import random
from textwrap import TextWrapper

import chain
from chain import NONWORD

import login

DEBUG = False


def main():
    if DEBUG:
        print("Running in bug squish mode.")
        print("Logging in:")
    tbot = login.main()
    if DEBUG:
        print("Generating Table")
    basis = chain.table_gen(tbot)
    markov = []

    for i in range(5):
        markov.append(NONWORD)
    if DEBUG:
        print("Building text")

    twit = []
    for lines in range(48):
        for chars in range(80):
            newchar = random.choice(basis[tuple(markov)])
            if newchar == NONWORD:
                if DEBUG:
                    print("Hicough on line {}".format(lines + 1))
                for i in range(5):
                    markov[i] = newchar
                break
            twit.append(newchar)
            for i in range(5):
                try:
                    markov[i] = markov[i + 1]
                except IndexError:
                    markov[-1] = newchar

    twit_string = ''.join(twit) + '\n'
    wrapper = TextWrapper(initial_indent="    ")

    if DEBUG:
        print("Writing to file")
    with open("lorem.txt", 'w+t', encoding='UTF-8-sig') as file:
        for paragraph in twit_string.splitlines(keepends=True):
            file.write(wrapper.fill(paragraph) + '\n')
    print("Done. See Lorem.txt")
    return


if __name__ == "__main__":
    main()
