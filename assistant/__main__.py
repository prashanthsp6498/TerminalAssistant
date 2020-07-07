import os
import json
import re
import sys

if __name__ == "__main__":

    if os.path.isfile("/usr/local/bin/user_details.json"):
        f = open("/usr/local/bin/user_details.json", 'r')
        data = json.load(f)
        print("\nHey "+data['name']+"!\n")

        assist_args=[re.sub(r'[[\]]','',i) for i in sys.argv[1:]]
        
        if(assist_args[0]=='--features'):
            from plugins import assist_instructions
            assist_instructions.features()

        elif(assist_args[0]=='--help'):
            from plugins import assist_instructions
            assist_instructions.help()
        
        elif(assist_args[0]=='--version'):
            from plugins import assist_instructions
            assist_instructions.version()

        elif(assist_args[0]=='--joke'):
            from plugins import jokes
            jokes.joke()

        elif(assist_args[0]=='--bitcoin-price'):
            from plugins import bitcoin_price
            bitcoin_price.price()

        elif(assist_args[0]=='--quotes'):
            from plugins import programming_quotes
            programming_quotes.quotes()

        elif(assist_args[0]=='--cat-fact'):
            from plugins import random_cat_fact
            random_cat_fact.fact()
        
        elif(assist_args[0]=='--check-speed'):
            os.system("python3 "+data['package_location']+"/assistant/plugins/speedtest.py")

        elif(assist_args[0]=='--forcast'):
            from plugins import weather_forcast
            weather_forcast.get_weather()    
        
