# Python Lib
import sys
import os

# Third Party
import boto3
from PIL import Image

# Local
from lib.twitter import Twitter

# Basic Definitions
BUCKET = 'mrp-paintings'
IMG_FILE = 'original.jpg'
SM_IMG_FILE = 'small.jpg'
BASE_WIDTH = 300
DEFAULT_STATUS = '#bobross #landscapepainting #oilpainting'

# Third Party Clients
S3 = boto3.client('s3', region_name='us-east-2')
TW = Twitter()


def image_check():
    return os.path.exists(IMG_FILE)


def resize():
    print('RESIZING_IMAGE...')
    img = Image.open(IMG_FILE)
    wpercent = (BASE_WIDTH / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((BASE_WIDTH, hsize), Image.ANTIALIAS)
    img.save(SM_IMG_FILE)


def s3_upload(name):
    print('S3_IMAGE_UPLOAD...')
    S3.upload_file(SM_IMG_FILE, BUCKET, f'{name}/{SM_IMG_FILE}')
    S3.upload_file(IMG_FILE, BUCKET, f'{name}/{IMG_FILE}')


def main(name):
    if image_check() is False:
        print('MISSING_MAIN_IMAGE')
        print('Exiting...')
        return
    resize()
    s3_upload(name)
    status = f'{name} {DEFAULT_STATUS}'
    TW.tweet(SM_IMG_FILE, status)


if __name__ == '__main__':
    name = sys.argv[1] # TODO error check when name is not provided
    main(name)
