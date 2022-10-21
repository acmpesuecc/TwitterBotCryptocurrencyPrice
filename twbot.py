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
    crypto = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Cethereum%2Csolana%2Cmatic%2C&vs_currencies=inr%2Cinr%2Cinr%2Cinr%2Cinr%2C'
    )
    price_crypto_inr = crypto.json()
    
    cardano = str(price_crypto_inr['cardano']['inr'])
    bitcoin = str(price_crypto_inr['bitcoin']['inr'])
    solana = str(price_crypto_inr['solana']['inr'])
    ethereum = str(price_crypto_inr['ethereum']['inr'])
    crypto = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Cethereum%2Csolana%2Cmatic%2C&vs_currencies=usd%2Cusd%2Cusd%2Cusd%2Cusd%2C'
    )
    price_crypto_usd = crypto.json()
    cardanoUS = str(price_crypto_usd['cardano']['usd'])
    bitcoinUS = str(price_crypto_usd['bitcoin']['usd'])
    solanaUS = str(price_crypto_usd['solana']['usd'])
    ethereumUS = str(price_crypto_usd['ethereum']['usd'])

    tweet = "BTC: " + bitcoin + " Rs | "+ bitcoinUS + " USD" + "\n" +  "ADA: " + cardano + " Rs |  "+ cardanoUS + " USD" + "\n" + "SOL: " + solana + " Rs | " + solanaUS + " USD" + "\n" + "ETH: " + ethereum + " Rs | " + ethereumUS + " USD"
    # tweet = "Hi"
    api.update_status(tweet)
    print(tweet)
    time.sleep(10*60*60)
    print("Tweeted")
