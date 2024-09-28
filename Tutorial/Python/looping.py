'''
It is also called a repetitive control structure. Sometimes we require a set of statements to be executed a number of times. This type of program execution is called looping. Python provides the following construct

while loop
for loop
'''


'''
while loopis the general format in Python. Statement written inside while statement will execute till condition remain true:

while condition:
   statement
   statement
   etc.

'''
'''
#Example:This program print message many times based on the the start and end with steps:

i = 0  # start with the first number with zero index
n = [1,2, 3, 4, 5]  # a list of numbers
#print("length n:", len(n))  # print the length of the list

while i < len(n):  # loop condition corrected
    print("I love programming in Python!")
    print("length n within i:", n[i])
    i += 1  # increment 

'''
'''
# Example: This program calculates the sum of numbers 

i = 1 #start if it start from 0 it means you give the process more index number and the total is wrong
n = [1,2,3,4]
sum = 0  
while i < len(n):  #while is starting with 1 binary index
    sum += n[i]  #  sum = 0 + num[i]   
    #print("length within i:",n[i])
    i += 1 # increment of jumping
print('The total is', sum)

'''

'''
A for loop is used for iterating over a sequence. You can generate a sequence using range function. The general format of range() function is like:

range (start, stop, step)
The range() function takes three arguments. Start and Step are the optional arguments. A start argument is a starting number of the sequence. If start is not specified it starts with 0.The stop argument is ending number of sequence. The step argument is linear difference of numbers. The default value of the step is 1 if not specified.
'''
'''
#Example:
for i in range(3, 31, 1): # The sequence begins at 3,  The sequence stops before 31, The numbers are incremented by 1.
    print(i)
'''
'''
#Example:
n = [2, 3, 4, 5]
for i in n:
    print(i)
'''
'''
#Example:This program prints backward counting

for i in range(5,0,-1):
    print(i)

'''

'''
#Example: This program prints pattern:A loop that inside another loop is called a nested loop 

for i in range(1,4): #this is how much block i you want to loop the next loop j
    for j in range(1,5):
        print("j=",j)
    

    print()
'''


#Example:

for i in range(0,8):
    print(i)


#Example: to check the even or odd numbers using for loop:

n = [1,2,3,4,5,6,7,8]
sum_even=0
sum_odd=0
count_even=0
count_odd=0


'''
for i in range(1,8,1): # here, it means that the loop is starting looping the first number with zero index counting from 0 to 7 since 0 is considered to have 8
    if n[i] % 2 == 0:
       #sum_even += n[i]
       sum_even = sum_even + n[i]
       count_even += 1
    else:
      sum_odd += n[i]
      count_odd += 1
'''
for i in n:
    if i % 2 ==0:
       sum_even += i
       count_even +=1
    else:
        sum_odd += i
        count_odd += 1

print("the total number of even:",sum_even)
print("how many even number:",count_even)
print("the total number of odd:",sum_odd)
print("how many odd number:",count_odd)











