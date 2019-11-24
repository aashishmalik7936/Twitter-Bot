# Twitter-Bot
## Introduction
This twitter bot is made using python and the functionalities that are added into it are:
1. Following particluar user.
2. Reply to the mentions.
3. Like and retweet the tweets in feed.
4. Tell name of those followers who are using abusive language in tweets.
5. Made the wordcloud using the recent 50 tweets of a particular user and stored them in a 
database created using MongoDB on local system. 

Model.tflite contains the machine learning model that will classify between abusive and 
non abusive tweets. I used this model to find the abusive tweets and finally displaying 
the name of the tweet author.

For demo I have made the wordcloud using the tweets of Narendra Modi:
![alt text](https://github.com/aashishmalik7936/Twitter-Bot/blob/master/modi_word_cloud.png)

## Tools
Tweepy, Matplotlib, Tensorflow, MongoDB, json, numpy, python.
