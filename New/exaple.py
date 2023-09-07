
a=100
def f1():
    a=99
    print(a)
    print(globals()[a])
def f2():
    print(a)
f1()
f2()    