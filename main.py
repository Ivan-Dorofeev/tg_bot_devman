import os
from pprint import pprint

import requests
import telegram
from dotenv import load_dotenv


def send_mail(tg_token, tg_chat_id, msg):
    tg_bot = telegram.Bot(token=tg_token)
    tg_bot.send_message(chat_id=tg_chat_id, text=msg)


def main(api_devman_token, tg_token, tg_chat_id):
    url = 'https://dvmn.org/api/long_polling/'
    authorization_token = f'Token {api_devman_token}'

    headers = {
        'Authorization': authorization_token
    }
    uploads = {}

    while True:
        try:
            response = requests.get(url, headers=headers, params=uploads)
            server_answer = response.json()
            pprint(server_answer)

            lessons_cheked = server_answer['new_attempts']
            for lesson in lessons_cheked:
                lesson_cheked_status = "Надо доработать" if lesson['is_negative'] else "Работат принята"
                lesson_cheked_url = lesson['lesson_url']

                message = f'Статус: {lesson_cheked_status}\nУрок: {lesson_cheked_url}'
                send_mail(tg_token, tg_chat_id, message)

        except requests.exceptions.ReadTimeout:
            timestamp_to_request = response.json()['timestamp_to_request']
            uploads = {
                'timestamp': timestamp_to_request
            }
            continue
        except ConnectionError:
            continue


if __name__ == '__main__':
    load_dotenv()
    tg_chat_id = os.environ['TG_MY_CHAT_ID']
    tg_token = os.environ['TG_BOT_TOKEN']
    api_devman_token = os.environ['DEVMAN_API_TOKEN']

    main(api_devman_token, tg_token, tg_chat_id)
