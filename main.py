import os
import tweepy
from dotenv import load_dotenv
load_dotenv()


IMG_FILE = 'original.jpg'
DEFAULT_MESSAGE = '#bobross #landscapepainting #oilpainting'

# Twitter auth values
CONSUMER_KEY = os.environ.get('TW_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TW_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TW_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TW_ACCESS_TOKEN_SECRET')


def main():
    if os.path.exists(IMG_FILE) is False:
        print('MISSING_MAIN_IMAGE')
        print('Exiting...')
        return
    title = input('Enter Title: ')
    status = f'{title} {DEFAULT_MESSAGE}'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    TW = tweepy.API(auth)
    try:
        TW.verify_credentials()
    except:
        print('TW_AUTH ERROR')
    print('TW_POSTING_IMAGE...')
    TW.update_with_media(IMG_FILE, status)


if __name__ == '__main__':
    main()
