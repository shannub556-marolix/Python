print('write a nested function to get sum and product of given numbers')
def fun1(x,y):
    print(f'sum = {x+y}')
    def pro(x,y):
        print(f'pro = {x*y}')
    pro(x,y)

x=int(input('enter a number 1: '))
y=int(input('enter a number 2: '))
fun1(x,y)

print()
print()

print('write a nested function to get greater and lowest of given numbers')
def fun2(x,y):
    print(f'greater = {x if x>y else y}')
    def low(x,y):
        print(f'lowest = {x if x<y else y}')
    low(x,y)

x=int(input('enter a number 1: '))
y=int(input('enter a number 2: '))
fun2(x,y)

print()
print()

print('write a nested function to get numbers multiplied by 10 and divided by 10 of given numbers')
def fun3(x,y):
    print(f'multiplied by 10 = {x*10,y*10}')
    def div(x,y):
        print(f'divided by 10 = {x/10,y/10}')
    div(x,y)

x=int(input('enter a number 1: '))
y=int(input('enter a number 2: '))
fun3(x,y)
