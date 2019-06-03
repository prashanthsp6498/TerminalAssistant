import requests
import json
from colorama import Fore


def fetch_location():
    url = 'http://api.ipstack.com/check?access_key=3a337b45688b83577a4ae4976582ae66'
    r = requests.get(url)
    location = json.loads(r.text)
    return location


def current_location():
    location = fetch_location()
    print(Fore.GREEN, "You are in ", location['city'], " ", Fore.RESET)
