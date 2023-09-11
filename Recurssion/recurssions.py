print('print numbers from 1 to given range on single line')
def fun(n,x=1):
    if x>n:
        return
    print(x,end=' ')
    return fun(n,x=x+1)

n=int(input('enter a number upto which you want to print: '))
fun(n)

print()
print()

print('write a programm to check given number is armstrong or not')
def armstrong(n,num,pow,sum=0):
    if n==0:
        return 'armstrong' if num==sum else ('not armstrong')
    return armstrong(n//10,num,pow,sum=sum+((n%10)**pow))

n=int(input('enter a number you wanted to check: '))
print(armstrong(n,n,len(str(n))))

print()
print()

print('write a programm to check given number is palindrome or not')
def pal(n,num,rev=0):
    if n==0:
        return 'palindrome' if num==rev else ('not palindrome') 
    return pal(n//10,num,rev=(rev*10)+(n%10))

n=int(input('enter a number that you want to check: '))
print(pal(n,n))
