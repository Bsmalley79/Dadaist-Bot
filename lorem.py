#!/usr/bin/env python3

import random

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
        print("Writing file")
    with open("lorem.txt", 'w+t', encoding='UTF-8-sig') as file:
        for lines in range(48):
            twit = []
            for chars in range(80):
                newchar = random.choice(basis[tuple(markov)])
                if newchar == NONWORD:
                    if DEBUG:
                        print("Hicough on line {}".format(lines + 1))
                    for i in range(5):
                        markov[i] = newchar
                    break

                for i in range(5):
                    try:
                        markov[i] = markov[i + 1]
                    except IndexError:
                        markov[-1] = newchar

                if newchar != '\n':
                    twit.append(newchar)
                else:
                    break
            file.write(''.join(twit) + '\n')
    print("Done. See Lorem.txt")
    return


if __name__ == "__main__":
    main()
