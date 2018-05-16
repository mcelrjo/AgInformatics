# Conditional Statements and Interation (Loops)

From the first section, we have learned about the primary types of variables/objects that are used in programming.  Along with this we have learned about the variation in these different data types.  Now we can begin to ask questions of the data, query the data, create new data, and solve problems.  Working with the data is accomplished using three different types of statements -- _if_, _while_, and _for_. 

### The _IF_ statement -- Setting a Condition

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



Conditional statements can also be utilized to yield a result in which there are multiple type outputs.  Let's use the _raw_input_ statement to capture use input and then running a conditional statement on that input.  Before you start, if you are using Enthought Canopy, open a new document and name it "conditionals.py".  Type out the following code and run it.  Trying different inputs to see the result.

```python

name = raw_input("Enter your name: ")

if name == "Dan":
	print "Welcome Dan"
elif name == "Stan":
	print "Welcome Stan"
else:
	print "You are not a valid user.  Good bye."
```

So what happened when you typed "stan" without the uppercase first letter?  It failed, that is because the question was asked is "stan" equal to "Stan", and it is not.  To handle different cases like this, I suggest you take a look at [String Operations](https://docs.python.org/2/library/string.html).  To handle input that may vary by capitalization, try .lower. Here is how it works. 

```python

name = raw_input("Enter your name: ")

if name.lower() == "dan":
	print "Welcome Dan"
elif name.lower() == "stan":
	print "Welcome Stan"
else:
	print "You are not a valid user.  Good bye."

```

For more information on conditional statements see this page: [Open Book Project](http://www.openbookproject.net/books/bpp4awd/ch04.html)

### The _FOR_ statement - Iteration

The _for_ statement allows for interation over an object or set of variables that is limited by the the length of the object or set of variables.  For instance, if you have a list of numbers, numList = [0, 1, 2, 3, 4], you can interate over this list calling each of the numbers individualy and performing some additonal function. Here is the most basic of _for_ loops.

```python

numList = [0, 1, 2, 3, 4]

for num in numList:
	print num
```

It is important to understand what is going on in the _for_ statement.  It is saying, for each number in this list of numbers, print that number.  In the first step of the for loop, num is set equal to 0, then the block of code is executed below the for statement with the understanding that num is equal to 0 in that iteration of the loop. After all the steps have been executed, in this case just a _print_ statement, it now goes back to the top of the _for_ loop and sets num = 1 and re-enters the code block to execute the code based on num being equal to 1.   So each time, the variable num is reassigned a new value before the code is executed.  If you ran the above code you see that it just prints each number vertically one below the other.

It is not so much what the _for_ statement says but what happens inside the _for_ loop is what is important.  Since you can set a new value to the _for_ loop variable each time through, this allows to have conditional statements imbeded within the _for_ loop.

```python

numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numList:
	if num % 2 == 0:
		print num 
```
In this case, you can iterate through the list and the number will only get printed if based on floor division (modulo) by 2 the result is equal to zero -- only even numbers will be printed.  

Notice the structure in the above code as it is critical to writing the correct syntax of Python code.  In using a _for_ or _if_ statement the code must be staggered.  The staggered code is inside each of the statements.  

One more thing on _for_ loops.  Consider what would happen if there were two lists that were iterated through but one iteration occurred inside the first statement.  
```python
numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
secList = [10,20,30,40,50]
for num in numList:
	for secNum in secList:
		print num, secList
```
The _for_ loop inside a _for_ loop illustrates the how loops work.  In this bit of code, the first _for_ loop will set num = 1 and the second will set secNum = 10 followed by printing of "0, 10". What happens next may be a bit confusing.  The code does not return to the first _for_ loop and set num = 1, rather num remains equal to 0 and secNum = 20.  The second _for_ loop has to complete before returning to the first _for_ loop.  After this num will be equal to 1 and the second _for_ loop will complete again.  

### Side note:  Break, continue, and pass statements

As you can see, _for_ loops have to iterate through every item in a list before the loop will terminate.  But imagine a situation in which you want to determine if there is a single item in a list.  If the item is found, there would be no need to continue through the list.  This could save computational time if the loop could terminate and move on to the next task.  This can be accomplished using the 'break' statement.

```python
items = ['wizard', 'hobbit', 'troll', "oger", "minion"]
counter = 0
for item in items:
	if item == 'troll':
		print "Found it"
		print counter
		break
print counter
counter = 0
for item in items:
	if item == 'troll':
		print "Found it again"
		print counter
print counter
```

The _break_ statement will cascade up and stop the first _for_ loop that it comes to.  If there are outer _for_ loops these will continue.

The _continue_ statement allow one to skip over blocks of code, but the _for_ loop itself is continued.

```python
items = ['wizard', 'hobbit', 'troll', "oger", "minion"]

for item in items:
	if item == 'troll':
		continue
	print item

```

In this case, when item is equal 'troll', that particular item is skipped but the loop continues.  

The _pass_ statement is one of the most innocuous.  At first glance it really does nothing at all.  I find the _pass_ statement to be most useful when setting up the structure of the code.  For instance, if I know I want an _if_statement or a _for_ loop in a given place, but I am unsure at the time what I want the code to do inside that code block, I just write a _pass_ statement inside that code block and it will just skip over that part for the time being and all other parts continue functioning.  That way I can get back to that code block later and I can keep writing other parts of the program.

```python
items = ['wizard', 'hobbit', 'troll', "oger", "minion"]

for item in items:
	if item == 'troll':
		pass
	print item
```
In this case, "troll" does print to standard output because there was nothing that stated not to in the code block, just the _pass_ statement.  The _pass_ statement really just allows one to include a statement without it actually doing anything.  So by doing something, it really does nothing.  If that makes any sense.  

### Side note:  The _RANGE_ Statement

Sometimes one needs to just iterate through a given set of values without setting a list.  This can be accomplished with the _range_ statement.  

```python

for i in range(10):
	print i
```
Notice how this bit of code prints 10 integers but actually prints 0 to 9 not 1 to 10. Do not forget about the zero based indexing that Python utilizes.  

There are other ways to use _range_ as well.  One could set a given start and end value.  range(1,11) would yield all the values from 1 to 10.  

### The _WHILE_ Statement:  Beware the Infinite Loop  (use CTRL-C to stop a run)

In some cases you need to evaluate a value of a variable/object until it reaches some predescribed value at which point the script can move on to do other things.  A continually re-evaluating loop can be accomplished using the _while_ statements.  _while_ statements are useful when trying to compute or look for a given values. They also work well for iteration when only wanted to iterate through a specific number of values and then stop.

Now, back to the _while_ statement.  

```python
setValue = 10
while setValue < 20:
	print setValue
	setValue += 1
print "out of the loop finally with value of " + str(setValue)

```
In this case the variable setValue was initialized at 10 then the while loop was entered, the while loop drew a line in the sand by stating that as long as setValue is less than 20, you cannot leave this loop (None shall pass!).  So inside the _while_ loop setValue is increased by 1 each time through.  Until finally it reaches a value that is greater than 20 and breaks out of the loop.  

To be honest, I do not use a lot of _while_ statements.  In code I write to solve a problem in doing my research I use a lot of _for_ loops and _if_ statements because I am really trying to go through a list of variables or maybe an entire column of data that functions like a list.  Not to say that while loops are not important.  As stated, one of the great functions is using them for computation. In those situations the _while_ loop will keep looking until it is found.  Or, it may never find the answer. If it never finds the answer it may enter an infinite loop.  To understand this, read and interpret the following code:
```python
setValue = 10
for i in range(10):
	while setValue < 20:
		print i
```
In this case, what will be printed.  The script enters a for loop and sets the value of i to 1.  It now enters the while loop and as long as "setValue" is less than 20 it will print "i" which is 1.  The problem here is that the value of setValue never changes.  Because it never changes, it keeps printing 1.  

### Exercise

There is only one way to learn to learn the python.  Not watching videos.  Not taking this class.  Not reading a book.  Well, actually those things can teach you Python, but if you are not writing code, then it is impossible to learn.  And by writing code I really mean really writing code.  I am going to give you some problems and you have to figure it out.  You have to bang your head against a wall :fearful: try 100 different ways before you finally get it type coding.  I honesly think that you have to see all the ways not to do things before you finally start understanding how to code. :sobbing:  That being said, we will start off with some simple excercises.  If you dedicate yourself to them you will learn how to code in this semester.  Here goes... :cold_sweat:

##### Exercise #1: Guess a number

Write a short program that continues to ask the user to guess a number between 1 and 20.  There will be a preset number, raw_input statement in the code, and when they get the number correct you need to give them a message of congratulations.  You may want to tell them that they missed it if they do not get the number before you tell them to guess again.  I would also think about telling them at the beginning that they are playing a number guessing game and ask them to guess a number.  If they do not get it correctly, I do not think you want them to get the same message again do you?  I tend to vary my guidance depending on the exercise, so on this one.  That is all you get.  

Start off by opening a new file in Enthought Canopy and saving it as numberGuessing.py.  :four_leaf_clover: :fireworks:

##### Exercise #2:  Find the largest odd number

Given any list of integers find the larges odd number in the list.  Start off with the test case below, but then develop your own test cases to challenge the program.  

```python
l = [1,2,3,4,5,6,7,8,9,11,489,15,19,27]
```
Once you are confident that your code is functioning properly, modify the code in such a way that it only evaluates integers in the list, not strings or floats.  

Once done and your coding partners are finished, share your above two files and let them test it to give you feedback.  