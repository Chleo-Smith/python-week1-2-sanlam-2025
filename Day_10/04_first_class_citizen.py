# in oythin
# function treated as first class citizen (value)

# rules
# 1. assign to variable
# 2. pass as argument
# 3. return

# rules
# 1. functions: assign to variable
# 2. functions: pass as argument
# 3. functions: return

# 1. assign to var
from Day_10 import f2

x = 1


def greet(name):
    return f"hi, {name}"


# print(type(greet))

# y = greet  # functions

# print(y("Jamie"))


def sayHello():
    return "Hello, "


# functions: pass as argument - say_hello(function) passed as argument
def greeting(say_hello, name):
    print(say_hello() + name)


# greeting(sayHello, "Python")

# -------------------------------------------------------------------------------

# functional languages: F#, Haskell, Scala - Recursion

# -------------------------------------------------------------------------------


# 3 function : returned


def f1():
    def f2():
        print("HI")

    return f2


# make it print hi


print(f1())
