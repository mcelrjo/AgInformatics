# The Basics of Bash Functions

Bash functions can make reusable code similar to Python or R. Bash functions as you will see can also take advantage of command line programs. Here is the basic outline of a bash function.

```bash
functionName () {
	# some code for the function
	return # a result
}
```
An alternative syntax is to use the _function_ call before the function name and drop the parenthesis (or keep them).

```bash
function function_name {
	# put code for function here
	return # a result
}
```

### Practice with Converters

To practice developing basic bash funcitons, let's work on developing basic converters -- a simple function that just converts between Imperial units to Metric units. Over vice-versa. For the function, you want to take from standard in a number and convert it to something else. 
- miles to kilometers
- feet to meters
- gallons to liters
- pounds to kilograms

Here is the basics of how it works.

```bash

someValue=$1 #take a value from STDIN

converter () {
	#first need to convert this value based on what you have learned
	newValue=$(echo "scale=3; ($someValue/57) * 3.14" | bc)
	#then echo it back to standard out
	echo $newValue
}
#last, call the function
converter
```

### Slicing up Date

Another good way to practice making functions is to slice up and return various parts of the _date_ function. When date is called in the command line, it returns something like this. 

- Fri Jul 30 08:37:39 CDT 2021

Notice how everything is space delimited. Now, develop a function that calls date and give a person the current time returned back to them. If you are confused, first play around with slicing up _date_ with _cut_. After that, run what works as a shell within a shell and assign it to a variable name inside a function. Then echo that back to STDOUT. 

### Arguments

Dealing with arguments is key to developing properly working function. One concept to understand when developing programs is _scope_. Some variables have _global scope_ meaning that a variable is present everywhere. _Local scope_ is present only in certain programs. Bash make all variables global by default. This is opposite of Python which restricts variable to local by default. To make a variable local, use the _local_ command.

```bash
function say_hello {
	local firstPerson=$1
}
echo $firstPerson # will echo a blank line
```

### Return

Including a _return_ command does not return data or a result of the program, instead it return the error code for the program. If you run a program that fails, you can find the last exit status by typing _$?_.

To get data from a function, assign the output to a variable name outside the function and echo value back to standard out.

