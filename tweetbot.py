#!/usr/bin/env python

import time
import random
import csv

import tweepy

import dada
import chain


def login(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET):
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        return api
    except tweepy.error.TweepError:
        print("Unable to contact Twitter services.")
        raise

def main():
# Twitter validation information:
    watch_dog = 0
    target = []
    with open('keys.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            target.append(row)


    tbot = login(''.join(target[0]), ''.join(target[1]), ''.join(target[2]), ''.join(target[3]))
    while True:
        try:
            roll = random.randint(1, 20)
            print(roll)
            if roll == 1:
                twit = dada.dada()
            elif (roll == 2 or roll == 3):
                twit = chain.chain(tbot, 1)
            elif (roll == 18 or roll == 19):
                twit = chain.chain(tbot, 3)
            elif roll == 20:
                twit = chain.chain(tbot, 4)
            else:
                twit = chain.chain(tbot, 2)

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
            tbot = login(''.join(target[0]), ''.join(target[1]), ''.join(target[2]), ''.join(target[3]))
            watch_dog += 1
            print("ARF!")
            if watch_dog >= 3:
                print("Multiple login errors")
                return


if __name__ == "__main__":
    main()
