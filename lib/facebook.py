import os
import requests
from dotenv import load_dotenv
load_dotenv()


token = os.environ.get('FB_ACCESS_TOKEN')
page_id = os.environ.get('FB_PAGE_ID')


def post(img_path, caption):
    data = {
        'caption': caption,
        'access_token': token,
    }
    files = { 'file': open(img_path, 'rb') }
    print('FB_POST...')
    res = requests.post(f'https://graph.facebook.com/v10.0/{page_id}/photos', data=data, files=files)
    json = res.json()
    if res.status_code == 200:
        print('FB_POST OK!')
    else:
        print('FB_POST ERROR!')
        print(json.get('error').get('message'))
