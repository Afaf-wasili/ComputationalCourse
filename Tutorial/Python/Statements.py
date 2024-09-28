'''
if condition:
   statement
   statement
   etc.
If the condition is true, statement is executed; otherwise it is skipped
'''
'''
#Example:
number = 5
if number < 0:
   print("The negative number is", number) 
if number == 5:
   print("The number is equal to:", number)
if number > 0:
   print("The positive number is", number)    
'''


'''
if else statement:

if condition:
   statement 1
   etc.
else:
   statement 2
   etc.
The given condition is evaluated first. If the condition is true, statement1 is executed. If the condition is false, statement 2 is executed.
'''

'''
#Example:
number = 5
if number > 0: 
  print("The positive number is", number)
else:
  print("Otherwise")
'''
   
'''
#Example:
# This program test a number is even or odd.

#number = int(input('Enter number: '))

number = 4
result = (number%2)

if number%2 ==0:  #num % 2 will equal 0 if num is even and 1 if number is odd. Does not matter the number 2 it can be 5 still the matter is what after the = is it is 0 or 1
    print("result=",result,"the number is even:",number)
else:
    print("result=",result,"the number is odd:",number)
'''

'''
#When there are more than two possibilities and we need more than two branches, if-elif-else statement is used. Here is the general format of the if-elif-else statement:

if condition_1:
   statement
   statement
   etc.
elif condition_2:
   statement
   statement
   etc.
else:
   statement
   statement
   etc.
elif is an abbreviation of "else if." Again, exactly one branch will be executed. There is no limit of the number of elif statements, but the last branch has to be an else statement.
'''

#Example:

# This program determines greater number.

#x = int(input("Enter first number x:"))
#y = int(input("Enter second number y:"))
'''
x = 4
y = 4

if x < y:
    print (x, "is less than", y)
elif x > y:
    print (x, "is greater than", y)
else:
    print (x, "and", y, "are equal")
    
'''



#Nested Decision Structures: One conditional can also be nested within another. We could have written the above example as follows:

#Example:
# This program determines greater number.

#x = int(input("Enter first number x:"))
#y = int(input("Enter second number y:"))

x = 4
y = 3

if x == y:
         print (x, "and", y, "are equal")
else:
#    print ("otherwise")
    if x < y:
            print (x, "is less than", y)
    else:
            print (x, "is greater than", y)

