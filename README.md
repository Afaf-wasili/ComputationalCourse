Some useful commands:

open or create  code (.py or .cpp ) and .txt
emacs -nw code (.py or .cpp ) and .txt 

change name of code or folder
mv  old name  new name

ls
to list the file inside directory  or folder

cd to enter the folder only

cd ../ to enter to back folder


save code (.py or .cpp) and .txt
control+x+s

to exit the code (.py or .cpp ) or .txt
control+z

mkdir name
to create a new folder 

rm ...
to remove code (.py or .cpp ) or .txt

rm -r ...
to remove folder


cp ..    .
copy code (.py or .cpp ) or .txt in same account

cp -r .. .
to copy directory in same account


scp -r origional-account  .
to copy directory from account to another one

pwd
to define the current path


comment out many lines in python or c++

'''


'''






comment out for one line in python or c++
# 




**  ^ power. Example, radius^2 it means radius**2
















Naming Rule of Variable:

To name variables in Python, you must follow these rules:

A variable name can be of any size
A variable name have allowed characters, which are a-z, A-Z, 0-9 and underscore (_)
A variable name should begin with an alphabet or underscore
A variable name should not be a keyword
A variable name cannot contain spaces.
Uppercase and lowercase characters are distinct.



Keywords:

There are some reserved words in Python which have predefined meaning called keywords. These words may not be used as variable name. Some commonly used Keywords are given below:

and	del	from	not	while
as	elif	global	or	with
assert	else	if	pass	yield
break	except	import	print	
class	exec	in	raise	
continue	finally	is	return	
def	for	lambda	try	



Garbage collection:


When you assign a value to a variable, the variable will reference that value until you assign it a different value. For example,  The statement in Line 1 creates a variable named amount and assigns it the value 10.

Then, the statement in Line 2 assigns a different value, 5, to the amount variable.


The old value, 10, is still in the computer’s memory, but it can no longer be used because it isn’t referenced by a variable. When a value in memory is no longer referenced by a variable, the Python interpreter automatically removes it from memory. This process is known as garbage collection.
# ComputationalCourse




math module
This module provides access to the mathematical functions. All return values of mathematical functions are floats. The Math Library not only has functions but also useful constants like π and e. To use the functions or the constants in your program you must apply the dot operator. The general syntax for usage is math.function() or math.constant.

Some of the functions and constants of math modules are:

math.sqrt(x)	Return the square root of x.
math.ceil(x)	Return the ceiling of x, the smallest integer greater than or equal to x.
math.floor(x)	Return the floor of x, the largest integer less than or equal to x.
math.pow(x,y)	Return x raised to the power y. Unlike the built-in ** operator, math.pow() converts both its arguments to type float. Use ** or the built-in pow() function for computing exact integer powers.
math.fabs(x)	Return the absolute value of x.
math.radians(x)	Return the radians of x degree.
math.sin(x)	Return the sine of x radians.
math.cos(x)	Return the cosine of x radians.
math.tan(x)	Return the tangent of x radians.
math.pi	The mathematical constant π = 3.141592….
math.e	The mathematical constant e = 2.718281…









statistics module
This module provides functions for calculating mathematical statistics of numeric (Real-valued) data.

statistics.mean(data)	Return the sample arithmetic mean of data which can be a sequence or iterable.
statistics.median(data)	Return the median (middle value) of numeric data, using the common "mean of middle two" method.
statistics.mode(data)	Return the single most common data point from discrete or nominal data.