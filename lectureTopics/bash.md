##Getting started with the Command Line and Bash Commands

If you use an Apple computer you have likely seen an application referred to as "Terminal". If you are unfamilar with the command line interface, opening up Terminal will illicit confusion. 

```bash
ls
```

```bash
cd
```

```bash
pwd
```

```bash
cd . # . is the current directory
cd .. # .. is the parent directory
```

Manual pages can show you what each command does and its flags that can give different information.


Using wild cards
```bash
ls myfile.*

ls ?yfile.txt

ls [a-z].txt

ls {myfile,yourfile}.txt
```

```bash

mkdir mydir

cp myfile.txt mydir/

cp myfile.txt yourfile.txt mydir/

cp *.txt mydir/

```

Can also move things which delete the previous version using the mv command
```bash
rm myfile.txt

rm -i myfile.txt #this will ask us if we are sure

#rm cannot delete directories. Have to use -r to move recursively

rm -r mydir/

```

Access the contents of files.
```bash
more 

less

head

tail

cat
```

```bash
wc

#word count

#number of lines in file, number of words in a file, number of characters in a file beside name of file

wc -l 

#just number of lines in a file

> 
#redirects the output from a function into a file

< 

# redirect standard input to a function

|

#takes the output to become the input of a different command. 

#cat piped to more allows one to see one page at a time.

```

```bash

sort

#sorts items in a list. By default sorts alphabetically. 

sort -k2

#sorts by column #2

sort -kn2 

#sorts by column #2 numerically

sort -kn2r

#r tells reverse order

sort -k 3 -k 2n 

#first sorts by colunn 3 then by numerically by column 2

cut 

#cut extracts a particular column. delimits based on tab as default

cut -f1,2 

#cuts columns 1 and 2

cut -f1-3

#cuts columns 1 to 3

cut -d " "

#use -d to specific a different delimiter

sort -u
	#statements

# identify unique entries

uniq 

#In order for Uniq to work, the file must first be sorted. 
#So you have to run sort and uniq in tandem

#as an exmaple consider you want to cut a column from a tab delimited file and count the number of uniq entries. For this example we cut the second column

cat theFile.txt | cut -d ',' -f 2 | sort | uniq -c

# in this case the -c counted the uniq names

#There may have been a problem. What if names are listed two different ways. For example, what if "Scott" was listed somewhere as "Scott McElroy". In this case you would need 
#to change the names. sed is a good option for this.

cat theFile.txt | sed 's/Scott/Scott McElroy/g' > theFile_edited.txt

# Make sure you direct sed output into a new file. 
```

### It is important to know the three data streams that are occuring in a bash script. 

1. STDIN (standard input). Data going into the program

2. STDOUT (standard output). Data coming out of the program

3. STDERR (standard error). Error data.

Unless redirected, these data streams will come from the terminal and write out, or print, to the terminal unless *redirected*.

To redirect STDERR and STDOUT to be deleted use the following code.

```bash
2> /dev/null #for STDERR

1> /dev/null #for STDOUT
```

### When using the pipe | you are redirecting the STDOUT to as STDIN to the next command. So for above, the output of *cat* becomes the input for *sed*. If an error occurs, it will print to the terminal as STDERR. 

## Argument 

### Bash scripts can also take arguments as input. Some key concepts for arguments and their use are as follows.

- Arguments can be accessed using the *$*. The first argument would be *$1* and the second as *$2* and so on. 

- ARGV is a way of saying all the arguments used by a bash script.

- *$@* and *$asterisk* (use the asterisk symbol don't write asterisk)

- *$#* gives the total number of arguments

## Executing a script to understand arguments

### Arguments are passed to the script by listing them after the script as such.

```bash

bash myScript.sh one two three four

```

### In this case the arguments are one, two, three, and four. To demonstrate how these are the arguments, copy the following script into a text document as save as *myArgs.sh*.

```bash

#!/usr/bash

echo $1
echo $2
echo $@
echo "There are this many arguments: " $# ""

```
### Now run the script as follows:

```bash

bash myArgs.sh one two three four

```
### The program should have printed the following to standard out.

```text

>>> one
>>> two
>>> one two three four 
>>> There are this many arguments: 4

```

# Bash Variables

Variables are created similar to other languages but then variables are referenced using the *$* sign. 

```bash

professor='McElroy'
class='Aginformatics'

```
The previous code creates two variables named _professor_ and _class_ that are assigned with the strings 'McElroy' and 'Aginformatics', respectively. You can now reference the variables using the _$_ sign.
```bash

echo "My professor for " $class " is Dr. " $professor

```
Here are some rules for creating and referncing variables:

-You must use the _$_ or bash does not know you are referencing a variable.

-You cannot not use spaces around _=_ sign. 

-Single quotation marks is interpreted literally by the shell.

-Double quotation marks interprets everything literally except for backticks and _$_ signs.

-Backticks can be used to run a command line program and capture standard output (STDOUT) which then assigns it to a variable. Think of it as running a shell within a shell. Backticks does some other strange things too.

Single and double quotes are not without their unique qwerks. First, consider referencing a variable with single vs double quotes.

```bash
name='scott'
name2='doug'
name3='$name'
name4="$name2"
```
If you echo all the variables you should get the following:
>>>scott
>>>doug
>>>$name 
>>>doug

Since double quotes interprets everything literally except _$_, it is used to reference name2 in this instance. Therefore echoing $name2 and $name4 returns 'doug' to STDOUT. Name3 is interpreted completely literally becuase of single quotes and returns exactly what was assigned to name3.

# Demonstrate backticks and $() for shell within a shell

To demonstrate the effect of backticks to call a shell program within a shell, let's look at the _date_ command. Start by typing date into the command line.

```bash
date
```
Which should have returned something like this

>>>Fri Jul 23 14:40:40 CDT 2021

Now, let's capture this into a variable and echo it.

```bash
currentDate="The current date and time is `date`"
echo $currentDate
anotherWay="The current date and time is $(date)"
echo $anotherWay
```
The first way demonstrates the usefulness of back ticks to execute a shell program and capture the output. The second way by using the _$_ and parentheses. 
http://mywiki.wooledge.org/BashFAQ/082


# Numeric variables in command line

Basic arithmetic cannot be done directly in the command line. Instead, we are going to use a command line program called _expr_. expr cannot handle decimal places. To overcome this use, _bc_ or basic calculator. But bc opens as program then one can leave the program by typing _quit_. Numeric variables can be piped _bc_ as follows:
```bash
echo "30 / 12 " | bc
#this will yield only an integer. To get floats, use the scale argument. 
echo "scale=5; 30 / 12 " | bc
```
Assigning string variables is similar to assigning strings. 
```bash
name='scott'
age=21
echo $name " is " $age " years old."
```
Double parentheses notation can be used to call _expr_. But remember that this uses integers not floating point numbers.
```bash
expr 89 - 7
#is the same as
echo $((89 - 7))

```
Using shell within a shell method can allow for passing variables to _bc_. This is a useful tool for accessing floating point numbers. 
```bash
num1=32.5
num2=25.5
echo "$(echo "$num1 + $num2" | bc)"
echo "$(echo "($num1 + $num2) / 3 " | bc)"
```

### I must fully admit one thing: The syntax of _$_ signs, _()_, quotation marks and nesting of all these things is definitely not intuitive. In fact, when I was first learning it, it was down right confusing and frustrating. I still make mistakes all the time leaving out _$_ signs and things. The best advise I can give is develop a cheat sheet for yourself to know when and where to reference and use which symbols. Good luck. :smiley:

# Practice converting temperatures

Write a bash script that takes as input as the first argument a temperature in farenheit and echo back to standard out the temperature in celsius.

# Arrays in the command line

There are two types of arrays in bash. 

1. A normal, numerical-indexed structure which is similar to a list in Python on a vector in R.
2. Associative arrays. Basically libraries in Python. 

### Numerically indexed arrays

There are two ways to create an array in bash. 

1. Use the _declare_ function to add make an array with no elements.

2. Create and add elemenets simultaneously.

```bash
# first way
declare -a new_array
#second way
new_array=(1 2 3)
```
Notice how spaces are used instead of commans.

Elements and length of an array can be captured using the following.

```bash
#to get all the elements
echo ${new_array[@]}

#to get the length of an array add the pound symbol
echo ${#new_array[@]}
```
_Yep. Those are curly brackets. Very specific syntax for accessing arrays in bash._

Elements of an array can be accessed using square brackets. Similar to Python, bash uses zero indexing of elements.

```bash
ages=(37 15 19 22 67)
#now access the third element
echo ${ages[2]}
```
Changing the value of an array is also similar to Python. Simply call the element of the array and reassign the value.

```bash
ages[3]=18
echo ${ages[@]}
```
Elements of an array can be sliced using the following notation _array[@]:start;numberToSlice_. For example,

```bash
echo ${ages[@]:1:3}
```
_A quick note: don't forget the [@] to get all elements of an array._

Appending to an array is simple from a syntax perspective. Just make sure you use the parentheses.

```bash
ages+=(45)
#don't for get the parentheses
echo ${ages[@]}
```
_Try not using parentheses and see what happens. It is weird._

### Associative arrays

There is only one way to make an associative array in bash -- using the _delcare_ statement. Keys will use square brackets and _=_ to associate the values. Here is the syntax for making an associative array.

```bash
declare -A personal
personal=([age]=21 [weight]=200 [smell]='good')

echo ${personal[@]} # prints the values
echo ${!personal[@]} # add the ! to print the keys

#print the values based on keys in this way
echo ${personal[age]} #prints the age value
```
An array can be declared and propagated at the same time. This can be done using the following syntax.

```bash
declare -A rick_sanchez=([age]=62 [weight]=140 [smell]='garlic')

echo ${!rick_sanchez[@]}
```