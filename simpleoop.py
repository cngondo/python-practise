#!/usr/bin/python3

# Simple fibonacci
class Fibonacci():
    #  The constructor
    def _init_(self, a, b):
         self.a = a
         self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

# f is the object of Fibonacci()
f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break
    print(r, end= ' ')
