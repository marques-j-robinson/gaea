import os
import tweepy
from dotenv import load_dotenv
load_dotenv()


CONSUMER_KEY = os.environ.get('TW_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TW_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TW_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TW_ACCESS_TOKEN_SECRET')


def tweet(img_path, status):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print('TW_AUTH OK!')
    except:
        print('TW_AUTH ERROR...')
    print('tweeting...')
    api.update_with_media(img_path, status)
