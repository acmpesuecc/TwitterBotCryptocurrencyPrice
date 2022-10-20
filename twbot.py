import tweepy
import requests
import json
import time


API = "Uejatc9R2cSCDKH7vXqFGAAut"
apisk = "WAMI3jQc3oWbK7LNwulOg8LLJNUy4HYZPSJh8iwALWy9QIQckp"
bearertoken = "AAAAAAAAAAAAAAAAAAAAACTnawEAAAAAuYmiH%2BjL34xuMRfr3ofphPZ1PgQ%3D7O2pwPxRJLtRKFnChR4wpqSJPFk2GJGRBR5LOKJ4n9YiNP2wTu"
accesskey = "824129756929150976-bVNNCMucltHJxwTsASFwhdYGDNEBVtY"
akst = "OZOm4FZn0int3GyegHBn0Wrc6XUuoYFSC8F0dwlUjRJqe"


auth_handler = tweepy.OAuthHandler(consumer_key = API, consumer_secret = apisk)
auth_handler.set_access_token(accesskey, akst) 

api = tweepy.API(auth_handler, wait_on_rate_limit= True)

switch = 1
while switch == 1:
    crypto = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Cethereum%2Csolana%2Cmatic%2C&vs_currencies=inr%2Cinr%2Cinr%2Cinr%2Cinr%2C')
    price_crypto_inr = crypto.json()

    cardano = str(price_crypto_inr['cardano']['inr'])
    bitcoin = str(price_crypto_inr['bitcoin']['inr'])
    solana = str(price_crypto_inr['solana']['inr'])
    ethereum = str(price_crypto_inr['ethereum']['inr'])

    api.update_status("BTC:", bitcoin, "rs", "ADA: ", cardano, "rs", "SOL: ", solana, "rs", "ETH: ", ethereum, "rs") 
    # print(tweet)
    time.sleep(10*60*60)
    print("Tweeted")
