print('1 #Membership operator using in and not in')
string='i am groot'
if 'g' in string:
    print('Membership in operator valid')
else:
    print('Membership in operator not valid')

print('---------------------------------------')
if 'k' not in string:
    print('Membership not in operator valid')
else:
    print('Membership not in operator not valid')

print('---------------------------------------')
if 'k' not in string:
    print('Membership not in operator valid')
elif 'in' in string:
    print('Membership in operator not valid')
else:
    print('Membership not in operator not valid')

print()
print()
print()

print('2 #Removing spaces from strip')
string='   i am groot    '
print(f'length of the strig before strip method {len(string)}')
s1=string.strip()
print(f'length of the string after strip method {len(s1)}')
print(s1)

print('---------------------------------------')
string='   i am groot    '
print(f'length of the strig before lstrip method {len(string)}')
s1=string.lstrip()
print(f'length of the string after lstrip method {len(s1)}')
print(s1)

print('---------------------------------------')
string='   i am groot    '
print(f'length of the strig before rstrip method {len(string)}')
s1=string.rstrip()
print(f'length of the string after rstrip method {len(s1)}')
print(s1)

print()
print()
print()

print('#3 Comparing two strings')
s1='praveen'
s2='naveen'
(print('s1 is greater')) if s1>s2 else (print('s2 is greater'))
print('-------------------------------------')
s1='naresh'
s2='naveen'
(print('s1 is greater')) if s1>s2 else (print('s2 is greater'))
print('-------------------------------------')
s1='Naveen'
s2='naveen'
(print('s1 is greater')) if s1>s2 else (print('s2 is greater'))
print('-------------------------------------')

print()
print()
print()

print('#4 Finding substrings by using index method')
string='i am good in python'
sub_string='o'
s1=string.index(sub_string)
print(f'index position of given {sub_string} is {s1}')
print('-----------------------------------------')
string='i am good in python'
sub_string='o'
s1=string.index(sub_string,7)
print(f'index position of given {sub_string} is {s1}')
print('-----------------------------------------')
string='i am good in python'
sub_string='o'
s1=string.index(sub_string,9,len(string))
print(f'index position of given {sub_string} is {s1}')
print('-----------------------------------------')

print()
print()
print()

print('#5 Finding substrings by using rindex method')
string='i am good in python'
sub_string='o'
s1=string.rindex(sub_string)
print(f'rindex position of given {sub_string} is {s1}')
print('-----------------------------------------')
string='i am good in python'
sub_string='o'
s1=string.rindex(sub_string,0,7)
print(f'rindex position of given {sub_string} is {s1}')
print('-----------------------------------------')
string='i am good in python'
sub_string='o'
s1=string.rindex(sub_string,0,9)
print(f'rindex position of given {sub_string} is {s1}')
print('-----------------------------------------')

print()
print()
print()

print('#6 Finding substrings by using find method')
string='i am good in python'
sub_string='o'
s1=string.find(sub_string)
print(f'index position of given {sub_string} is {s1}')
print('-----------------------------------------')
string='i am good in python'
sub_string='o'
s1=string.find(sub_string,8)
print(f'index position of given {sub_string} is {s1}')
print('-----------------------------------------')
string='i am good in python'
sub_string='z'
s1=string.find(sub_string,9,len(string))
print(f'index position of given {sub_string} is {s1}')
print('-----------------------------------------')

print()
print()
print()

print('#7 Finding substrings by using rfind method')
string='i am good in python'
sub_string='o'
s1=string.rfind(sub_string)
print(f'index position of given {sub_string} is {s1}')
print('-----------------------------------------')
string='i am good in python'
sub_string='o'
s1=string.rfind(sub_string,0,7)
print(f'index position of given {sub_string} is {s1}')
print('-----------------------------------------')
string='i am good in python'
sub_string='z'
s1=string.rfind(sub_string,9,len(string))
print(f'index position of given {sub_string} is {s1}')
print('-----------------------------------------')

print()
print()
print()

print('#8 replace the string using replace method')
string='i am good in python'
s1=string.replace('good', 'bad')
print(f'replaced string: {s1}')
print('-------------------------------')
string='i am bad in python and good in theory'
s1=string.replace('bad', 'good',1)
print(f'replaced string: {s1}')
print('-------------------------------')
string='i am good good good good in python and good in theory'
s1=string.replace('good', '',3)
print(f'replaced string: {s1}')
print('-------------------------------')

print()
print()
print()

print('#9 Separate the string using split method')
string='i am good in python'
s1=string.split()
print(f'separated string: {s1}')
print('-------------------------------')
string='i am good good good good in python and good in theory'
s1=string.split('good',1)
print(f'separated string: {s1}')
print('-------------------------------')
string='i am good good good good in python and good in theory'
s1=string.split('good',3)
print(f'separated string: {s1}')
print('-------------------------------')

print()
print()
print()

print('#10 Join the strings using join method')
list=['i', 'am', 'good', 'in', 'python']
s1=(' ').join(list)
print(f'New string after joining: {s1}')
print('-------------------------------')
tuple=('i am ', ' good good good in python and good in theory')
s1=('-').join(tuple)
print(f'New string after joining: {s1}')
print('-------------------------------')
set={'i am ', ' ', ' ', ' good in python and good in theory'}
s1=('--').join(set)
print(f'New string after joining: {s1}')
