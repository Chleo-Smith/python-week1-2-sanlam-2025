# f = input("Please provide your fahrenheit: ")
# c = (float(f) - 32) * 5 / 9
# c = int(c)

# print(f"The {f}°F is {c}°C")

# year = input("Please provide your birth year: ")
# out = 2025 - int(year)
# print(f"Your age is {out}")


# r = input("Provide the radius of the circle : ")
# r = float(r)
# area = 3.14 * r**2

# print("Area of circle is: " + str(area))


# QUESTION 4
load = input("Please enter your number: ")
loader = int(load) // 10
output = loader * "="
blank = (10 - loader) * " "
print(f"[{output}{blank}] {load}%")
