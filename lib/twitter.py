import os
import tweepy
from dotenv import load_dotenv
load_dotenv()


consumer_key = os.environ.get('TW_CONSUMER_KEY')
consumer_secret = os.environ.get('TW_CONSUMER_SECRET')
token = os.environ.get('TW_ACCESS_TOKEN')
token_secret = os.environ.get('TW_ACCESS_TOKEN_SECRET')


def tweet(img_path, status):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print('TW_AUTH OK!')
    except:
        print('TW_AUTH ERROR...')
    print('tweeting...')
    api.update_with_media(img_path, status)
