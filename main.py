import os
import requests
from lib.twitter import tweet
from lib.instagram import post as ig_post
from lib.facebook import post as fb_post


IMG_FILE = 'original.jpg'
DEFAULT_MESSAGE = '#bobross #landscapepainting #oilpainting'


def main():
    if os.path.exists(IMG_FILE) is False:
        print('MISSING_MAIN_IMAGE')
        print('Exiting...')
        return
    # title = input('Enter Title: ')
    title = "Some Other Riverbank"
    msg = f'{title} {DEFAULT_MESSAGE}'
    # tweet(IMG_FILE, msg)
    # ig_post(IMG_FILE, msg)
    fb_post(IMG_FILE, msg)


if __name__ == '__main__':
    main()
