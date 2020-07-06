import os
import json
import re
import sys

if __name__ == "__main__":

    if os.path.isfile("/usr/local/bin/user_details.json"):
        f = open("/usr/local/bin/user_details.json", 'r')
        data = json.load(f)
        print("\nHey "+data['name']+"!\n")

        if(sys.argv[1]=='--joke'):
            from plugins import jokes
            jokes.joke()
