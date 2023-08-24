print('1.Write a python program to remove a given  character from string.')
string=input('enter a string : ')
sub_string=input('enter a character to remove from string: ')
new_string=string.replace(sub_string,'')
print(new_string)

print()
print()

print('2.Write a program to check String is Palindrome or not.')
string=input('enter a string : ')
if string == (string[::-1]):
    print('palindrome ')
else:
    print('not palindrome')

print()
print()

print('3.Write a python program to check given character is vowel or consonant.')
sub_string=input('enter a character to check: ')
if sub_string in 'aeiouAEIOU':
    print('Given character is vowel')
else:
    print('Given Character is consonant')

print()
print()

print('4.Write a python program to replace string space with given character in Python.')
string=input('enter a string: ')
sub_string=input('enter character to replace: ')
new_string=string.replace(' ',sub_string)
print(new_string)

print()
print()

print('5.Write a python program to count alphabets, digits, and special characters in the string.')
string=input('enter a string: ')
alphabets=0
digits=0
special_characters=0
for ch in string:
    if ch.isalpha():
        alphabets+=1
    elif ch.isdigit():
        digits+=1
    else:
        special_characters+=1
print(f'alphabet count = {alphabets}')
print(f'digits count = {digits}')
print(f'special_characters count = {special_characters}')

print()
print()

print('6.Write a python program to remove all the blank spaces in a given string.')
string=input('enter a string: ')
new_string=string.replace(' ','')
print(new_string)

print()
print()

print('7.Write a python program to find sum of integers in the string.')
string=input('enter a string: ')
sum=0
for ch in string:
    if ch.isdigit():
        sum+=int(ch)
print(sum)

print()
print()

print('8.Write a python program to Remove Repeated Character from String.')
string=input('enter a string: ')
new_string=''
for ch in string:
    if ch not in new_string:
        new_string+=ch
print(new_string)

print()
print()

print('9.Write a python program to count occurrence of given character in string.')
string=input('enter a string: ')
sub_string=input('enter a character: ')
print(string.count(sub_string))

print()
print()

print('10.Write a python program to check string is anagrams or not in Python.')
string=input('enter a string1: ')
string2=input('enter a string2: ')
if len(string)==len(string2):
    for ch in string:
        if ch not in string2:
            print('not anagram')
            break
    else:
        print('anagram')
else:
    print('not anagram')