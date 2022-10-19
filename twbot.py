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
    crypto = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Cethereum%2Csolana%2Cmatic%2C&vs_currencies=inr%2Cinr%2Cinr%2Cinr%2Cinr%2C')
    price_crypto_inr = crypto.json()

    cardano = str(price_crypto_inr['cardano']['inr'])
    bitcoin = str(price_crypto_inr['bitcoin']['inr'])
    solana = str(price_crypto_inr['solana']['inr'])
    ethereum = str(price_crypto_inr['ethereum']['inr'])


    tweet = '🚀 $BTC: ' + bitcoin + 'rs' '\n' '🤑 $ETH: ' + ethereum + 'rs' '\n' '💰 $SOL: ' + solana + 'rs' '\n' '💸 $ADA: ' + cardano + 'rs' + '\n' '#Crypto' ' #Bitcoin' + ' #Solana' + ' #Ethereum' + ' #Cardano'
    api.update_status(tweet) 
    # print(tweet)
    time.sleep(10*60*60)
    print("Tweeted")



