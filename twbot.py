import tweepy
import requests
import json
import time

# Enter your own API keys here
API = "YNDmqZ7KIQfz05mJ5UH2iUW96"
api_key_secret = "inPMlkfKG1bAu3jEAMQmPPQKVTnK72NX8eEXsbJnZWAkp656ga"
bearertoken = "AAAAAAAAAAAAAAAAAAAAALXtawEAAAAA0Iue9sAXNWk1HVqXKWU9zpFWz5A%3DP8PCB5VTt8ud4OopsI57SqL3Adz2vAWl7gLqFmZDOpnY7zn1HN"
accesstoken = "1509571461266419715-sMZB14yh7DAcV94AnhUJZ9jwjvpnwp"
access_token_secret = "CvmUMbXvS4CKj3nFTch5Ciigdvwvm3qccbCdCf2KlayRx"

auth_handler = tweepy.OAuthHandler(consumer_key=API, consumer_secret=api_key_secret)
auth_handler.set_access_token(accesstoken, access_token_secret)

api = tweepy.API(auth_handler, wait_on_rate_limit=True)

switch = 1

# while switch == 1:
#     crypto_ma = requests.get(
#         'https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=inr'
#     )
#     price_crypto_inr = crypto_ma.json()

#     matic = str(price_crypto_inr['matic-network']['inr'])
#     tweet = "\U0001F449MATIC:" + matic
#     api.update_status(tweet)
#     print(tweet)
#     time.sleep(10*60*60)
#     print("Tweeted")
    

# while switch == 1:
#     crypto_s = requests.get(
#         'https://api.coingecko.com/api/v3/simple/price?ids=decentraland%2Cthe-sandbox&vs_currencies=inr'
#     )
#     price_crypto_inr = crypto_s.json()

#     mana = str(price_crypto_inr['decentraland']['inr'])
#     sand = str(price_crypto_inr['the-sandbox']['inr'])
#     tweet = "\U0001F449MANA:" + mana + "\n\U0001F449SAND:" + sand
#     api.update_status(tweet)
#     print(tweet)
#     time.sleep(10*60*60)
#     print("Tweeted")
    
   
# while switch == 1:
#     crypto_usd = requests.get (
#             "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Csolana%2Cetheruem%20&vs_currencies=usd"
#     )
#     crypto_inr = requests.get(
#             "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Csolana%2Cetheruem%20&vs_currencies=inr"
#      )
   
#     price_crypto_usd = crypto_usd.json()
#     cardano_usd = str(price_crypto_usd['cardano']['usd'])
#     bitcoin_usd = str(price_crypto_usd['bitcoin']['usd'])
#     solana_usd = str(price_crypto_usd['solana']['usd'])
#     #ethereum_usd = str(price_crypto_usd['ethereum']['usd'])
     
#     price_crypto_inr = crypto_inr.json()
#     cardano_inr = str(price_crypto_inr['cardano']['inr'])
#     bitcoin_inr = str(price_crypto_inr['bitcoin']['inr'])
#     solana_inr = str(price_crypto_inr['solana']['inr'])
#     # ethereum_inr = str(price_crypto_inr['ethereum']['inr'])

while switch == 1:
    nft_inr = requests.get (
            "https://api.coingecko.com/api/v3/simple/price?ids=xmon%2Cilv%2Cflow%2Cape&vs_currencies=inr"
        )
    
    price_nft_inr = nft_inr.json()

    crypto_s = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=decentraland%2Cthe-sandbox&vs_currencies=inr'
    )
    
    crypto_inr = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Csolana%2Cetheruem%20&vs_currencies=inr"
     )
    
    price_crypto_inr = crypto_s.json()
    xmon_inr = str(price_nft_inr['xmon']['inr'])
    flow_inr = str(price_nft_inr['flow']['inr'])
    ape_inr = str(price_nft_inr['ape']['inr'])
    price_crypto_inr = crypto_s.json()
    mana = str(price_crypto_inr['decentraland']['inr'])
    sand = str(price_crypto_inr['the-sandbox']['inr'])
    price_crypto_inr = crypto_inr.json()
    cardano_inr = str(price_crypto_inr['cardano']['inr'])
    bitcoin_inr = str(price_crypto_inr['bitcoin']['inr'])
    solana_inr = str(price_crypto_inr['solana']['inr'])
    ethereum_inr = str(price_crypto_inr['ethereum']['inr'])
    tweet_2 = "BTC:" + bitcoin_inr + " INR " + "ADA: " + cardano_inr + " INR " + "SOL: " + solana_inr + " INR " + "ETH: "
    tweet_3 =  "💸 $XMON: " + xmon_inr + " INR " + "\n" + "🌊 $FLOW: " + flow_inr + " INR " + "\n" + "🐵 $APE: " + ape_inr + " INR " +"💵🚀" 
   
    api.update_status(tweet_2) 
    print(tweet_2)
    
    time.sleep(60) # after 1 minute
    
    api.update_status(tweet_3)
    print(tweet_3)
    
    time.sleep(10*60*60) # after 10 hours.
    print("Tweeted")
