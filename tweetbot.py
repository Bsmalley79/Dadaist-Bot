#!/usr/bin/env python3

import time
import random

import tweepy

import dada
import chain
import login


def main():

    watch_dog = 0
    tbot = login.main()

    while True:
        try:
            roll = random.randint(1, 20)
            print(roll)
            if roll == 1:
                twit = dada.dada()
            elif (roll == 2 or roll == 3):
                twit = chain.chain(tbot, 1)
            elif roll in [4, 5, 6]:
                twit = chain.chain(tbot, 2)
            elif roll in [15, 16, 17]:
                twit = chain.chain(tbot, 4)
            elif (roll == 18 or roll == 19):
                twit = chain.chain(tbot, 5)
            elif roll == 20:
                twit = chain.chain(tbot, 6)
            else:
                twit = chain.chain(tbot, 3)

            tbot.update_status(status=twit)
            try:
                print(twit)
            except UnicodeEncodeError:
                print(ascii(twit))

# At least 1 tweet every hour, but no more than every 5 minutes
            timer = random.randint(5, 60)
            print('{}\n'.format(timer))
            time.sleep(timer * 60)
            watch_dog = 0

        except tweepy.error.TweepError:
            time.sleep((5 ** watch_dog) * 60)
            tbot = login.main()
            watch_dog += 1
            print("ARF! " + time.asctime())
            if watch_dog >= 3:
                print("Multiple login errors")
                return


if __name__ == "__main__":
    main()
