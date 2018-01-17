class Complex_number(object):
    def __init__(self,real,imag):
        self.real=real 
        self.imag=imag
        
    def View(self):
        '''In order to represent the operation here abs= absolute'''
        global x
        opr=['+','-','/','*','abs']
        while True:
            x=input("Enter the operation from the following(here abs=absolute): \n'+'\n'-'\n'*'\n'/'\n'abs'\n")
            if x=='abs':
                z=(self.real**2+self.imag**2)**0.5
                print("Absolute value:{}".format(z))
                break
            elif x in opr:
                print("Complex no:{}{}{}i".format(self.real,x,self.imag))
                break
            else:
                print("\nLooks like you have entered something else")
    def Real(self):
        '''return Real no'''
        return self.real
    def Imag(self):
        """"return imaginary no"""
        return self.imag
    def argument(self):
        '''returns argument'''
        import math
        try:
            theta=math.degrees(math.atan(self.imag/self.real))
            print("Argument=2πn+{} ,where n=0,±1,±2......".format(theta))
        except ZeroDivisionError:
            print("Can't divide by zero zerodivision error")
    def conjugate(self):
        '''returns conjugate'''
        if x=='+':
            print("Conjugate of complex no:{}-{}i".format(self.real,self.imag))
        elif x=='-':
            print("Conjugate of complex no:{}+{}i".format(self.real,self.imag))
        else:
            pass