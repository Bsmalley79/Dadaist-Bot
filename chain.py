import random
import re

import tweepy

nonword = "\a"
maxchar = 140  # Tweepy ignores strings over 140 characters


def loop_check(item, array):
    for spam in array:
    	if item != spam:
            return False
    return True


def chain(api, links=2):
    # GENERATE TABLE
    markov = []
    table = {}
    for i in range(links):
        markov.append(nonword)
    statuses = api.home_timeline(count=maxchar)
    for tweet in statuses:
        base = tweet.text
        base = re.sub(r'https?.{,18}', '', base)
        for char in base:
            if not loop_check(char, markov):
                table.setdefault(markov, []).append(char)
                for i in range(links):
                    markov[i] = markov[i+1]
                markov[-1] = char
    table.setdefault(markov, []).append(nonword)  # mark EOF

# GENERATE OUTPUT
    for i in range(links):
        markov[i] = nonword
    twit = ''

    for i in range(maxchar):
        newchar = random.choice(table[markov])
        if newchar == nonword:
            break
        twit += newchar
        for i in range(links):
            markov[i] = markov[i+1]
        markov[-1] = char
    return twit
