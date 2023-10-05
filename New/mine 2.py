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

d1={'a': 300, 'b': 200, 'd':400}
d2={'a': 100, 'b': 200, 'c':300}
d1.update(d2)
print(d1)


from functools import *
h=[]
def add(*args):
    result=reduce(lambda a,b: (a*b),*args)
    print(f'sum of numbers is :{result}')
    h.append(f'sum is {result}')

a=eval(input('Enter values separated by comma(","): '))
add(a)
    

#Variable length arguments. 
#2. Write a program to enter employee details and also filter the stored employee  details  with name and empid and designation and email. 
Employees = {}
def add_employee():
    name = input("enter the employee name: ")
    empid = input("enter the employee id: ")
    email = input("enter the employee email id: ") 
    designation = input("enter the employee designation: ")
    Employees[name] = {'empid':empid, 'emailid':email, 'designation':designation}
    print("employee details added successfully")

def fliter_stored_employees_details():
    designation = input("enter fliter designation: ")
    found = False
    for key , value in Employees.items():
        if (value['designation'] == designation):
            print(key,value)
            found = True
    if not found:
        print("employees not found with this desgination")
        
            
no_of_employees = int(input("enter number of employees: "))
for i in range(no_of_employees):
    add_employee()
print(Employees) 


fliter_stored_employees_details()



d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
d4={}
d3.update(d2)
d3.update(d1)
for key in d3.keys():
    if key in d1 and key in d2 :
        d4[key]=d1.get(key)+d2.get(key)
    elif key in d1:
        d4[key]=d1.get(key)
    elif key in d2:
        d4[key]=d2.get(key)
print(d4)

print(d1)
print(d2)
print(d3)
print(d4)
'''
class Example:
    def __init__(self,name,age):
        self.name= name
        self.age=age
        print('hello')
        print(self.name)

    def display(self,name):
        print(name)
    
    def merg(slef):
        print('printing')

s=Example('shan',32)





