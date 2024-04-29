# input_data=[1,2,3,4,5,6,7,8,9,0]
# for i in range(int(len(input_data))):
#     for j in range(i+1,int(len(input_data))):
#         if (i+j)==4:
#             print(i,j)


# def fun():
#     string=input()
#     for ch in string:
#         if ch=='(' or ')':
#             if ')' not in string or ')' not in string:
#                 return False
#         if ch=='{' or '}':
#             if '{' not in string or '}' not in string:
#                 return False
#         if ch=='[' or ']':
#             if '[' not in string or ']' not in string:
#                 return False
#     return True
# print(fun())
  

f=map(lambda a : a*2 if a%2==0 else a,[1,2,3,5,6,667])
print(f)
print(list(f))

from functools import reduce

f=reduce(lambda a,b : a-b, [1,2,3,5])
print(f)

def modify(fun):
    def fun1(a,b):
        if a<b :
            a,b= b,a
        return fun(a,b)
    return fun1

@modify
def div(a,b):
    print(a/b)

div(5,2)
div(2,5)


class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)    