from . import color as c


def features():
    print("These are the list of all the features provided by Assist : \n")
    print('--bitcoin-price\t\tCheck current bitcoin price')
    print('--quotes\t\tProgramming Quotes to motivate you during Coding')
    print('--cat-fact\t\tCat facts for your cat :)')
    print('--check-speed\t\tCheck Internet Speed')
    print('--dictionary\t\tCheck the meaning of the word.')
    print('--forcast\t\tThe Current Weather Forcast in your city')
    print('--joke\t\t\tFunny jokes to clear your mind!\n')

    print("Refer documentation for further explination with examples")
    print("Documentation link : ", end="")
    c.prGreen(
        "https://github.com/kushtej/Assist/blob/master/TEMPLATES/FEATURES.md\n\n")


def help():
    print("usage : assist <command>")
    print("Example : assist --bitcoin-price\n")


def version():
    print("assist version 1.0.1")
