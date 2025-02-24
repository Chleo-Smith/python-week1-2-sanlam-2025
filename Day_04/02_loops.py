i = 1

# while i <= 3:
#    print("vote for Jevan")
#    i = i + 1

# for j in range(3):
#    print(j)

# easy way 1.2
##print odd numbers 1 to 50
# for i in range(1, 50, 2):
#    print(i)

# hard way 1.1
# for i in range(1, 50):
#    if i % 2 != 0:
#        print(i)

##refactor jevan loop 1.3
# for j in range(3):
#    print("vote for Jevan")

# Task 1.1
i = 1
while i < 6:
    print("🔥" * i)
    i = i + 1


# Task 1.2
for j in range(6):
    print("🔥" * j)

# Task 1.3
rows = int(input("Please tell the no of rows? "))
symbol = input("Please tell the pattern?")
n = 1

while n < rows + 1:
    print(symbol * n)
    n = n + 1

# Task 1.4
rows = int(input("Please tell the no of rows? "))
symbol = input("Please tell the pattern?")

# loop stuff
for m in range(1, rows + 1):
    print(symbol * m)
