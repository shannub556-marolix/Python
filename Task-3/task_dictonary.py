print('1.Write a Python script to add a key to a dictionary.')
d={0: 10, 1: 20}
key=input('enter a key to add: ')
value=input('enter a value to add: ')
d[key]=value
print(d)

print()
print()

print('2.Write a Python script to check whether a given key already exists in a dictionary.')
d={'a': 100, 'b': 200, 'c':300}
key=input('enter a key to check: ')
if d.get(key) == None:
    print('Given key is not in dictnoary')
else:
    print('given key is in dictonary')

print()
print()

print('3.Write a Python program to iterate over dictionaries using for loops')
d={'a': 100, 'b': 200, 'c':300}
for items in d.items():
    print(items)

print()
print()

print('4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.')
d={}
for i in range(1,16):
    d[i]=i*i
print(d)

print()
print()

print('5.Write a Python program to create a dictionary from a string.')
s=input('enter a string: ')
s=s.replace(' ','')
d={}
for ch in s:
    d[ch]=s.count(ch)
print(d)

print()
print()

print('6. Write a Python program to sum all the items in a dictionary.')
d={'a': 300, 'b': 200, 'd':400}
sum=()
for i in d.items():
    sum+=i
print(sum)

print()
print()

print('7.Write a Python program to combine two dictionary by adding values for common keys.')
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d1.keys():
    if key in d2.keys():
        d2[key]=d1.get(key)+d2.get(key)
    else:
        d2[key]=d1.get(key)
print(d2)

print()
print()

print('8.Write a Python program to access dictionary keys element by index.')
d={'physics': 23, 'math': 67, 'chemistry':88}
print(d.items())
index=int(input('enter a index position from 0 to 2: '))
print(list(d.keys())[index])

print()
print()

print('9.Write a Python program to remove a key from a dictionary.')
d = {'a': 100, 'b': 200, 'c':300}
print(d)
key=input('enter a key to remove: ')
d.pop(key)
print(d)

print()
print()

print('10.Write a Python script to merge two Python dictionaries.d')
d1={'a': 300, 'b': 200, 'd':400}
d2={'e': 100, 'f': 200, 'c':300}
print(d1)
print(d2)
d1.update(d2)
print(d1)