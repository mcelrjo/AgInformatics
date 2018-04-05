
# Objects

The most basic principle of Python is the object.  What is an object?  Very simply it is a thing.  I realize that defining "object" as a "thing" is probably the worst definition ever (computer scientist are the worst at coming up with names for things). So the easiest way to think about it is that everything is an object but there are certain types of objects.  And what did that brainy computer scientist decide to call the "types" of objects -- you guessed it, "type".  


# Variables

There are six primary types of objects used in Python - integers, floats, boolean, lists, tuples, and dictionaries.  When a object is instantiated, it is assigned a specific "type" based on the syntax.  Rather than trying to explain what a object is, let's start off by creating variables and learning about their properties.  Try out some of the following code.

> num = 7

By typing "num = 7" you have bound the object "7" to the name "num".  In essence you have created a _variable_. You can now learn the type of "num" by typeing:

> type(num)

You can see that "num" is of type _int_ because it was an integer.  

Multiple variables can also be assigned at a time. 

> num1, num2, num3 = 19, True, "Hippo"

In this case we assigned num1 to the integer _19_, num2 to the boolean _True_, and num3 to the string hippo.  You can see the types of these objects by typing type(varaibleName)

But before getting too deep into to the types of variables used it is important to understand some rules related to the naming of variables.

## Naming Variables 

There are a few rules for naming variables/objects (notice I cannot decide whether to refer to things as variables or objects.  I really prefer calling these particular "things" we are making variables, but I am sure someone out there would disagree with me if I did.  Having said, that I am just going to keep flip-flopping so bare with me.) First varibles names cannot start with a number, but the name can contain a number. So,

> 1sec = 1

is a no-no, but

> sec1 = 1

is okay.

Second, there are certain _reserved words_ can variables cannot be named.  Examples include _and_, _def_, _import_, _open_, etc.  For a full list of reserved words, see

https://pentangle.net/python/handbook/node52.html


### Types of Variables/Objects:  Integers and Floats

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

All of the other mathematical operators be have exactly as you would expect.  But one should discuss is the double equal - ==.  

### Logical Operators

The double equal is really more of a question than it is a mathematical operator.  I guess that is because it is not a maathematical operator, rather it is a _logical operator_.  In essence, what you are asking when you use == is if two objects are equivalent.  To demonstrate:

> a = 7
> b = 7
> a == b
>>> True

In this example, two int objects were created and assigned variable names.  From this point we asked, are a and b _equal_.  And indeed they are equal so they are equal so the boolean True was returned.  True and False, I should point out, are booleans binary logical objects that can also be assigned to variable names.

> a = True
> b = False
> a == b
>>> False
> a != b
>>> True

In this case, the logical operator _not equal_ was used to determine if a and b were _not_ equivalent which they indeed were not, there for it returned True.  

Many assume that two more logical operators are equivalent _is_ and _is not_.  While in some instances _is_ will return the same and _is not_ will return the same as !=, in most cases in some cases it will not.

``` python
numInt = 7
numFloat = 7.0
numInt == numFloat

numInt is numFloat
False
```

In the first case it was asked if numInt is equal to numFloat, which it is.  There is no mathematical difference between an 7 and 7.0.  But when asked if numInt _is_ numFloat, these cannot be equivalent because even though they are mathematically equal they are two different types.  



### Scoping

x = 7

def genX(someVariable):
	x = someVariable
	print x

genX(8)

print x

From these few lines of code can you determine what "x" is going to print?  At the start there is a function that defined "genX" that is passed the variable "someVariable".  This function will then set x equal to someVariable and print x. The important point is that all this happens in the genX function scope and does not change what is happening outside the function.  "x" is defined before the genX function is defined and called to create a new value of x but the implementation of genX does not change the original value of "x".  This is the most basic rule of scoping.   

Complex examples of scoping abound on the old interweb.  Just Google "scoping rules python" to see some.  But what I have found over the years is to just remember that what happens in a function (Vegas) stays in a function (Vegas).  In other words, variables created in functions remain within the scope of the function and do not enter the top level scope.  As we will see later, you can return the result of a function to a variable but this creates a new variable or overwrites an existing variable.  As I said, more on this later.

### Types of Variables/Objects: Booleans

Booleans are 

:octocat: