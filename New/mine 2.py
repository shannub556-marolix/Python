'''
s=eval(input('enter input: '))
print(s)
print(type(s))
s=list(s)
print(type(s))
print(type(s[0]))
print(type(s[1]))
print(type(s[2]))


print('6.write a python program to insert an elemet  at given index location.')
l=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
index=eval(input('enter a index position to insert element at that position'))
element=input('enter a element to insert in a list: ')
l.insert(index,element)
print(f'list after inserting elements at a given index position: {l}')


l1=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
l2=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
merged_list=l1+l2
print(merged_list)



print('2.Write a Python script to check whether a given key already exists in a dictionary.')
d={'a': 100, 'b': 200, 'c':300}
key=input('enter a key to check')
if d.get(key) == None:
    print('Given key is not in dictnoary')
else:
    print('given key is in dictonary')



d={'a': 300, 'b': 200, 'd':400}
sum=()
for i in d.items():
    sum+=i
print(sum)


print('7.Write a Python program to combine two dictionary by adding values for common keys.')
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d1.keys():
    if key in d2.keys():
        d2[key]=d1.get(key)+d2.get(key)
    else:
        d2[key]=d1.get(key)
print(d2)



print('8.Write a Python program to access dictionary keys element by index.')
d={'physics': 23, 'math': 67, 'chemistry':88}
index=int(input('enter a index position from 0 to 2: '))
print(list(d.keys())[index])
'''
d1={'a': 300, 'b': 200, 'd':400}
d2={'a': 100, 'b': 200, 'c':300}
d1.update(d2)
print(d1)