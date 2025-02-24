user_input = input("Enter your favorite ice cream flavour: ")

stock = ["vanilla", "chocolate", "cookie dough", "tin roof"]

cleaned_input = user_input.strip(" ").lower()

# 1.1 and 1.2
# if cleaned_input == "vanilla":
#    print(f"Yes, We have {cleaned_input} in stock 😊")
# elif cleaned_input == "chocolate":
#    print(f"Yes, We have {cleaned_input} in stock 😊")
# elif cleaned_input == "cookie dough":
#    print(f"Yes, We have {cleaned_input} in stock 😊")
# elif cleaned_input == "tin roof":
#    print(f"Yes, We have {cleaned_input} in stock 😊")
# else:
#    print(f"Unfortunately, we are all out of {cleaned_input} 😥 ")

if (
    (cleaned_input == "vanilla")
    or (cleaned_input == "chocolate")
    or (cleaned_input == "cookie dough")
    or (cleaned_input == "tin roof")
):
    print(f"Yes, We have {cleaned_input} in stock 😊")
else:
    print(f"Unfortunately, we are all out of {cleaned_input} 😥 ")

# 1 . 3
if cleaned_input in stock:
    print(f"Yes, We have {cleaned_input} in stock 😊")
else:
    print(f"Unfortunately, we are all out of {cleaned_input} 😥 ")
