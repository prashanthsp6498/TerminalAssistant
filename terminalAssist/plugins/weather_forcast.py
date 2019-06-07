import requests
import colorama
import json


def weather_forcast():
    #url = 'https://community-open-weather-map.p.rapidapi.com/weather'
    url='https://community-open-weather-map.p.rapidapi.com/weather?callback=test&id=2172797&units=%22metric%22+or+%22imperial%22&mode=xml%2C+html&q=Delhi%2Cin'
    headers = {
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
        "X-RapidAPI-Key": "bec0ac22dbmshaa67ef6ae8d3009p1734b7jsn5e7b105167d1"
    }
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED,
              'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return
    #print(response)
    weather=json.loads(response)
    print(weather)

