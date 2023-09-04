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
'''

print('10.Write a Python program to remove duplicates from a list.')
l1=list(set(eval(input('enter a group of elements separated by comma(,) in a single line: '))))
print(f'list after removing duplicates: {l1}')