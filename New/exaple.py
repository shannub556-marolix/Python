'''
def add(a,b,c=120):
    print('hello')
    print(a,b)
    print(c)

print(add(10,20,30))

d=[{'name':'shannu','roll':'12'}]
d[0].pop('name')
print(d)


x=(1,2)
y=(2,4)
print(x+y)


print('7.Write a Python program to combine two dictionary by adding values for common keys.')
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d1.keys():
    if key in d2.keys():
        d2[key]=d1.get(key)+d2.get(key)
    else:
        d2[key]=d1.get(key)
print(d2)




for i in range(5,1,-1):
    for j in range(1,i):
        print(j,'*',end=' ')
    print()



s='we are code1rs2 3'
s1=sorted(s)
l=[1,35,5,'a']

print(l)

t=sorted(s)
print(t)

'''

s=input('neter ')
s1=input('enter')
s=s.lower()
s1=s1.lower()
s=sorted(s)
s1=sorted(s1)
if len(s)==len(s1):
    if s==s1:
        print('anagram')
    else:
        print('not anagram')
else:
    print('not anagram')