'''
#A class is a set of statements that define methods and data attributes. Let’s look at a simple example.
class Rectangle:
    def __init__(self, x, y):
        self.length = x
        self.width = y

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)
r = Rectangle(23,5)
a = r.get_area()
p = r.get_perimeter()

print('Area =',a)
print('Perimeter =',p)

'''
#To make a method or attribute private, start its name with two underscores. Private members are accessible only inside the class. The following example demonstrates this:
class Test:
    def __init__(self):
        self.a = 10
        self.__b = 5

    def display(self):
        print('a =', self.a)
        # private members are accessible within class 
        print('b =', self.__b)


t = Test()
print(t.a)
print(t.display())
# Error! not accesible outside class
#print(t.b)


#The __ str()__ method
class Demo:
    def __init__(self):
        self.message = 'hello world!'
        
    def __str__(self):
        return self.message

d = Demo()
print(d)
