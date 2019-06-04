#! /usr/bin/python3
import os
import sys

if sys.argv[1] == '--h':
    print('--auto\tAutomaticaly follow PEP8')
    print('--run\tTo check standard')

try:
    if sys.argv[1] == '--auto':
        os.system("autopep8 -i terminalAssist/")

    if sys.argv[1] == '--run':
        os.system("flake8 --max-line-length=90 terminalAssist/")
        choice = input("Is code in PEP8 standard...? [y/n]")
        if choice == 'n' or 'N':
            os.system("autopep8 -i terminalAssist/*/*.py")

        print("Code is checked")
except Exception as e:
    print(e)
