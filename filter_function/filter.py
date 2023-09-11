print('write a programm to filter even or odd')
l=eval(input('enter a numbers that you want in a single line sperated by comma(,): '))
f=filter(lambda n : True if n%2==0 else False,l)
print(list(f))

print()
print()

print('write a programm to filter whether number is in between 1 to 100 or not')
l=eval(input('enter a numbers that you want in a single line sperated by comma(,): '))
f=filter(lambda n : True if 1<=n<=100 else False,l)
print(list(f))

print()
print()

print('write a programm to filter whether given number is divisible by 3 and 5 ')
l=eval(input('enter a nums that you want in a single line sperated by comma(,): '))
f=filter(lambda n : True if n%3==0 and n%5==0 else False,l)
print(list(f))

