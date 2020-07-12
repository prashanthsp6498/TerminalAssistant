import requests
import colorama
import json
import random


def currency_exchange(add,base):
    url = 'https://api.exchangeratesapi.io/latest'+add+base

    try:
        response = requests.get(url)
        # print(response)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return

    data = response.json()
    print("\nBASE : "+data['base']+"\n")

    count = 0
    f = open("/usr/local/bin/.user_details.json", 'r')
    user_details = json.load(f)
    
    for key,value in data['rates'].items():
        if key == data['base']:
            continue
        if(count % 5==0):
            print()
        print(key+" : "+str("{:.2f}".format(value)),end="\t")
        count+=1
    print()    

def currency():
    
    f = open("/usr/local/bin/.user_details.json", 'r')
    user_details = json.load(f)
    
    if('currency' in user_details):
        base=user_details['currency']
        add='?base='
        currency_exchange(add,base)
        print("\nTo set Default assist --currency --setdefault\n")
    else:
        add=''
        base=''
        currency_exchange.currency_exchange(add,base)
        print("\n\nTo Customise Currency Output, Please set default.")
        print("To set Default assist --currency --setdefault\n")