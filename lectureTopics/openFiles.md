
# Opening, reading, and writing to documents

Most Python programs you will be writing will need to extract data from somewhere in order to use it in the script/program to make some calculation, do some counting, or other processing needs you may have.  In this lesson we will be discussing the processing of information from files.  How to access and handle those files and utilize the information in your Python scripts.

### The _Open_ Statement

Files are opened very simply by using the _open_ statement.  _open_ statements must include a call that declares if a file is open for reading, writing, or both.  

```python
myFile = open('myFile.txt', "r")

print myFile
```

Notice what happened when you printed the open file.  It should have printed something like this.

```python
<open file 'myFile.txt', mode 'r' at 0x7f559b0d4c90>
```

What actually happened is that you printed the object 'myFile'.  Whenever you print an object, this is telling you that there is dot notation attributes/functions that you can now call on that object.  In otherwords, there are functions and attributes that are associated with that object that let you do stuff to it or with it.  In order to find that out what those things are, let's play around with a small text file to see how things work.  Download the [practice text file](/practiceTextFile.txt).

Now change your working directory to match the working directory where the text file is stored. Now open the file (try not to look below but try to write it from memory).

```python
practice = open('practiceTextFile.txt', "r")

```

Now your file is open, let's do something with that file.  First, do a simple iteration through the file.  It is simplier than you think.

```python
for line in practice:
	print line
```

This will print out each line of the file.  Now try running the same code again.  Nothing happened.  This is one of the great curiosities/pains surrounding the _open_ function, once you go through the object it is "emptied out" and there is nothing else to go through.

### A LITTLE WARNING

Before you do anything else, type this bit of code.

```python
practice.close()
```
Whenever you finish with a program it is good practice to close that object before doing anything else.  I can quote you some text about how the file object is stored in memory and then you need to clear the memory when you finish with the object.  If you do not close the object bad things can happen with the source file-- corruption, overwritten, deleted, etc.  Things like this have happened to me before.  I do not fully understand how or why they happen, nor can I predict when bad things happen.  I do know that if you just take the time to close the file object, bad things do not happen.  

###Some file object functions

There are different ways of getting through the object other than just iterating through it.  One way is _.readlines()_.

```python
#open the object again.
practice.readlines()
```
_.readlines()_ will print a list of all the lines in an object.  A couple items.  If you do this again, the list will be empty.  Second, you could have iterated through the lines and printed them out individually.  And one more thing I just remembered, notice how when you just printed the list is printed all the carriage returns.  When you print the lines individually all the carriage returns ('\n') will disappear. 

A few other ones and what they do:

```python
practice.read()
``` 
This prints out the lines in the file as one string.  It simply read the lines.

```python
practice.readline()
```
This reads each line individually, not as a list.  With _.readline()_ you can continue to iterate through the file until you come to the end, going line by line.  



### Functions on lines of a file

There are sometimes that you only want to print out certain lines of a file based on some attribute.  Of course you can use regular expressions for this, but there are also some good built in functions to make it easier on you.  

```python
for line in practice:
	if line.startswith('It'):
		print line
```
_.startswith_ does exactly that.  It just matches patterns at the front of a line.  You could also put the logical operator 'not' in front of the function and get the opposite.

```python
for line in practice:
	if not line.startswith('It'):
		print line
```  
You can do the same thing with _endswith()_ and only capture things at end of a string. _startswith_ and _endswith_ have more functionality to be able to also have start and end indexing to only look at a slice of a string.  These two functions are not functions of _open_.  They are string operators that just operate on strings.  Since the line output of opening a file are strings this allows one to utilize the string operators.  

##### Practice #1: Take the [contact.txt]() file and parse it to print only names and email addresses together.

### Other Items to Help You Parse Strings

When interating through a file you may need to process each line further to make it easier to deal with.  For example, you may deal with a string that has carriage returns or white space at the end of a string.  In order to match the string exactly it would be easier to strip off the non-characters at the end of a string.  This can be done using _rstrip_.

```python
myString = "676-787-0920                    "
print myString
myString = myString.rstrip()
print myString

```

The _find_ function can be used to identify the numerical location of the start of a search string in a string of interest.  

```python
mystr = "I am a little teapot short and stout.  Eat some biscuits.      "
mystr = mystr.rstrip()
print mystr 
mystr.find('biscuits')
>>>46
```

Searching for 'biscuits' returned the integer 46 meaning it started at the 46th position..

### Practice #2

In a single line of code, find the start of the word "Eat" and slice out the entire phrase 'Eat some biscuits'.


### Writing to a file

The above files were opened in the read mode.  Now let's open a file in the write mode.  When opening a file in write mode, if it does not exit it is created.  So there is no need to go and create a file separately then open it and write to it.  

```python
myfile = open('text.txt', 'w')
```
The flags in the open statement determine the mode of the document.  If you use the 'w' flag to write, if the file exists then it will be overwritten.  To append on to a document use the 'a', thus preventing the existing file from being overwritten.  'r+' or 'rw' opens for reading and writing.  

To write to a file use the _.write()_ method associated with the open file object.  

```python
newLine1 = "here is the first line"
myfile.write(newLine1)
newLine2 = "here is the second line"
myfile.write(newLine2)
myfile.close()
```
Now open the file back up and print the lines.

```python
myfile = open('text.txt', r)

for line in myfile:
	print line
myfile.close()
```
The problem is that it only printed one line.  When printing new lines there has to be a newline/carriage return chracter at the end of the line or it simply will keep writing to the same line.  The line inputs should have been written as so.

```python
newLine1 = "here is the first line \n"
```

### Practice #3

Create a program that asks for a person's name, email address, mailing address, city, state, zip code.  Write all this to a file and make it where new entries can be made.  After three people have entered data, recall all the names and cities from which the people are from.


For more info on writing to a file see the [Python Documentation](https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files).

