#!/usr/bin/env python
# coding: utf-8

# In[ ]:


consumer_key="yyjbA1N5m2sIxBCEGtsy5wOW9";
consumer_secret="1ZNU6d9P0HTGVNRECHvvSqrwFcd7k1iVspJ4irmie7WVQNDVfd";
access_token_key="1108065502969167872-whFkt1iPDVk067kP27b7qNTGxhNnv2";
access_token_secret="YC0qXzT17DD7EnUOSxaMydtFTZmH3P97Gc7dbV6ICRFwm";


# In[ ]:


# Storing the recent 50 tweets of Narendra Modi and making word cloud
import tweepy
from pymongo import MongoClient
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_all_tweets(screen_name):
    client=MongoClient("mongodb://localhost:27017/");
    db=client.db_twitter;
    tweets=db.Tweets;
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret);
    auth.set_access_token(access_token_key, access_token_secret);
    api = tweepy.API(auth);

    total_tweets=[];
    new_tweets = api.user_timeline(screen_name=screen_name, count=50);
    total_tweets.extend(new_tweets);
    oldest = total_tweets[-1].id - 1;
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=screen_name, count=50, max_id=oldest);
        total_tweets.extend(new_tweets);
        oldest = total_tweets[-1].id - 1;
        
    for tweet in total_tweets:
        tweets.insert(tweet._json);
    print("Execution is finished.");
    return total_tweets

tweet=get_all_tweets("@narendramodi");
final_tweets=[];
for i in range(0, 50):
    tw_=tweet[i]._json['text'];
    final_tweets.append(tw_);
    
words=' ';
for line in final_tweets:
    words+=line;
    
wordcloud = WordCloud(
    background_color='black',
    max_words=500,
    width=1800,
    height=1400).generate(words)

plt.imshow(wordcloud.recolor(random_state=3))
plt.axis('off')
plt.savefig('./modi_word_cloud.png', dpi=300)
plt.show()

