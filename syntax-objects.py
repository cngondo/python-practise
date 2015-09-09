#!/usr/bin/python3

class Egg:
    #following self can be arguments
    def __init__(self, kind = "fried"):
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    fried = Egg()
    scrambled = Egg("scrambled")
    prime()
    print(fried.whatKind())

def prime():
    eatable = Egg()
    print(eatable.whatKind())

if __name__ == "__main__": prime()
# ln 21 allows us to call the main function that contains code that enables us to
# run modules and functions even before they have been definesd in the code
