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
watch_dog = 0

tbot = login()
while True:
    try:
        roll = random.randint(1, 20)
        print(roll)
        if roll == 1:
            twit = dada.dada()
        # elif roll == 20: twit = wordchain.chain(tbot)
        else:
            twit = chain.chain(tbot)
        tbot.update_status(status=twit)
        try:
            print(twit)
        except UnicodeEncodeError:
            print("This tweet contains emjoi, see tweetdeck")

# At least 1 tweet every hour, but no more than every 5 minutes
        timer = random.randint(5, 60)
        print('{}\n'.format(timer))
        time.sleep(timer * 60)
        watch_dog = 0

    except tweepy.error.TweepError:
        tbot = login()
        watch_dog += 1
        print("ARF!")
        if watch_dog >= 3:
            print("Multiple login errors")
            break
