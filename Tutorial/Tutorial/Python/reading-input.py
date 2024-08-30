
#Reading String: The input function reads data that has been entered by the keyboard and returns that data, as a string.

# Get the user's name.
name = str(input("Enter your name: "))  
# Print a greeting to the user. 
print("Hello", name)





#Reading Integer: If we input a number than it returns as string. To convert string number to int we will use int() function that converts a string to an integer.

# Get the user's age.
age = int(input("What is your age? "))

# Display the age.
print("Age:", age)





#Reading Floating Point: Similarly, if we input a floating number than it returns as string. To convert string number to float we will use float() function that converts a string to float number

# Get the length of rectangle.
length = float(input('Enter length '))

# Get the width of rectangle.
width = float(input('Enter width '))

# Calculate the area and assign the result to area variable.
area = length * width

# Display the area.
print('Area of rectangle is', area)

