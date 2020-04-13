import sys

print(sys.version)
print(sys.executable)


def greet(whotogreet):
    greeting = "Hello, {}".format(whotogreet)
    return greeting


print(greet("World"))
print(greet("Tom"))
print("This is change testing")
