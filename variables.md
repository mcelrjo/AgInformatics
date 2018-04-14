
# Objects

The most basic principle of Python is the object.  What is an object?  Very simply it is a thing.  I realize that defining "object" as a "thing" is probably the worst definition ever (computer scientist are the worst at coming up with names for things). So the easiest way to think about it is that everything is an object but there are certain types of objects.  And what did that brainy computer scientist decide to call the "types" of objects -- you guessed it, "type".  


# Variables

There are six primary types of objects used in Python - integers, floats, boolean, lists, tuples, and dictionaries.  When a object is instantiated, it is assigned a specific "type" based on the syntax.  Rather than trying to explain what a object is, let's start off by creating variables and learning about their properties.  Try out some of the following code.

```python
num = 7
```

By typing "num = 7" you have bound the object "7" to the name "num".  In essence you have created a _variable_. You can now learn the type of "num" by typeing:

```python
type(num)
```

You can see that "num" is of type _int_ because it was an integer.  

Multiple variables can also be assigned at a time. 

```python
num1, num2, num3 = 19, True, "Hippo"
```

In this case we assigned num1 to the integer _19_, num2 to the boolean _True_, and num3 to the string hippo.  You can see the types of these objects by typing type(varaibleName)

But before getting too deep into to the types of variables used it is important to understand some rules related to the naming of variables.

## Naming Variables 

There are a few rules for naming variables/objects (notice I cannot decide whether to refer to things as variables or objects.  I really prefer calling these particular "things" we are making variables, but I am sure someone out there would disagree with me if I did.  Having said, that I am just going to keep flip-flopping so bare with me.) First varibles names cannot start with a number, but the name can contain a number. So,

```python
1sec = 1
```

is a no-no, but
```python
sec1 = 1
```

is okay.

Second, there are certain _reserved words_ can variables cannot be named.  Examples include _and_, _def_, _import_, _open_, etc.  For a full list of reserved words, see

https://pentangle.net/python/handbook/node52.html


### Types of Variables/Objects:  Integers and Floats

Integers (abbreviated INTs and often referred to as such) are non-decimal numbers.  

```python
num = 8
print num
```

Notice you cannot name a variable "int" because int is a special resserved word.  If you are using Canopy or another IDE, special reserved key words will likely turn green or change to another color indicating that variables cannot be named using that word.

Floats are decimal numbers.  

```python
parade = 17.4
type(parade)
```

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
```python
13/2
```

Notice that 13/2 returned the number 6 and the remainder is not returned.  Also, if you were to assign the result of 13/2 to a variable name, the resulting object would have the type int.  So int/int division results in an int.  If the numerator or denominator of division is a float the result will also be a float.  

To get the remainder of an int/int division, use the modulo (%) operator.

```python
13%2
```

Submitting 13%2 returns only the remainder of two ints.  Modulo does not work on float, only ints.  For future reference, modulo or floor division is a good way to check if an int is even or odd as even number will return 0 and odd numbers will return 1.  

All of the other mathematical operators be have exactly as you would expect.  But one should discuss is the double equal - ==.  

### Logical Operators

The double equal is really more of a question than it is a mathematical operator.  I guess that is because it is not a maathematical operator, rather it is a _logical operator_.  In essence, what you are asking when you use == is if two objects are equivalent.  To demonstrate:

```python
a = 7
b = 7
a == b
```

In this example, two int objects were created and assigned variable names.  From this point we asked, are a and b _equal_.  And indeed they are equal so they are equal so the boolean True was returned.  True and False, I should point out, are booleans binary logical objects that can also be assigned to variable names.

```python
a = True
b = False
a == b

a != b
```

In this case, the logical operator _not equal_ was used to determine if a and b were _not_ equivalent which they indeed were not, there for it returned True.  

Many assume that two more logical operators are equivalent _is_ and _is not_.  While in some instances _is_ will return the same and _is not_ will return the same as !=, in most cases in some cases it will not.

```python
numInt = 7
numFloat = 7.0
numInt == numFloat

numInt is numFloat
False
```

In the first case it was asked if numInt is equal to numFloat, which it is.  There is no mathematical difference between an 7 and 7.0.  But when asked if numInt _is_ numFloat, these cannot be equivalent because even though they are mathematically equal they are two different types. :tada:



### Scoping

```python
x = 7

def genX(someVariable):
	x = someVariable
	print x

genX(8)

print x
```
From these few lines of code can you determine what "x" is going to print?  At the start there is a function that defined "genX" that is passed the variable "someVariable".  This function will then set x equal to someVariable and print x. The important point is that all this happens in the genX function scope and does not change what is happening outside the function.  "x" is defined before the genX function is defined and called to create a new value of x but the implementation of genX does not change the original value of "x".  This is the most basic rule of scoping.   

Complex examples of scoping abound on the old interweb.  Just Google "scoping rules python" to see some.  But what I have found over the years is to just remember that what happens in a function (Vegas) stays in a function (Vegas).  In other words, variables created in functions remain within the scope of the function and do not enter the top level scope.  As we will see later, you can return the result of a function to a variable but this creates a new variable or overwrites an existing variable.  As I said, more on this later.

### Types of Variables/Objects: Booleans

Booleans are True/False values.  They are binary values that will be returned from the use of logical operators.  Notice that the syntax for booleans are capitalized True or False.  Booleans will be very important when we get into conditional statements that need to take a specific action when once a given answer has been reached. :+1:

```python
first = True
second = False

#Try some logical operation

first == second
first != second

first is not second

bool(1)

bool(0)
```
[More on Booleans](https://docs.python.org/2.3/whatsnew/section-bool.html)

### Mutability

As we get into the final data types, the question of mutability will arise.  Mutability is just a fancy way to say is something changable after it has been instantiated.  Some data types will be mutable whereas others will not be able to be changed, referred to as immutable.

### Types of Variables/Objects: Strings

Strings are created by enclosing characters in single or double quotes.  Python accepts single or double quotes but single or double quotes cannot be mixed.

```python
myString = "Dr. McElroy is awesome says everyone."
print myString
```
Strings are mutable so they can be changed.  Mutability can be seen by simply adding more characters to the end of the phrase.
```python
myString = myString + " This is a fact."
print myString
```
Notice how the additional string was added to the first string by using the mathematical operator and that this was able to be done by using the variable itself.  This may seem a little strange but this is how it works.  When you assign an object to a name, the first thing that occurs is everything to the right of the equal sign.  So in this case the "myString" and the new string are concatenated together to create an entirely new string.  After the newString is established, it is assigned to the name at the left of the equal sign overwriting the previous name.  It is this order of operations that allows for this to occur.  

So, strings are mutable.  Strings are also indexed making them callable using slicing. For a given string, "string" the "s" is in the 0 position, "t" is in the 1 position, "r" in the 2 position, so on and so forth.  Starting indexing with 0 or 1 varies with language.  Python starts indexing at 0 whereas R indexes starting at 1.  Try out the following code.

```python
myString = "Dr. McElroy is awesome.  Everyone loves him."
myString[0]
myString[1]
#the previous two just return the value at that position.  Let's try slicing now.
myString[0:1]
```
Notice how the last command only returned "D" and not "Dr".  When slicing, the second number is not going to be returned, only the part of the string up to that position.  You can also put in three numbers in the bracket to call positions in a string intermittenly.
```python
#Here are a few methods to call every other element of a string from beginning to end.
myString[0::2]
myString[0:-1:2]
#-1 is just another way to get the last position.  Alternatively if you just leave   # the middle number blank in the slice call it will utilize the entire string.  A    # more #creative way is to do the following.
lastPosition = len(myString)
myString[0:lastPosition:2]
```
The _len()_ function calls the length of a given string (list, tuple, or dictionary).

A string can be called in reverse order.
```python
myString[::-1]
```
Becoming comfortable with the string data type is critical.  Spend some time with the following links to become familiar with other aspects of strings.
[Tutorials Point - Strings](https://www.tutorialspoint.com/python/python_strings.htm)

### Types of Variables/Objects: Lists and Tuples

Lists, Tuples, and Dictionaries are ways of producing collections of other objects.  Lists and Tuples are (for our purposes) essentially the same thing except lists are mutable and tuples are immutable.  Lists are instantiated with brackets whereas Tuples are instantiated with parenthesis.  

Lists and tuples are also indexed, thus making them callable and sliceable (is that even a word?).  So you can get object from a list or tuple easily.  You can also add to lists by positions or just add to the end of a list.  But not tuples of course because they are not mutable.  
```python
fruits = ['apple', 'pear', 'banana']

fruits[0]

fruits.append('kiwi')

print fruits

len(fruits)

fruits[0] = 'grapes'

print fruits

```
In the above, the append function was demonstrated.  This is one of many functions that can be applied to lists using dot notation.  In this case dot notation works by taking the created object, placing a period after it and then typing append.  Sicne append is a function, you then open parenthesis and enter what you would like to append.  You can see the other dot notation functions in Canopy by typing the list object name, followed by a period, then tab to auto complete and return a list of possible functions.  Google some of them and try them out to learn more about them.  

Within a list you can mix the different data types and basically have lists of anything.  You can even have lists of lists-- even lists, within lists, within lists. If it is an object it can be contained within a list.

_Tuples_ function the same was as lists except they are immutable.  So when they are created that is it.  This is beneficial for creating a collection of objects and making sure they do not change over time (which some objects can strangely do). Try creating a tuple using () and then check out the possibility of dot notation associated with the created tuple object -- there is not much functionality to a tuple.

### Types of Variables/Objects: Dictionaries

Dictionaries, also referred to as libraries, are collections of objects with associated key-value pairs.  Dictionaries are extremely useful for creating collection of objects and making them referenceable via a key.  Dictionaries are instantiated with curly brackets/braces {} and key to value are associated by a colon, and different key-value pars are separated by commas.  
```python
students = {'Kevin': ['93', '9873452', 'Virgo'], 'Shirley':['88', '8977652', 'Gemini'], 'Ursula':['99', '9812365', 'Leo']}

print students['Kevin']

print students['Kevin'][0]

#You can append a new key:value pair

students['Nox'] = ['87','9873421','Sagittarius']

#Print the keys of a dictionary

print students.keys()

#what happens when you leave off the parenthesis?

print student.keys

#notice how it printed information about the "object" itself.  More on this later.
```

:octocat: