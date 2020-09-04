## MOVE THIS FILE OFF GITHUB REPO BEFORE SYNCING!

## Register an app: https://dev.twitter.com/

#pip install tweepy
import tweepy

## Check the documentation page
## http://docs.tweepy.org/en/v3.2.0/

## Get access to API
## Copy/paste your keys here, move file out of github repo, import keys to public files.
auth = tweepy.OAuthHandler('your consumer key', 'your consumer secret')
auth.set_access_token('your access token', 'your access token secret')    
client = tweepy.API(auth, wait_on_rate_limit = False)