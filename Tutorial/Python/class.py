# A class is a set of statements that define methods and data attributes with many functions. Let’s look at
# a simple example.

'''

                              
# The __str__ method

class Demo:
    def __init__(self):  #Initializes the state of the object when it is created.
        self.message = 'hello world!'

    def __str__(self):   #Defines how the object is converted to a string for display.
        return self.message

Demo()
print(Demo())
'''

                                                                                                     

#Example:
class Rectangle:
    # Define the Rectangle class with methods to initialize and calculate area and perimeter.

    def __init__(self, x, y): # initialization
        # Constructor method to initialize a Rectangle object.
        # Parameters:
        # x - length of the rectangle
        # y - width of the rectangle
    
        self.length = x
        self.width = y
    def get_area(self):
        # Method to calculate the area of the rectangle.
        # Returns:
        # The area of the rectangle (length * width).
        return self.length * self.width

    def get_perimeter(self):
        # Method to calculate the perimeter of the rectangle.
        # Returns:
        # The perimeter of the rectangle (2 * (length + width)).
        return 2 * (self.length + self.width)


#for simiplicity reason:
#Rectangle(23,5).get_perimeter()
#print(Rectangle(23,5).get_perimeter())

'''
Create an instance of the Rectangle class with length 23 and width 5.
r = Rectangle(23, 5)
# Call the get_area method on the instance r and store the result in variable a.
a = Rectangle(23, 5).get_area()

# Call the get_perimeter method on the instance r and store the result in variable p.
p = Rectangle(23, 5).get_perimeter()

# Print the calculated area and perimeter.
print('Area =', a, 'Perimeter =', p)
'''








# To make a method or attribute private, start its name with two underscores.
# Private members are accessible only inside the class. The following example demonstrates this:

class Test:
    def __init__(self):
        self.a = 10       # Public attribute
        self.b = 5       # Protected attribute (conventionally, should be used internally)
        self.c = 20      # Private attribute (name mangling)

    def display(self):
        print('a =', self.a)
        # private members are accessible within class                                                       
        print('b =', self.b)
        print('c =', self.c)   # Accessing the private attribute __c within the class

# Create an instance of the Test class

Test().display()
#print(Test().display())
