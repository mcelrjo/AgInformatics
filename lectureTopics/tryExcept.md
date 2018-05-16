## Keeping It Running: Try/Except Statements

As you begin to debug code and find errors, it is beneificial to try to catch problems in the middle of a program, handle the program so the program does not crash, and keep the program running.  This is done with _try_ _except_ statements.

Try/except statements are extremely useful for catching issues you know your script may encounter that would normally cause the program to crash. When I say you catch an error, I am talking about what are commonly referred to as "standar errors" or "exceptions".  These "exceptions" have specific names that Python recognizes as programming errors.  To undertand this more, try the following code.

```python
import doubledutch
```
This raised an "ImportError".  There is no module named doubledutch.
```python
int('two')
```
This raised a "ValueError".  A string cannot be converted to an integer.
```python
print greenGrass
```
This raised a "NameError".  Unless the object/variable 'greenGrass' has been defined.
```python
myList = [1,2,3]
myList[4]
```
This raised an "IndexError" as there was not a fourth object in the list.

What makes try/except statements so useful is that you can "catch" these exceptions, handle them, and allow your program to keep running.  Let's take the last example above and handle it.
```python
myList = [1,2,3]
try:
	print myList[4]
except IndexError:
	print "The list is only " + str(len(myList)) + " objects long."
```
In this case the exception was actually named, so it is only going to catch and handle the index error.  You can leave the "IndexError" out but then it will capture anything.

Exceptions can also be captured with "if" statements but these are less robust. 

```python
num = 1
denom = 0
if denom == 0:
	print "the denominator cannot be zero"
else:
	print num/denom 
```

```python
num = 1
denom = 0
try:
	num/denom
except ZeroDivisionError:
	print "Denominator cannot be zero"
```
In the above two examples, the same goal is accomplished because there is only one type of exception to catch.  Most problems are not going to be this way.

##### Problem #1:

Develop a function that takes two user inputs and multiply the two inputs and return the result.  In your test case, accidentially enter one of the inputs as a string.  Handle the exception and return a message to the user that only numbers are not allowed.  