#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
from config import create_api
import time
import sys
sys.path.insert(0, 'modelo')
from modelo import interactive_conditional_samples
import warnings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

warnings.filterwarnings("ignore")


def send_tweet(api, message):
    try:
        api.update_status(status=message)
        logger.info("Tweet sent")

    except tweepy.error.TweepError:
        print("Error sending the tweet")
        pass

def main():
    api = create_api()
    while True:
        text = interactive_conditional_samples.interact_model(
            text="Todo empezo. /n",
            length=200).split("<|endoftext|>")[0][:279].split("\n\n\n")[0]
        send_tweet(api=api, message=text)
        time.sleep(3600)

if __name__ == "__main__":
    main()


