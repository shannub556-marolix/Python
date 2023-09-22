#Choosing a random participant from the employee's group
from random import *

employee_Details = ['lakshmi','harshini','naheda','nikhil','shanmukha','ravi teja','mommin','ravi chandra','suresh maloth','suresh miriyala','jyoshna','sivarama','santosh','vamsi krishna','bhuvanesh','gopi bhavani','ramya shree','ravi mishra','siva shankar','venkat sai n','venkat sai kumar ']
printed=[]
def fun(): 
    def fun2():
        global employee_Details
        global printed
        s=choice(employee_Details)
        if s not in printed :
            print(s)
            print()
            printed.append(s)
            n=input('just hit enter to choose next opponent: ')
            if n=='':
                fun2()
        else:
            if len(printed)==len(employee_Details):
                print('Done with the activity')
                return
            else:
                fun2()
    fun2()


fun()






