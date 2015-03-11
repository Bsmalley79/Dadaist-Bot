#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, dada
 
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'Tz8HUw6lZZhh04iRFvowzaFAx'
CONSUMER_SECRET = '4JLP0MsupmKYp1qHTrvifDbATDmpYHz21hx8pj2YSbro14NX4i'
ACCESS_KEY = '3078493577-dmEWlkLKy1oSSgevjyhmmFoEHRCFeP04rOazBRC'
ACCESS_SECRET = 'NhLjDhZTs8azIT8rHY0tA8dvGZRSoQAu4nYfZNIUwW8Ap'
twit = dada.dada()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(status=twit)
print 'done'
#time.sleep(900)#Tweet every 15 minutes