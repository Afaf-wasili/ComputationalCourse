'''
It is also called a repetitive control structure. Sometimes we require a set of statements to be executed a number of times. This type of program execution is called looping. Python provides the following construct

while loop
for loop
'''


'''
Here is the general format of the while loop in Python. Statement written inside while statement will execute till condition remain true:

while condition:
   statement
   statement
   etc.

'''
'''
#Example:This program print message 5 times.

i = 1 #first
while i <= 5: #end , the end must stop at 5
    print("I love programming in Python!")
 #   print("i=",i)

    i += 1  # i = i+ 1 #steps one by one, i = i +2 steps two numbers by two, etc
'''
'''
# This program print n natural numbers.

#n = int(input('Enter the value of n: '))
n = [0,1,2,3,4]
i = 0
while i < len(n):
    #print("i=",i)    
    print("Afaf")
    i += 1
'''

# This program calculates the sum of numbers entered by the user.
'''
i = 0#start
sum = 0 #start
num = [1,2,3,4]


while i < len(num):
    sum += num[i]
    i += 1 #steps  i = i+1 same as i +=1
print('The total is', sum)
'''


'''
A for loop is used for iterating over a sequence. You can generate a sequence using range function. The general format of range() function is like:

range (start, stop, step)
The range() function takes three arguments. Start and Step are the optional arguments. A start argument is a starting number of the sequence. If start is not specified it starts with 0.The stop argument is ending number of sequence. The step argument is linear difference of numbers. The default value of the step is 1 if not specified.
'''

'''
#Example:
for i in range (10):
     print(i, end = ' ')
'''
'''

#Example:
for i in range(3, 31, 1):
    print(i, end = ' ')

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

#Example: to check the even or odd numbers

n = [1,2,3,4,5,6,7,8]
sum_even=0
sum_odd=0
count_even=0
count_odd=0
for i in range(0,8,2):
    if n[i] % 2 == 0:
       sum_even += n[i]
       count_even += 1
    else:
      sum_odd += n[i]
      count_odd += 1

print("the total number of even:",sum_even)
print("how many even number:",count_even)
print("the total number of odd:",sum_odd)
print("how many odd number:",count_odd)

