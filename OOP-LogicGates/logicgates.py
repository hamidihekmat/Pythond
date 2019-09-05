
'''
@auth: Hekmat Hamidi
@purpose: To learn class inheritance
'''

class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic() # -> this method will be performed on the child class
        return self.output

    '''
    Creating a subclass of LogicGate based on number of pins
    Binary -> 2
    Unary -> 2
    Binary -> AND OR
    Unary -> NOT
    '''

class BinaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input('Enter Pin A input for the gate {} --> '.format(self.label)))


    def getPinB(self):
        return int(input('Enter Pin B input for the gate {} --> '.format(self.label)))


class UnaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pin = None

    def getPin(self):
        return int(input('Enter Pin input for the gate {} --> '.format(self.label)))


'''
super(self).__init__(param)
'''


class AndGate(BinaryGate):

    def __init__(self, label):
        super(AndGate, self).__init__(label)

    def performGateLogic(self): # hidden function used by the parent class 1st in the hierchy, we can use getOutput function to call this method 

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


g1 = AndGate('g1')
out = g1.getOutput()
print(out)
