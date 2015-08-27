#!/usr/bin/env python

import time
import random
import csv

import tweepy

import dada

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
    while True:
        twit = dada.dada(0)
# dada.dada takes a while to run. it's here to avoid twitter time out
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        api.update_status(status=twit)
        print(twit)
    
        timer = random.randint(1 * 5, 12 * 5)
        print(timer)
        time.sleep(timer * 60) # Tweet at random 
except KeyboardInterrupt:
    print("Thank you for using Dadaist Bot. Shutting down.")
except TweepError:
    print("Unable to contact Twitter services.  Please check your Internet connection.")

