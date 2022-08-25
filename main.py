import os
from pprint import pprint

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()

    # url = 'https://dvmn.org/api/user_reviews/'
    url = 'https://dvmn.org/api/long_polling/'
    api_devman_token = os.environ['DEVMAN_API_TOKEN']
    authorization_token = f'Token {api_devman_token}'

    headers = {
        'Authorization': authorization_token
    }

    while True:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.ReadTimeout:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
