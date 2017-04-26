#!/usr/bin/env python3

import random
import time

import tweepy

import chain
import login

DEBUG = False


def main():
    if DEBUG:
        print("Running in bug squish mode. No tweets will be published")
    watch_dog = 0
    tbot = login.main()

    while True:
        try:
            roll = random.randint(1, 20)
            print(roll)
            if roll == 1:
                twit = chain.chain(tbot, 1)
            elif (roll == 2 or roll == 3):
                twit = chain.chain(tbot, 3)
            else:
                twit = chain.chain(tbot, 5)

            if not DEBUG:
                tbot.update_status(status=twit)
            try:
                print(twit)
            except UnicodeEncodeError:
                print(ascii(twit))

            if DEBUG:
                return

# At least 1 tweet every hour, but no more than every 5 minutes
            timer = random.randint(5, 60)
            print('{}\n'.format(timer))
            time.sleep(timer * 60)
            watch_dog = 0

        except tweepy.error.TweepError:
            print("ARF! " + time.asctime())
            time.sleep((5 ** (watch_dog + 1)) * 60)
            tbot = login.main()
            watch_dog += 1
            if watch_dog >= 3:
                print("Multiple login errors")
                return


if __name__ == "__main__":
    main()
