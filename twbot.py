import tweepy
import requests
import json
import time

API = "YNDmqZ7KIQfz05mJ5UH2iUW96"
api_key_secret = "inPMlkfKG1bAu3jEAMQmPPQKVTnK72NX8eEXsbJnZWAkp656ga"
bearertoken = "AAAAAAAAAAAAAAAAAAAAALXtawEAAAAA0Iue9sAXNWk1HVqXKWU9zpFWz5A%3DP8PCB5VTt8ud4OopsI57SqL3Adz2vAWl7gLqFmZDOpnY7zn1HN"
accesstoken = "1509571461266419715-sMZB14yh7DAcV94AnhUJZ9jwjvpnwp"
access_token_secret = "CvmUMbXvS4CKj3nFTch5Ciigdvwvm3qccbCdCf2KlayRx"

auth_handler = tweepy.OAuthHandler(consumer_key=API, consumer_secret=api_key_secret)
auth_handler.set_access_token(accesstoken, access_token_secret)

api = tweepy.API(auth_handler, wait_on_rate_limit=True)

switch = 1

while switch == 1:
    crypto_s = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=decentraland%2Cthe-sandbox&vs_currencies=inr'
    )
    price_crypto_inr = crypto_s.json()

    mana = str(price_crypto_inr['decentraland']['inr'])
    sand = str(price_crypto_inr['the-sandbox']['inr'])
    tweet = "\U0001F449MANA:" + mana + "\n\U0001F449SAND:" + sand
    api.update_status(tweet)
    print(tweet)
    time.sleep(10*60*60)
    print("Tweeted")
    
   
while switch == 1:
    crypto_usd = requests.get (
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Csolana%2Cetheruem%20&vs_currencies=usd"
    )
    crypto_inr = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Csolana%2Cetheruem%20&vs_currencies=inr"
     )
   
    price_crypto_usd = crypto_usd.json()
    cardano_usd = str(price_crypto_usd['cardano']['usd'])
    bitcoin_usd = str(price_crypto_usd['bitcoin']['usd'])
    solana_usd = str(price_crypto_usd['solana']['usd'])
    #ethereum_usd = str(price_crypto_usd['ethereum']['usd'])
     
    price_crypto_inr = crypto_inr.json()
    cardano_inr = str(price_crypto_inr['cardano']['inr'])
    bitcoin_inr = str(price_crypto_inr['bitcoin']['inr'])
    solana_inr = str(price_crypto_inr['solana']['inr'])
    # ethereum_inr = str(price_crypto_inr['ethereum']['inr'])
    


    tweet = "BTC:" + bitcoin_usd + " usd " + "ADA: " + cardano_usd + " usd " + "SOL: " + solana_usd + " usd " 
    tweet_2 = "BTC:" + bitcoin_inr + " inr " + "ADA: " + cardano_inr + " inr " + "SOL: " + solana_inr + " inr " + "ETH: " 
    tweet = "Hi"
    api.update_status(tweet)
    print(tweet)
    print(tweet_2)
    time.sleep(10*60*60)
    print("Tweeted")
