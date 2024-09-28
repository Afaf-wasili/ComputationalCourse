import numpy as np 
'''
<<<<<<< HEAD
#Example: Function to print a string
def Hello():
=======
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
print('len(num):',len(num))
print('sum(num):',sum(num))
print('max(num):',max(num))
print('min(num):',min(num))
'''


'''

def message():
>>>>>>> e81fefab9d5bec8c1f5d1a05cb5f1015ba47b505
    print("Hello world!")
#calling and closing
Hello()
'''
<<<<<<< HEAD

'''
#Example:
def carea():
    radius = 5
=======
'''
def carea(radius):
>>>>>>> e81fefab9d5bec8c1f5d1a05cb5f1015ba47b505
    area = 3.14**radius
    print('Area of circle is', area)
#here a is same is radius, radius=5, we can define a = 5 and do carea(a)
carea()
'''
'''
def carea(radius):
    area = np.pi ** radius
    print('Area of circle is', area)
carea(5)
''
'''
'''
'''
#Example:
def simple_interest(principle=1200, rate = 8, time = 1):
    
    si = principle * rate * time / 100
    print('si:',si)

simple_interest()
'''

<<<<<<< HEAD



#Example: same for the above with different style
=======
'''
>>>>>>> e81fefab9d5bec8c1f5d1a05cb5f1015ba47b505
def simple_interest():
    principle = 1200
    rate = 8
    time =1
    
    si = (principle * rate * time) / 100
#    print("output:",(principle * rate * time) / 100)
#calling and closing otherwise not result will be priniting
simple_interest()
'''
