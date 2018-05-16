## Some side notes

At this point I need to give you some pointer.  Some side notes if you will that help making coding easier to debug and easier for other to undertand your code.

#### Print

Print statements are great ways to debug code.  You can imbed print statements inside code to determine where a given program is failing.  The print statement will print to standard out any variables you request.

#### Use words as variable names

This one just makes life so much easier.  Instead of naming a variable 'i' or 'a', name it close to what it is.  For example,

```python
l = [1,2,3,4,5]

for i in l:
	print i**2

#Instead, this would be much better
listOfInts = [1,2,3,4,5]

for integer in listOfInts:
	print "The squared value of ", str(integer), " is ", str(integer**2)
```

For one thing, the second set of variables is much easier to read.  And chances are when you come back to this code in the future it will be much easier to understand.  Second, instead of just printing the result to standard output, a more constructive sentence is provided so you have a better idea of what is going on.  This is a great example of the way you can use _print_ to debug code.

#### Leave notes in your code

We are all in a hurry.  We want to write some code to solve a problem and move on.  But the one thing that we want out of code is __reusability__.  If the code does something useful, chances are you are going to need that code again.  But unless you have an incredible memory, by the time you come back to the code you may have completely forgotten about how to use the code, what it does, or why you even wrote it in the first place.  To overcome this you need to leave notes and documentation in your code.  Let's take a look at a simple example

There are two ways to leave documentation in the code.  First is using a "#" to make a line unreadable.  The second it using triple single quotes to create a "docstring".  Docstrings provide more info, where as inline "#" comments are just quick notes.