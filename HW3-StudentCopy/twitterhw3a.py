# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.
import tweepy
import nltk

# Unique code from Twitter
access_token = "791353118411853824-IWKlip0IeTKVpp658xA5RubN7ejw663"
access_token_secret = "EIm7btp3vNhMPhfwJff0Bq8qy1DFHapsIIsWzKIJHcrZP"
consumer_key = "MIic8lvBm1nV1kg59W931HLV5"
consumer_secret = "DZZCWsam2qoICZ2pzTgylj3GJTw2BtpOgsAXIWvbyZtTmU3958"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

hashtags = "#UMSI-206 #Proj3"
try:
	api.update_with_media("teacup.jpg", status=hashtags)
	print ("Check the image on Twitter!")
except:
	print ("Sorry, an error occurred uploading your image.")
# You will demo this live for grading.
