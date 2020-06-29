#tweepy-bots/bots/config.py
import tweepy
import logging
import os
from dotenv import load_dotenv


logger = logging.getLogger()
load_dotenv()


def create_api():
    APIKEY = os.environ.get("APIKEY")
    APISECRETKEY = os.environ.get("APISECRETKEY")
    ACCESSTOKEN = os.environ.get("ACCESSTOKEN")
    ACCESSTOKENSECRET = os.environ.get("ACCESSTOKENSECRET")

    auth = tweepy.OAuthHandler(APIKEY, APISECRETKEY)
    auth.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
