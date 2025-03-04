# Scope of the variable
# Lifetime of variable
# Area in which variable is alive (which line no to which line no.)
# t1 = 100


# def simple():
#    t2 = 10
# t2 can only be accessed here
# t2 --> simple function scope
#   print(t2)


# simple()

# error because t2 out of scope and not accessible from this point#
# NameError: name is not defined
# print(t1, t2)

price = 100

# lexical scope
# get_price
# 1. first check for local 'price' available
# 2. Then goes to outer scope(Lexical scope)

# closure is own scope + lexical scope
# grandfather not lexical scopeof child. because child asks father and father resolves call to granfather


# Case 1:
def get_price():
    print("The price of the book is: ", price)


get_price()

# Case 2:
