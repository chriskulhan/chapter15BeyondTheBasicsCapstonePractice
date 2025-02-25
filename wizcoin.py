#This is from Chapter 15 Object Oriented Programming and Classese

class Wizcoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new Wizcoin object with galleons, sickles, and knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        #NOTE: __init__() methods never have a return statement

    def value(self):
        """The value (in knuts) of all the coins in this Wizcoin object."""
        return(self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """Returns the weight of the coins in grams"""    
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
        
