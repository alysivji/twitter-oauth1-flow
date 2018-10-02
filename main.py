import os

import requests


def oauth2(consumer_key, consumer_secret):
    r = requests.post(
        "https://api.twitter.com/oauth2/token",
        auth=(consumer_key, consumer_secret),
        headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"},
        data={"grant_type": "client_credentials"},
    )
    return r.json()


if __name__ == "__main__":
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY", None)
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET", None)
    r = oauth2()
    # https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview
