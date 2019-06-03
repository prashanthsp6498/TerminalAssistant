#! /usr/bin/python3
import os

os.system("rm assistant")
if os.path.isfile("assistant"):
    os.system("rm assistant")
pwd = os.getcwd()
with open("assistant", "w") as fo:
    fo.write("python3 "+pwd+"/terminalAssist/")
os.system("sudo cp assistant /usr/local/bin/")
