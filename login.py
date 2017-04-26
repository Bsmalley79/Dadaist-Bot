import tweepy

from keys import ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def main():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        return api
    except tweepy.error.TweepError:
        print("Unable to contact Twitter services.")
        raise
