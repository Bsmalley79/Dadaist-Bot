import html
import random
import re

import tweepy

NONWORD = "\b"


def loop_check(item, array):
    for spam in array:
        if item != spam:
            return False
    return True


def cleaner(dirty):
    # strip links
    clean = re.sub(r'https?.{,18}', '', dirty)
    # strip retweet sources
    clean = re.sub(r'RT @.*?: ?', '', clean)
    clean = re.sub(r'@', '', clean)
    # strip &gt; etc
    clean = html.unescape(clean)
    # put a space on the end to prevent words running together
    clean = clean + ' '
    return clean


def table_gen(api, links=5, maxchar=140):
    # GENERATE TABLE
    markov = []
    table = {}
    for i in range(links):
        markov.append(NONWORD)

    statuses = api.home_timeline(count=maxchar)
    if statuses[0].user == api.me:
        print('No fresh tweets')
        raise tweepy.error.TweepError

    for tweet in statuses:
        base = cleaner(tweet.text)
        for char in base:
            if not loop_check(char, markov):
                table.setdefault(tuple(markov), []).append(char)
                for i in range(links):
                    try:
                        markov[i] = markov[i + 1]
                    except IndexError:
                        markov[-1] = char
    table.setdefault(tuple(markov), []).append(NONWORD)  # mark EOF
    return table


def tweet_gen(table, links=5, maxchar=140):
    # GENERATE OUTPUT
    markov = []
    twit = []

    for i in range(links):
        markov.append(NONWORD)

    for i in range(maxchar):
        newchar = random.choice(table[tuple(markov)])
        if newchar == NONWORD:
            break
        twit.append(newchar)
        for i in range(links):
            try:
                markov[i] = markov[i + 1]
            except IndexError:
                markov[-1] = newchar
    bad_end = ''.join(twit)
    good_end = bad_end.rpartition(" ")
    return good_end[0]


def chain(api, links=5, maxchar=140):
    ikea = table_gen(api, links, maxchar)
    return tweet_gen(ikea, links, maxchar)
