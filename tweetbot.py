#!/usr/bin/env python

import time
import random

import tweepy

import dada

# Twitter validation information:
CONSUMER_KEY = 'Tz8HUw6lZZhh04iRFvowzaFAx'
CONSUMER_SECRET = '4JLP0MsupmKYp1qHTrvifDbATDmpYHz21hx8pj2YSbro14NX4i'
ACCESS_KEY = '3078493577-dmEWlkLKy1oSSgevjyhmmFoEHRCFeP04rOazBRC'
ACCESS_SECRET = 'NhLjDhZTs8azIT8rHY0tA8dvGZRSoQAu4nYfZNIUwW8Ap'


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

assert False, "You shouldn't be here"
