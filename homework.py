import time
import os

import requests
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
vk_token = os.getenv("VK_TOKEN")


def get_status(user_id):
    url = 'https://api.vk.com/method/users.get'
    data = {
        'user_ids': user_id,
        'v': '5.92',
        'access_token': vk_token,
        'fields': 'online'
        
    }
    result = requests.post(url, params=data).json().get('response')
    status = result[0]['online']
    return status


def sms_sender(sms_text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=os.getenv('NUMBER_TO'),
        from_=os.getenv('NUMBER_FROM'),
        body=("Он зашел ВКОНТАКТЕ!)")
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
