import os
import json
import re
import sys
from datetime import datetime
from plugins import *

if __name__ == "__main__":

    if os.path.isfile("/usr/local/bin/.user_details.json"):
        f = open("/usr/local/bin/.user_details.json", 'r')
        user_details = json.load(f)
        print("\nHey "+user_details['name']+"!\t\t\t"+"Day : " +
              datetime.now().strftime('%B %d,%Y, %H:%M:%S')+"\n")

        assist_args = [re.sub(r'[[\]]', '', i) for i in sys.argv[1:]]

        if(assist_args[0] == '--features'):
            assist_instructions.features()

        if(assist_args[0] == '--help'):
            assist_instructions.help()

        if(assist_args[0] == '--version'):
            assist_instructions.version()

        if(assist_args[0] == '--joke'):
            jokes.joke()

        if(assist_args[0] == '--bitcoin-price'):
            bitcoin_price.price()

        if(assist_args[0] == '--quotes'):
            programming_quotes.quotes()

        if(assist_args[0] == '--cat-fact'):
            random_cat_fact.fact()

        if(assist_args[0] == '--check-speed'):
            os.system("python3 "+user_details['package_location'] +
                      "/assistant/plugins/speedtest.py")

        if(assist_args[0] == '--forcast'):
            forcast.get_weather(user_details['city']["latitude"],
                                user_details['city']["longitude"])

        if(assist_args[0] == '--dictionary'):
            word = input("Enter the Word : ")
            en_dictionary.meaning(word)

        if(assist_args[0] == '--currency'):
            currency_exchange.currency()
        elif('--currency' and '--setbase' in assist_args):
            user_details.currency_setbase()
