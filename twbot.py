import tweepy
import requests
import json


API = ""
apisk = ""
bearertoken = ""
accesskey = ""
akst = ""

auth_handler = tweepy.OAuthHandler(consumer_key = API, consumer_secret = apisk)
auth_handler.set_access_token(accesskey, akst) 

api = tweepy.API(auth_handler, wait_on_rate_limit= True)

cryptocoin = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=inr')
price_inr = cryptocoin.json()
ADA = str(price_inr['cardano']['inr'])
tweet = '>>>Current Price of ADA in INR: ' + ADA + 'Rs'
api.update_status(tweet) 


