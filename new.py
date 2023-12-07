#strings
#reomve a character from stroing
# s1=input('enter your string')
# s2=input('ch to remove')
# print(s1.replace(s2,''))

print('#2 count the occuramces of givem chara')
s1=input('enetr your string')
s2=input('enetr yoir ch to count')
print(s1.count(s2))


print('#3 check whether two strings is anagram or no')
s1=input('enetr your string1')
s2=input('enetr your string2')
x1=sorted(s1)
x2=sorted(s2)
print(x1)
print(x2)
if len(x1)==len(x2):
    if x1==x2:
        print('anagram')
    else:
        print('anagram')
else:
    print('anagram')


print('#4 check whether given string is palindrome or not')
s1=input('enetr your string1')
rev=s1[::-1]
if rev == s1:
    print('palindrome')
else:
    print('not palindrome')


print('#5 check whether given character is vowels or not')
s1=input('enetr charcter to chek')
if s1 in 'AEIOUaeiou':
    print('character is vowel')
else:
    print('ch is constgant')


print('#6 check whether given character is digit or not using isdigit')
s1=input('enetr charcter to chek')
if s1.isdigit():
    print('it is digit')
else:
    print('not a digit')


print('#7 check whether given character is digit or not')
s1=input('enetr charcter to chek')
if '0'<= s1 <='9':
    print('it is digit')
else:
    print('not a digit')


print('#8 replace space with given character')
s1=input('enetr your string')
s2=input('enetr yoir ch to replace')
s3=''
for ch in s1:
    if ch==' ':
        s3+=s2
    else:
        s3+=ch
print(s3)



print('#9 replace space with given character using replace method')
s1=input('enetr your string')
s2=input('enetr yoir ch to replace')
s3=s1.replace(' ',s2)
print(s3)


print('#10 convert lower case with uppper case ')
s1=input('enetr your string')
s2=s1.upper()
print(s2)


print('#11 convert lower case vowels to uppper case ')
s1=input('enetr your string')
s2=''
for ch in s1:
    if ch in 'aeiou':
        s2+=chr(ord(ch)-32)
    else:
        s2+=ch
print(s2)


print('#12 delete  vowels in a string ')
s1=input('enetr your string')
s2=''
for ch in s1:
    if ch not in 'aeiouAEIOU':
        s2+=ch
print(s2)   


print('#13 count the occurances of  vowels and constants in a string ')
s1=input('enetr your string')
vowels=0
constant=0
for ch in s1:
    if ch in 'aeiouAEIOU':
        vowels+=1
    else:
        constant+=1
print('vowels count = ',vowels)   
print('constant count = ',constant)

print('#14 print highest frequency ch in a string ')
s1=input('enter your string')
h=0
s2=set(s1)
for ch in s2:
    if s1.count(ch) > h:
        h=s1.count(ch)
for ch in s2:
    if h==s1.count(ch):
        print('highest frequency of a character',ch)



print('#15 replace first occurance of  vowels in a string with -')
s1=input('enetr your string')
s2=''
for ch in range(int(len(s1))):
    if s1[ch] in 'aeiouAEIOU':
        s2+=s1[:ch]+'-'+s1[ch+1:]
        break
print(s2)   

print('#16 count alphabest and digits and special character in a string')
s1=input('enetr your string')
alpha=0
digits=0
special=0
for ch in s1:
    if ch.isdigit():
        digits+=1
    elif ch.isalpha():
        alpha+=1
    else:
        special+=1
print('alphabest count=' ,alpha)
print('digits count=' ,digits)
print('special characters count=' ,special)


print('#18 programm to remove blank spaces character in a string')
s1=input('enetr your string')
s2=s1.replace(' ','')
print(s2)


print('#19 programm to conactinate two strings using join method in a string')
s1=input('enetr your string1')
s2=input('enetr your string2')
s3=[s1,s2]
print(('').join(s3))


print('#20 programm to conactinate two strings in a string')
s1=input('enetr your string1')
s2=input('enetr your string2')
print(s1+s2)


print('#21 programm to remove repeated ch in a string')
s1=input('enter your string')
s2=[]
for ch in s1:
    if ch not in s2:
        s2.append(ch)
print(('').join(s2))


print('#22 programm to sum integers in a string')
s1=input('enter your string')
sum=0
for ch in s1:
    if ch.isdigit():
        sum+=int(ch)
print(sum)



print('#21 programm to print all non-repeated ch in a string')
s1=input('enter your string')
s2=set(s1)
for ch in s2:
    print(ch)


print('#21 programm to sort ch in ascending order in a string')
s1=input('enter your string')
s2=list(s1)
s2.sort()
print(('').join(s2))


print('#21 programm to sort ch in descending order in a string')
s1=input('enter your string')
s2=list(s1)
s2.sort(reverse=True)
print(('').join(s2))