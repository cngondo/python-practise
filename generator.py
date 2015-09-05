#!/usr/bin/python3

# syntax for functions
# The following checks if a number is prime and prints "x is prime"
def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

# The generator function
# Yield is like return, but in this case when isprime() is called again,
# it continues execution to the next line...sort of like saving the state
# the function continues to execute
# Creates an iterator
def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1

for n in primes():
    if n > 100: break
    print(n)
