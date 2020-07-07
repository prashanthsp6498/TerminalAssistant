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
    fo.write("#! /usr/bin/python3\n\nimport os\nimport sys\n")
    fo.write("if(len(sys.argv)>1):\n\t")
    # fo.write("source "+pwd+"/venv/bin/activate\n")
    fo.write("os.system(\"python3 "+pwd+"/assistant/ \"+str(sys.argv[1:]))\n")
    fo.write("else:\n\tprint(\"usage: assist [--version] [--help] [--features]\")")
os.system("sudo mv assist /usr/local/bin/")
os.system("sudo chmod +x /usr/local/bin/assist")

from assistant import user_details
user_details.main()