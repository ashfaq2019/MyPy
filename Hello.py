import sys

print(sys.version)
print(sys.executable)


def greet(parm2):
    greeting = "Hello, {}".format(parm2)
    return greeting


print(greet("World"))
print(greet("Tom"))

print("This is second change testing")
