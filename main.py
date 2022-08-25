import datetime
import os
import time

import requests
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_chat_id = os.environ['TG_MY_CHAT_ID']
    tg_token = os.environ['TG_BOT_TOKEN']
    api_devman_token = os.environ['DEVMAN_API_TOKEN']

    tg_bot = telegram.Bot(token=tg_token)

    url = 'https://dvmn.org/api/long_polling/'
    authorization_token = f'Token {api_devman_token}'

    headers = {
        'Authorization': authorization_token
    }
    uploads = {
        'timestamp': datetime.datetime.now().timestamp()
    }

    while True:
        try:
            response = requests.get(url, headers=headers, params=uploads)
            homework_review = response.json()

            lessons_cheked = homework_review['new_attempts']
            for lesson in lessons_cheked:
                lesson_cheked_status = "Надо доработать" if lesson['is_negative'] else "Работат принята"
                lesson_cheked_url = lesson['lesson_url']

                message = f'Статус: {lesson_cheked_status}\nУрок: {lesson_cheked_url}'
                tg_bot.send_message(chat_id=tg_chat_id, text=message)

        except requests.exceptions.ReadTimeout:
            timestamp_to_request = response.json()['timestamp_to_request']
            uploads = {
                'timestamp': timestamp_to_request
            }
            continue
        except ConnectionError:
            time.sleep(30)
            continue


if __name__ == '__main__':
    main()
