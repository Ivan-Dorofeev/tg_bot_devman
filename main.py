import os
from pprint import pprint

import requests
import telegram
from dotenv import load_dotenv


def send_mail(tg_token, tg_chat_id):
    tg_bot = telegram.Bot(token=tg_token)
    tg_bot.send_message(chat_id=tg_chat_id, text="Привет, дружище")


def main(api_devman_token):
    url = 'https://dvmn.org/api/long_polling/'
    authorization_token = f'Token {api_devman_token}'

    headers = {
        'Authorization': authorization_token
    }

    while True:
        try:
            response = requests.get(url, headers=headers)
        except requests.exceptions.ReadTimeout:
            timestamp_to_request = response.json()['timestamp_to_request']
            uploads = {
                'timestamp': timestamp_to_request
            }
            response = requests.get(url, headers=headers, params=uploads)
        except ConnectionError:
            response = requests.get(url, headers=headers)

        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    load_dotenv()
    tg_chat_id = os.environ['TG_MY_CHAT_ID']
    tg_token = os.environ['TG_BOT_TOKEN']
    api_devman_token = os.environ['DEVMAN_API_TOKEN']

    # main(api_devman_token)
    send_mail(tg_token, tg_chat_id)
