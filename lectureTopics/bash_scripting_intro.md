# Introduction to Bash Scripting

### Now it is time to get down to the nitty gritty of writing actual bash scripts. In the intro chapter we learned a lot about working in the command line and also working with arrays. Now it is time to learn how to put it all together into an actual script.

The first conditional statement we will learn in _IF_ which is followed by _THEN_ which executes if an if statement is true. An _ELSE_ statement executes if it is not true (else is not mandatory). _If_ statements end with _fi_ which is _if_ backwards. Here is the basic syntax for _if_ statements.

```bash

if [ condition ]; then
	# execute this code here
else
	# execute this code here
fi
```

_if_ statements are just logicial statements. Don't overcomplicte them in your head as something complicated. Think of it like this

```bash

if [ it is not raining ]; then
	# I will go to the grocery
else
	# I will watch The Great British Baking Show on Nexflix
fi
```

In fact, all the conditional statments we will deal with in Bash and Python are just logical statements. You establish a condition and if that condition is met, one thing happens. If it is not met, another thing happens. 

A couple things on syntax.  

1. Notice the space between conditions and square brackets on both sides.

2. Notice the semi-colon after brackets. 

Don't forget those square brackets ... unless you don't need them. If doing arithmetic statements, use double parenthesis as follows.

```bash
score=98
if (($score > 100)); then
	echo "You win. You scored: $score"
else
	echo "You lose. You scored: $score"
fi

```

There are special flags you can use for arithmetic comparisons. Special flags do allow you to keep using square brackets instead of double parentheis. Special comparision flags are:

1. -gt --Greater than

2. -ge --Greater than or equal to

3. -eq --Equal to

4. -ne --Not equal to

5. -lt --Less than

6. -le --Less than or equal to

Syntax for these special flags are as shown:

```bash
points=30
if [ $points -ge 30 ]; then
	echo "You win. Score: $points"
else
	echo "You lose. Score: $points"
fi

```

I am just letting you know these exist. I am not recommending. I don't like having to look up exactly what the comparisons are everythime, although they are not that hard to remember. I like using traditional arithmetic comparisions:


<, >, <=, >=, =, !=

There are ton of other conditional flags that you can use. Here is a (website)[https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html] that has an exhaustive list to use for files. Examples include:

1. -a --If the file exists

2. -d --If the file exists and is a directory. 

3. -z --True if lenght of string is zero.

### Using And/Or Notation

To set up more than one condition, use _and_ or _or_ notation. 

- _and_ use &&

- _or_ use ||

To use multiple conditional statements using the following syntax.

```bash
if [ this is true ] && [ this is also true ]; then
	# do this thing
else 
	# do this thing
fi

# an alternative notation is to use double square brackets

if [[ this is true || this is true ]]; then
	# do this thing
else 
	# do this thing instead
fi

```
Both syntax get the same result.

Command line programs can be executed in conditionals by removing the square brackets.

```bash
if ls Templates; then
	echo "File exists"
else
	echo "File does not exist"
fi
```

This simple if/else statement just checks if a file exists (there are better ways to do this.) and demonstrates how a command line program can be used in a conditional statmennt.  If you use _grep_ inside a conditional you may want to use the _-q_ flag to suppress its output to STDOUT. 

# _For Loops_

_for_ loops are similar to R and Python with some Bash-esque syntax. 

```bash
for number in 17 18 19
do # do starts the loop
	echo $number
done # done exits the loop
```
As you can see from running this code, it prints the numbers to standard output. Notice how there is no punctuation after the list of numbers, no parenthesis either. It seems naked to me. 

_Brace expansion_ can be used to find a numeric range to iterate through. Brace expanson looks like this.

```bash
for number in {start..stop..increment}
do
	echo $number
done
```
Brace expansion uses braces, or curly brackets, and it has to have the two periods between the numbers. 

_Three expression syntax_ can also be used to iterate through a set of numbers. The syntax is a bit jumbled to look at but it somewhat simplfies the code. By using double parentheses you don't have assign a variable name outside, but it is assigned inside. Similar to brace expansion, the first part is the start and the middle is the end or stop. The last part is the iterator. In order for the iterator to work you must do something with the defined variable to increase it to the middle number or you will enter an infinite loop. 

```bash
for ((number=10;number<=100;number*=2))
do
	echo $number
done
```
In this case, we increase _number_ by multiplying by 2 each time through the loop 10, 20, 40, 80, then the loop ends. 

_Glob expansion_ is a method of doing pattern matching. The best way I know how to demonstrate this is the use the _*_ symbol to print files in a directory. So pick a directory you have and let's print out all the files in that directory.

```bash
for files in Desktop/*
do
	echo #files
done
```
I lied a little when I said there was not punctuation. Sometimes you may want to put everything on a single line just straight into the comamnd line. To do that, try this.

```bash
for filename in Desktop/*; do echo $filename; done
```
You probably noticed it was doing this if you looked at the code after you copied and pasted it. Or at least you should have. :scream:

Let's recall shell within shell to run command line program in a for loop. To run command line programs in the shell within a shell set up remember to use to _$()_ notation. 

```bash
for filename in $(ls Downloads | grep '.sh')
do
	echo $filename
done
```
The follow file checks for any files in your Downloads directory that is a shell script. Try it and replace it with whatever. Remember to direct it correctly to your Downloads directory.  This is cool because you basically created a search function. Maybe we can think of a way to search through multiple directories. :astonished:

# While Loops

_While_ loops are useful to check the status of a variable each time through the loop. As long as the variable remains _True_, the _while_ loop keeps running. Once the variable is _False_, the _while_ loop terminates and the script breaks out of the loop. 

The condition is going to be wrapped in a square bracket similar to a for loop. Similar to the _for_ loop, numercial flags (ex. -ge) can be used. Multiple conditions can be checked with _&&_ and _||_ just like in the _for_ loop. Here is the basic syntax for a _while_ loop. 

```bash
while [ this thing is true ];
do
	#do this thing
	#what ever you are checking has to change 
done
```