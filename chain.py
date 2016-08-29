import random
import re
import html

import tweepy

nonword = "\n"

def loop_check(item, array):
    for spam in array:
        if item != spam:
            return False
    return True


def chain(api, links=3, maxchar=140):
    # GENERATE TABLE
    markov = []
    table = {}
    for i in range(links):
        markov.append(nonword)
    statuses = api.home_timeline(count=maxchar)
    for tweet in statuses:
        base = tweet.text
        base = re.sub(r'https?.{,18}', '', base)
        base = re.sub(r'RT @', r'.@', base)
        base = html.unescape(base)
        for char in base:
            if not loop_check(char, markov):
                table.setdefault(tuple(markov), []).append(char)
                for i in range(links):
                    try:
                        markov[i] = markov[i+1]
                    except IndexError:
                        markov[-1] = char
    table.setdefault(tuple(markov), []).append(nonword)  # mark EOF

# GENERATE OUTPUT
# if maxchar > 140:
#    raise warning
#    maxchar = 140

    for i in range(links):
        markov[i] = nonword
    twit = []

    for i in range(maxchar):
        newchar = random.choice(table[tuple(markov)])
        if newchar == nonword:
            break
        twit.append(newchar)
        for i in range(links):
            try:
                markov[i] = markov[i+1]
            except IndexError:
                markov[-1] = newchar
    return ''.join(twit)
