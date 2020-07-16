#! /usr/bin/python3
import os
import sys


try:
    if (sys.argv[1] == '--h' or sys.argv[1] == '--help'):
        print('\n--auto\tAutomaticaly follow PEP8')
        print('--run\tTo check standard\n')

    elif sys.argv[1] == '--auto':
        os.system("autopep8 -i assistant/*/*.py")

    elif sys.argv[1] == '--run':
        os.system("flake8 --max-line-length=90 assistant/")
        choice = input("Is code in PEP8 standard...? [y/n]")
        if choice == 'n' or 'N':
            os.system("autopep8 -i assistant/*/*.py")
        print("Code is Checked")
    else:
        print("unknown option: "+str(sys.argv[1]))
        print("usage: assist [--help] [--auto] [--run]")
except Exception:
    print("usage: ./test.py [--help] [--auto] [--run]")
