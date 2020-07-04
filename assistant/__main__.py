import os
import json
import plugins.speedtest as speed


import re
def validate_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def validate_dob(dob):
  import datetime
  try:
      datetime.datetime.strptime(dob,"%d/%m/%y")
  except ValueError as err:
      print(err)

validate_dob('33/09/2002')

# if __name__ == "__main__":
#     data = {}
#     if not os.path.isfile("user_details.json"):
#         print("Enter user details")

#         data['name'] = input("Username : ")
#         data['email'] = input("Email ID : ")
#         data['dob'] = input("Date Of Birth(dd/mm/yyyy) : ")

#         with open("user_details.json", "w") as fo:
#             json.dump(data, fo)
    
#     if os.path.isfile("user_details.json"):
#         speed.test_speed()
