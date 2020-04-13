import sys

print(sys.version)
print(sys.executable)


def greet(parm1):
    greeting = "Hello, {}".format(parm1)
    return greeting


print(greet("World"))
print(greet("Tom"))
print("This is change testing")
