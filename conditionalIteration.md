# Conditional Statements and Interation (Loops)

From the first section, we have learned about the primary types of variables/objects that are used in programming.  Along with this we have learned about the variation in these different data types.  Now we can begin to ask questions of the data, query the data, create new data, and solve problems.  Working with the data is accomplished using three different types of statements -- _if_, _while_, and _for_. 

_if_ is commonly referred to as a conditional statement, meaning it is used to establish a condition and if that condition is satified the code contained in the _if_ statement is excuted. Here is an example.  Please note this is not the correct syntax, I just want you to get a feel for how statements are typed.  

```python
if <what I am saying here is True>:
	<Execute this block of code>
```

 Conditional statements are based on a *boolean* result in that the condition has to be True or False.  And that is how conditional statements will read, if this condition is True then do this thing I am telling you to do.  

Conditional statements can be chained together using _elif_ (else if) and _else_.  As you will learn, _elif_ will set another condition and execute if it is True.  Notice how in the code below, the _if_ asks if it is True and the _elif_ asks if it is False.  This is a simple binary question.  There are only two possibilites in this case.

```python
if <what I am saying here is True>:
	<Execute this block of code>
elif <what I am saying here is False>:
	<Execute this block of code>
```

_else_ does not contain a conditional statements, rather _else_ executes if the other conditional statements above it have not been executed.  Rather that writing in pseudocode, let us now look at some actually conditional statements.

```python

a = 19  #set a to be any value you want

if a > 7:
	print "a is greater than 7"
elif a < 7:
	print "a is less than 7"
else:
	print "a is equal to 7"
```

The example above sets a situation where there are three possibilites.  A given integer can be greater than, less than, or equal to another integer.  Using the code we can capture all possible solutions to such a problem.  Think of the pervious problem in terms of this flow chart in which you enter a code block and the code block is only exited when a statement yields True or until the _else_ condition is reached.

![Conditional Statement Logo](http://www.openbookproject.net/books/bpp4awd/_images/flowchart_chained_conditional.png)



Conditional statements can also be utilized to yield a result in which there are multiple type outputs.  Let's use the _raw_input_ statement to capture use input and then running a conditional statement on that input.  Before you start, if you are using Enthought Canopy, open a new document and name it "conditionals.py".

```python

name = raw_input("Enter your name: ")

if name == "Dan":
	print "Welcome Dan"
elif name == "Stan":
	print "Welcome Stan"
else:
	print "You are not a valid user.  Good bye."
```


For more information on conditional statements see this page: [Open Book Project](http://www.openbookproject.net/books/bpp4awd/ch04.html)