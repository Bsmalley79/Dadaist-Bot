import random
import re
import html

import tweepy

import dada

nonword = "\b"


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
    # strip Trump (ew) to be removed after election, probably
    clean = re.sub(r'\b[tT][rR][uU][mM][pP]\b', dada.long_word(5), clean)
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
        markov.append(nonword)

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
                        markov[i] = markov[i+1]
                    except IndexError:
                        markov[-1] = char
    table.setdefault(tuple(markov), []).append(nonword)  # mark EOF
    return table


def tweet_gen(table, links=5, maxchar=140):
    # GENERATE OUTPUT
    markov = []
    twit = []

    for i in range(links):
        markov.append(nonword) 

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


def chain(api, links=5, maxchar=140):
    ikea = table_gen(api, links, maxchar)
    return tweet_gen(ikea, links, maxchar)
