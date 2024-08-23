import requests

from config.settings import TELEGRAM_URL, TGAPIKEY


def send_tg_message(chat_id, message):
    params = {"text": message, "chat_id": chat_id}

    requests.get(f"{TELEGRAM_URL}{TGAPIKEY}/sendMessage", params=params)
