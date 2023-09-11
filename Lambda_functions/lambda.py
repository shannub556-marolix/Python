print('write a lambda function to add two numbers')
n1=int(input('enter a number1 to add: '))
n2=int(input('enter a number2 to add: '))
l=lambda n1,n2 : (n1+n2)
print(l(n1,n2))

print()
print()

print('write a lambda function to check whether sum is even or odd')
n1=int(input('enter a number1 to add: '))
n2=int(input('enter a number2 to add: '))
l=lambda n1,n2 : 'even' if (n1+n2)%2==0 else 'odd'
print(l(n1,n2))

print()
print()

print('write a lambda function to get product of two numbers')
n1=int(input('enter a number1 to add: '))
n2=int(input('enter a number2 to add: '))
l=lambda n1,n2 : n1*n2
print(l(n1,n2))
