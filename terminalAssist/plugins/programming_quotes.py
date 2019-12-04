# Random Programmng Quotes

import requests
import colorama
import json
import random


def quotes():
    url = 'https://programming-quotes-api.herokuapp.com/quotes/lang/en'

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return

    data = response.json()

    quotes_dict={}

    for i in range(len(data)):
        quotes_dict[data[i]['author']] = data[i]['en']
    
    author,quote=random.choice(list(quotes_dict.items()))

    print(quote+'\n- '+ author)