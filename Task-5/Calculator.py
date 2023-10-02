'''Hello guys take a look at below questions and submit 

1.write a program to create a calculator using functions (sum,sub,mul,div)

Variable length arguments. 

'''
from functools import *

history=[]
def add(*args):
    result=reduce(lambda a,b: (a+b),*args)
    print(f'sum of numbers is :{result}')
    history.append(f'sum is {result}')
    print()
    print()

def sub(*args):
    result=reduce(lambda a,b: (a-b),*args)
    print(f'subtraction of numbers is :{result}')
    history.append(f'subtraction is {result}')
    print()
    print()


def mul(*args):
    result=reduce(lambda a,b: (a*b),*args)
    print(f'multiplication of numbers is :{result}')
    history.append(f'multiplication is {result}')
    print()
    print()


def div(*args):
    result=reduce(lambda a,b: (a//b),*args)
    print(f'division of numbers is :{result}')
    history.append(f'division is {result}')
    print()
    print()


while True:
    n=input('To add type a, to sub type s, to mul type m, to div type d, for history type h: ')
    if n=='h':
        print(history)
        print()
        print()

    else:
        x=eval(input('Enter values separated by comma(","): '))
        if n == 'a':
            add(x)
        elif n=='s':
            sub(x)
        elif n=='m':
            mul(x)
        elif n=='d':
            div(x)
        