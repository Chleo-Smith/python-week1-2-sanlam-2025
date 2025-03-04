# -------------------------------------------------------------------------------
# Case 2

price = 200


def get_price_2():
    # try to access before declaration: UnboundLocalError
    # local variable prefereence calways
    # print("The price of the book is: ", price)
    price = 100
    print("The price of the book is: ", price)


get_price_2()

# -------------------------------------------------------------------------------
# Case 3: Both same variable name(Inside and outside)


def get_price_3():
    price = 100  # shadowing
    # outer price lives in shadow of local price
    # local variable has priority
    print("The price of the book is: ", price)
    print("The price of the book is: ", price)


get_price_3()

# -------------------------------------------------------------------------------
# Case 4: Pythin knows locally the variable is present


def get_price_4():
    # try to access before declaration: UnboundLocalError
    # print("The price of the book is: ", price)
    price = 100
    print("The price of the book is: ", price)


get_price_4()

# -------------------------------------------------------------------------------

# 2 phase execution
# 1. compilation - declaration noted. name is noted not value
# 2. execution - print the values

# SUMMARY
# 1. local var preferrence
# 2. UnboundLocalError --> if you try to access before declaration
