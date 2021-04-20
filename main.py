import sys
from os import path

import boto3
from PIL import Image

S3 = boto3.client('s3', region_name='us-east-2')
BUCKET = 'mrp-paintings'
IMG_FILE = 'original.jpg'
SM_IMG_FILE = 'small.jpg'
BASE_WIDTH = 300


def image_check():
    return path.exists(IMG_FILE)


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


if __name__ == '__main__':
    name = sys.argv[1] # TODO error check when name is not provided
    main(name)
