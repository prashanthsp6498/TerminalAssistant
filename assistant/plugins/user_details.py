import os
import json
import re

data = {}

def validate_email(email):
    if(bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)) is True):
        data['email'] = email
        return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))
    else:
        print("enter correct email address")
        exit(0)


def validate_dob(dob):
    import datetime
    try:
        date = dob.split("/")
        datetime.datetime(year=int(date[2]), month=int(
            date[1]), day=int(date[0]), hour=0)
        data['dob'] = dob
    except ValueError as err:
        print(err)
        exit(0)


def validate_city(city):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="assist")
    try:
        location = geolocator.geocode(city)
        choice = input("\n Is your city Address " +
                       str(location.address)+" (Yy/Nn) :  ")
        if(choice == 'y' or choice == 'Y'):
            city_dict = {}
            city_dict['address'] = location.address
            city_dict['latitude'] = location.latitude
            city_dict['longitude'] = location.longitude
            data['city'] = city_dict

        elif(choice == 'N' or choice == 'n'):
            print("please enter correct city name")
    except:
        print("Please enter correct city or some functions may not be available")


def main():
    if not os.path.isfile("/usr/local/bin/.user_details.json"):
        print("Enter your profile details : ")

        
        data['name'] = input("Username : ")
        validate_email(input("Enter Email :"))
        validate_dob(input("Enter date of Birth(dd/mm/yyyy) :"))
        validate_city(input("Enter your city name : "))

        data['package_location']=os.getcwd()
        
        with open(".user_details.json", "w") as fo:
            json.dump(data, fo)  # indent=4

        os.system("mv .user_details.json /usr/local/bin/")
