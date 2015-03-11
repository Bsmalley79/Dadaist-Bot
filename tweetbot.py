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

onest = []
onest = dada.fill_table('first_let.csv')
print (onest)
twolet = []
twolet = dada.fill_table('two_let.csv')
print (twolet)
genlet = []
genlet = dada.fill_table('gen_let.csv')
print (genlet)

# while True
# {
twit = dada.dada(onest, twolet, genlet)
# dada.dada takes a while to run. it's here to avoid twitter time out
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(status=twit)
print (time.process_time()) #lets see how long this takes
# timer = random.randint(37, 11 * 60) * 60
# time.sleep(timer) #Tweet at random between 37 minutes and 11 hours
# }
# assert False "You shouldn't be here"
