import numpy as np 
'''
#Example: Function to print a string
def Hello():
    print("Hello world!")
#calling and closing
Hello()
'''

'''
#Example:
def carea():
    radius = 5
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

'''
'''
#Example:
def simple_interest(principle=1200, rate = 8, time = 1):
    
    si = principle * rate * time / 100
    print('si:',si)

simple_interest()
'''




#Example: same for the above with different style
def simple_interest():
    principle = 1200
    rate = 8
    time =1
    
    si = (principle * rate * time) / 100
#    print("output:",(principle * rate * time) / 100)
#calling and closing otherwise not result will be priniting
simple_interest()
