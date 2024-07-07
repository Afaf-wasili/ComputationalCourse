import numpy as np
'''
useful methods:
append()
Python provides methods that operate on lists. For example, append adds a new element to the end of a list
extend()
extend takes a list as an argument and appends all of the elements
sort()
sort arranges the elements of the list from low to high
pop()
Delete an element from list at the specified position. If you don't provide an index, it deletes and returns the last element.
remove()
If you know the element you want to remove (but not the index), you can use remove
insert()
Adds an element at the specified position
index()
Returns the index of the first element with the specified value or in different words, it tells us the index of element
reverse()
Reverses the order of the list
count()
Returns the number of elements with the specified value
The list() Constructor
The list() constructor creates a new empty list.
np.arange() method
np.arange() will create arrays with regularly incrementing values. A few examples are given here:
'''
'''
t = ['a', 'b', 'c','d']
y =['m', 'n']
t.append(y)
print(t)
'''
'''
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
'''
'''
L = [34,66,12,89,28,99]
L.sort(reverse = True)
print(L)
'''
'''
t = ['a', 'b', 'c']
#x = t.pop()
x = t.pop(1)
print(t)
print(x)
'''
'''
t = ['a', 'b', 'c']
#t.remove('b')
#t.insert(2,'x')
x = t.index('b')
print(t)
print(x)
'''
'''
t = [4,8,7,8,8]
x = t.count(7)
print(x)
'''
'''
#n = list(range(10))
#n  = range(10)
print(n)
'''
a = np.arange(10)
#a = np.arange(3,8)
#a = np.arange(1,10,2)
print(a)
