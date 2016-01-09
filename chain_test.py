import re

import tweepy
import login

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


tbot = login.main()
pull_urls(tbot)
print ("---\n")
