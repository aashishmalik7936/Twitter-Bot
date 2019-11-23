#!/usr/bin/env python
# coding: utf-8

# In[ ]:


consumer_key="yyjbA1N5m2sIxBCEGtsy5wOW9";
consumer_secret="1ZNU6d9P0HTGVNRECHvvSqrwFcd7k1iVspJ4irmie7WVQNDVfd";
access_token_key="1108065502969167872-whFkt1iPDVk067kP27b7qNTGxhNnv2";
access_token_secret="YC0qXzT17DD7EnUOSxaMydtFTZmH3P97Gc7dbV6ICRFwm";


# In[ ]:


# Finding those users who are using abusive words in tweets
import tweepy
import logging
from config import create_api
import time
import tensorflow as tf
import json
import numpy

interpreter = tf.lite.Interpreter(model_path="model_lite.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

dictionary=json.load("tokenizer.json");
def pred_abuse_tweet(dictionary, tweet):
    arr_inp=numpy.zeros(1000);
    arr_tw=[i for item in lst for i in item.split()];
    for word_ in arr_tw:
        i=0;
        for feat_ in dictonary:
            if word_==feat_:
                arr_inp[i]=1;
            i+=1;
    return arr_inp
    

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class abusive_tweet_finder(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
    
    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or             tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                arr=pred_abuse_tweet(dictionary, tweet);
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
                
        interpreter.set_tensor(input_details[0]['index'], arr);
        interpreter.invoke();
        output_data = interpreter.get_tensor(output_details[0]['index']);
        output_data=output_data[0];
        if(output_data>0.5):
            print(f"{tweet.author.name} is using abusive words in tweets")
                
    def on_error(self, status):
        logger.error(status)

def main(keywords):
    api = create_api()
    tweets_listener = abusive_tweet_finder(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    main(["Python", "Tweepy"])

