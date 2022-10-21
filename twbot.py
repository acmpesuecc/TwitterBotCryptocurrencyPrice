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
    cardano_US = str(float(cardano)*0.012)
    bitcoin_US = str(float(bitcoin)*0.012)
    solana_US = str(float(solana)*0.012)
    ethereum_US = str(float(ethereum)*0.012)

    # tweet = "BTC:" + bitcoin + "rs" + " $" + bitcoin_US + " ADA: " + cardano + "rs" + " $" + cardano_US + " SOL: " + solana + "rs" + " $" + solana_US + " ETH: " + ethereum + "rs" + " $" + ethereum_US
    tweet = f"BTC: ₹{bitcoin} : ${bitcoin_US}\nADA: ₹{cardano} : ${cardano_US}\nSOL: ₹{solana} : ${solana_US}\nETH: ₹{ethereum} : ${ethereum_US}\n"
    output = "Crypto as of now 🚀\n" + tweet
    # tweet = "Hi"
    api.update_status(output)
    print(output)
    time.sleep(10*60*60)
    print("Tweeted")