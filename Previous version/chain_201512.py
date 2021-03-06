import random
import re

import tweepy

nonword = "\a"
maxchar = 140  # Tweepy ignores strings over 140 characters


def chain(api):
    # GENERATE TABLE
    c1 = nonword
    c2 = nonword
    table = {}
    statuses = api.home_timeline(count=maxchar)
    for tweet in statuses:
        base = tweet.text
        base = re.sub(r'https?.{,18}', '', base)
        for char in base:
            if not (c1 == c2 and c2 == char):
                table.setdefault((c1, c2), []).append(char)
                c1, c2 = c2, char
    table.setdefault((c1, c2), []).append(nonword)  # mark EOF

# GENERATE OUTPUT
    c1 = nonword
    c2 = nonword
    twit = ''

    for i in range(maxchar):
        newchar = random.choice(table[(c1, c2)])
        if newchar == nonword:
            break
        twit += newchar
        c1, c2 = c2, newchar
    return twit
