# Task 1.1
i = 1
while i < 6:
    print("🔥" * i)
    i = i + 1


# Task 1.2
for j in range(6):
    print("🔥" * j)

# Task 1.3
rows = int(input("Please tell the no of rows?:  "))
symbol = input("Please tell the pattern?: ")
n = 1

while n < rows + 1:
    print(symbol * n)
    n = n + 1

# Task 1.4
rows = int(input("Please tell the no of rows?: "))
symbol = input("Please tell the pattern?: ")

for m in range(1, rows + 1):
    print(symbol * m)
