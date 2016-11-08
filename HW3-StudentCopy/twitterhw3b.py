# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "791353118411853824-IWKlip0IeTKVpp658xA5RubN7ejw663"
access_token_secret = "EIm7btp3vNhMPhfwJff0Bq8qy1DFHapsIIsWzKIJHcrZP"
consumer_key = "MIic8lvBm1nV1kg59W931HLV5"
consumer_secret = "DZZCWsam2qoICZ2pzTgylj3GJTw2BtpOgsAXIWvbyZtTmU3958"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('"Jessica Jones" @Marvel')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


print("Average subjectivity is")
print("Average polarity is")
