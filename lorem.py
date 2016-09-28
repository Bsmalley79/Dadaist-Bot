#!/usr/bin/env python3

import time
import random

import tweepy

import chain
import login

DEBUG = True


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
        markov.append(chain.nonword)
    if DEBUG:
        print("Writing file")
    with open("lorem.txt", 'w+t', errors = 'replace') as file:
        for lines in range(48):
            twit = []
            for chars in range(79):
                newchar = random.choice(basis[tuple(markov)])
                if newchar == chain.nonword:
                    if DEBUG:
                        print("Hicough on line {}".format(lines+1))
                    for i in range(5):
                        markov[i] = newchar
                    break
                twit.append(newchar)
                for i in range(5):
                    try:
                        markov[i] = markov[i+1]
                    except IndexError:
                        markov[-1] = newchar
            file.write(''.join(twit) + '\n')
    print("Done. See Lorem.txt")
    return


if __name__ == "__main__":
    main()
