#!/usr/bin/env python
# coding: utf-8

# In[ ]:


consumer_key="yyjbA1N5m2sIxBCEGtsy5wOW9";
consumer_secret="1ZNU6d9P0HTGVNRECHvvSqrwFcd7k1iVspJ4irmie7WVQNDVfd";
access_token_key="1108065502969167872-whFkt1iPDVk067kP27b7qNTGxhNnv2";
access_token_secret="YC0qXzT17DD7EnUOSxaMydtFTZmH3P97Gc7dbV6ICRFwm";


# In[ ]:


# Follow-follower bot
import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for foll_ in tweepy.Cursor(api.followers).items():
        if not foll_.following:
            logger.info(f"Following: {foll_.name}")
            foll_.follow()

def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()

