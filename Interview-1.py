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
  

# f=map(lambda a : a*2 if a%2==0 else a,[1,2,3,5,6,667])
# print(f)
# print(list(f))

# from functools import reduce

# f=reduce(lambda a,b : a-b, [1,2,3,5])
# print(f)

# def modify(fun):
#     def fun1(a,b):
#         if a<b :
#             a,b= b,a
#         return fun(a,b)
#     return fun1

# @modify
# def div(a,b):
#     print(a/b)

# div(5,2)
# div(2,5)


# class Student:    
#     count = 0    
#     def __init__(self):    
#         Student.count = Student.count + 1    
# s1=Student()    
# s2=Student()    
# s3=Student()    
# print("The number of students:",Student.count)    

# a='shanmukha'
# a2=''
# a3=''
# l=len(a)//2
# for i in range(l):
#     a2=a[i]+a2
# for i in range(l,len(a)):
#     a3=a[i]+a3
# print(a2+a3)

# n=int(input('Enter your input'))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('prime')
# else:
#     print('not prime')


# s=[1,2,3,4,5,6,9]
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if (i+j)==7:
#             print(i,j)


from threading import *
from time import  *
class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello-1')
            sleep(1)

            print(current_thread().getName())


class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi-2')
            sleep(1)

            print(current_thread().getName())


class Hi1(Thread):
    def run(self):
        for i in range(10):
            print('Hi-3')
            sleep(1)

            print(current_thread().getName())



c=Hello()
c1=Hi()
c2=Hi1()
print(current_thread().getName())
c.start()
c1.start()
c2.start()
c.join()
c1.join()
c2.join()
print('byee')
print(current_thread().getName())