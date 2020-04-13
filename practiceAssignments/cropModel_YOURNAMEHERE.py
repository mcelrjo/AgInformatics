'''Below is a outline of an object oriented program you must complete.  It is a
class called hectareCrop.  hectareCrop is meant to model a given crop with
common variables of a crop -- how much rainfall it receives, how much N is lost, 
the yield of the crop, etc.  At the bottom are unit test that run to determine 
if you have implemented each class function correctly.  
'''


import random, pylab

class hectareCrop(object):
    '''Used to project yearly yield for a crop based on fertilizer and rainfall 
    inputs.
    '''
    def __init__(self, NFert, irrigation):
        ''' NFert average is 200, as in 200 kg N/ha
            Irrigation, boolean
        '''
        
        
        pass
        
    def rainfall(self):
        '''returns an annual rainfall amount based on normal probability distribution.
        Average rainfall during growth period is 50 cm and a standard deviation of 20 cm 
        return self.rainAmt
        '''
        pass
        

    def Nloss(self):
        '''Loss of N based on amount of rainfall that occurred.  For every cm of rain,
        3.0% loss of N occurs.
        Runs self.rainfall() to get self.rainAmt, returns an int of NAmt remaining based
        on yearly rainfall.  Int returned is not a object variable and does not replace
        self.NAmt
        '''
        pass
       
        
    def cropYield(self):
        '''Predicts the yearly yield of a crop based on rainfall and fertilizer
        inputs.
        Average yield is 100 bushels per acre based on average rainfall and 200 kg/ha
        per year N fertility.  A very basic model was used to predict yield where
        yield = rainAmt + (0.25 * N amt in kg/ha).  Need to use NAmt after rainfall
        for calcualtion.  
        RETURN: self.yearYield which is the yield in bushels per acre
        '''
        pass
        
    def profit(self):
        '''Assume $7 dollar per bushel yield.  However, a loss of $10 for each cm below 
        50 cm if irrigation is True.  If irrigation is True, rainfall is supplemented up to 50 cm if it is 
        below.  If rainfall is 50 cm or greater, no additional irrigation takes
        place.
        RETURN grossProfit, not an object attribute
        '''
        pass


def modelYield(NFert, Irrigation= False, cycles = 10000):
    '''Model yield for 10,000 iterations and plot the yield in a histogram.
    '''
    pass
    
#modelYield(200)
 
def modelProfit(NFert, cycles=1000):
    '''Model profit for 10,000 iterations for both irrigated and non-irrigated.
    Plot the predictions in four (2x2) subplot windows - histogram and boxplot for
    each of the data sets.
    '''
    pass
    
#modelProfit(200)

#Uncomment to run
random.seed(1)
print("Unit Test 1") 
crop1 = hectareCrop(200, False) 
money = crop1.profit() 
print money #answer is 783.29
print crop1.yearYield #answer is 111.899
print crop1.rainAmt #answer 62.149
print crop1.NFert #answer is 200
print crop1.irrigation #answer is False


# print("Unit Test 2")
# crop2 = hectareCrop(100, True) 
# money = crop2.profit()
# print money #521.258
# print crop2.yearYield #74.465
# print crop2.rainAmt #49.715
# print crop2.NFert #100
# print crop2.irrigation #True
# 
