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
    fo.write("source "+pwd+"/assistant/bin/activate\n")
    fo.write("python3 "+pwd+"/terminalAssist/")
os.system("sudo cp assist /usr/local/bin/")
os.system("sudo chmod 777 /usr/local/bin/assist")
os.system("rm assist")
