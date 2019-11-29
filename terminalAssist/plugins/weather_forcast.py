import requests
import colorama
import json
import random
from datetime import date


today = date.today()
now_today=str(today)
res=now_today.split('-')


def get_woeid(query):
    url = 'https://www.metaweather.com/api/location/search/?query='+query
    #print(url)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return
    
    data = response.json()
    woeid=data[0]['woeid']
    return woeid


def get_weather(woeid):
    url='https://www.metaweather.com/api/location/'+str(woeid)+'/'+str(res[0])+'/'+str(res[1])+'/'+str(res[2])+'/'
    #print(url)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return
    
    data = response.json()
    name=data[0]['weather_state_name']
    min_temp=data[0]['min_temp']
    max_temp=data[0]['max_temp']

    return name,min_temp,max_temp


city_name = input("Enter the City Name :  ")
woeid=get_woeid('london')
temp_name,min_temp,max_temp=get_weather(woeid)

print(temp_name)
print("MINIMUM TEMPARATURE"+str(min_temp))
print("MAXIMUM TEMPARATURE"+str(max_temp))

