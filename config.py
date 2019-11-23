#!/usr/bin/env python
# coding: utf-8

# In[ ]:


consumer_key="yyjbA1N5m2sIxBCEGtsy5wOW9";
consumer_secret="1ZNU6d9P0HTGVNRECHvvSqrwFcd7k1iVspJ4irmie7WVQNDVfd";
access_token_key="1108065502969167872-whFkt1iPDVk067kP27b7qNTGxhNnv2";
access_token_secret="YC0qXzT17DD7EnUOSxaMydtFTZmH3P97Gc7dbV6ICRFwm";


# In[ ]:


# Creating the config file
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

