import random
import sys
import csv

import tweepy

nonword = "\n"  
maxchar = 140  # Tweepy ignores strings over 140 characters
testing = True


def login():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        return api
    except tweepy.error.TweepError:
        print("Unable to contact Twitter services.
              Please check your Internet connection.")
        raise

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

dada = login()

while testing:
    # GENERATE TABLE
    c1 = nonword
    c2 = nonword
    table = {}
    statuses = dada.home_timeline(count=50)
    for tweet in statuses:
        for char in tweet.text:
            table.setdefault((c1, c2), []).append(char)
            c1, c2 = c2, char

# GENERATE OUTPUT
    c1 = nonword
    c2 = nonword
    twit = ''

    for i in range(maxchar):
        newchar = random.choice(table[(c1, c2)])
        twit += newchar
        c1, c2 = c2, newchar

# PUBLISH TWEET
    try:
        dada.update_status(status=twit)
    except tweepy.error.TweepError:
        dada = login()
        dada.update_status(status=twit)

    try:
        print(twit)
    except UnicodeEncodeError:
        print("The bot tried to speak unicode.
              Check Tweet Deck for actual tweet.")
    timer = random.randint(5, 60)  # at least 1/hr, no more than every 5 min
    print(timer)
    # time.sleep(timer * 60)
    testing = False
