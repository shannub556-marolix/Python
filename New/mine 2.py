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

'''

s=eval[input()]
print(s)