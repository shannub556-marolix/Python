print('write a programm to filter even or odd')
l=eval(input('enter a numbers that you want in a single line sperated by comma(,): '))
f=filter(lambda n : True if n%2==0 else False,l)
print(list(f))
