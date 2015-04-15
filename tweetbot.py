#!/usr/bin/env python

import time
import random

import tweepy

import dada

# Twitter validation information:
# These are not the keys you're looking for

try:
    while True:
        twit = dada.dada()
# dada.dada takes a while to run. it's here to avoid twitter time out
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        api.update_status(status=twit)
        print(twit)
    
        timer = random.randint(1 * 15, 11 * 15)
        print(timer)
        time.sleep(timer * 60) # Tweet at random between 1 and 11 hours
except KeyboardInterrupt:
    print("Thank you for using Dadaist Bot. Shutting down.")

