from functools import*
print('write a programm to get sum of all the digits')
l=eval(input('enter a numbers that you want in a single line sperated by comma(,): '))
f=reduce(lambda n,m : n+m,l)
print(f)

print()
print()

print('write a programm to get product of every element')
l=eval(input('enter a numbers that you want in a single line sperated by comma(,): '))
f=reduce(lambda n,m : n*m,l)
print(f)

print()
print()

print('write a programm to get highest element in a given elements ')
l=eval(input('enter a nums that you want in a single line sperated by comma(,): '))
f=reduce(lambda n,m : n if n>m else m,l)
print(f)

