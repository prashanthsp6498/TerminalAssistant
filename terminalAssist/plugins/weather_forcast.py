from packages import map
import requests
import colorama
import json
import random
from datetime import date
import os
import sys


package_path = os.path.abspath("packages/map.py")
path_list = package_path.split('/')
path = "/".join(path_list[:6])

sys.path.insert(0, path)

location = map.fetch_location()
map.current_location()
latt = location['latitude']
long = location['longitude']

today = date.today()
now_today = str(today)
res = now_today.split('-')


def get_woeid():
    url = 'https://www.metaweather.com/api/location/search/?lattlong=' + \
        str(latt)+','+str(long)+''
    # print(url)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return

    data = response.json()
    woeid = data[0]['woeid']
    return woeid


def get_weather(woeid):
    url = 'https://www.metaweather.com/api/location/' + \
        str(woeid)+'/'+str(res[0])+'/'+str(res[1])+'/'+str(res[2])+'/'
    # print(url)
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

    return name, min_temp, max_temp


woeid = get_woeid()
temp_name, min_temp, max_temp = get_weather(woeid)

print(temp_name)
print("MINIMUM TEMPARATURE"+str(min_temp))
print("MAXIMUM TEMPARATURE"+str(max_temp))
