#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, dada
 
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'Scrubbed'
CONSUMER_SECRET = 'Nope'
ACCESS_KEY = 'bad idea'
ACCESS_SECRET = 'not on a public git project'
twit = dada.dada()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(status=twit)
print 'done'
#time.sleep(900)#Tweet every 15 minutes