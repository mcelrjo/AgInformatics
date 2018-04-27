Consider the following block of code:

```python
L = ['bubbles', 1, 1.3, "cats", "farmers", 'Yucutan', 9000, 'forest']

counter = 0
for item in L:
    if type(item) == str:
        counter += 1
print counter
```
First a variable equal to zero is instantiated before a _for_ loop.  The _for_ loop takes a list object "L" and iterates through it to check if an item is of type string.  If it is not of type string, the _if_ statememt is not entered.  If the _if_ statement is entered, a counter is increased by 1 for every item that is a string objecct.  After all objects have been iterated through, the number of string objects is printed via the variable "counter".  

This is a useful piece of code if you have a very large list, say thousands of items long, and you need to know how many string objects are in this list.  _The problem is that this code only works for the one list variable._  What if you had numerous lists that needed to be sorted through and specific items counted?  The code needs to be reusable and adaptable to any list situations.

### Defining a function

I now introduce one of the most useful components of programming -- the function.  A function is a reusable piece of code that takes an input, most commonly referred to as an _argument_ and utilizes that argument inside the function code block.  Generically here is what a function looks like:

```python
def functionName(agrument1, argument2, argument3):
	#do stuff with those arguments
	return something
```
To define a function you first begin with the _def_ statement.  The _def_ statement does just that it defines the function.  The second term defins the name of the function -- in this case functionName.  The function name is followed by open and close parenthesis.  Inside the parenthesis are the arguments that are _passed_ to the function -- that is the correct way to say it by the way.  One _passes an argument to the function_.  The definition line ends with a colon and the entire code block is tabbed once. At the end of a code block (typically) is the _return_ statement.  The _return_ statement returns something as you exit the code block.  Functions can _print_ or _return_ something depending on the needs of the function.  Functions could also do nothing, just execute the block of code. 

To understand more about function let's rebuild the above code block into a function.  Remember, in rebuilding the code block we want to make is resusable and extensible to any list object.

```python
def stringCounter(listObject):
	counter = 0
	for item in listObject:
	    if type(item) == str:
	        counter += 1
	return counter

L = ['bubbles', 1, 1.3, "cats", "farmers", 'Yucutan', 9000, 'forest']

stringCounter(L)

print stringCounter(L)

numStrings = stringCounter(L)
```




#### Args and Kwargs

There are two types of arguments, arguments (or args) and keyword arguments (kwargs).  That is a little confusing I know, so unless I specificially say keyword argument just assume I mean standard argument.  The difference between standard arguments and keyword arguments is that the later have a default input.  More on those later.