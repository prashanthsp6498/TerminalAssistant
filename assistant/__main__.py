import os
import json
import re
import sys

if __name__ == "__main__":

    import user_details
    user_details.main()

    if os.path.isfile("/usr/local/bin/user_details.json"):
        f = open("/usr/local/bin/user_details.json", 'r')
        data = json.load(f)
        print("\nHey "+data['name']+"!\n")


