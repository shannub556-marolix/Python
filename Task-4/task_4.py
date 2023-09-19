
details = []
def add():
    global details
    n=int(input('Enter number of employees you want to take: '))
    for i in range(1,n+1):
        d={}
        print(f'enter details of employee-{i}')
        d['Name']=input('Enter name of employee: ')
        d['Emp id']=input('Enter employee i:')
        d['Domain']=input('Enter domain of the emplpoyee: ')
        d['Email']=input('Enter email of the employee: ')
        details.append(d)
        print()
    print()
    print()
    con()

def remove():
    global details
    n=input('to remove an employee type e , to remove attribute of element type a, to delete entire employe details type d: ')
    if n=='e':
        ch=input('enter an attribute of emplpoyee to reomove: ')
        for i in details:
            if ch == i.get('Name') or (ch == i.get('Emp id') or (ch == i.get('Domain') or ch == i.get('Email'))) :
                details.remove(i)
                break
        else :
            print('employee with given attribute not found: ')
        print()
        print()
        con()        
    elif n=='a':
        ch=input('Enter an element which that element to be reomved from that employee details')

        for i in range(len(details)):
            if ch == details[i].get('Name') :
                details[i].pop('Name')
                break
            elif ch == details[i].get('Emp id'):
                details[i].pop('Emp id')
                break
            elif ch == details[i].get('Domain'):
                details[i].pop('Domain')
                break
            elif ch == details[i].get('Email'):
                details[i].pop('Email')
                break
        else :
            print('employee with given attribute not found: ')
        print()
        print()
        con()
    elif n== 'd':
        details.clear() 
        print()
        print()
        con()

def p():
    global details
    n=input('to print an employee type e , to print detalis of all the employees type a: ')
    if n=='e':
        ch=input('enter an attribute of emplpoyee to print employe details: ')
        for i in details:
            if ch == i.get('Name') or (ch == i.get('Emp id') or (ch == i.get('Domain') or ch == i.get('Email'))) :
                print(i)
        else :
            print('employee with given attribute not found: ')
        print()
        print()
        con()        
    elif n=='a':
        print(details)
        print()
        print()
        con()

def con():
    n=input('to add type a, to remove type r, to print type p : ')
    if n=='a':
        add()
    elif n=='r':
        remove()
    elif n=='p':
        p()

con()
    





