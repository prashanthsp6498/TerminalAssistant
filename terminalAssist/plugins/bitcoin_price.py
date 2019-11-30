
import requests
import colorama
import json
import random

def price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    try:
        response = requests.get(url)
        #print(response)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return
    
    text_list=[]
    data = response.json()
    print("TODAY'S BITCOIN RATE : \n\n")
    print(str(data['bpi']['USD']['description'])+' - '+str(data['bpi']['USD']['rate'])+' Dollars')
    print(str(data['bpi']['EUR']['description'])+' - '+str(data['bpi']['EUR']['rate'])+' Euro')
    print(str(data['bpi']['GBP']['description'])+' - '+str(data['bpi']['GBP']['rate'])+' Pound')