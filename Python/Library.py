import math
import statistics
import numpy as np
'''                                                                                                                                                                                      
x1, y1 = (2,3)                                                                                                                                                                           
x2, y2 =  (0,0)                                                                                                                                                                          
d = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))                                                                                                                           
print('The distance between A and B is', d)                                                                                                                                              
'''

'''                                                                                                                                                                                      
angle_degrees = 45                                                                                                                                                                       
angle_radians = math.radians(angle_degrees)                                                                                                                                              
                                                                                                                                                                                         
sin_value = math.sin(angle_radians)                                                                                                                                                      
cos_value = math.cos(angle_radians)                                                                                                                                                      
tan_value = math.tan(angle_radians)                                                                                                                                                      
                                                                                                                                                                                         
print("Angle:", angle_degrees, "degrees")                                                                                                                                                
print("Sine:", sin_value)                                                                                                                                                                
print("Cosine:", cos_value)                                                                                                                                                              
print("Tangent:", tan_value)

'''

'''


data = (21, 3, 7, 17, 35, 31, 46, 7, 43)

a = statistics.mean(data)
b = statistics.median(data)
c = statistics.mode(data)

print('mean =', a)
print('median =', b)
print('mode =', c)
'''
'''
n = math.sqrt(10)
print('Cube =', n)

'''
'''
n = [1,2,3,4,5]
for i in list(n):
    i += 2
print(i)
'''
a = np.array([10,20,30])
b = np.array([1,2,0])
c = a + b
print(c)
