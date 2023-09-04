print('1. write a python program to merge two lists')
l1=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
l2=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
l3=l1+l2
print(f'Merging two lists: {l3}')

print()
print()

print('2.write a python program to find the sum of list elements.')
l1=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
sum=0
for i in l1:
    sum+=i
print(f'sum of elements in list: {sum}')

print()
print()

print('3.write a python program to print even and odd numbers seperatly in list.')
l=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
print(f'odd numbers in a given list: {odd}')
print(f'even numbers in a given list: {even}')

print()
print()

print('4.write a python program to delete element of given index in list.')
l=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
index=eval(input('enter a index position which you want to remove: '))
l.pop(index)
print(f'list after removing element in given index position: {l}')

print()
print()

print('5.write a python program to delete given elemet from the list.')
l=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
element=eval(input('enter a element to remove from list: '))
l.remove(element)
print(f'list after removing given elements from list: {l}')

print()
print()

print('6.write a python program to insert an elemet  at given index location.')
l=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
index=eval(input('enter a index position to insert element at that position: '))
element=eval(input('enter a element to insert in a list: '))
l.insert(index,element)
print(f'list after inserting elements at a given index position: {l}')

print()
print()

print('7.write a python program to check the sizes of given two lists are same.')
l1=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
l2=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
if (len(l1) == len(l2)):
    print('size of both the lists are same')
else:
    print('size of both the lists are not same')

print()
print()

print('8.Write a Python function that takes two lists and returns True if they have at least one common member.')
def list_fun():
    l1=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
    l2=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
    for ch in l1:
        if ch in l2:
            return(True)
            break
    else:
        return(False)
print(list_fun())

print()
print()

print('Write a Python program to remove a specified column from a given nested list. Original Nested list: [[1, 2, 3], [2, 4, 5], [1, 1, 1]]')
l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
l1=[]
for i in range(int(len(l))):
    element=l[i]
    element.pop(0)
    l1.append(element)
print(f'new list after removing specified elements: {l1}')

print()
print()

print('9. Write a Python program to convert a list of multiple integers into a single integer.')
l=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
l1=''
for i in l:
    l1+=str(i)
print(f'string which formed after adding integers: {l1}')

print()
print()

print('10.Write a Python program to remove duplicates from a list.')
l1=list(set(eval(input('enter a group of elements separated by comma(,) in a single line: '))))
print(f'list after removing duplicates: {l1}')