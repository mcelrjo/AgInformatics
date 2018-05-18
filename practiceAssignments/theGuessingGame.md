## The Guessing Game by Bisection Search

We have covered two types of search algorithms - exaustive enumeration and bisection search.  You have also created a short program to guess a number using a while loop.  Now let's combine these ideas and create a bisection search algorithm to guess a number between 1 and k (k being any number).  There are numerous examples of this on the web so please do not google this.  Sometimes it is bad to google.  I will start you off with some code to work with to help you get started.

Something to remember, these types of searches work only on ordered lists.  Bisection search is dividing an ordered sequence every pass through to decrease the search space in which the answer lies.  If the sequence is unordered there is no way to cut the list.

```python
high = 1000
low = 0
guess = (high + low)/2

numGuesses = 0

secretNumber = int(raw_input("Enter a number that I will guess: "))

stillGuessing = True 

while stillGuessing:
	pass

print "And it only took this many guesses: ", numGuesses
```

Think about how this search would look with exaustive enumeration.  

```python
high = 1000
low = 0
guess = low

secretNumber = int(raw_input("Enter an integer between 0 and 1000: "))

numGuesses = 0

stillGuessing = True 

while stillGuessing:
	if secretNumber < low or secretNumber > high:
		stillGuessing = False
		print "Guess a number between 0 and ", high
	elif guess == secretNumber:
		stillGuessing = False
		print "The secret number was ", guess
	else:
		print "The last guess was wrong. Last guess: ", guess
		guess += 1
		numGuesses +=1

print "And it only took this many guesses: ", numGuesses
```