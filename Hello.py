import sys

A = 6
b = 7
C= 1
print ("Hello World", A)
print("My second hello", A + b)
print(sys.version)
print(sys.executable)


def greet(whotogreet):
    greeting = "Hello, {}".format(whotogreet)
    return greeting


print(greet("World"))
print(greet("Tom"))
