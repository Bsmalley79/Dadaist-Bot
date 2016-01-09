#!/usr/bin/env python3

import sys

import tweepy

import dada
import login


twit = "@" + str(sys.argv[1]) + " "
twit += dada.dada(len(twit))
try:
    api = login.main()
    api.update_status(status=twit)
except tweepy.error.TweepError:
    print("Unable to contact Twitter services.  Please check your connection.")
finally:
    print(twit)
