import os
import json
import re
import sys
from datetime import datetime

if __name__ == "__main__":

    if os.path.isfile("/usr/local/bin/.user_details.json"):
        f = open("/usr/local/bin/.user_details.json", 'r')
        user_details = json.load(f)
        print("\nHey "+user_details['name']+"!\t\t\t"+"Day : "+datetime.now().strftime('%B %d,%Y, %H:%M:%S')+"\n")

        assist_args = [re.sub(r'[[\]]', '', i) for i in sys.argv[1:]]
        
        if(assist_args[0] == '--features'):
            from plugins import assist_instructions
            assist_instructions.features()

        if(assist_args[0] == '--help'):
            from plugins import assist_instructions
            assist_instructions.help()

        if(assist_args[0] == '--version'):
            from plugins import assist_instructions
            assist_instructions.version()

        if(assist_args[0] == '--joke'):
            from plugins import jokes
            jokes.joke()

        if(assist_args[0] == '--bitcoin-price'):
            from plugins import bitcoin_price
            bitcoin_price.price()

        if(assist_args[0] == '--quotes'):
            from plugins import programming_quotes
            programming_quotes.quotes()

        if(assist_args[0] == '--cat-fact'):
            from plugins import random_cat_fact
            random_cat_fact.fact()

        if(assist_args[0] == '--check-speed'):
            os.system("python3 "+user_details['package_location'] +
                      "/assistant/plugins/speedtest.py")

        if(assist_args[0] == '--forcast'):
            from plugins import forcast
            forcast.get_weather(user_details['city']["latitude"],
                                user_details['city']["longitude"])

        if(assist_args[0] == '--dictionary'):
            from plugins import en_dictionary
            word=input("Enter the Word : ")
            en_dictionary.meaning(word)
        
        if(assist_args[0] == '--currency'):
            from plugins import currency_exchange
            currency_exchange.currency()

        elif('--currency' and '--setbase' in assist_args ):
            from plugins import user_details
            user_details.currency_setbase()
        # elif('--currency' and '--addcountry' in assist_args ):
        #     print("hi")