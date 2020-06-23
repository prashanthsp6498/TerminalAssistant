import sys
import time


def spinning_cursor():
    while True:
        for cursor in '|/\\/\/\/':
            yield cursor


def spin():
    spinner = spinning_cursor()
    print("Processing....", end='')
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    print()
