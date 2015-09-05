#!/usr/bin/python3

# syntax for functions
# The following checks if a number is prime and prints "x is prime"
def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} * {}".format(n, x, n // x))
            return False
    else:
        print(n, " is a prime number")
        return True

for x in range(1,20):
    # The function is invoked in a for loop
    isprime(x)
