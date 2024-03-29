# tg_bot_devman

## Описание

Телеграмм бот, который информирует о получении результата проверки работ на Devman

![image](https://user-images.githubusercontent.com/58893102/188298977-3ad0fb84-7988-41a5-ab3a-580ff2a5da2a.png)

## Установка

- скачать репозиторий
- установите необходимы библиотеки командой:

    ```pip install -r requirements.txt```
    
- создайте файл ```.env``` в корневом каталоге
- положите в него:

    ```TG_BOT_TOKEN``` - свой токен от бота

    ```TG_MY_CHAT_ID``` - свой айди чата
    
    ```DEVMAN_API_TOKEN``` - токен от Devman

## Запуск

Запустите бота командой:

```python main.py```

### Запус в Docker

В корне директории уже лежит Dockerfile.
Нужнл только собрать контейнер:

```docker build -t tg_bot_devman```

И после сборки запустить его:

```docker run tg_bot_devman```

## Логирование

О начале запуска и обо всех ошибках работы, бот информирует сообщением в телеграмм чат.
А также все логи пишет в ```tg_bot_log.log```.

![image](https://user-images.githubusercontent.com/58893102/188298954-a30f0449-dfd5-44d4-9e6a-64159fba562a.png)

