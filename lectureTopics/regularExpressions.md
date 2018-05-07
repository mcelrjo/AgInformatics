
## Regular Expressions

'Regular expressions are great to learn.  I have learned them dozens of times.'

I am going to try to define what a regular expression is in my own words.  This may be dangerous, but here goes.  __Regular expressions__ are coded statements that can be used to match and extract specific text patterns in documents.  Regular expressions are most useful for "find and replace" or "find and count" type of operations.  They are difficult to grasp at first but once you do they are extremely powerful tools for data mining from large text documents.

To learn regular expressions we are going to be using the website [RegEx101](https://regex101.com/).  Make sure you switch your 'flavor' to Python.  We will learn the specifics about Python regular expression later, but for now we need to focus on just learning what regular expressions do and how they work.

The first think you should know is that regular expressions match text exactly.  So if you know how to do keyword search in a Word document, the first part is easy.  Take the following list and paste it in the "TEST STRING" are on regex101.  

Ben ben bean benn abena bebenbe beN -ben-

Now in the "REGULAR EXPRESSION" part type "ben" (without the quotes).  This should have captured four instance of the letters "ben" in order.  but you want to capture every instance of "ben" no matter the capitalization.  Now type '[Bb]en' in the search.  This should have capture five instances.  [Bb] is saying for a single letter, it can be B or b.  But you are still missting a few so now type '[Bb][Ee][Nn]'.  This will captuere every instance of 'ben' no matter the case.  But that is still not what you wanted.  You really wanted just 'ben' any case that is not a stand alone word.  So you need white space in front and behind. Now is time to use __Regular Expression Tokens__.  Regular expression tokens allow one to capture or eliminate certain types of characters.  For example, 

\s - caputres any whitespace character
\S - caputures any non-whitespace character

Notice that if you type: \s[Bb][Ee][Nn]\s that you capture the first 'Ben' because it does not have whitespace at the beginning of the line.  Also, this captures the actual whitespace itself, and you don't want that.  You only want the letters themselves.  In this case you need to use the boundary character - \b.

\b[Bb][Ee][Nn]\b

This expression will capture only "occurrences" of 'ben' that have no other letters before them. 

### A slight increase in complexity.  

Take a look at the following bit of text.  First, this is a single line of text even though it wraps to other lines because there is not a new line character (\n) until after Arabidopsis.  Now image you have thousands of these lines in file and you want to extract everything out after "Full=" but before the next semicolon.  

CXE13_ARATH^CXE13_ARATH^Q:93-266,H:4-63^45%ID^E:2.23e-09^RecName: Full=Probable carboxylesterase 13;^Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta; Spermatophyta; Magnoliophyta; eudicotyledons; Gunneridae; Pentapetalae; rosids; malvids; Brassicales; Brassicaceae; Camelineae; Arabidopsis

To solve this problem you are going to need to learn how the most commonly used tokens actually work.  You have learned about brackets and \s, but let me provide a clear definition of what these are.

[Bb] - capture a single character of 'B' or 'b'

\s - captures any whitespace character

\S - captures any non-whitespace character -- like ; , . : < >  They are not whitespace but they are not letters or numbers either.  Think of it as capturing symbols.

\d - captures any digit

\D - captures any non-digit.  So it will capture letters, whitespace, symbols -- so long as they are not digits.

\w - captures letters

\W - captures non-letters

Followed by these standard tokens are quantifiers which can be used to signify none, one, or multiple of a given token.

\d* - captures zero or more digits

\d+ - captures one or more digits

[^\d] - captures anything but digit

[^\d]+ - Will capture anything except digits (until it encouters a digit, then it will stop capturing)

Before moving on, copy and paste the text above and try to find a regular expression to capture the phrase as decribed.

### The _RE_ module

Python contains the regular expression module _re_ in its standard library which allows for search and capture using regular expressions.  Start by importing the module.

```python
import re
```

What you are going to learn is some basic functionality of using a regular expression in Python.  The first thing you need to know is using the _r_ flag when writing your regular expression.  The _r_ flag is used as such.

```python
regExpression = r'\w+'
```
The _r_ flag is interpreted to mean that it is a raw string that should be interpreted as a regular expression.  If the _r_ flag is not used it can create problems with the need for escaped characters.  As part of this point you can see that the regular expression itself needs to be enclosed in a single or double quotation mark.

The second aspect is that Python allows for capturing into groups using parenthesis.  Parenthesis are interpreted by Python to mean that you want to capture the text by the regular expression and use it/recall it later.  

```python
regExpression = r'(\w+)(\d+)'

```
In the above case, Python could use this regular expression to capature a set of one or more letters followed by one or more digits.  It will store both of these into separate groups that can be recalled later.

Now that you know how to build a regular expression for Python interpretation, the are a couple _re_ functions you need to use - _re.search_ and _re.groups_.

```python
regex = r'(\w+)(\d+)'
text = 
output = re.search(regex, text)

print output

print output.groups()

result = output.groups()

print result
print result[0]
print result[1]
```
When "output" is printed, it prints a regular expression seasrch _object_.  When you see an object is printed you know that there are other dot notation fuctions that an be used to access the object.  You can access dot notation objects in Canopy by end the object with a period (dot) and hitting the tab button.  This will autocomplete and give you rows of fuctions that can be accessed. "output.groups()" prints a tuple of objects that were captured by the regular expression.  Only items in parenthesis are captured in the search object.  

Instead of just printing the group object, it is useful to pass that tuple to another object that will be set equal to the tuple.  In this result becomes the search group tuple object.  Now the items can be called with brackets of the ordered tuple.  These items can be printed to standard output, added to a csv file, or other uses you may need.

### Now the answer to the above problem

In a relatively short string like the one below the term "Full=" is only going to appear once in the string, so use "Full=" as an anchor.  The regular expression will search until it finds "Full=" text pattern and skip over all the other.  

```python
import re

regex = r"Full=([\w\s]+);"

sprotEntry = "CXE13_ARATH^CXE13_ARATH^Q:93-266,H:4-63^45%ID^E:2.23e-09^RecName: Full=Probable carboxylesterase 13;^Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta; Spermatophyta; Magnoliophyta; eudicotyledons; Gunneridae; Pentapetalae; rosids; malvids; Brassicales; Brassicaceae; Camelineae; Arabidopsis"
```



Practice #1:

The following is a list of books from [The Gutenberg Project](): [1997 Book List](https://www.gutenberg.org/dirs/GUTINDEX.1997.iso-8859-1.txt) or download it [here](https://github.com/mcelrjo/AgInformatics/blob/master/otherFiles/GUTINDEX.1997.iso-8859-1.txt).  Open the file and parse it to count the number author entries in the list (what data type would be best for this?).  As you will notice, some names are listed slightly differently for each author?  How can you use regular expressions to overcome this problem?  Make sure to develop your program into a function that can be used for any Gutenberg book list.

Practice #2:  

Now we are going to develop a more complete project that parses 