from PyDictionary import PyDictionary
import sys
import os


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore


def enablePrint():
    sys.stdout = sys.__stdout__


def meaning(word):
    try:
        dictionary = PyDictionary()
        blockPrint()
        data = dictionary.meaning(word)
        enablePrint()
        for key, value in data.items():
            print()
            print(key+"\n")
            for i in value:
                print("- "+i)

        blockPrint()
        synonym = dictionary.synonym(word)
        enablePrint()

        blockPrint()
        antonym = dictionary.antonym(word)
        enablePrint()

        if(type(synonym) == type(None)):
            pass
        else:
            print("\nSynonym : "+str(synonym))

        if(type(antonym) == type(None)):
            pass
        else:
            print("Antonym : "+str(antonym)+"\n")
    except:
        enablePrint()
        print("Sorry! "+word +
              " is not in English Dictionary. Please check the spelling...\n")
