#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:30:52 2020

@author: taylor
"""
#import os
#os.chdir('/Users/taylor/Documents/GitHub/python_summer2020/HW/')

import importlib # to import file
import sys # add directory to system PATH
import io
import re
import time
import json

sys.path.insert(0, '/Users/taylor/Documents/GitHub/python_summer2020/HW')

twitter = importlib.import_module('HW3twitter')
api = twitter.client

# See rate limit
limit = api.rate_limit_status()

polisci = api.get_user('WUSTLPoliSci')

# =============================================================================
# One-Degree Separation
# =============================================================================

#look up each user
polsAll = polisci.followers_ids() #creates a list of user ids - up to 5000
len(polsAll)

#######need to find how many tweets everyone has
tweetCount = [] #how many tweets the followers have
folfol= [] #how many followers each follower has

#takes ~5 minutes to run
for follower_id in polsAll[0:len(polsAll)]:
    try:
        user = api.get_user(follower_id)
        tweetCount.append(user.statuses_count)
        folfol.append(user.followers_count)
    except:
        pass

######finding most active follower
active_follower = api.get_user(polsAll[tweetCount.index(max(tweetCount))])
print(active_follower.name)

######finding most popular follower
pop_follower = api.get_user(polsAll[folfol.index(max(folfol))])
print(pop_follower.name)

#######need to find info about those WUSTL follows
friends = api.friends_ids(polisci.id)

#######finding how many people the friends follow and how many tweets they've made
friendFol = []
friendTweets = []
for friend_id in friends[0:len(friends)]:
    try:
        user = api.get_user(friend_id)
        friendTweets.append(user.statuses_count)
        friendFol.append(user.followers_count)
    except:
        pass
    
#######creating layman, expert and celebrity categories
laymanID = []; expertID = []; celebrityID = []
laymanTweet = []; expertTweet = []; celebrityTweet = []

for friend_id in friends[0:len(friends)]:
    user = api.get_user(friend_id)
    if user.followers_count < 100:
        laymanID.append(friend_id)
        laymanTweet.append(user.statuses_count)
        #active_layman = api.get_user(laymanID[laymanTweet.index(max(laymanTweet))])
        #print(active_layman.name)
    elif user.followers_count > 1000:
        celebrityID.append(friend_id)
        celebrityTweet.append(user.statuses_count)
        #active_celebrity = api.get_user(celebrityID[celebrityTweet.index(max(celebrityTweet))])
        #print(active_celebrity.name)
    else:
        expertID.append(friend_id)
        expertTweet.append(user.statuses_count)
        #active_expert = api.get_user(expertID[expertTweet.index(max(expertTweet))])
        #print(active_expert.name) 

#######find most active of each category          
active_layman = api.get_user(laymanID[laymanTweet.index(max(laymanTweet))])
print(active_layman.name)

active_celebrity = api.get_user(celebrityID[celebrityTweet.index(max(celebrityTweet))])
print(active_celebrity.name)

active_expert = api.get_user(expertID[expertTweet.index(max(expertTweet))])
print(active_expert.name)

#######find most popular friend
popular_friend = api.get_user(friends[friendFol.index(max(friendFol))])
print(popular_friend.name)

# =============================================================================
# Two-Degree Separation
# =============================================================================
truncFriends = []
truncFriends = laymanID + expertID

# Limit the followers to laymen and experts
truncFollowers = []
for follower_id in polsAll[0:len(polsAll)]:
    user = api.get_user(follower_id)
    if user.followers_count <= 1000:
        truncFollowers.append(follower_id)
    else:
    	continue

folFols = []
folFolTweet = []
for follower_id in truncFollowers:
    user = api.get_user(follower_id)
    folFols.append(user.followers_ids())
    folFolTweet.append(user.statuses_count)

#####finding most active follower of followers
active_folFol = api.get_user(truncFollowers[folFolTweet.index(max(folFolTweet))])
print(active_folFol.name)

active_friFri = api.get_user(truncFriends[folFolTweet.index(max(folFolTweet))])
print(active_friFri.name)





























