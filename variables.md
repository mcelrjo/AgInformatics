
# Objects

The most basic principle of Python is the object.  What is an object?  Very simply it is a thing.  I realize that defining "object" as a "thing" is probably the worst definition ever (computer scientist are the worst at coming up with names for things). So the easiest way to think about it is that everything is an object but there are certain types of objects.  And what did that brainy computer scientist decide to call the "types" of objects -- you guessed it, "type".  


# Variables

There are six primary types of objects used in Python - integers, floats, boolean, lists, tuples, and dictionaries.  When a object is instantiated, it is assigned a specific "type" based on the syntax.  Rather than trying to explain what a object is, let's start off by creating variables and learning about their properties.  Try out some of the following code.

> num = 7

By typing "num = 7" you have bound the object "7" to the name "num".  In essence you have created a _variable_. You can now learn the type of "num" by typeing:

> type(num)

You can see that "num" is of type _int_ because it was an integer.  

But before getting too deep into to the types of variables used it is important to understand some rules related to the naming of variables.

Naming Variables 

### Integers and Floats

Integers (abbreviated INTs and often referred to as such) are non-decimal numbers.  

> num = 8

Notice you cannot name a variable "int" because int is a special resserved word.  If you are using Canopy or another IDE, special reserved key words will likely turn green or change to another color indicating that variables cannot be named using that word.

> print num

Floats are decimal numbers.  

> parade = 17.4

> type(parade)

To understand why it is important to distinguish between ints and floats, let's do some simple mathematical operations using (you guessed it) _operators_.  

1. addition - +
2. subtraction - -
3. comparision (equivalent) - ==
4. comparison (not equivalent) - !=
5. division - /
6. floor division - %
7. multiplication - *
8. exponential - **

To see the differences between ints and floats try the following

> 13/2
>>> 6

Notice that 13/2 returned the number 6 and the remainder is not returned.  Also, if you were to assign the result of 13/2 to a variable name, the resulting object would have the type int.  So int/int division results in an int.  If the numerator or denominator of division is a float the result will also be a float.  

To get the remainder of an int/int division, use the modulo (%) operator.

> 13%2
>>> 1

Submitting 13%2 returns only the remainder of two ints.  Modulo does not work on float, only ints.  For future reference, modulo or floor division is a good way to check if an int is even or odd as even number will return 0 and odd numbers will return 1.  

All of the other mathematical operators be have exactly as you would expect.



### Scoping

x = 7

def genX(someVariable):
	x = someVariable
	print x

genX(8)

print x

From these few lines of code can you determine what "x" is going to print?  At the start there is a function that defined "genX" that is passed the variable "someVariable".  This function will then set x equal to someVariable and print x. The important point is that all this happens in the genX function scope and does not change what is happening outside the function.  "x" is defined before the genX function is defined and called to create a new value of x but the implementation of genX does not change the original value of "x".  This is the most basic rule of scoping.   
