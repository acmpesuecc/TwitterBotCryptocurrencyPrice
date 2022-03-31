import tweepy
import requests
import json
import time


API = ""
apisk = ""
bearertoken = ""
accesskey = ""
akst = ""

auth_handler = tweepy.OAuthHandler(consumer_key = API, consumer_secret = apisk)
auth_handler.set_access_token(accesskey, akst) 

api = tweepy.API(auth_handler, wait_on_rate_limit= True)

switch = 1
while switch == 1:
    cardano = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=inr')
    price_cardano_inr = cardano.json()

    bitcoin = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr')
    price_bitcoin_inr = bitcoin.json()

    ADA = str(price_cardano_inr['cardano']['inr'])
    BTC = str(price_bitcoin_inr['bitcoin']['inr'])

    tweet = '>>>Current Price of ADA in INR: ' + ADA + 'rs' '\n' '>>>Current Price of BTC in INR: ' + BTC + 'rs'
    api.update_status(tweet) 
    time.sleep(1*60*60)
    print("Tweeted")
