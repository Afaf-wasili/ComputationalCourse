'''
len():The function len returns the length of a list.
sum():Returns the sum of a list.
max():Returns the largest item in a list.
min():Returns the smallest item in a list.
'''
'''
num = [10,4,90]
len(num)
sum(num)
max(num)
min(num)
print(len(num))
print(sum(num))
print(max(num))
print(min(num))
'''
'''
def message():
    print("Hello world!")

message()
'''
'''
def carea(radius):
    area = 3.14*radius*radius
    print('Area of circle is', area)
#here a is same is radius, radius=5, we can define a = 5 and do carea(a)
a = 5
carea(a)
'''

def simple_interest(principle = 1200, rate = 8, time = 1):

    si = principle * rate * time / 100
    print(si)

simple_interest()
#simple_interest(principle=1200) # this is correct is principle does not have a value in the function
