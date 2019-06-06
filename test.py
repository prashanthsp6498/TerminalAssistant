#! /usr/bin/python3
import os
import sys



try:
    if (sys.argv[1] == '--h' or sys.argv[1] == '--help' ):
        print('--auto\tAutomaticaly follow PEP8')
        print('--run\tTo check standard')
    
    elif sys.argv[1] == '--auto':
        os.system("autopep8 -i terminalAssist/")

    elif sys.argv[1] == '--run':
        os.system("flake8 --max-line-length=90 terminalAssist/")
        choice = input("Is code in PEP8 standard...? [y/n]")
        if choice == 'n' or 'N':
            os.system("autopep8 -i terminalAssist/*/*.py")
        print("Code is Checked")
    else:
        print("unknown option: "+str(sys.argv[1]))
        print("usage: assist [--help] [--auto] [--run]")    
except Exception:
    print("usage: ./test.py [--help] [--auto] [--run]")
