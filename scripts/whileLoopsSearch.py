
#while loops

x = True

while x == True:
    print "x is True"
    


while x == True:
    print "x is True"
    x = False

x = 0
while x < 10:
    print "x is less than 10"
    x = x + 1 # or x += 1
    
    
    
    
    
#exaustive enumeration

x = 30
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print "number of guesses = ", numGuesses

if abs(ans**2 - x) >= epsilon:
    print "Unable to find answer to ", x
    print "Last guess was ", ans
else:
    print ans, " is a close approximation"
    

#what if x is 0.25?  How could you correct this?   

#Try different numbers and see what happens.  
    
    
    
    
    

#bisection search

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:
    print "low = ", low, ', high = ', high, " ans = ", ans
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
    
print 'numGuesses = ', numGuesses
print 'answer = ', ans
    
    

# now modify the code to find cubed roots
    