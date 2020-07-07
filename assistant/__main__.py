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
        
        if(assist_args[0]=='--joke'):
            from plugins import jokes
            jokes.joke()



