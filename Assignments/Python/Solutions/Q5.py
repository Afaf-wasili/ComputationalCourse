# Taking integer input from the user
number = int(input("Enter an integer: "))

# Checking conditions
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif number == 0:
    print("The number is zero.")
else:  # number is negative
    if number % 2 == 0:
        print("The number is negative and even.")
    else:
        print("The number is negative and odd.")
