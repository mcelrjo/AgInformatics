def fib(n):
    """Calculate the nth number from a fibbonacci sequence"""
    sequence = [1]
    a = 1
    b = 1
    while len(sequence) < n:
        sequence.append(b) 
        c = a + b
        a = b
        b = c
    print sequence, str(len(sequence)), sequence[-1]
    
def fib2(n):
    """Calculate the nth number from a fibbonacci sequence"""
    sequence = [1]
    a = 1
    b = 1
    while len(sequence) < n:
        sequence.append(b) 
        c = a + b
        a = b
        b = c
    print sequence
    print "The length is " + str(len(sequence)) + " and the final number is " + str(sequence[-1])
    
    
    
    
def fibFinal(n):
    """Calculate the nth number from a fibbonacci sequence"""
    sequence = [1]
    a = 1
    b = 1
    if n == 0:
        return "The length is " + str(0) + " and the final number is " + str(0)
    if n == 1:
        return "The length is " + str(len(sequence)) + " and the final number is " + str(sequence[-1])
    while len(sequence) < n:
        sequence.append(b) 
        c = a + b
        a = b
        b = c
    print sequence
    return "The length is " + str(len(sequence)) + " and the final number is " + str(sequence[-1])