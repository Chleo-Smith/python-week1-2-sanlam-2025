# conditionals (control flow)
# Take a decision -> Choice

# if ... else
# <= 2 -> bike else car
no_of_person = 1

# codition should return boolean| if expects a boolean
if no_of_person <= 2:
    print("We will take the bike for the party")
else:
    print("We will take the car to the party")


name_one = input("Enter user name one: ")
name_two = input("Enter user name two: ")
height_one = float(input("Enter user one height: "))
height_two = float(input("Enter user two height: "))

difference = abs(height_one - height_two)

if height_one > height_two:
    print(f"{name_one} is taller than {name_two} by {difference}cm")
elif height_two > height_one:
    print(f"{name_two} is taller than {name_one} by {difference}cm")
else:
    print(f"{name_one} and {name_two} are the same height")
