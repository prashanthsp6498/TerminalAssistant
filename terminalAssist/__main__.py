import os
import json
import plugins.speedtest as speed

if __name__ == "__main__":
    data = {}
    '''if not os.path.isfile(".user_details.json"):
        print("Enter user details")
        data['name'] = input("Username : ")
        data['email'] = input("Email ID : ")
        data['dob'] = input("Date Of Birth(dd/mm/yyyy) : ")

        with open(".user_details.json", "w") as fo:
            json.dump(data, fo)
    '''
    if os.path.isfile(".user_details.json"):
        speed.test_speed()`
