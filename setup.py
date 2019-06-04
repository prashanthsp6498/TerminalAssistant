#! /usr/bin/python3
import os

os.system("clear")
if os.path.isfile("/usr/bin/python3"):
    print("Python3 is found")
else:
    print("Python3 is not found")
    os.system("sudo apt-get install python3")
    os.system("sudo apt install python3-pip")
os.system("sudo pip3 install -r requirements.txt")
if os.path.isfile("assistant"):
    os.system("rm assistant")
pwd = os.getcwd()
with open("assistant", "w") as fo:
    fo.write("python3 "+pwd+"/terminalAssist/")
os.system("sudo cp assistant /usr/local/bin/")
