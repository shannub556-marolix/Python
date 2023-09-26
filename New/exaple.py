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


'''


for i in range(5,1,-1):
    for j in range(1,i):
        print(j,'*',end=' ')
    print()


