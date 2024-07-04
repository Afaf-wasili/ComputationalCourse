'''
There are three logical operators in Python.
The "and" operator is used to combine two or more conditions. It returns True if all the conditions are true. Otherwise, it returns False
'''

'''
#Example: Checking Age and Salary for Loan Eligibility
age = 25
salary = 50000

if age >= 18 and salary >= 30000:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")

'''

'''
Example 3: Checking if a User Entered a Valid Username and Password

username = "admin"
password = "pass123"
if username == "admin" and password == "pass123":
    print("Login successful!")
'''
'''
#Example: Checking if a Number is both Positive and Even

num = 8 # test 8 and 9 to understand 
numb =  num % 2
if num > 0 and num % 2 == 0:
    print("The number is positive and even.",num)
else:
     print("The number is positive and odd.",num)
'''



'''
 The "or" operator is used to combine two or more conditions. It returns True if at least one of the conditions is true, and False if all the conditions are false.
'''
'''
#Example: Checking if a Student has Passed in at Least One Subject
subject1 = 70
subject2 = 55
      
if subject1 >= 50 or subject2 >= 50:
    print("The student has passed in at least one subject.")
else:
    print("The student has failed in all subjects.")
'''

#Example: Checking if a Number is Either Divisible by 2 or 5
num = 17  #test 16 
if num % 2 == 0 or num % 5 == 0:
    print("The number is divisible by either 2 or 5.")
else:
    print("The number is not divisible by 2 or 5.")
