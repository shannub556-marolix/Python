# import re
# p=input("enter pattern to check:")
# m=re.match(p,"harshini")      
# if m!=None:
#     print("provided pattern is  matched at starting of target string")
# else:
#     print("provided pattern is not matched at target string")   



import re
p=input("enter pattern to check:")
m=re.fullmatch(p,"harshini")      
if m!=None:
    print("provided pattern is  matched at starting of target string")
else:
    print("provided pattern is not matched at target string")   
