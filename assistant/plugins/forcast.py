import requests
import colorama
import json
import random


def get_woeid(lat,long):
    
    url = 'https://www.metaweather.com/api/location/search/?lattlong=' + \
        str(lat)+','+str(long)+''
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return

    data = response.json()
    woeid = data[0]['woeid']
    return woeid


def get_weather(lat,long):
    woeid = get_woeid(lat,long)

    from datetime import date
    today = date.today()
    now_today = str(today)
    res = now_today.split('-')

    url = 'https://www.metaweather.com/api/location/' + \
        str(woeid)+'/'+str(res[0])+'/'+str(res[1])+'/'+str(res[2])+'/'
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return

    data = response.json()
    name = data[0]['weather_state_name']
    min_temp = data[0]['min_temp']
    max_temp = data[0]['max_temp']

    print(name)
    print("MINIMUM TEMPARATURE : "+str(min_temp))
    print("MAXIMUM TEMPARATURE : "+str(max_temp))

    return name, min_temp, max_temp
