import os

import requests
from requests_oauthlib import OAuth1

consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")

# need to pull this from DB
oauth_token = os.getenv("OAUTH_TOKEN")
oauth_token_secret = os.getenv("OAUTH_TOKEN_SECRET")

oauth = OAuth1(
    client_key=consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=oauth_token,
    resource_owner_secret=oauth_token_secret,
)


url = u"https://api.twitter.com/1.1/account/settings.json"
r = requests.get(url, auth=oauth)

print(r.status_code)
print(r.json())
