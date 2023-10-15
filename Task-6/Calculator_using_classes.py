from functools import *
class Calculator:
    def __init__(self):
        print('____________________________________________WELCOME TO CALCULATOR__________________________________')
        self.operations()
    
    def operations(self):
        print(''' Select operations from dropdown
                            1.Addition
                            2.Subtarction
                            3.Multipliaction
                            4.Divison
              Press 1 for Add , 2 for sub, 3 for Mul, 4 for Div
''')
        n=input()
        self.x=eval(input('enter numbers separated by comma(,): '))
        if n=='1':
            self.add(self.x)
        elif n=='2':
            self.sub(self.x)
        elif n=='3':
            self.mul(self.x)
        elif n=='4':
            self.div(self.x)
        else:
            print('PLEASE CHOOSE FROM THE BELOW DROPDOWN ONLY')
            self.operations()

    def add(self,*args):
        print(f'Sum of digits is {sum(*args)}')

    def sub(self,*args):
        self.s=reduce(lambda x,y : (x-y) if x>y else (y-x),*args)
        print(f'Subtraction of digits is {self.s}')

    def mul(self,*args):
        self.m=reduce(lambda x,y : (x*y),*args)
        print(f'Multiplication of digits is {self.m}')

    def div(self,*args):
        self.d=reduce(lambda x,y : (x/y) if x>y else (y/x),*args)
        print(f'Divison of digits is {self.d}')
s=Calculator()
        