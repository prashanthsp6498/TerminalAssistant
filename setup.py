#! /usr/bin/python3
import os

os.system("clear")
if os.path.isfile("/usr/bin/python3"):
    print("Python3 is found")
else:
    print("Python3 is not found")
    os.system("sudo apt-get install python3")
    os.system("sudo apt install python3-pip")
os.system("sudo apt-get install python3-venv")
os.system("sudo pip3 install -r requirements.txt")
if os.path.isfile("assist"):
    os.system("rm assist")
pwd = os.getcwd()
with open("assist", "w") as fo:
    fo.write("source "+pwd+"/venv/bin/activate\n")
    fo.write("python3 "+pwd+"/assistant/")
os.system("sudo cp assist /usr/local/bin/")
os.system("sudo chmod +x /usr/local/bin/assist")
os.system("rm assist")
