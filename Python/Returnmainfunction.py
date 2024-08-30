# Define a function that adds two numbers and returns the result
def add_numbers(a, b):
    result = a + b
    return result  # Return the result of the addition

# Define the main function
def main():
    # Call the add_numbers function with two integers
    sum_result = add_numbers(5, 3)
    
    # Print the result
    print(f"The sum of 5 and 3 is: {sum_result}")
    
    # Return an exit code (simulating int main)
    return 0

# Directly call main and store the return value

main()
