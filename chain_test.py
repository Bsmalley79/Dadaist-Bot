import csv
import re

import tweepy

maxchar = 140  # Tweepy ignores strings over 140 characters


def pull_urls(api):

    statuses = api.home_timeline(count=maxchar)
    for tweet in statuses:
        base = tweet.text
        try:
            print(base)
        except UnicodeEncodeError:
            print("Unicode Error {}".format(len(base)))
        base = re.sub(r'https?.{,18}', '', base)
        try:
            print(base + "\n")
        except UnicodeEncodeError:
            print("Unicode Error {}\n".format(len(base)))
def login():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        return api
    except tweepy.error.TweepError:
        print("Unable to contact Twitter services.")
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

tbot = login()
pull_urls(tbot)
print ("---\n")
