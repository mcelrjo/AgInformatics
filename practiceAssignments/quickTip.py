
def calcTip(tipPercent, amount):
    '''Return the tip amount
    '''
    
def calcTax(taxPercent, amount):
    '''Return tax amount
    '''
    
def totalBill(tipPercent, taxPercent, amount):
    '''Return total amount using the two previous functions.
    '''
    
tip = 0.15

tax = 0.08

amount = 35.92
    
print "The total is $%.2f for original amount of $%.2f with %.2f% tax and %.2f% tip." % (totalBill(tip, tax, amount), amount, tax, tip)