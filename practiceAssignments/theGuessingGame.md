## The Guessing Game by Bisection Search

Scenario: Someone tells asks you to guess a number between 1 and 100.  How would you do this and have the least number of guesses.  I present two possible options -- _exhaustive enumeration_ or _bisection search_.

*Exhaustive enumeration* goes through each possible answer one by one until the answer is reached. In other words, you would answer "Is it 1?" and receive a yes or no answer.  Then, "is it 2?"  Yes or no, so on and so forth until you arrive at the correct answer.

*Bisection search* attempts to cut the search space in half at each iteration.  At the first turn, one would start at the mid point and if the guess is incorrect, it would ask if the answer is higher or lower than the guess.  The next iteration would take the midpoint of the search space and repeat the guess and halving of the search space.  

The problem is that exhaustive enumeration searches one by one through all possibilities.  It is __computationally intensive__.  If there are a million numbers the average number of guesses per number would be 1,000,000 divided by 2 - 500,000.  Considering having to search through hundreds, thousands, or millions of individual numbers.  The numbers of guesses per search would be 500,000 x X, where x is the number of searches.  

We need a way to reduce the number of guesses to decrease the computational intensity.  _Bisection search_ is used to cut the search space in half at every iteration.  Using bisection search, can reduce very large searches spaces to just a few guesses, greatly reducing the computational intensity.  


#### The problem

Develop two functions -- exhaustiveSearch and bisectionSearch.  

1. Use the module Random to generate a random integer between one and one billion which is used as input to each function.  Pass the integer to each function.

2. Each function should arrive at the correct guess.

3.  Count the number of guesses that is made.

4.  Return the answer and the number of guesses made as a string statement from each function.  

5.  Bonus points -- use the module Time to correctly time the speed of each function and report the time in seconds in the returned string.

:octocat: