import requests
import colorama
import json
import random


def currency_exchange(add, base):
    url = 'https://api.exchangeratesapi.io/latest'+add+base

    try:
        response = requests.get(url)
        # print(response)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return

    data = response.json()
    return data


def print_currency_exchange(add, base):
    data = currency_exchange(add, base)
    print("\nBASE : "+data['base']+"\n")

    count = 0
    f = open("/usr/local/bin/.user_details.json", 'r')
    user_details = json.load(f)

    for key, value in data['rates'].items():
        if key == data['base']:
            continue
        if(count % 5 == 0):
            print()
        print(key+" : "+str("{:.2f}".format(value)), end="\t")
        count += 1
    print()


def currency():

    f = open("/usr/local/bin/.user_details.json", 'r')
    user_details = json.load(f)

    if('currency' in user_details):
        base = user_details['currency']['base']
        add = '?base='
        print_currency_exchange(add, base)
        print("\nCurrent currency BASE : "+str(user_details['currency']['base']))
        print(
            "To change Default Currency BASE : assist [--currency] [--setbase]\n")
    else:
        print_currency_exchange('', '')
        print("\nCurrent currency BASE : EUR")
        print(
            "To change Default Currency BASE : assist [--currency] [--setbase]\n")
