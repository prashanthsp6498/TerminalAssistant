# Random Cat Fact Generator


import requests
import colorama
import json
import random


def fact():
    url = 'https://cat-fact.herokuapp.com/facts'

    try:
        response = requests.get(url)
        # print(response)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return

    text_list = []
    data = response.json()
    for item in data['all']:
        # print(item['text'])
        text_list.append(item['text'])

    print(random.choice(text_list))
