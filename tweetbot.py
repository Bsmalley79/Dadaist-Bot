#!/usr/bin/env python

import time
import random
import csv

import tweepy

import dada
import chain
# import wordchain


def login():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        return api
    except tweepy.error.TweepError:
        print("Unable to contact Twitter services.")
        raise

# Twitter validation information:
target = []
with open('keys.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        target.append(row)

CONSUMER_KEY = ''.join(target[0])
CONSUMER_SECRET = ''.join(target[1])
ACCESS_KEY = ''.join(target[2])
ACCESS_SECRET = ''.join(target[3])

try:
    tbot = login()
    while True:
        roll = random.randint(1, 20)
        if roll == 1:
            twit = dada.dada(0)
        # elif roll == 20: twit = wordchain.chain(tbot)
        else:
            try:
                twit = chain.chain(tbot)
            except tweepy.error.TweepError:
                tbot = login()
                twit = chain.chain(tbot)
        tbot.update_status(status=twit)

        try:
            print(twit)
        except UnicodeEncodeError:
            print(repr(twit))

# At least 1 tweet every hour, but no more than every 5 minutes
        timer = random.randint(5, 60)
        print(timer)
        time.sleep(timer * 60)

except KeyboardInterrupt:
    print("Thank you for using Dadaist Bot. Shutting down.")
except tweepy.error.TweepError:
    pass
