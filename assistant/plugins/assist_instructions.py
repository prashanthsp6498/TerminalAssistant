def features():
    print("These are the list of all the features provided by Assist : \n")
    print('--bitcoin-price\tCheck current bitcoin price')
    print('--quotes\tProgramming Quotes to motivate you during Coding')
    print('--cat-fact\tCat facts for your cat :)')
    print('--check-speed\tCheck Internet Speed')
    print('--forcast\tThe Current Weather Forcast in your city')
    print('--joke\tFunny jokes to clear your mind!\n')

    print("Refer documentation for further explination with examples")
    print("Documentation link : ",end="")
    print("https://github.com/kushtej/Assist/blob/master/TEMPLATES/FEATURES.md\n")

def help():
    print("usage : assist <command>")
    print("Example : assist --bitcoin-price\n")

def version():
    print("assist version 1.0.0")