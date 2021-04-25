import os
from instabot import Bot
from dotenv import load_dotenv
load_dotenv()


username = os.environ.get('IG_USERNAME')
password = os.environ.get('IG_PASSWORD')


def post(img_path, caption):
    api = Bot()
    api.login(username, password)
    api.upload_photo(img_path, caption)
