print('#CREATING TABLE USING FOR AND WHILE LOOP')
num=int(input('for loop table :'))
for i in range(1,11):
    print(num,' x ',i,' = ',num*i)

print()
print()

number=int(input('while loop table :'))
count=1
while count<=10:
    print(number,' x ',count,' = ',number*count)
    count+=1

print()
print()
print()
print()

print('#CREATE A LOGIC USING CONDITIONAL STATEMENTS')
list=[1,2,23,45,6,7]
for num in list:
    if num==2:
        print('num is ',num)
    elif num==23:
        print('found number ', num)
    else:
        print('number not found')

print()
print()
print()
print()



print('#CREATE A LOGIC USING LOGICAL AND RELATIONAL OPERATORS')
t=(44,55,88,92,33,23,56,98)
for num in t:
    if((num==98) or (num==98)):
        print(num,'State Topper')
    elif (num>90):
        print(num,'District topper ')
    elif (num>=50 and num<90):
        print(num,'passed in DISTINCTION')
    else:
        print(num,'failed')