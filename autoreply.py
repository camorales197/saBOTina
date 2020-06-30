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


whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def check_mentions(api, keywords, since_id, whitelist=whitelist):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword.lower() in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            mention = cleaning_mention(mention=tweet.text, whitelist=whitelist)

            text_generated = interactive_conditional_samples.interact_model(
                text=mention,
                length=200).split("<|endoftext|>")[0][:260].split("\n\n\n")[0]
            text_answer = "@" + tweet.user.screen_name + " " + text_generated

            try:
                api.update_status(status=text_answer, in_reply_to_status_id=tweet.id)
                logger.info("Tweet sent")
            except tweepy.error.TweepError:
                logger.info("Error sending tweet")
                pass
    return new_since_id

def cleaning_mention(mention, whitelist=whitelist):
    clean_mention = ''.join(filter(whitelist.__contains__, mention))
    return clean_mention

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["@JSaBOTina"], since_id)
        logger.info("Waiting...")
        time.sleep(3600)

if __name__ == "__main__":
    main()