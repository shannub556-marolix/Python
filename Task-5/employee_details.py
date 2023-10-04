'''
2. Write a program to enter employee details and also filter  the stored employee  details  with name and empid and designation and email. 
'''
d=[]
def add():
    dictonary={}
    dictonary['Name']=input('Enter the name of employee : ')
    dictonary['Email']=input('Enter the email of employee : ')
    dictonary['Empid']=input('Enter the employee id of employee : ')
    dictonary['Designation']=input('Enter the designation of employee : ')
    d.append(dictonary)
    print('Employee details succesfully added')
    print()
    print()

def printing():
    ch=input('enter a attribute to filter employee details: ')
    for dict in d:
        if dict.get('Name') == ch :
            print(dict)
            break
        elif dict.get('Email') == ch :
            print(dict)
            break
        elif dict.get('Empid') == ch :
            print(dict)
            break
        elif dict.get('Designation') == ch :
            print(dict)
            break
    else:
        print('Employee with this attribute not found to filter')
    print()
    print()


while True:
    n=input('To add employee type a, To filter type f: ')
    if n == 'a':
        add()
    elif n == 'f' :
        printing()



    
