import tweepy
import os
from dotenv import load_dotenv


load_dotenv()


APIKEY = os.environ.get("APIKEY")
APISECRETKEY = os.environ.get("APISECRETKEY")
ACCESSTOKEN = os.environ.get("ACCESSTOKEN")
ACCESSTOKENSECRET = os.environ.get("ACCESSTOKENSECRET")


# Authenticate to Twitter
auth = tweepy.OAuthHandler(APIKEY, APISECRETKEY)
auth.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create a tweet
api.update_status("No quería un amor civilizado pero… Joaquín Sabina se ha casado con Jimena Coronado")







