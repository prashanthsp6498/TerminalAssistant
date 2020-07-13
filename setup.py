#! /usr/bin/python3
from assistant.plugins import user_details
import os

os.system("clear")
if os.path.isfile("/usr/bin/python3"):
    print("Python 3.x was previously installed!")
else:
    print("Python 3.x is not installed!")
    ch = input(
        "Press Y/y to install python 3.x or any other key to Externally install it : ")
    if(ch in ['y', 'Y']):
        print("\nInstalling python3...\n\n")
        os.system("sudo apt-get install python3")

ch = input("Is python3-pip already installed in your machine[yY/Nn] : ")
if(ch in ['y', 'Y']):
    pass
else:
    print("\nInstalling python3-pip...\n\n")
    os.system("sudo apt install python3-pip")

ch = input("\n\nIs python3-venv already installed in your machine[yY/Nn] : ")
if(ch in ['y', 'Y']):
    pass
else:
    print("\nInstalling python3-venv...\n\n")
    os.system("sudo apt install python3-venv")
    print("\n\n Installing required packages for ASSIST\n\n")
    os.system("sudo pip3 install -r requirements.txt")

if os.path.isfile("assist"):
    os.system("rm assist")

if os.path.isfile("usr/local/bin/assist"):
    os.system("rm usr/local/bin/assist")

pwd = os.getcwd()
with open("assist", "w") as fo:
    fo.write("#! /usr/bin/python3\n\nimport os\nimport sys\n")
    fo.write("if(len(sys.argv)>1):\n\t")
    # fo.write("source "+pwd+"/venv/bin/activate\n")
    fo.write("os.system(\"python3 "+pwd+"/assistant/ \"+str(sys.argv[1:]))\n")
    fo.write(
        "else:\n\tprint(\"usage: assist [--version] [--help] [--features]\")")
os.system("sudo mv assist /usr/local/bin/")
os.system("sudo chmod +x /usr/local/bin/assist")

user_details.main()
print("\n\nCongratulations! Assist is all setup and good to go...🎉🎉\n\n")
