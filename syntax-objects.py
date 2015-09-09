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
    print(fried.whatKind())

def prime():
    eatable = Egg()
    print(eatable.whatKind())

main()
prime()
# if __name__ == "__main__": prime()
