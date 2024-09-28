# Function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Main function
def main():
    # Prompting user for input
    number = int(input("Enter an integer: "))
    
    # Checking if the number is even
    if is_even(number):
        print("The number is even.")
    else:
        print("The number is odd.")

# Calling the main function to run the script
main()
