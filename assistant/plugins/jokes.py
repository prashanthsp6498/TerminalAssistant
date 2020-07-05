import requests
import colorama
import json
import random


def joke():
    genre = ['nsfw', 'religious', 'political']
    url = 'https://sv443.net/jokeapi/category/Programming?blacklistFlags=' + \
        random.choice(genre)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return

    text_list = []
    data = response.json()
    # print(data.keys())

    print(colorama.Fore.GREEN, "------JOKE------\n\n", colorama.Fore.RESET)
    if('joke' in data.keys()):
        print(data['joke'])
    else:
        print(data['setup'])
        print()
        print(data['delivery'])
